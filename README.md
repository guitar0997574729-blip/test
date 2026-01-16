[form.html](https://github.com/user-attachments/files/24664323/form.html)
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">[Uploading index.html…]()

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>กรอกข้อมูลส่วนตัว</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }

        nav a:hover {
            opacity: 0.8;
        }

        main {
            max-width: 600px;
            margin: 80px auto 0;
        }

        .container {
            background: white;
            padding: 3rem;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        h1 {
            color: #667eea;
            margin-bottom: 2rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #333;
            font-weight: 500;
        }

        input, textarea, select {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            font-family: inherit;
            transition: border-color 0.3s;
        }

        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
        }

        textarea {
            resize: vertical;
            min-height: 100px;
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }

        @media (max-width: 600px) {
            .form-row {
                grid-template-columns: 1fr;
            }
        }

        .form-group-half {
            margin-bottom: 1.5rem;
        }

        .button-group {
            display: flex;
            gap: 1rem;
            justify-content: space-between;
            margin-top: 2rem;
        }

        button {
            flex: 1;
            padding: 0.75rem;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .btn-submit {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-reset {
            background: #ddd;
            color: #333;
        }

        .btn-reset:hover {
            background: #ccc;
        }

        .success-message {
            display: none;
            background: #4caf50;
            color: white;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 2rem;
            text-align: center;
        }

        .logout-btn {
            display: inline-block;
            margin-top: 2rem;
            background: #ff6b6b;
            color: white;
            padding: 0.75rem 1.5rem;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            text-align: center;
            width: 100%;
            cursor: pointer;
            border: none;
            transition: background 0.3s;
        }

        .logout-btn:hover {
            background: #ff5252;
        }

        .user-info {
            background: #f5f5f5;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 2rem;
            text-align: center;
            color: #667eea;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">✨ MyWebsite</div>
            <ul>
                <li><a href="index.html">หน้าแรก</a></li>
                <li><a href="#" onclick="logout()">ออกจากระบบ</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <div class="container">
            <div style="text-align: center; margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 2px solid #f0f0f0;">
                <p style="color: #999; font-size: 0.9rem;">เว็บไซต์ของ: <strong style="color: #667eea; font-size: 1.1rem;">พิเชฐ จันทร์แก้ว</strong></p>
            </div>

            <div id="successMessage" class="success-message">
                ✓ บันทึกข้อมูลสำเร็จ!
            </div>

            <div class="user-info" id="userInfo">
                ยินดีต้อนรับ, ผู้ใช้
            </div>

            <h1>กรอกข้อมูลส่วนตัว</h1>

            <form id="personalForm" onsubmit="handleSubmit(event)">
                <div class="form-row">
                    <div class="form-group-half">
                        <label for="firstName">ชื่อ:</label>
                        <input type="text" id="firstName" name="firstName" required>
                    </div>
                    <div class="form-group-half">
                        <label for="lastName">นามสกุล:</label>
                        <input type="text" id="lastName" name="lastName" required>
                    </div>
                </div>

                <div class="form-group">
                    <label for="email">อีเมล:</label>
                    <input type="email" id="email" name="email" readonly>
                </div>

                <div class="form-group">
                    <label for="phone">เบอร์โทรศัพท์:</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>

                <div class="form-group">
                    <label for="address">ที่อยู่:</label>
                    <textarea id="address" name="address" required></textarea>
                </div>

                <div class="form-row">
                    <div class="form-group-half">
                        <label for="city">จังหวัด:</label>
                        <input type="text" id="city" name="city" required>
                    </div>
                    <div class="form-group-half">
                        <label for="zipcode">รหัสไปรษณีย์:</label>
                        <input type="text" id="zipcode" name="zipcode" required>
                    </div>
                </div>

                <div class="form-group">
                    <label for="birthdate">วันเกิด:</label>
                    <input type="date" id="birthdate" name="birthdate" required>
                </div>

                <div class="form-group">
                    <label for="gender">เพศ:</label>
                    <select id="gender" name="gender" required>
                        <option value="">-- เลือกเพศ --</option>
                        <option value="male">ชาย</option>
                        <option value="female">หญิง</option>
                        <option value="other">อื่น ๆ</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="occupation">อาชีพ:</label>
                    <input type="text" id="occupation" name="occupation" required>
                </div>

                <div class="form-group">
                    <label for="notes">หมายเหตุ:</label>
                    <textarea id="notes" name="notes" placeholder="ข้อมูลเพิ่มเติม (ไม่บังคับ)"></textarea>
                </div>

                <div class="button-group">
                    <button type="reset" class="btn-reset">ล้างข้อมูล</button>
                    <button type="submit" class="btn-submit">บันทึกข้อมูล</button>
                </div>
            </form>

            <button class="logout-btn" onclick="logout()">ออกจากระบบ</button>
        </div>
    </main>

    <script>
        // ตรวจสอบการเข้าสู่ระบบเมื่อโหลดหน้า
        window.addEventListener('load', function() {
            const isLoggedIn = localStorage.getItem('isLoggedIn');
            const userEmail = localStorage.getItem('userEmail');

            if (isLoggedIn !== 'true' || !userEmail) {
                alert('กรุณาเข้าสู่ระบบก่อน');
                window.location.href = 'login.html';
                return;
            }

            // แสดงอีเมลในฟอร์มและในข้อมูลผู้ใช้
            document.getElementById('email').value = userEmail;
            document.getElementById('userInfo').textContent = 'ยินดีต้อนรับ, ' + userEmail;

            // โหลดข้อมูลที่บันทึกไว้ (ถ้ามี)
            loadSavedData();
        });

        function handleSubmit(event) {
            event.preventDefault();

            const formData = {
                firstName: document.getElementById('firstName').value,
                lastName: document.getElementById('lastName').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                address: document.getElementById('address').value,
                city: document.getElementById('city').value,
                zipcode: document.getElementById('zipcode').value,
                birthdate: document.getElementById('birthdate').value,
                gender: document.getElementById('gender').value,
                occupation: document.getElementById('occupation').value,
                notes: document.getElementById('notes').value,
                timestamp: new Date().toLocaleString('th-TH')
            };

            // บันทึกข้อมูลใน localStorage
            localStorage.setItem('personalData', JSON.stringify(formData));

            // แสดงข้อความสำเร็จ
            const successMsg = document.getElementById('successMessage');
            successMsg.style.display = 'block';

            setTimeout(() => {
                // ไปยังหน้าร้านค้า
                window.location.href = 'shop.html';
            }, 2000);

            console.log('บันทึกข้อมูล:', formData);
        }

        function loadSavedData() {
            const savedData = localStorage.getItem('personalData');
            if (savedData) {
                const data = JSON.parse(savedData);
                document.getElementById('firstName').value = data.firstName || '';
                document.getElementById('lastName').value = data.lastName || '';
                document.getElementById('phone').value = data.phone || '';
                document.getElementById('address').value = data.address || '';
                document.getElementById('city').value = data.city || '';
                document.getElementById('zipcode').value = data.zipcode || '';
                document.getElementById('birthdate').value = data.birthdate || '';
                document.getElementById('gender').value = data.gender || '';
                document.getElementById('occupation').value = data.occupation || '';
                document.getElementById('notes').value = data.notes || '';
            }
        }

        function logout() {
            if (confirm('คุณต้องการออกจากระบบใช่หรือไม่?')) {
                localStorage.removeItem('isLoggedIn');
                localStorage.removeItem('userEmail');
                window.location.href = 'index.html';
            }
        }
    </script>
</body>
</html>
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>เว็บไซต์ของฉัน</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }

        nav a:hover {
            opacity: 0.8;
        }

        main {
            margin-top: 60px;
        }

        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 6rem 2rem;
            text-align: center;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }

        .btn {
            display: inline-block;
            background: white;
            color: #667eea;
            padding: 0.75rem 2rem;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
            border: none;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-card h3 {
            color: #667eea;
            margin-bottom: 1rem;
        }

        .feature-card p {
            color: #666;
        }

        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }

        footer p {
            margin: 0.5rem 0;
        }

        .admin-login-btn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 60px;
            height: 60px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 50%;
            font-size: 2rem;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: all 0.3s;
            z-index: 50;
        }

        .admin-login-btn:hover {
            background: #764ba2;
            transform: scale(1.1);
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }

        .admin-login-btn:active {
            transform: scale(0.95);
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">✨ MyWebsite</div>
            <ul>
                <li><a href="#home">หน้าแรก</a></li>
                <li><a href="#features">ฟีเจอร์</a></li>
                <li><a href="shop.html">ร้านค้า</a></li>
                <li><a href="#contact">ติดต่อ</a></li>
                <li><a href="login.html">เข้าสู่ระบบ</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home" class="hero">
            <h1>ยินดีต้อนรับ</h1>
            <p>สร้างเว็บไซต์ที่สวยงามและมีประสิทธิภาพ</p>
            <button class="btn" onclick="goToLogin()">เริ่มต้นใช้งาน</button>
        </section>

        <section id="features" class="container">
            <h2 style="text-align: center; margin-bottom: 2rem;">ฟีเจอร์หลัก</h2>
            <div class="features">
                <div class="feature-card">
                    <h3>🎨 ดีไซน์สวยงาม</h3>
                    <p>เว็บไซต์ที่มีดีไซน์สมัยใหม่และตัดสินใจได้ง่าย</p>
                </div>
                <div class="feature-card">
                    <h3>📱 ตอบสนองได้</h3>
                    <p>ทำงานได้ดีในทุกอุปกรณ์ เทเล็ต โทรศัพท์ และเดสก์ทอป</p>
                </div>
                <div class="feature-card">
                    <h3>⚡ เร็ว</h3>
                    <p>โหลดเร็วและสำรองข้อมูลด้วยประสิทธิภาพสูง</p>
                </div>
            </div>
        </section>

        <section id="about" class="container" style="background: #f0f4ff; margin: 3rem 0; padding: 3rem 2rem; border-radius: 8px;">
            <h2 style="text-align: center; margin-bottom: 2rem; color: #667eea;">เกี่ยวกับเราและเจ้าของเว็บไซต์</h2>
            <div style="text-align: center; background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                <h3 style="color: #667eea; margin-bottom: 1rem;">👤 เจ้าของเว็บไซต์</h3>
                <p style="font-size: 1.5rem; color: #333; font-weight: bold; margin-bottom: 0.5rem;">พิเชฐ จันทร์แก้ว</p>
                <p style="color: #666;">ผู้สร้างและผู้ดูแลเว็บไซต์นี้</p>
            </div>
        </section>

        <section id="contact" class="container" style="background: #f5f5f5; margin: 3rem 0; padding: 3rem 2rem; border-radius: 8px; text-align: center;">
            <h2>ติดต่อเรา</h2>
            <p style="margin: 1rem 0; color: #666;">ติดต่อ: <strong>พิเชฐ จันทร์แก้ว</strong></p>
            <p style="margin: 1rem 0; color: #666;">มีคำถามหรือสนใจมากขึ้น? โปรดติดต่อเรา</p>
            <button class="btn" onclick="showMessage()">ส่งข้อความ</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 MyWebsite - พิเชฐ จันทร์แก้ว</p>
        <p>ออกแบบด้วย ❤️</p>
    </footer>

    <!-- ปุ่มเข้า Admin ลับ (ซ่อนจากลูกค้า) -->
    <button class="admin-login-btn" onclick="checkAdminLogin()" title="Admin Login"></button>

    <script>
        function handleClick() {
            alert('ยินดีต้อนรับ! คุณได้คลิกปุ่มเริ่มต้นใช้งาน');
        }

        function goToLogin() {
            window.location.href = 'login.html';
        }

        function showMessage() {
            alert('ขอบคุณที่ติดต่อเรา! เราจะตอบกลับให้ในเร็ว ๆ นี้');
        }

        // เพิ่มผลเบลอเมื่อเลื่อนหน้า
        window.addEventListener('scroll', function() {
            const header = document.querySelector('header');
            if (window.scrollY > 50) {
                header.style.boxShadow = '0 4px 10px rgba(0,0,0,0.2)';
            } else {
                header.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
            }
        });

        function checkAdminLogin() {
            const isAdmin = localStorage.getItem('isAdmin');
            const userEmail = localStorage.getItem('userEmail');
            const AUTHORIZED_ADMIN_EMAIL = 'guitar0997574729@gmail.com';

            if (isAdmin === 'true' && userEmail === AUTHORIZED_ADMIN_EMAIL) {
                // ถ้าเป็น Admin ให้ไปหน้า Admin Dashboard
                window.location.href = 'admin.html';
            } else {
                // ถ้าไม่ใช่ Admin ให้ไปหน้า Login
                window.location.href = 'login.html';
            }
        }
    </script>
</body>
</html>

<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>เข้าสู่ระบบ</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }

        nav a:hover {
            opacity: 0.8;
        }

        .container {
            background: white;
            padding: 3rem;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 100%;
            max-width: 400px;
            margin-top: 60px;
        }

        h1 {
            text-align: center;
            color: #667eea;
            margin-bottom: 2rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #333;
            font-weight: 500;
        }

        input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
        }

        button {
            width: 100%;
            padding: 0.75rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .link-container {
            text-align: center;
            margin-top: 1.5rem;
        }

        .link-container p {
            color: #666;
        }

        .link-container a {
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }

        .link-container a:hover {
            text-decoration: underline;
        }

        .back-link {
            display: inline-block;
            margin-top: 1.5rem;
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }

        .back-link:hover {
            text-decoration: underline;
        }

        .admin-notice {
            background: #fff3cd;
            border: 1px solid #ffc107;
            color: #856404;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1.5rem;
            font-size: 0.9rem;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">✨ MyWebsite</div>
            <ul>
                <li><a href="index.html">หน้าแรก</a></li>
                <li><a href="login.html">เข้าสู่ระบบ</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <h1>เข้าสู่ระบบ</h1>
        <p style="text-align: center; color: #999; font-size: 0.9rem; margin-bottom: 2rem;">เว็บไซต์ของ: <strong style="color: #667eea;">พิเชฐ จันทร์แก้ว</strong></p>
        
        <div class="admin-notice">
            💡 <strong>ทดสอบ Admin:</strong> guitar0997574729@gmail.com (สามารถเข้า Admin Dashboard ได้)
        </div>

        <form id="loginForm" onsubmit="handleLogin(event)">
            <div class="form-group">
                <label for="email">อีเมล:</label>
                <input type="email" id="email" name="email" required>
            </div>

            <div class="form-group">
                <label for="password">รหัสผ่าน:</label>
                <input type="password" id="password" name="password" required>
            </div>

            <button type="submit">เข้าสู่ระบบ</button>
        </form>

        <div class="link-container">
            <p>ยังไม่มีบัญชี? <a href="register.html">สมัครสมาชิก</a></p>
        </div>

        <a href="index.html" class="back-link">← กลับไปหน้าแรก</a>
    </div>

    <script>
        // กำหนด Admin Email และ Password สำหรับระบบ Admin
        const ADMIN_EMAIL = 'guitar0997574729@gmail.com';
        const ADMIN_PASSWORD = 'admin2025'; // รหัสผ่าน admin secret

        function handleLogin(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            if (email && password) {
                // ตรวจสอบว่าเป็นอีเมล admin หรือไม่
                if (email === ADMIN_EMAIL) {
                    // ตรวจสอบรหัสผ่าน admin
                    if (password === ADMIN_PASSWORD) {
                        alert('✓ ยินดีต้อนรับ Admin! เข้าระบบสำเร็จ');
                        localStorage.setItem('userEmail', email);
                        localStorage.setItem('isLoggedIn', 'true');
                        localStorage.setItem('isAdmin', 'true');
                        localStorage.setItem('adminLoginTime', new Date().getTime());
                        // นำไปยังแดชบอร์ด admin
                        window.location.href = 'admin.html';
                    } else {
                        alert('❌ รหัสผ่าน Admin ไม่ถูกต้อง!');
                    }
                } else {
                    alert('✓ ยินดีต้อนรับ! ' + email);
                    localStorage.setItem('userEmail', email);
                    localStorage.setItem('isLoggedIn', 'true');
                    localStorage.setItem('isAdmin', 'false');
                    // นำไปยังหน้าฟอร์มกรอกข้อมูล
                    window.location.href = 'form.html';
                }
            } else {
                alert('❌ กรุณากรอกอีเมลและรหัสผ่าน');
            }
        }

        // ตรวจสอบว่าผู้ใช้เข้าสู่ระบบแล้ว
        window.addEventListener('load', function() {
            const isLoggedIn = localStorage.getItem('isLoggedIn');
            if (isLoggedIn === 'true') {
                // ถ้าเข้าสู่ระบบแล้ว ให้ไปหน้า form.html โดยตรง
                // window.location.href = 'form.html';
            }
        });
    </script>
</body>
</html>
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ประวัติการสั่งซื้อ</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
        }

        .header {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header h1 {
            color: #667eea;
            font-size: 2rem;
        }

        .back-btn {
            background: #667eea;
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.3s;
        }

        .back-btn:hover {
            background: #764ba2;
        }

        .orders-list {
            display: grid;
            gap: 1.5rem;
        }

        .order-card {
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .order-card:hover {
            transform: translateY(-2px);
        }

        .order-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 1rem;
            margin-bottom: 1rem;
        }

        .order-id {
            font-size: 1.2rem;
            font-weight: bold;
            color: #667eea;
        }

        .order-date {
            color: #999;
            font-size: 0.9rem;
        }

        .order-status {
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9rem;
        }

        .status-processing {
            background: #fff3cd;
            color: #856404;
        }

        .status-completed {
            background: #d4edda;
            color: #155724;
        }

        .status-shipped {
            background: #d1ecf1;
            color: #0c5460;
        }

        .order-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-bottom: 1rem;
        }

        .order-section {
            background: #f9f9f9;
            padding: 1rem;
            border-radius: 5px;
        }

        .order-section h3 {
            color: #667eea;
            margin-bottom: 0.75rem;
            font-size: 0.95rem;
        }

        .order-section p {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }

        .items-list {
            grid-column: 1 / -1;
        }

        .item-row {
            display: grid;
            grid-template-columns: 1fr 100px 100px 100px;
            gap: 1rem;
            padding: 0.75rem 0;
            border-bottom: 1px solid #eee;
            align-items: center;
            font-size: 0.9rem;
        }

        .item-row:last-child {
            border-bottom: none;
        }

        .item-name {
            color: #333;
            font-weight: 500;
        }

        .item-qty {
            text-align: center;
            color: #666;
        }

        .item-price {
            text-align: right;
            color: #666;
        }

        .item-subtotal {
            text-align: right;
            color: #667eea;
            font-weight: bold;
        }

        .order-summary {
            grid-column: 1 / -1;
            background: white;
            padding: 1rem;
            border-radius: 5px;
            display: grid;
            grid-template-columns: 1fr 150px;
            gap: 1rem;
            align-items: center;
        }

        .summary-row {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            font-size: 0.9rem;
            color: #666;
        }

        .summary-total {
            font-weight: bold;
            font-size: 1.1rem;
            color: #667eea;
            border-top: 2px solid #eee;
            padding-top: 0.5rem;
            margin-top: 0.5rem;
        }

        .empty-message {
            background: white;
            padding: 3rem 2rem;
            border-radius: 10px;
            text-align: center;
            color: #999;
        }

        .empty-message p {
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }

        .shop-btn {
            background: #667eea;
            color: white;
            padding: 0.75rem 2rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            font-size: 1rem;
            transition: background 0.3s;
        }

        .shop-btn:hover {
            background: #764ba2;
        }

        @media (max-width: 768px) {
            .order-header {
                flex-direction: column;
                align-items: flex-start;
            }

            .order-content {
                grid-template-columns: 1fr;
            }

            .item-row {
                grid-template-columns: 1fr;
            }

            .item-row span {
                display: inline-block;
                margin-right: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📦 ประวัติการสั่งซื้อของฉัน</h1>
            <button class="back-btn" onclick="goToShop()">← กลับไปร้านค้า</button>
        </div>

        <div id="ordersList" class="orders-list">
            <!-- ประวัติการสั่งซื้อจะแทรกที่นี่ -->
        </div>
    </div>

    <script>
        function loadOrders() {
            const orderHistory = JSON.parse(localStorage.getItem('orderHistory') || '[]');
            const userEmail = localStorage.getItem('userEmail');
            const ordersContainer = document.getElementById('ordersList');

            if (!userEmail) {
                ordersContainer.innerHTML = `
                    <div class="empty-message">
                        <p>⚠️ กรุณาเข้าสู่ระบบเพื่อดูประวัติการสั่งซื้อ</p>
                        <button class="shop-btn" onclick="window.location.href='login.html'">เข้าสู่ระบบ</button>
                    </div>
                `;
                return;
            }

            if (orderHistory.length === 0) {
                ordersContainer.innerHTML = `
                    <div class="empty-message">
                        <p>📭 ยังไม่มีประวัติการสั่งซื้อ</p>
                        <p style="font-size: 0.9rem; margin-bottom: 2rem;">เริ่มช้อปปิ้งเพื่อดูคำสั่งซื้อของคุณที่นี่</p>
                        <button class="shop-btn" onclick="goToShop()">ไปร้านค้า</button>
                    </div>
                `;
                return;
            }

            // แสดงประวัติการสั่งซื้อแบบย้อนกลับ (ล่าสุดก่อน)
            orderHistory.reverse().forEach(order => {
                const orderCard = createOrderCard(order);
                ordersContainer.appendChild(orderCard);
            });
        }

        function createOrderCard(order) {
            const card = document.createElement('div');
            card.className = 'order-card';

            const statusClass = `status-${order.status.replace(/[^a-zA-Z]/g, '').toLowerCase()}`;
            const itemsHTML = order.items.map(item => `
                <div class="item-row">
                    <div class="item-name">${item.emoji} ${item.name}</div>
                    <div class="item-qty">x${item.quantity}</div>
                    <div class="item-price">฿${item.price}</div>
                    <div class="item-subtotal">฿${(item.priceNumber * item.quantity).toLocaleString()}</div>
                </div>
            `).join('');

            card.innerHTML = `
                <div class="order-header">
                    <div>
                        <div class="order-id">#${order.orderId}</div>
                        <div class="order-date">📅 ${order.orderDate}</div>
                    </div>
                    <span class="order-status ${statusClass}">${order.status}</span>
                </div>

                <div class="order-content">
                    <div class="order-section">
                        <h3>🏠 ที่อยู่ส่ง</h3>
                        <p>${order.recipient}</p>
                        <p>${order.address}, ${order.province} ${order.zipcode}</p>
                        <p>📞 ${order.phone}</p>
                    </div>

                    <div class="order-section">
                        <h3>💳 วิธีการชำระเงิน</h3>
                        <p>${getPaymentMethodName(order.paymentMethod)}</p>
                        <h3 style="margin-top: 1rem;">📝 หมายเหตุ</h3>
                        <p>${order.notes || 'ไม่มี'}</p>
                    </div>

                    <div class="items-list">
                        <h3 style="color: #667eea; margin-bottom: 1rem;">📦 สินค้า</h3>
                        ${itemsHTML}
                    </div>

                    <div class="order-summary">
                        <div>
                            <div class="summary-row">
                                <span>ยอดรวม:</span>
                                <span>฿${order.subtotal.toLocaleString()}</span>
                            </div>
                            <div class="summary-row">
                                <span>ส่วนลด (10%):</span>
                                <span>-฿${order.discount.toLocaleString()}</span>
                            </div>
                            <div class="summary-row">
                                <span>ค่าจัดส่ง:</span>
                                <span>฿${order.shipping}</span>
                            </div>
                            <div class="summary-total">
                                รวมทั้งสิ้น: ฿${order.total.toLocaleString()}
                            </div>
                        </div>
                    </div>
                </div>
            `;

            return card;
        }

        function getPaymentMethodName(method) {
            const methods = {
                'bank': '💳 โอนเงินจากธนาคาร',
                'promptpay': '🤖 PromptPay QR Code',
                'cod': '🚚 ชำระเงินปลายทาง',
                'credit': '💰 บัตรเครดิต'
            };
            return methods[method] || method;
        }

        function goToShop() {
            window.location.href = 'shop.html';
        }

        // โหลดประวัติการสั่งซื้อเมื่อเปิดหน้า
        window.addEventListener('load', loadOrders);
    </script>
</body>
</html>

<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>สมัครสมาชิก</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }

        nav a:hover {
            opacity: 0.8;
        }

        .container {
            background: white;
            padding: 3rem;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 100%;
            max-width: 450px;
            margin-top: 60px;
        }

        h1 {
            text-align: center;
            color: #667eea;
            margin-bottom: 2rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #333;
            font-weight: 500;
        }

        input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
        }

        button {
            width: 100%;
            padding: 0.75rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .link-container {
            text-align: center;
            margin-top: 1.5rem;
        }

        .link-container p {
            color: #666;
        }

        .link-container a {
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }

        .link-container a:hover {
            text-decoration: underline;
        }

        .back-link {
            display: inline-block;
            margin-top: 1.5rem;
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }

        .back-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">✨ MyWebsite</div>
            <ul>
                <li><a href="index.html">หน้าแรก</a></li>
                <li><a href="login.html">เข้าสู่ระบบ</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <h1>สมัครสมาชิก</h1>
        <p style="text-align: center; color: #999; font-size: 0.9rem; margin-bottom: 2rem;">เว็บไซต์ของ: <strong style="color: #667eea;">พิเชฐ จันทร์แก้ว</strong></p>
        <form id="registerForm" onsubmit="handleRegister(event)">
            <div class="form-group">
                <label for="fullname">ชื่อเต็ม:</label>
                <input type="text" id="fullname" name="fullname" required>
            </div>

            <div class="form-group">
                <label for="email">อีเมล:</label>
                <input type="email" id="email" name="email" required>
            </div>

            <div class="form-group">
                <label for="phone">เบอร์โทรศัพท์:</label>
                <input type="tel" id="phone" name="phone" required>
            </div>

            <div class="form-group">
                <label for="password">รหัสผ่าน:</label>
                <input type="password" id="password" name="password" required>
            </div>

            <div class="form-group">
                <label for="confirmPassword">ยืนยันรหัสผ่าน:</label>
                <input type="password" id="confirmPassword" name="confirmPassword" required>
            </div>

            <button type="submit">สมัครสมาชิก</button>
        </form>

        <div class="link-container">
            <p>มีบัญชีแล้ว? <a href="login.html">เข้าสู่ระบบ</a></p>
        </div>

        <a href="index.html" class="back-link">← กลับไปหน้าแรก</a>
    </div>

    <script>
        function handleRegister(event) {
            event.preventDefault();
            const fullname = document.getElementById('fullname').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            if (password !== confirmPassword) {
                alert('รหัสผ่านไม่ตรงกัน');
                return;
            }

            alert('สมัครสมาชิกสำเร็จ! ยินดีต้อนรับ ' + fullname);
            localStorage.setItem('userEmail', email);
            localStorage.setItem('isLoggedIn', 'true');
            window.location.href = 'form.html';
        }
    </script>
</body>
</html>
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ร้านค้าของพิเชฐ จันทร์แก้ว</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }

        nav a:hover {
            opacity: 0.8;
        }

        main {
            margin-top: 60px;
            padding: 2rem;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header-section {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }

        .header-section h1 {
            color: #667eea;
            margin-bottom: 0.5rem;
            font-size: 2.5rem;
        }

        .header-section p {
            color: #666;
            font-size: 1.1rem;
        }

        .owner-info {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 2rem;
        }

        .owner-info h2 {
            margin-bottom: 0.5rem;
        }

        .filters {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
            justify-content: center;
        }

        .filter-btn {
            padding: 0.75rem 1.5rem;
            border: 2px solid #667eea;
            background: white;
            color: #667eea;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }

        .filter-btn.active {
            background: #667eea;
            color: white;
        }

        .filter-btn:hover {
            background: #667eea;
            color: white;
        }

        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 2rem;
        }

        .product-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        }

        .product-image {
            width: 100%;
            height: 250px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            color: white;
        }

        .product-info {
            padding: 1.5rem;
        }

        .product-name {
            font-size: 1.2rem;
            color: #333;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        .product-description {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 1rem;
            min-height: 50px;
        }

        .product-price {
            font-size: 1.5rem;
            color: #667eea;
            font-weight: bold;
            margin-bottom: 1rem;
        }

        .product-category {
            display: inline-block;
            background: #f0f0f0;
            color: #666;
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            margin-bottom: 1rem;
        }

        .btn-buy {
            width: 100%;
            padding: 0.75rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .btn-buy:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }

        .back-link {
            display: inline-block;
            margin-bottom: 2rem;
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
            background: white;
            padding: 0.75rem 1.5rem;
            border-radius: 5px;
        }

        .back-link:hover {
            text-decoration: underline;
        }

        .empty-state {
            text-align: center;
            padding: 3rem 2rem;
            color: #666;
        }

        .empty-state p {
            font-size: 1.1rem;
        }

        .admin-chat-buttons {
            display: flex;
            gap: 1rem;
            justify-content: flex-start;
            margin-bottom: 2rem;
        }

        .admin-btn, .chat-btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }

        .admin-btn {
            background: #28a745;
            color: white;
        }

        .admin-btn:hover {
            background: #218838;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(40, 167, 69, 0.3);
        }

        .chat-btn {
            background: #17a2b8;
            color: white;
        }

        .chat-btn:hover {
            background: #138496;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(23, 162, 184, 0.3);
        }

        .admin-login-btn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 60px;
            height: 60px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 50%;
            font-size: 2rem;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: all 0.3s;
            z-index: 50;
        }

        .admin-login-btn:hover {
            background: #764ba2;
            transform: scale(1.1);
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }

        .admin-login-btn:active {
            transform: scale(0.95);
        }

        .cart-icon {
            position: relative;
            cursor: pointer;
            font-size: 1.5rem;
        }

        .cart-count {
            position: absolute;
            top: -8px;
            right: -8px;
            background: #ff6b6b;
            color: white;
            border-radius: 50%;
            width: 24px;
            height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">🛍️ ร้านค้า</div>
            <ul>
                <li><a href="index.html">หน้าแรก</a></li>
                <li><a href="shop.html">ร้านค้า</a></li>
                <li style="cursor: pointer; position: relative;" onclick="goToCart()">
                    <span class="cart-icon">
                        🛒
                        <span class="cart-count" id="cartBadge" style="display:none;">0</span>
                    </span>
                </li>
                <li><a href="#" onclick="logout()">ออกจากระบบ</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <div class="container">
            <div class="owner-info">
                <h2>🏪 ร้านค้าของ พิเชฐ จันทร์แก้ว</h2>
                <p>ยินดีต้อนรับสู่ร้านค้าออนไลน์ของเรา</p>
            </div>

            <div class="header-section">
                <h1>สินค้าของเรา</h1>
                <p>เลือกซื้อสินค้าที่คุณต้องการจากหมวดหมู่ด้านล่าง</p>
            </div>

            <div class="filters">
                <button class="filter-btn active" onclick="filterProducts('all')">ทั้งหมด</button>
                <button class="filter-btn" onclick="filterProducts('electronics')">อิเล็กทรอนิกส์</button>
                <button class="filter-btn" onclick="filterProducts('clothing')">เสื้อผ้า</button>
                <button class="filter-btn" onclick="filterProducts('books')">หนังสือ</button>
                <button class="filter-btn" onclick="filterProducts('home')">สินค้าบ้าน</button>
            </div>

            <div class="admin-chat-buttons">
                <button class="admin-btn" onclick="goToAdmin()">⚙️ Admin Dashboard</button>
                <button class="chat-btn" onclick="goToChat()">💬 แชทกับเจ้าของ</button>
                <button class="chat-btn" onclick="goToOrders()">📦 ประวัติการสั่งซื้อ</button>
            </div>

            <div class="products" id="productsContainer">
                <!-- สินค้าจะถูกแทรกที่นี่ -->
            </div>
        </div>
    </main>

    <footer>
        <p>&copy; 2026 ร้านค้าของพิเชฐ จันทร์แก้ว</p>
        <p>ออกแบบด้วย ❤️</p>
    </footer>

    <!-- ปุ่มเข้า Admin ลับ (ซ่อนจากลูกค้า) -->
    <button class="admin-login-btn" onclick="checkAdminLogin()" title="Admin Login"></button>

    <script>
        const products = [
            {
                id: 1,
                name: 'หูฟัง Bluetooth',
                price: '1,299 บาท',
                category: 'electronics',
                emoji: '🎧',
                description: 'หูฟังไร้สายคุณภาพสูง เสียงชัด เบาสบาย'
            },
            {
                id: 2,
                name: 'พาวเวอร์แบงก์',
                price: '899 บาท',
                category: 'electronics',
                emoji: '🔋',
                description: 'แบตสำรองพลังงาน 20000mAh ชาร์จเร็ว'
            },
            {
                id: 3,
                name: 'เสื้อยืดสีเขียว',
                price: '399 บาท',
                category: 'clothing',
                emoji: '👕',
                description: 'เสื้อยืด 100% ผ้าคอตตอน นุ่มสบาย'
            },
            {
                id: 4,
                name: 'กางเกงยีนส์',
                price: '599 บาท',
                category: 'clothing',
                emoji: '👖',
                description: 'กางเกงยีนส์เข้ารูป ดีไซน์สมัยใหม่'
            },
            {
                id: 5,
                name: 'Python Programming',
                price: '499 บาท',
                category: 'books',
                emoji: '📚',
                description: 'หนังสือสอนโปรแกรมมิ่ง Python สำหรับผู้เริ่มต้น'
            },
            {
                id: 6,
                name: 'Web Development Guide',
                price: '599 บาท',
                category: 'books',
                emoji: '📖',
                description: 'คู่มือการพัฒนาเว็บไซต์ HTML CSS JavaScript'
            },
            {
                id: 7,
                name: 'โคมไฟ LED',
                price: '299 บาท',
                category: 'home',
                emoji: '💡',
                description: 'โคมไฟ LED ประหยัดไฟ ปรับสว่างได้'
            },
            {
                id: 8,
                name: 'พูลหมอน',
                price: '199 บาท',
                category: 'home',
                emoji: '🛏️',
                description: 'หมอนหนุนสุดนุ่ม เหมาะสำหรับพักผ่อน'
            },
            {
                id: 9,
                name: 'กระบอกน้ำ',
                price: '299 บาท',
                category: 'home',
                emoji: '🥤',
                description: 'กระบอกน้ำสแตนเลส เก็บความเย็น 24 ชั่วโมง'
            }
        ];

        let filteredCategory = 'all';

        function displayProducts(category) {
            const container = document.getElementById('productsContainer');
            container.innerHTML = '';

            const filtered = category === 'all' 
                ? products 
                : products.filter(p => p.category === category);

            if (filtered.length === 0) {
                container.innerHTML = '<div class="empty-state"><p>ไม่มีสินค้าในหมวดหมู่นี้</p></div>';
                return;
            }

            filtered.forEach(product => {
                const card = document.createElement('div');
                card.className = 'product-card';
                card.innerHTML = `
                    <div class="product-image">${product.emoji}</div>
                    <div class="product-info">
                        <div class="product-category">${getCategoryName(product.category)}</div>
                        <div class="product-name">${product.name}</div>
                        <div class="product-description">${product.description}</div>
                        <div class="product-price">${product.price}</div>
                        <button class="btn-buy" onclick="addToCart(${product.id}, '${product.name}', '${product.price}', '${product.emoji}')">เพิ่มลงตะกร้า</button>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        function getCategoryName(category) {
            const names = {
                'electronics': 'อิเล็กทรอนิกส์',
                'clothing': 'เสื้อผ้า',
                'books': 'หนังสือ',
                'home': 'สินค้าบ้าน'
            };
            return names[category] || 'อื่น ๆ';
        }

        function filterProducts(category) {
            filteredCategory = category;
            displayProducts(category);

            // อัพเดตสถานะปุ่ม
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
        }

        function addToCart(id, productName, price, emoji) {
            // ดึงข้อมูลตะกร้า
            let cart = JSON.parse(localStorage.getItem('cart') || '[]');
            
            // ตรวจสอบว่าสินค้านี้มีในตะกร้าแล้วหรือไม่
            const existingItem = cart.find(item => item.id === id);
            
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                // เอาเฉพาะตัวเลขราคา
                const priceNumber = parseFloat(price.replace(/,/g, ''));
                cart.push({
                    id: id,
                    name: productName,
                    price: price,
                    priceNumber: priceNumber,
                    emoji: emoji,
                    quantity: 1
                });
            }
            
            // บันทึกตะกร้า
            localStorage.setItem('cart', JSON.stringify(cart));
            
            // อัพเดตแบดจ์ตะกร้า
            updateCartBadge();
            
            // แสดงข้อความสำเร็จ
            alert(`เพิ่ม "${productName}" ลงตะกร้าแล้ว`);
        }

        function updateCartBadge() {
            const cart = JSON.parse(localStorage.getItem('cart') || '[]');
            const badge = document.getElementById('cartBadge');
            const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
            
            if (totalItems > 0) {
                badge.textContent = totalItems;
                badge.style.display = 'flex';
            } else {
                badge.style.display = 'none';
            }
        }

        function goToCart() {
            window.location.href = 'cart.html';
        }

        function goToChat() {
            window.location.href = 'chat.html';
        }

        function goToOrders() {
            window.location.href = 'orders.html';
        }

        function logout() {
            if (confirm('คุณต้องการออกจากระบบใช่หรือไม่?')) {
                localStorage.removeItem('isLoggedIn');
                localStorage.removeItem('userEmail');
                window.location.href = 'index.html';
            }
        }

        function checkAdminLogin() {
            const isAdmin = localStorage.getItem('isAdmin');
            const userEmail = localStorage.getItem('userEmail');
            const AUTHORIZED_ADMIN_EMAIL = 'guitar0997574729@gmail.com';

            if (isAdmin === 'true' && userEmail === AUTHORIZED_ADMIN_EMAIL) {
                // ถ้าเป็น Admin ให้ไปหน้า Admin Dashboard
                window.location.href = 'admin.html';
            } else {
                // ถ้าไม่ใช่ Admin ให้ไปหน้า Login
                window.location.href = 'login.html';
            }
        }

        // โหลดสินค้าเมื่อเปิดหน้า
        window.addEventListener('load', function() {
            const isLoggedIn = localStorage.getItem('isLoggedIn');
            if (isLoggedIn !== 'true') {
                // ถ้ายังไม่เข้าสู่ระบบ ให้ดูได้เพียงอย่างเดียว
            }
            displayProducts('all');
            updateCartBadge();
        });
    </script>
</body>
</html>
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
            display: flex;
        }

        .sidebar {
            width: 250px;
            background: linear-gradient(135deg, #323f78 0%, #764ba2 100%);
            color: white;
            padding: 2rem 1rem;
            min-height: 100vh;
            position: fixed;
            left: 0;
            top: 0;
            overflow-y: auto;
        }

        .sidebar h1 {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            text-align: center;
            border-bottom: 2px solid rgba(255,255,255,0.3);
            padding-bottom: 1rem;
        }

        .sidebar ul {
            list-style: none;
        }

        .sidebar li {
            margin-bottom: 1rem;
        }

        .sidebar a {
            color: white;
            text-decoration: none;
            display: block;
            padding: 0.75rem 1rem;
            border-radius: 5px;
            transition: background 0.3s;
        }

        .sidebar a:hover,
        .sidebar a.active {
            background: rgba(255,255,255,0.2);
        }

        main {
            margin-left: 250px;
            flex: 1;
            padding: 2rem;
        }

        .header {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header h1 {
            color: #667eea;
            font-size: 2rem;
        }

        .logout-btn {
            background: #ff6b6b;
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.3s;
        }

        .logout-btn:hover {
            background: #ff5252;
        }

        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .stat-card {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            border-top: 4px solid #667eea;
        }

        .stat-card h3 {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }

        .stat-number {
            font-size: 2.5rem;
            color: #667eea;
            font-weight: bold;
        }

        .content-section {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: none;
        }

        .content-section.active {
            display: block;
        }

        .content-section h2 {
            color: #667eea;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 1rem;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        table th {
            background: #f5f5f5;
            padding: 1rem;
            text-align: left;
            color: #667eea;
            font-weight: bold;
            border-bottom: 2px solid #ddd;
        }

        table td {
            padding: 1rem;
            border-bottom: 1px solid #eee;
        }

        table tr:hover {
            background: #f9f9f9;
        }

        .status-badge {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
        }

        .status-active {
            background: #d4edda;
            color: #155724;
        }

        .status-inactive {
            background: #f8d7da;
            color: #721c24;
        }

        .action-btn {
            padding: 0.5rem 1rem;
            margin-right: 0.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s;
        }

        .btn-edit {
            background: #007bff;
            color: white;
        }

        .btn-edit:hover {
            background: #0056b3;
        }

        .btn-delete {
            background: #dc3545;
            color: white;
        }

        .btn-delete:hover {
            background: #c82333;
        }

        .btn-message {
            background: #28a745;
            color: white;
        }

        .btn-message:hover {
            background: #218838;
        }

        @media (max-width: 768px) {
            .sidebar {
                width: 100%;
                height: auto;
                position: relative;
                min-height: auto;
            }

            main {
                margin-left: 0;
                padding: 1rem;
            }

            .header {
                flex-direction: column;
                gap: 1rem;
            }

            .dashboard {
                grid-template-columns: 1fr;
            }
        }

        .message-list {
            max-height: 600px;
            overflow-y: auto;
        }

        .message-item {
            background: #f9f9f9;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
            border-left: 4px solid #667eea;
        }

        .message-item strong {
            color: #667eea;
        }

        .message-item p {
            margin-top: 0.5rem;
            color: #666;
        }

        .message-item small {
            color: #999;
        }

        .customer-detail {
            background: #f9f9f9;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            border-left: 4px solid #667eea;
        }

        .customer-detail h4 {
            color: #667eea;
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }

        .detail-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .detail-item {
            background: white;
            padding: 1rem;
            border-radius: 5px;
        }

        .detail-label {
            font-size: 0.85rem;
            color: #999;
            font-weight: 500;
            margin-bottom: 0.3rem;
        }

        .detail-value {
            color: #333;
            font-weight: bold;
        }

        @media (max-width: 768px) {
            .detail-row {
                grid-template-columns: 1fr;
            }
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.7);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }

        .modal.show {
            display: flex;
        }

        .modal-content {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            width: 90%;
            max-width: 500px;
            max-height: 90vh;
            overflow-y: auto;
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 1rem;
        }

        .modal-header h3 {
            color: #667eea;
            font-size: 1.5rem;
        }

        .modal-close {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: #999;
        }

        .modal-form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .modal-form label {
            display: block;
            margin-bottom: 0.3rem;
            color: #333;
            font-weight: 500;
            font-size: 0.9rem;
        }

        .modal-form input,
        .modal-form textarea {
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            font-family: inherit;
            transition: border-color 0.3s;
        }

        .modal-form input:focus,
        .modal-form textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
        }

        .modal-buttons {
            display: flex;
            gap: 1rem;
            justify-content: flex-end;
            margin-top: 1.5rem;
        }

        .modal-btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }

        .modal-btn-save {
            background: #28a745;
            color: white;
        }

        .modal-btn-save:hover {
            background: #218838;
        }

        .modal-btn-cancel {
            background: #ddd;
            color: #333;
        }

        .modal-btn-cancel:hover {
            background: #ccc;
        }
    </style>
</head>
<body>
    <aside class="sidebar">
        <h1>⚙️ Admin</h1>
        <ul>
            <li><a href="#" onclick="showSection('dashboard')" class="nav-link active">📊 Dashboard</a></li>
            <li><a href="#" onclick="showSection('customers')" class="nav-link">👤 ข้อมูลลูกค้า</a></li>
            <li><a href="#" onclick="showSection('users')" class="nav-link">👥 ผู้ใช้ทั้งหมด</a></li>
            <li><a href="#" onclick="showSection('products')" class="nav-link">📦 สินค้า</a></li>
            <li><a href="#" onclick="showSection('chat')" class="nav-link">💬 ข้อความ</a></li>
            <li><a href="#" onclick="logout()" class="nav-link">🚪 ออกจากระบบ</a></li>
        </ul>
    </aside>

    <main>
        <div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 1rem; margin: 1rem; border-radius: 5px; color: #856404;">
            <strong>⚠️ สำรองเฉพาะสำหรับผู้ดูแลระบบเท่านั้น</strong><br>
            <span style="font-size: 0.9rem;">อีเมล: guitar0997574729@gmail.com | สิทธิ์การเข้าถึง: Admin Full Access</span>
        </div>

        <div class="header">
            <h1>🏢 Admin Dashboard</h1>
            <button class="logout-btn" onclick="logout()">ออกจากระบบ</button>
        </div>

        <!-- Dashboard Section -->
        <div id="dashboard" class="content-section active">
            <h2>สรุปข้อมูล</h2>
            <div class="dashboard">
                <div class="stat-card">
                    <h3>จำนวนผู้ใช้ทั้งหมด</h3>
                    <div class="stat-number" id="totalUsers">0</div>
                </div>
                <div class="stat-card">
                    <h3>จำนวนสินค้า</h3>
                    <div class="stat-number">9</div>
                </div>
                <div class="stat-card">
                    <h3>ข้อความใหม่</h3>
                    <div class="stat-number" id="newMessages">0</div>
                </div>
                <div class="stat-card">
                    <h3>สถานะระบบ</h3>
                    <div class="stat-number" style="color: #28a745;">✓</div>
                </div>
            </div>
        </div>

        <!-- Customers Section -->
        <div id="customers" class="content-section">
            <h2>📋 ข้อมูลลูกค้า</h2>
            <div id="customersContainer">
                <!-- ข้อมูลลูกค้าจะแทรกที่นี่ -->
            </div>
        </div>

        <!-- Users Section -->
        <div id="users" class="content-section">
            <h2>รายชื่อผู้ใช้ทั้งหมด 🔒 (อ่านเท่านั้น)</h2>
            <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">✓ การแก้ไขและลบข้อมูลผู้ใช้ไม่อนุญาต</p>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>อีเมล</th>
                        <th>ชื่อ</th>
                        <th>สถานะ</th>
                        <th>วันที่สมัคร</th>
                        <th>การจัดการ</th>
                    </tr>
                </thead>
                <tbody id="usersTable">
                    <!-- ข้อมูลผู้ใช้จะแทรกที่นี่ -->
                </tbody>
            </table>
        </div>

        <!-- Products Section -->
        <div id="products" class="content-section">
            <h2>รายชื่อสินค้า</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>ชื่อสินค้า</th>
                        <th>หมวดหมู่</th>
                        <th>ราคา</th>
                        <th>สถานะ</th>
                        <th>การจัดการ</th>
                    </tr>
                </thead>
                <tbody id="productsTable">
                    <!-- ข้อมูลสินค้าจะแทรกที่นี่ -->
                </tbody>
            </table>
        </div>

        <!-- Chat Section -->
        <div id="chat" class="content-section">
            <h2>ข้อความจากผู้ใช้</h2>
            <div class="message-list" id="messagesList">
                <!-- ข้อความจะแทรกที่นี่ -->
            </div>
        </div>
    </main>

    <!-- Modal แก้ไขสินค้า -->
    <div class="modal" id="editProductModal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>แก้ไขสินค้า</h3>
                <button class="modal-close" onclick="closeEditModal()">✕</button>
            </div>
            <form class="modal-form" onsubmit="saveProductChanges(event)">
                <div>
                    <label>ชื่อสินค้า:</label>
                    <input type="text" id="editProductName" required>
                </div>
                <div>
                    <label>หมวดหมู่:</label>
                    <input type="text" id="editProductCategory" required>
                </div>
                <div>
                    <label>ราคา:</label>
                    <input type="text" id="editProductPrice" required>
                </div>
                <div>
                    <label>รายละเอียด:</label>
                    <textarea id="editProductDescription" rows="3"></textarea>
                </div>
                <div class="modal-buttons">
                    <button type="button" class="modal-btn modal-btn-cancel" onclick="closeEditModal()">ยกเลิก</button>
                    <button type="submit" class="modal-btn modal-btn-save">บันทึกการเปลี่ยนแปลง</button>
                </div>
            </form>
        </div>
    </div>

    <script>
        // กำหนด Admin Email ที่อนุญาต
        const AUTHORIZED_ADMIN_EMAIL = 'guitar0997574729@gmail.com';

        // ตรวจสอบสิทธิ์ admin อย่างเข้มงวด
        window.addEventListener('load', function() {
            const isLoggedIn = localStorage.getItem('isLoggedIn');
            const isAdmin = localStorage.getItem('isAdmin');
            const userEmail = localStorage.getItem('userEmail');

            // ตรวจสอบทั้ง 3 เงื่อนไข: login, admin flag, และ authorized email
            if (isLoggedIn !== 'true' || isAdmin !== 'true' || userEmail !== AUTHORIZED_ADMIN_EMAIL) {
                alert('❌ ระบบ Admin\n\nสำหรับเฉพาะผู้ดูแลระบบเท่านั้น!\n(' + AUTHORIZED_ADMIN_EMAIL + ')');
                window.location.href = 'index.html';
                return;
            }

            // แสดงอีเมล admin ที่เข้าสู่ระบบ
            const adminInfo = document.querySelector('.sidebar h1');
            if (adminInfo) {
                adminInfo.innerHTML = '<span style="font-size: 0.8rem; display: block; margin-top: 0.5rem;">👤 Admin</span>';
            }

            loadDashboard();
        });

        function showSection(sectionId) {
            // ซ่อนทั้งหมด
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            // ลบ active จากนาวิเก
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
            });

            // แสดงเซคชันที่เลือก
            document.getElementById(sectionId).classList.add('active');
            event.target.classList.add('active');

            // โหลดข้อมูล
            if (sectionId === 'customers') {
                loadCustomers();
            } else if (sectionId === 'users') {
                loadUsers();
            } else if (sectionId === 'products') {
                loadProducts();
            } else if (sectionId === 'chat') {
                loadMessages();
            }
        }

        function loadDashboard() {
            const userData = localStorage.getItem('personalData');
            if (userData) {
                document.getElementById('totalUsers').textContent = '1+';
            }

            // นับข้อความ
            const messages = JSON.parse(localStorage.getItem('adminMessages') || '[]');
            document.getElementById('newMessages').textContent = messages.length;
        }

        function loadCustomers() {
            const container = document.getElementById('customersContainer');
            container.innerHTML = '';

            const personalData = JSON.parse(localStorage.getItem('personalData') || '{}');
            const userEmail = localStorage.getItem('userEmail') || 'ไม่ระบุ';

            if (!personalData.firstName) {
                container.innerHTML = '<p style="text-align: center; color: #999; padding: 2rem;">ยังไม่มีข้อมูลลูกค้า</p>';
                return;
            }

            const customerHTML = `
                <div class="customer-detail">
                    <h4>📌 ข้อมูลลูกค้า</h4>
                    <div class="detail-row">
                        <div class="detail-item">
                            <div class="detail-label">อีเมล</div>
                            <div class="detail-value">${userEmail}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">ชื่อจริง</div>
                            <div class="detail-value">${personalData.firstName || '-'}</div>
                        </div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-item">
                            <div class="detail-label">นามสกุล</div>
                            <div class="detail-value">${personalData.lastName || '-'}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">เบอร์โทรศัพท์</div>
                            <div class="detail-value">${personalData.phone || '-'}</div>
                        </div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-item">
                            <div class="detail-label">ที่อยู่</div>
                            <div class="detail-value">${personalData.address || '-'}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">จังหวัด</div>
                            <div class="detail-value">${personalData.city || '-'}</div>
                        </div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-item">
                            <div class="detail-label">รหัสไปรษณีย์</div>
                            <div class="detail-value">${personalData.zipcode || '-'}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">วันเกิด</div>
                            <div class="detail-value">${personalData.birthdate || '-'}</div>
                        </div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-item">
                            <div class="detail-label">เพศ</div>
                            <div class="detail-value">${getCategoryName(personalData.gender) || '-'}</div>
                        </div>
                        <div class="detail-item">
                            <div class="detail-label">อาชีพ</div>
                            <div class="detail-value">${personalData.occupation || '-'}</div>
                        </div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-item" style="grid-column: 1 / -1;">
                            <div class="detail-label">หมายเหตุ</div>
                            <div class="detail-value">${personalData.notes || '-'}</div>
                        </div>
                    </div>
                </div>
            `;

            container.innerHTML = customerHTML;
        }

        function getCategoryName(category) {
            const names = {
                'male': 'ชาย',
                'female': 'หญิง',
                'other': 'อื่น ๆ'
            };
            return names[category] || category;
        }

        function loadUsers() {
            const usersTable = document.getElementById('usersTable');
            usersTable.innerHTML = '';

            const users = [
                {
                    id: 1,
                    email: localStorage.getItem('userEmail') || 'user@example.com',
                    name: 'ผู้ใช้ทดสอบ',
                    status: 'เข้าใช้งาน',
                    date: new Date().toLocaleDateString('th-TH')
                }
            ];

            users.forEach(user => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${user.id}</td>
                    <td>${user.email}</td>
                    <td>${user.name}</td>
                    <td><span class="status-badge status-active">${user.status}</span></td>
                    <td>${user.date}</td>
                    <td>
                        <button class="action-btn btn-edit">แก้ไข</button>
                        <button class="action-btn btn-delete">ลบ</button>
                    </td>
                `;
                usersTable.appendChild(row);
            });
        }

        function loadProducts() {
            const productsTable = document.getElementById('productsTable');
            productsTable.innerHTML = '';

            const products = [
                { id: 1, name: 'หูฟัง Bluetooth', category: 'อิเล็กทรอนิกส์', price: '1,299 บาท', description: 'หูฟังไร้สายคุณภาพสูง' },
                { id: 2, name: 'พาวเวอร์แบงก์', category: 'อิเล็กทรอนิกส์', price: '899 บาท', description: 'แบตสำรองพลังงาน 20000mAh' },
                { id: 3, name: 'เสื้อยืดสีเขียว', category: 'เสื้อผ้า', price: '399 บาท', description: 'เสื้อยืด 100% ผ้าคอตตอน' },
                { id: 4, name: 'กางเกงยีนส์', category: 'เสื้อผ้า', price: '599 บาท', description: 'กางเกงยีนส์เข้ารูป' },
                { id: 5, name: 'Python Programming', category: 'หนังสือ', price: '499 บาท', description: 'หนังสือสอนโปรแกรมมิ่ง' },
                { id: 6, name: 'Web Development Guide', category: 'หนังสือ', price: '599 บาท', description: 'คู่มือการพัฒนาเว็บไซต์' },
                { id: 7, name: 'โคมไฟ LED', category: 'สินค้าบ้าน', price: '299 บาท', description: 'โคมไฟ LED ประหยัดไฟ' },
                { id: 8, name: 'พูลหมอน', category: 'สินค้าบ้าน', price: '199 บาท', description: 'หมอนหนุนสุดนุ่ม' },
                { id: 9, name: 'กระบอกน้ำ', category: 'สินค้าบ้าน', price: '299 บาท', description: 'กระบอกน้ำสแตนเลส' }
            ];

            products.forEach(product => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.id}</td>
                    <td>${product.name}</td>
                    <td>${product.category}</td>
                    <td>${product.price}</td>
                    <td><span class="status-badge status-active">พร้อมจำหน่าย</span></td>
                    <td>
                        <button class="action-btn btn-edit" onclick="openEditModal(${product.id}, '${product.name}', '${product.category}', '${product.price}', '${product.description}')">แก้ไข</button>
                        <button class="action-btn btn-delete" onclick="deleteProduct(${product.id})">ลบ</button>
                    </td>
                `;
                productsTable.appendChild(row);
            });
        }

        function loadMessages() {
            const messagesList = document.getElementById('messagesList');
            messagesList.innerHTML = '';

            const messages = JSON.parse(localStorage.getItem('adminMessages') || '[]');

            if (messages.length === 0) {
                messagesList.innerHTML = '<p style="text-align: center; color: #999;">ยังไม่มีข้อความใหม่</p>';
                return;
            }

            messages.forEach((msg, index) => {
                const div = document.createElement('div');
                div.className = 'message-item';
                div.innerHTML = `
                    <strong>${msg.email}</strong> - ${msg.name}
                    <p>${msg.message}</p>
                    <small>${new Date(msg.timestamp).toLocaleString('th-TH')}</small>
                    <br>
                    <button class="action-btn btn-message" onclick="replyToMessage('${msg.email}')">ตอบกลับ</button>
                `;
                messagesList.appendChild(div);
            });
        }

        function replyToMessage(email) {
            const reply = prompt('พิมพ์ข้อความตอบกลับ:');
            if (reply) {
                alert('ส่งข้อความตอบกลับไปยัง ' + email + ' แล้ว');
            }
        }

        function logout() {
            if (confirm('คุณต้องการออกจากระบบใช่หรือไม่?')) {
                localStorage.removeItem('isLoggedIn');
                localStorage.removeItem('userEmail');
                localStorage.removeItem('isAdmin');
                localStorage.removeItem('adminLoginTime');
                alert('✓ ออกจากระบบ Admin สำเร็จ');
                window.location.href = 'index.html';
            }
        }

        // ตัวแปรเก็บ ID สินค้าที่กำลังแก้ไข
        let editingProductId = null;

        function openEditModal(id, name, category, price, description) {
            editingProductId = id;
            document.getElementById('editProductName').value = name;
            document.getElementById('editProductCategory').value = category;
            document.getElementById('editProductPrice').value = price;
            document.getElementById('editProductDescription').value = description;
            document.getElementById('editProductModal').classList.add('show');
        }

        function closeEditModal() {
            document.getElementById('editProductModal').classList.remove('show');
            editingProductId = null;
        }

        function saveProductChanges(event) {
            event.preventDefault();

            const updatedName = document.getElementById('editProductName').value;
            const updatedCategory = document.getElementById('editProductCategory').value;
            const updatedPrice = document.getElementById('editProductPrice').value;
            const updatedDescription = document.getElementById('editProductDescription').value;

            // บันทึกข้อมูลสินค้าที่แก้ไข (ในที่นี้เก็บใน localStorage)
            const editedProducts = JSON.parse(localStorage.getItem('editedProducts') || '{}');
            editedProducts[editingProductId] = {
                id: editingProductId,
                name: updatedName,
                category: updatedCategory,
                price: updatedPrice,
                description: updatedDescription,
                editedAt: new Date().toLocaleString('th-TH')
            };

            localStorage.setItem('editedProducts', JSON.stringify(editedProducts));

            alert('บันทึกการเปลี่ยนแปลงสินค้า "' + updatedName + '" สำเร็จ');
            closeEditModal();
            loadProducts();
        }

        function deleteProduct(id) {
            if (confirm('คุณต้องการลบสินค้านี้ใช่หรือไม่?')) {
                const deletedProducts = JSON.parse(localStorage.getItem('deletedProducts') || '[]');
                deletedProducts.push(id);
                localStorage.setItem('deletedProducts', JSON.stringify(deletedProducts));

                alert('ลบสินค้า ID: ' + id + ' สำเร็จ');
                loadProducts();
            }
        }

        // ปิด modal เมื่อคลิกนอก modal
        window.addEventListener('click', function(event) {
            const modal = document.getElementById('editProductModal');
            if (event.target === modal) {
                closeEditModal();
            }
        });
    </script>
</body>
</html>
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ตะกร้าสินค้า</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
        }

        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        nav a {
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }

        nav a:hover {
            opacity: 0.8;
        }

        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .page-title {
            color: #667eea;
            margin-bottom: 2rem;
            font-size: 2rem;
        }

        .cart-container {
            display: grid;
            grid-template-columns: 1fr 350px;
            gap: 2rem;
        }

        .cart-items {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .cart-item {
            display: flex;
            gap: 1.5rem;
            padding: 1.5rem;
            border-bottom: 1px solid #eee;
            align-items: center;
        }

        .cart-item:last-child {
            border-bottom: none;
        }

        .item-emoji {
            font-size: 3rem;
            min-width: 60px;
            text-align: center;
        }

        .item-details {
            flex: 1;
        }

        .item-name {
            font-weight: bold;
            color: #333;
            margin-bottom: 0.5rem;
            font-size: 1.1rem;
        }

        .item-price {
            color: #667eea;
            font-weight: bold;
            font-size: 1rem;
        }

        .item-actions {
            display: flex;
            gap: 0.5rem;
            align-items: center;
        }

        .qty-btn {
            width: 30px;
            height: 30px;
            border: 1px solid #ddd;
            background: white;
            cursor: pointer;
            border-radius: 3px;
            font-weight: bold;
            color: #667eea;
            transition: all 0.3s;
        }

        .qty-btn:hover {
            background: #667eea;
            color: white;
        }

        .qty-display {
            min-width: 40px;
            text-align: center;
            font-weight: bold;
        }

        .remove-btn {
            background: #ff6b6b;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }

        .remove-btn:hover {
            background: #ff5252;
        }

        .empty-cart {
            text-align: center;
            padding: 3rem;
            color: #999;
        }

        .empty-cart p {
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }

        .back-shopping {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 0.75rem 1.5rem;
            text-decoration: none;
            border-radius: 5px;
            margin-bottom: 1rem;
        }

        .back-shopping:hover {
            background: #764ba2;
        }

        .cart-summary {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 1.5rem;
            height: fit-content;
            position: sticky;
            top: 20px;
        }

        .summary-title {
            font-size: 1.2rem;
            font-weight: bold;
            color: #333;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 1rem;
        }

        .summary-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
            color: #666;
        }

        .summary-row.total {
            border-top: 2px solid #f0f0f0;
            padding-top: 1rem;
            margin-top: 1rem;
            font-size: 1.3rem;
            font-weight: bold;
            color: #667eea;
        }

        .checkout-btn {
            width: 100%;
            padding: 1rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            font-size: 1.1rem;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
            margin-top: 1.5rem;
        }

        .checkout-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .checkout-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
            transform: none;
        }

        .admin-login-btn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 60px;
            height: 60px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 50%;
            font-size: 2rem;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: all 0.3s;
            z-index: 50;
        }

        .admin-login-btn:hover {
            background: #764ba2;
            transform: scale(1.1);
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }

        .admin-login-btn:active {
            transform: scale(0.95);
        }

        @media (max-width: 768px) {
            .cart-container {
                grid-template-columns: 1fr;
            }

            .cart-summary {
                position: relative;
                top: 0;
            }

            .cart-item {
                flex-wrap: wrap;
            }

            nav {
                padding: 0 1rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">🛍️ ร้านค้า</div>
            <div>
                <a href="shop.html">← กลับไปร้านค้า</a>
            </div>
        </nav>
    </header>

    <main>
        <h1 class="page-title">🛒 ตะกร้าสินค้า</h1>

        <div class="cart-container">
            <div class="cart-items" id="cartItemsContainer">
                <!-- สินค้าในตะกร้าจะแทรกที่นี่ -->
            </div>

            <div class="cart-summary">
                <div class="summary-title">สรุปคำสั่ง</div>
                <div class="summary-row">
                    <span>ราคาสินค้า:</span>
                    <span id="subtotal">0 บาท</span>
                </div>
                <div class="summary-row">
                    <span>ค่าจัดส่ง:</span>
                    <span id="shipping">50 บาท</span>
                </div>
                <div class="summary-row">
                    <span>ส่วนลด:</span>
                    <span id="discount">0 บาท</span>
                </div>
                <div class="summary-row total">
                    <span>รวมทั้งสิ้น:</span>
                    <span id="totalPrice">0 บาท</span>
                </div>
                <button class="checkout-btn" id="checkoutBtn" onclick="goToCheckout()" disabled>
                    ดำเนินการชำระเงิน
                </button>
                <button class="checkout-btn" onclick="goToOrders()" style="background: #17a2b8; margin-top: 0.5rem;">
                    📦 ประวัติการสั่งซื้อ
                </button>
            </div>
        </div>
    </main>

    <script>
        const SHIPPING_FEE = 50;
        const MIN_ORDER = 0; // ค่าต่ำสุดสำหรับจัดส่ง

        window.addEventListener('load', function() {
            displayCart();
            updateSummary();
        });

        function displayCart() {
            const cart = JSON.parse(localStorage.getItem('cart') || '[]');
            const container = document.getElementById('cartItemsContainer');

            if (cart.length === 0) {
                container.innerHTML = `
                    <div class="empty-cart">
                        <p>ตะกร้าสินค้าว่างเปล่า</p>
                        <a href="shop.html" class="back-shopping">เลือกซื้อสินค้า</a>
                    </div>
                `;
                document.getElementById('checkoutBtn').disabled = true;
                return;
            }

            container.innerHTML = '';
            cart.forEach((item, index) => {
                const itemTotal = item.priceNumber * item.quantity;
                const row = document.createElement('div');
                row.className = 'cart-item';
                row.innerHTML = `
                    <div class="item-emoji">${item.emoji}</div>
                    <div class="item-details">
                        <div class="item-name">${item.name}</div>
                        <div class="item-price">${item.price}</div>
                    </div>
                    <div class="item-actions">
                        <button class="qty-btn" onclick="updateQuantity(${index}, -1)">−</button>
                        <div class="qty-display" id="qty-${index}">${item.quantity}</div>
                        <button class="qty-btn" onclick="updateQuantity(${index}, 1)">+</button>
                        <button class="remove-btn" onclick="removeItem(${index})">ลบ</button>
                    </div>
                `;
                container.appendChild(row);
            });

            document.getElementById('checkoutBtn').disabled = false;
        }

        function updateQuantity(index, change) {
            const cart = JSON.parse(localStorage.getItem('cart') || '[]');
            cart[index].quantity += change;

            if (cart[index].quantity <= 0) {
                cart.splice(index, 1);
            }

            localStorage.setItem('cart', JSON.stringify(cart));
            displayCart();
            updateSummary();
        }

        function removeItem(index) {
            const cart = JSON.parse(localStorage.getItem('cart') || '[]');
            cart.splice(index, 1);
            localStorage.setItem('cart', JSON.stringify(cart));
            displayCart();
            updateSummary();
        }

        function updateSummary() {
            const cart = JSON.parse(localStorage.getItem('cart') || '[]');
            
            // คำนวณราคารวม
            let subtotal = 0;
            cart.forEach(item => {
                subtotal += item.priceNumber * item.quantity;
            });

            // คำนวณค่าจัดส่ง
            let shipping = subtotal > 0 ? SHIPPING_FEE : 0;

            // คำนวณส่วนลด (10% สำหรับคำสั่งมากกว่า 500)
            let discount = subtotal > 500 ? Math.floor(subtotal * 0.1) : 0;

            // รวมทั้งสิ้น
            const total = subtotal + shipping - discount;

            // อัพเดต UI
            document.getElementById('subtotal').textContent = subtotal.toLocaleString('th-TH') + ' บาท';
            document.getElementById('discount').textContent = discount.toLocaleString('th-TH') + ' บาท';
            document.getElementById('totalPrice').textContent = total.toLocaleString('th-TH') + ' บาท';

            // บันทึกราคารวม
            localStorage.setItem('orderTotal', JSON.stringify({
                subtotal: subtotal,
                shipping: shipping,
                discount: discount,
                total: total
            }));
        }

        function goToCheckout() {
            const cart = JSON.parse(localStorage.getItem('cart') || '[]');
            if (cart.length === 0) {
                alert('กรุณาเลือกสินค้าก่อน');
                return;
            }
            window.location.href = 'checkout.html';
        }

        function goToOrders() {
            window.location.href = 'orders.html';
        }

        function checkAdminLogin() {
            const isAdmin = localStorage.getItem('isAdmin');
            const userEmail = localStorage.getItem('userEmail');
            const AUTHORIZED_ADMIN_EMAIL = 'guitar0997574729@gmail.com';

            if (isAdmin === 'true' && userEmail === AUTHORIZED_ADMIN_EMAIL) {
                window.location.href = 'admin.html';
            } else {
                window.location.href = 'login.html';
            }
        }
    </script>

    <!-- ปุ่มเข้า Admin ลับ (ซ่อนจากลูกค้า) -->
    <button class="admin-login-btn" onclick="checkAdminLogin()" title="Admin Login"></button>
</body>
</html>
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ระบบแชท</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }

        .chat-container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            width: 100%;
            max-width: 600px;
            height: 600px;
            display: flex;
            flex-direction: column;
        }

        .chat-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 10px 10px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .chat-header h1 {
            font-size: 1.5rem;
        }

        .close-btn {
            background: rgba(255,255,255,0.3);
            border: none;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.3s;
        }

        .close-btn:hover {
            background: rgba(255,255,255,0.5);
        }

        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 1.5rem;
            background: #f9f9f9;
        }

        .message {
            margin-bottom: 1.5rem;
            display: flex;
            animation: fadeIn 0.3s ease-in;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .message.user {
            justify-content: flex-end;
        }

        .message.admin {
            justify-content: flex-start;
        }

        .message-content {
            background: #667eea;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 18px;
            max-width: 80%;
            word-wrap: break-word;
        }

        .message.admin .message-content {
            background: #e9ecef;
            color: #333;
        }

        .message-time {
            font-size: 0.75rem;
            color: #999;
            margin-top: 0.25rem;
            padding: 0 1rem;
        }

        .chat-input-area {
            padding: 1.5rem;
            background: white;
            border-top: 1px solid #eee;
            display: flex;
            gap: 1rem;
        }

        .message-input {
            flex: 1;
            padding: 0.75rem 1.5rem;
            border: 1px solid #ddd;
            border-radius: 25px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        .message-input:focus {
            outline: none;
            border-color: #667eea;
        }

        .send-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.75rem 2rem;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .send-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .info-message {
            text-align: center;
            color: #999;
            padding: 2rem;
            font-size: 0.95rem;
        }

        @media (max-width: 600px) {
            .chat-container {
                height: 80vh;
            }

            .message-content {
                max-width: 90%;
            }
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h1>💬 ระบบแชท</h1>
            <button class="close-btn" onclick="goBack()">ปิด</button>
        </div>

        <div class="chat-messages" id="chatMessages">
            <div class="info-message">
                <p>👋 ยินดีต้อนรับสู่ระบบแชท</p>
                <p>พิมพ์ข้อความของคุณด้านล่าง เจ้าของเว็บไซต์จะตอบกลับในเร็ว ๆ นี้</p>
            </div>
        </div>

        <div class="chat-input-area">
            <input 
                type="text" 
                id="messageInput" 
                class="message-input" 
                placeholder="พิมพ์ข้อความของคุณ..." 
                onkeypress="handleKeyPress(event)"
            >
            <button class="send-btn" onclick="sendMessage()">ส่ง</button>
        </div>
    </div>

    <script>
        const userEmail = localStorage.getItem('userEmail') || 'ผู้เยี่ยมชม';
        const personalData = JSON.parse(localStorage.getItem('personalData') || '{}');
        const userName = personalData.firstName || 'ผู้ใช้';

        // โหลดข้อความเก่า
        window.addEventListener('load', function() {
            loadChatHistory();
        });

        function loadChatHistory() {
            const chatHistory = JSON.parse(localStorage.getItem('chatHistory') || '[]');
            const chatMessages = document.getElementById('chatMessages');
            
            if (chatHistory.length === 0) {
                return; // แสดงข้อความต้อนรับเพียงอย่างเดียว
            }

            chatMessages.innerHTML = '';
            chatHistory.forEach(msg => {
                displayMessage(msg.message, msg.sender, msg.timestamp, false);
            });
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();

            if (message === '') {
                alert('กรุณาพิมพ์ข้อความ');
                return;
            }

            const timestamp = new Date();
            
            // เพิ่มข้อความลงในแชท
            displayMessage(message, 'user', timestamp, true);

            // บันทึกข้อความลงใน localStorage
            const chatHistory = JSON.parse(localStorage.getItem('chatHistory') || '[]');
            chatHistory.push({
                sender: 'user',
                message: message,
                timestamp: timestamp.toLocaleString('th-TH'),
                email: userEmail,
                name: userName
            });
            localStorage.setItem('chatHistory', JSON.stringify(chatHistory));

            // บันทึกลงใน adminMessages เพื่อให้ admin เห็น
            const adminMessages = JSON.parse(localStorage.getItem('adminMessages') || '[]');
            adminMessages.push({
                email: userEmail,
                name: userName,
                message: message,
                timestamp: timestamp
            });
            localStorage.setItem('adminMessages', JSON.stringify(adminMessages));

            // ล้างช่องพิมพ์
            input.value = '';
            input.focus();

            // ตอบกลับอัตโนมัติจากเจ้าของ (ท่าทีเท่านั้น)
            setTimeout(() => {
                const replies = [
                    'ขอบคุณที่ติดต่อเรา จะตอบกลับให้ในเร็ว ๆ นี้ 😊',
                    'ขอบคุณสำหรับข้อความ จะตอบกลับทันที 🙏',
                    'รับข้อความแล้ว จะติดต่อกลับให้ 📱'
                ];
                const randomReply = replies[Math.floor(Math.random() * replies.length)];
                displayMessage(randomReply, 'admin', new Date(), true);

                const chatHistory = JSON.parse(localStorage.getItem('chatHistory') || '[]');
                chatHistory.push({
                    sender: 'admin',
                    message: randomReply,
                    timestamp: new Date().toLocaleString('th-TH'),
                    email: 'admin',
                    name: 'พิเชฐ จันทร์แก้ว'
                });
                localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
            }, 1000);
        }

        function displayMessage(message, sender, timestamp, scroll = true) {
            const chatMessages = document.getElementById('chatMessages');
            
            // ลบข้อความต้อนรับถ้ามี
            const infoMessage = chatMessages.querySelector('.info-message');
            if (infoMessage) {
                infoMessage.remove();
            }

            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}`;

            const timeStr = typeof timestamp === 'object' 
                ? timestamp.toLocaleTimeString('th-TH', { hour: '2-digit', minute: '2-digit' })
                : timestamp;

            messageDiv.innerHTML = `
                <div>
                    <div class="message-content">${message}</div>
                    <div class="message-time">${timeStr}</div>
                </div>
            `;

            chatMessages.appendChild(messageDiv);

            // เลื่อนไปด้านล่าง
            if (scroll) {
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }

        function goBack() {
            if (confirm('ออกจากแชท?')) {
                window.location.href = 'shop.html';
            }
        }
    </script>
</body>
</html>
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ชำระเงิน</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }

        .checkout-container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }

        .checkout-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }

        .checkout-header h1 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        .step-indicator {
            display: flex;
            justify-content: space-around;
            padding: 2rem;
            background: #f9f9f9;
            border-bottom: 2px solid #eee;
        }

        .step {
            text-align: center;
            color: #999;
        }

        .step.active {
            color: #667eea;
            font-weight: bold;
        }

        .step.completed::before {
            content: '✓';
            display: block;
            color: #28a745;
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .checkout-content {
            padding: 2rem;
        }

        .section {
            margin-bottom: 2rem;
        }

        .section-title {
            font-size: 1.3rem;
            color: #667eea;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 1rem;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #333;
            font-weight: 500;
        }

        input[type="text"],
        input[type="email"],
        input[type="tel"],
        input[type="date"],
        select,
        textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            font-family: inherit;
            transition: border-color 0.3s;
        }

        input:focus,
        select:focus,
        textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }

        .payment-methods {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }

        .payment-option {
            border: 2px solid #ddd;
            padding: 1rem;
            border-radius: 8px;
            cursor: pointer;
            text-align: center;
            transition: all 0.3s;
        }

        .payment-option:hover {
            border-color: #667eea;
            background: #f9f9f9;
        }

        .payment-option input {
            margin-top: 0.5rem;
        }

        .payment-option.selected {
            border-color: #667eea;
            background: #f0f4ff;
        }

        .order-summary {
            background: #f9f9f9;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 2rem;
        }

        .summary-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
            color: #666;
        }

        .summary-item.total {
            border-top: 2px solid #ddd;
            padding-top: 1rem;
            font-size: 1.3rem;
            font-weight: bold;
            color: #667eea;
        }

        .button-group {
            display: flex;
            gap: 1rem;
            justify-content: space-between;
            margin-top: 2rem;
        }

        .btn {
            flex: 1;
            padding: 1rem;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s;
        }

        .btn-back {
            background: #ddd;
            color: #333;
        }

        .btn-back:hover {
            background: #ccc;
        }

        .btn-pay {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-pay:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-pay:disabled {
            background: #ccc;
            cursor: not-allowed;
            transform: none;
        }

        .success-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.7);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }

        .success-modal.show {
            display: flex;
        }

        .success-content {
            background: white;
            padding: 3rem;
            border-radius: 10px;
            text-align: center;
            max-width: 500px;
        }

        .success-icon {
            font-size: 5rem;
            margin-bottom: 1rem;
            animation: scaleIn 0.5s ease;
        }

        @keyframes scaleIn {
            from {
                transform: scale(0);
            }
            to {
                transform: scale(1);
            }
        }

        .success-content h2 {
            color: #28a745;
            margin-bottom: 1rem;
            font-size: 1.8rem;
        }

        .success-content p {
            color: #666;
            margin-bottom: 0.5rem;
        }

        .order-id {
            background: #f0f0f0;
            padding: 1rem;
            border-radius: 5px;
            margin: 1.5rem 0;
            font-weight: bold;
            color: #667eea;
        }

        @media (max-width: 768px) {
            .form-row {
                grid-template-columns: 1fr;
            }

            .step-indicator {
                flex-direction: column;
                gap: 1rem;
            }

            .button-group {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="checkout-container">
        <div class="checkout-header">
            <h1>💳 ชำระเงิน</h1>
            <p>ยืนยันข้อมูลและเลือกวิธีการชำระเงิน</p>
        </div>

        <div class="step-indicator">
            <div class="step completed">ตะกร้า</div>
            <div class="step active">ข้อมูลจัดส่ง</div>
            <div class="step">ชำระเงิน</div>
            <div class="step">สำเร็จ</div>
        </div>

        <div class="checkout-content">
            <!-- ข้อมูลสรุปคำสั่ง -->
            <div class="order-summary">
                <div class="summary-item">
                    <span>ราคาสินค้า:</span>
                    <span id="summarySubtotal">0</span>
                </div>
                <div class="summary-item">
                    <span>ค่าจัดส่ง:</span>
                    <span id="summaryShipping">50 บาท</span>
                </div>
                <div class="summary-item">
                    <span>ส่วนลด:</span>
                    <span id="summaryDiscount">0</span>
                </div>
                <div class="summary-item total">
                    <span>รวมทั้งสิ้น:</span>
                    <span id="summaryTotal">0</span>
                </div>
            </div>

            <form id="checkoutForm">
                <!-- ข้อมูลการจัดส่ง -->
                <div class="section">
                    <h3 class="section-title">📍 ข้อมูลการจัดส่ง</h3>

                    <div class="form-row">
                        <div class="form-group">
                            <label>ชื่อผู้รับ:</label>
                            <input type="text" id="recipientName" required>
                        </div>
                        <div class="form-group">
                            <label>เบอร์โทรศัพท์:</label>
                            <input type="tel" id="recipientPhone" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>ที่อยู่:</label>
                        <textarea id="address" required></textarea>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label>จังหวัด:</label>
                            <input type="text" id="province" required>
                        </div>
                        <div class="form-group">
                            <label>รหัสไปรษณีย์:</label>
                            <input type="text" id="zipcode" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>หมายเหตุเพิ่มเติม (ไม่บังคับ):</label>
                        <textarea id="notes" placeholder="เช่น บ้านหลัง ที่จุดเด่นใดๆ"></textarea>
                    </div>
                </div>

                <!-- วิธีการชำระเงิน -->
                <div class="section">
                    <h3 class="section-title">💳 วิธีการชำระเงิน</h3>

                    <div class="payment-methods">
                        <label class="payment-option selected">
                            <div>🏦</div>
                            <div>โอนผ่านธนาคาร</div>
                            <input type="radio" name="paymentMethod" value="bank" checked required>
                        </label>
                        <label class="payment-option">
                            <div>📱</div>
                            <div>PromptPay (QR)</div>
                            <input type="radio" name="paymentMethod" value="promptpay" required>
                        </label>
                        <label class="payment-option">
                            <div>💰</div>
                            <div>เงินสด ณ ที่ส่ง</div>
                            <input type="radio" name="paymentMethod" value="cash" required>
                        </label>
                        <label class="payment-option">
                            <div>🎁</div>
                            <div>บัตรเครดิต</div>
                            <input type="radio" name="paymentMethod" value="credit" required>
                        </label>
                    </div>
                </div>

                <!-- ข้อมูลที่อยู่ใบเสร็จ -->
                <div class="section">
                    <h3 class="section-title">🧾 ข้อมูลใบเสร็จ</h3>

                    <div class="form-group">
                        <label>
                            <input type="checkbox" id="useRecipientInfo" checked>
                            ใช้ข้อมูลผู้รับสินค้าเดียวกัน
                        </label>
                    </div>

                    <div id="billInfoSection" style="display: none;">
                        <div class="form-group">
                            <label>ชื่อบริษัท/องค์กร (ไม่บังคับ):</label>
                            <input type="text" id="billCompany">
                        </div>
                    </div>
                </div>

                <!-- ปุ่มดำเนิน -->
                <div class="button-group">
                    <button type="button" class="btn btn-back" onclick="goBack()">← กลับ</button>
                    <button type="submit" class="btn btn-pay">ยืนยันและชำระเงิน</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Modal สำเร็จ -->
    <div class="success-modal" id="successModal">
        <div class="success-content">
            <div class="success-icon">✓</div>
            <h2>สำเร็จ!</h2>
            <p>ขอบคุณที่ทำการซื้อสินค้า</p>
            <div class="order-id">
                <p>เลขที่คำสั่ง: <span id="orderId"></span></p>
            </div>
            <p>สินค้าจะส่งให้คุณภายใน 1-3 วันธุรกิจ</p>
            <p style="margin-top: 1.5rem; color: #999;">กำลังเปลี่ยนหน้า...</p>
        </div>
    </div>

    <script>
        window.addEventListener('load', function() {
            loadCheckoutData();
            setupPaymentOptions();
            setupBillInfoToggle();
        });

        function loadCheckoutData() {
            const orderTotal = JSON.parse(localStorage.getItem('orderTotal') || '{}');
            const personalData = JSON.parse(localStorage.getItem('personalData') || '{}');

            // อัพเดตสรุป
            document.getElementById('summarySubtotal').textContent = 
                (orderTotal.subtotal || 0).toLocaleString('th-TH') + ' บาท';
            document.getElementById('summaryShipping').textContent = 
                (orderTotal.shipping || 0).toLocaleString('th-TH') + ' บาท';
            document.getElementById('summaryDiscount').textContent = 
                (orderTotal.discount || 0).toLocaleString('th-TH') + ' บาท';
            document.getElementById('summaryTotal').textContent = 
                (orderTotal.total || 0).toLocaleString('th-TH') + ' บาท';

            // ใส่ข้อมูลผู้ใช้
            if (personalData.firstName) {
                document.getElementById('recipientName').value = 
                    personalData.firstName + ' ' + (personalData.lastName || '');
            }
            if (personalData.phone) {
                document.getElementById('recipientPhone').value = personalData.phone;
            }
            if (personalData.address) {
                document.getElementById('address').value = personalData.address;
            }
            if (personalData.city) {
                document.getElementById('province').value = personalData.city;
            }
            if (personalData.zipcode) {
                document.getElementById('zipcode').value = personalData.zipcode;
            }
        }

        function setupPaymentOptions() {
            document.querySelectorAll('input[name="paymentMethod"]').forEach(radio => {
                radio.addEventListener('change', function() {
                    document.querySelectorAll('.payment-option').forEach(opt => {
                        opt.classList.remove('selected');
                    });
                    this.parentElement.classList.add('selected');
                });
            });
        }

        function setupBillInfoToggle() {
            const checkbox = document.getElementById('useRecipientInfo');
            const billSection = document.getElementById('billInfoSection');

            checkbox.addEventListener('change', function() {
                billSection.style.display = this.checked ? 'none' : 'block';
            });
        }

        document.getElementById('checkoutForm').addEventListener('submit', function(e) {
            e.preventDefault();
            submitCheckout();
        });

        function submitCheckout() {
            const cart = JSON.parse(localStorage.getItem('cart') || '[]');
            const personalData = JSON.parse(localStorage.getItem('personalData') || '{}');
            const orderTotal = JSON.parse(localStorage.getItem('orderTotal') || '{}');

            const formData = {
                orderId: generateOrderId(),
                orderDate: new Date().toLocaleString('th-TH'),
                recipient: document.getElementById('recipientName').value,
                phone: document.getElementById('recipientPhone').value,
                address: document.getElementById('address').value,
                province: document.getElementById('province').value,
                zipcode: document.getElementById('zipcode').value,
                notes: document.getElementById('notes').value,
                paymentMethod: document.querySelector('input[name="paymentMethod"]:checked').value,
                items: cart,
                subtotal: orderTotal.subtotal || 0,
                shipping: orderTotal.shipping || 50,
                discount: orderTotal.discount || 0,
                total: orderTotal.total || 0,
                status: 'กำลังประมวลผล'
            };

            // บันทึกข้อมูลคำสั่ง
            localStorage.setItem('lastOrder', JSON.stringify(formData));

            // เพิ่มไปยังประวัติการสั่งซื้อ
            const orders = JSON.parse(localStorage.getItem('orderHistory') || '[]');
            orders.push(formData);
            localStorage.setItem('orderHistory', JSON.stringify(orders));

            // ล้างตะกร้า
            localStorage.removeItem('cart');

            // แสดง modal สำเร็จ
            showSuccessModal(formData.orderId);
        }

        function generateOrderId() {
            return 'ORD' + Date.now() + Math.random().toString(36).substr(2, 9).toUpperCase();
        }

        function showSuccessModal(orderId) {
            document.getElementById('orderId').textContent = orderId;
            const modal = document.getElementById('successModal');
            modal.classList.add('show');

            // เปลี่ยนหน้าหลังจาก 3 วินาที
            setTimeout(() => {
                window.location.href = 'shop.html';
            }, 3000);
        }

        function goBack() {
            window.location.href = 'cart.html';
        }
    </script>
</body>
</html>
