# HHH คอมมู - Discord Server Landing Page

🚀 **A Modern, Responsive Discord Community Showcase Website**

---

## 📋 Features

✅ **Modern Design** - Beautiful UI with animated elements and gradients  
✅ **Fully Responsive** - Works perfectly on desktop, tablet, and mobile devices  
✅ **Live Discord Widget** - Shows real-time server stats and member list  
✅ **Editable Content** - Password-protected admin panel to manage content  
✅ **SEO Optimized** - Built-in meta tags for search engines and social sharing  
✅ **Fast Loading** - No dependencies, single HTML file  
✅ **Dark Theme** - Modern Discord-inspired color scheme  

---

## 🎯 Content Sections

1. **Hero Section** - Server name, description, and CTA button
2. **Live Stats** - Online members and total member count
3. **Features** - Why users should join your server
4. **News & Announcements** - Latest updates and promotions
5. **Discord Widget** - Live server preview with member list
6. **Editable Settings** - Admin panel with password protection

---

## 📝 How to Customize

### Open Admin Panel
Click the **⚙️ (Settings)** button at the bottom-right of the page

### Default Password
```
369
```

### Edit These Settings
- **Server Name** - Display name of your Discord server
- **Description** - Short tagline for your server
- **Guild ID** - Your Discord server ID (for widget)
- **Invite Link** - Direct Discord invite URL
- **Button Text** - CTA button label
- **News/Announcements** - Up to 3 announcement items
- **Password** - Change admin panel password

---

## 🌐 Deployment Options

### Option 1: **Vercel** (Recommended) ⭐
Free, fast, and easy deployment

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
```

**Benefits:**
- Free hosting
- Automatic HTTPS
- CDN worldwide
- One-command deployment

### Option 2: **GitHub Pages**
Free hosting directly from GitHub

1. Create a GitHub repository
2. Upload `discord-widget.html` as `index.html`
3. Enable GitHub Pages in settings
4. Your site is live!

### Option 3: **Netlify**
Drag-and-drop deployment

1. Visit [netlify.com](https://netlify.com)
2. Drag the HTML file into the deploy box
3. Get a live URL instantly

### Option 4: **Firebase Hosting**

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Initialize
firebase init hosting

# Deploy
firebase deploy
```

### Option 5: **Traditional Web Hosting**
- Upload `discord-widget.html` as `index.html` to your server
- Works with any hosting provider (GoDaddy, Bluehost, etc.)

---

## 📱 Browser Support

✅ Chrome/Brave/Edge (latest)  
✅ Firefox (latest)  
✅ Safari (latest)  
✅ Mobile browsers (iOS Safari, Chrome Android)  

---

## 🔒 Security Note

⚠️ **Important**: The password is visible in the HTML source code. This is NOT suitable for sensitive data.

For production use with sensitive information:
- Use a backend server for authentication
- Never store credentials in HTML
- Consider using Discord OAuth for admin authentication

---

## 📊 Getting Your Guild ID

1. Enable Developer Mode in Discord (User Settings → Advanced)
2. Right-click your server name
3. Copy the Server ID
4. Paste it in the admin panel under "Guild ID"

---

## 🎨 Customization Tips

### Change Colors
Edit the CSS variables at the top of the `<style>` block:

```css
:root{
  --bg:#0d0f13;           /* Background color */
  --surface:#161920;      /* Card background */
  --accent:#5865f2;       /* Main accent (Discord blue) */
  --accent2:#eb459e;      /* Secondary accent (Pink) */
  --text:#e8eaf0;         /* Text color */
  --muted:#6b7080;        /* Muted text color */
}
```

### Add More News Items
Edit the JavaScript section to add more than 3 news items

### Custom Domain
1. Deploy to Vercel/Netlify/Firebase
2. Point your domain to the deployment
3. Enable HTTPS (automatic)

---

## 📞 Support

**Discord Invite Link**: https://discord.gg/sXqUet9P

---

## 📄 License

This project is open source. Feel free to use and modify for your community!

---

**Last Updated**: May 23, 2026  
**Version**: 1.0  
**Maintenance**: Active
