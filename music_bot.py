import discord
from discord.ext import commands
import yt_dlp
import asyncio
from collections import deque

# ==========================================
#  ตั้งค่า Bot Token ของคุณที่นี่
# ==========================================
TOKEN = "MTQ4NTY0NzczMTgyMDIwMDE0OA.GzBZ8T.B5P0WjU3mNhxGvp5bYf9j2KsbCYxKlqOAjK0bk"

# ==========================================
#  ตั้งค่า yt-dlp และ FFmpeg
# ==========================================
YTDL_OPTIONS = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "quiet": True,
    "default_search": "ytsearch",
    "source_address": "0.0.0.0",
}

FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}

ytdl = yt_dlp.YoutubeDL(YTDL_OPTIONS)

# ==========================================
#  ตั้งค่า Bot
# ==========================================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# เก็บ queue แยกตาม guild
queues: dict[int, deque] = {}
now_playing: dict[int, dict] = {}


def get_queue(guild_id: int) -> deque:
    if guild_id not in queues:
        queues[guild_id] = deque()
    return queues[guild_id]


# ==========================================
#  ฟังก์ชันค้นหาและดึง URL เพลง
# ==========================================
async def fetch_source(query: str) -> dict | None:
    loop = asyncio.get_event_loop()

    def _search():
        try:
            if query.startswith("http"):
                info = ytdl.extract_info(query, download=False)
            else:
                info = ytdl.extract_info(f"ytsearch:{query}", download=False)
                if "entries" in info:
                    info = info["entries"][0]
            return {
                "url": info["url"],
                "title": info.get("title", "ไม่ทราบชื่อเพลง"),
                "duration": info.get("duration", 0),
                "thumbnail": info.get("thumbnail", ""),
                "webpage_url": info.get("webpage_url", ""),
            }
        except Exception as e:
            print(f"[yt-dlp error] {e}")
            return None

    return await loop.run_in_executor(None, _search)


# ==========================================
#  เล่นเพลงถัดไปใน queue
# ==========================================
async def play_next(ctx: commands.Context):
    guild_id = ctx.guild.id
    queue = get_queue(guild_id)

    if not queue:
        now_playing.pop(guild_id, None)
        await ctx.send("✅ เล่นเพลงครบทุกเพลงในคิวแล้วครับ!")
        return

    song = queue.popleft()
    now_playing[guild_id] = song

    source = discord.FFmpegPCMAudio(song["url"], **FFMPEG_OPTIONS)
    source = discord.PCMVolumeTransformer(source, volume=0.5)

    def after_play(error):
        if error:
            print(f"[Player error] {error}")
        asyncio.run_coroutine_threadsafe(play_next(ctx), bot.loop)

    ctx.voice_client.play(source, after=after_play)

    duration = song["duration"]
    mins, secs = divmod(duration, 60)
    embed = discord.Embed(
        title="🎵 กำลังเล่น",
        description=f"[{song['title']}]({song['webpage_url']})",
        color=discord.Color.green(),
    )
    embed.add_field(name="⏱ ความยาว", value=f"{mins}:{secs:02d}")
    if song["thumbnail"]:
        embed.set_thumbnail(url=song["thumbnail"])
    await ctx.send(embed=embed)


# ==========================================
#  คำสั่ง !play
# ==========================================
@bot.command(name="play", aliases=["p"])
async def play(ctx: commands.Context, *, query: str):
    """เล่นเพลงจาก YouTube  ใช้: !play ชื่อเพลง หรือ URL"""

    # เช็คว่าผู้ใช้อยู่ใน voice channel
    if not ctx.author.voice:
        return await ctx.send("❌ กรุณาเข้า Voice Channel ก่อนนะครับ!")

    voice_channel = ctx.author.voice.channel

    # เชื่อมต่อ voice channel ถ้ายังไม่ได้เชื่อมต่อ
    if ctx.voice_client is None:
        await voice_channel.connect()
    elif ctx.voice_client.channel != voice_channel:
        await ctx.voice_client.move_to(voice_channel)

    # แสดงข้อความกำลังค้นหา
    msg = await ctx.send(f"🔍 กำลังค้นหา **{query}** ...")

    song = await fetch_source(query)
    if not song:
        return await msg.edit(content="❌ ไม่พบเพลงที่ค้นหาครับ กรุณาลองใหม่อีกครั้ง")

    queue = get_queue(ctx.guild.id)

    # ถ้ากำลังเล่นอยู่แล้ว ให้เพิ่มเข้า queue
    if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
        queue.append(song)
        await msg.edit(content=f"➕ เพิ่ม **{song['title']}** เข้าคิวแล้วครับ (ตำแหน่งที่ {len(queue)})")
    else:
        queue.append(song)
        await msg.delete()
        await play_next(ctx)


# ==========================================
#  คำสั่ง !pause
# ==========================================
@bot.command(name="pause")
async def pause(ctx: commands.Context):
    """หยุดพักเพลงชั่วคราว"""
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("⏸ หยุดพักเพลงชั่วคราวแล้วครับ")
    else:
        await ctx.send("❌ ไม่มีเพลงที่กำลังเล่นอยู่ครับ")


# ==========================================
#  คำสั่ง !resume
# ==========================================
@bot.command(name="resume", aliases=["r"])
async def resume(ctx: commands.Context):
    """เล่นเพลงต่อ"""
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("▶️ เล่นเพลงต่อแล้วครับ")
    else:
        await ctx.send("❌ ไม่มีเพลงที่ถูกหยุดพักอยู่ครับ")


# ==========================================
#  คำสั่ง !skip
# ==========================================
@bot.command(name="skip", aliases=["s"])
async def skip(ctx: commands.Context):
    """ข้ามเพลงปัจจุบัน"""
    if ctx.voice_client and (ctx.voice_client.is_playing() or ctx.voice_client.is_paused()):
        ctx.voice_client.stop()
        await ctx.send("⏭ ข้ามเพลงแล้วครับ")
    else:
        await ctx.send("❌ ไม่มีเพลงที่กำลังเล่นอยู่ครับ")


# ==========================================
#  คำสั่ง !queue
# ==========================================
@bot.command(name="queue", aliases=["q"])
async def show_queue(ctx: commands.Context):
    """แสดงคิวเพลงทั้งหมด"""
    guild_id = ctx.guild.id
    queue = get_queue(guild_id)
    current = now_playing.get(guild_id)

    if not current and not queue:
        return await ctx.send("📭 ไม่มีเพลงในคิวครับ")

    embed = discord.Embed(title="🎶 คิวเพลง", color=discord.Color.blurple())

    if current:
        embed.add_field(
            name="▶️ กำลังเล่น",
            value=f"[{current['title']}]({current['webpage_url']})",
            inline=False,
        )

    if queue:
        queue_text = "\n".join(
            f"`{i+1}.` {song['title']}" for i, song in enumerate(queue)
        )
        embed.add_field(name=f"📋 ในคิว ({len(queue)} เพลง)", value=queue_text[:1024], inline=False)

    await ctx.send(embed=embed)


# ==========================================
#  คำสั่ง !stop
# ==========================================
@bot.command(name="stop")
async def stop(ctx: commands.Context):
    """หยุดเพลงและล้างคิวทั้งหมด"""
    guild_id = ctx.guild.id
    queues.pop(guild_id, None)
    now_playing.pop(guild_id, None)

    if ctx.voice_client:
        ctx.voice_client.stop()
        await ctx.voice_client.disconnect()
        await ctx.send("⏹ หยุดเพลงและออกจาก Voice Channel แล้วครับ")
    else:
        await ctx.send("❌ บอทไม่ได้อยู่ใน Voice Channel ครับ")


# ==========================================
#  คำสั่ง !nowplaying
# ==========================================
@bot.command(name="nowplaying", aliases=["np"])
async def nowplaying(ctx: commands.Context):
    """แสดงเพลงที่กำลังเล่น"""
    current = now_playing.get(ctx.guild.id)
    if not current:
        return await ctx.send("❌ ไม่มีเพลงที่กำลังเล่นอยู่ครับ")

    duration = current["duration"]
    mins, secs = divmod(duration, 60)
    embed = discord.Embed(
        title="🎵 กำลังเล่นอยู่",
        description=f"[{current['title']}]({current['webpage_url']})",
        color=discord.Color.gold(),
    )
    embed.add_field(name="⏱ ความยาว", value=f"{mins}:{secs:02d}")
    if current["thumbnail"]:
        embed.set_thumbnail(url=current["thumbnail"])
    await ctx.send(embed=embed)


# ==========================================
#  คำสั่ง !clear
# ==========================================
@bot.command(name="clear")
async def clear_queue(ctx: commands.Context):
    """ล้างคิวเพลงทั้งหมด (แต่ยังเล่นเพลงปัจจุบันต่อ)"""
    queues[ctx.guild.id] = deque()
    await ctx.send("🗑️ ล้างคิวเพลงทั้งหมดแล้วครับ")


# ==========================================
#  คำสั่ง !volume
# ==========================================
@bot.command(name="volume", aliases=["vol"])
async def volume(ctx: commands.Context, vol: int):
    """ปรับระดับเสียง (0-100)  ใช้: !volume 50"""
    if not ctx.voice_client or not ctx.voice_client.is_playing():
        return await ctx.send("❌ ไม่มีเพลงที่กำลังเล่นอยู่ครับ")

    if not 0 <= vol <= 100:
        return await ctx.send("❌ กรุณาใส่ตัวเลขระหว่าง 0-100 ครับ")

    ctx.voice_client.source.volume = vol / 100
    await ctx.send(f"🔊 ปรับระดับเสียงเป็น **{vol}%** แล้วครับ")


# ==========================================
#  คำสั่ง !help
# ==========================================
@bot.command(name="help")
async def help_command(ctx: commands.Context):
    """แสดงคำสั่งทั้งหมด"""
    embed = discord.Embed(
        title="🎵 Music Bot - คำสั่งทั้งหมด",
        color=discord.Color.purple(),
    )
    commands_list = [
        ("!play / !p [ชื่อ/URL]", "ค้นหาและเล่นเพลงจาก YouTube"),
        ("!pause", "หยุดพักเพลงชั่วคราว"),
        ("!resume / !r", "เล่นเพลงต่อ"),
        ("!skip / !s", "ข้ามไปเพลงถัดไป"),
        ("!stop", "หยุดเพลงและออกจาก Voice Channel"),
        ("!queue / !q", "แสดงคิวเพลงทั้งหมด"),
        ("!nowplaying / !np", "แสดงเพลงที่กำลังเล่น"),
        ("!volume / !vol [0-100]", "ปรับระดับเสียง"),
        ("!clear", "ล้างคิวเพลงทั้งหมด"),
    ]
    for cmd, desc in commands_list:
        embed.add_field(name=f"`{cmd}`", value=desc, inline=False)
    await ctx.send(embed=embed)


# ==========================================
#  Event: Bot พร้อมใช้งาน
# ==========================================
@bot.event
async def on_ready():
    print(f"✅ บอทออนไลน์แล้ว! เข้าสู่ระบบในชื่อ: {bot.user}")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name="!help สำหรับคำสั่ง"
    ))


# ==========================================
#  รัน Bot
# ==========================================
if __name__ == "__main__":
    bot.run(TOKEN)
