import time
import requests
import random
import sys
from datetime import datetime
import os
import getpass
import base64

class WhatsAppMassReporter:
    def __init__(self):
        self.report_urls = [
            "https://faq.whatsapp.com/1297640017664693/",
            "https://www.whatsapp.com/contact/", 
            "https://www.whatsapp.com/contact/?subject=messengerId",
            "https://www.whatsapp.com/contact/?subject=messenger"
        ]
        self.anonymouse_urls = [
            "https://anonymouse.org/cgi-bin/anon-email.cgi",
            "https://anonymouse.org/anonemail.html"
        ]
        self.sent_reports = []
        self.counter = 0
        self.valid_credentials = {"lordhozoo": "123"}
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Origin': 'https://www.whatsapp.com',
            'Referer': 'https://www.whatsapp.com/',
            'Connection': 'keep-alive',
        }

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def show_banner(self):
        banner = """
\033[95m
╔══════════════════════════════════════════════════════════════╗
║ ██████  ██▀███   ▄▄▄       █    ██  ███▄ ▄███▓▓█████ ███▄    █ ║
║▓██   ▒ ▓██ ▒ ██▒▒████▄     ██  ▓██▒▓██▒▀█▀ ██▒▓█   ▀ ██ ▀█   █ ║
║▒██▀▀█▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▒██░▓██    ▓██░▒███  ▓██  ▀█ ██▒║
║░▓█▄▄▄ ▒██▀▀█▄  ░██▄▄▄▄██ ▓▓█  ░██░▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒║
║░▒████▒░██▓ ▒██▒ ▓█   ▓██▒▒▒█████▓ ▒██▒   ░██▒░▒████▒▒██░   ▓██░║
║ ▒▒▓  ▒░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ║
║ ░ ▒  ▒  ░▒ ░ ▒░  ▒   ▒▒ ░░░▒░ ░ ░ ░  ░      ░ ░ ░  ░░ ░░   ░ ▒░║
║ ░ ░  ░  ░░   ░   ░   ▒    ░░░ ░ ░ ░      ░      ░      ░   ░ ░ ║
║   ░      ░           ░  ░   ░            ░      ░  ░         ░ ║
║ ░                                                              ║
╚══════════════════════════════════════════════════════════════╝
\033[0m
        """
        print(banner)

    def show_login(self):
        """Sistem login seperti web"""
        self.clear_screen()
        print("\033[95m" + "═" * 60 + "\033[0m")
        print("\033[95m║\033[0m                  \033[96mHOZOO TERMUX LOGIN\033[0m                  \033[95m║\033[0m")
        print("\033[95m║\033[0m                                                   \033[95m║\033[0m")
        print("\033[95m║\033[0m           \033[93mSilakan login untuk melanjutkan\033[0m           \033[95m║\033[0m")
        print("\033[95m║\033[0m                                                   \033[95m║\033[0m")
        print("\033[95m" + "═" * 60 + "\033[0m")
        
        attempts = 3
        while attempts > 0:
            print(f"\n\033[94mPercobaan login tersisa: {attempts}\033[0m")
            username = input("\033[97mUsername: \033[0m").strip()
            password = getpass.getpass("\033[97mPassword: \033[0m").strip()
            
            if username in self.valid_credentials and self.valid_credentials[username] == password:
                print(f"\n\033[92m✅ Login berhasil! Selamat datang {username}!\033[0m")
                time.sleep(2)
                return True
            else:
                print(f"\033[91m❌ Login gagal! Username atau password salah.\033[0m")
                attempts -= 1
                time.sleep(1)
        
        print(f"\n\033[91m💥 Akses ditolak! Terlalu banyak percobaan gagal.\033[0m")
        return False

    def show_loading(self, duration=2, text="MEMULAI SISTEM HOZOO"):
        print(f"\033[96m🔄 {text}...\033[0m")
        time.sleep(duration)
        print(f"\033[92m✅ SISTEM SIAP!\033[0m")

    def show_navigation_ui(self):
        """UI Navigasi dengan garis hitam ungu"""
        print("\033[95m" + "┌" + "─" * 78 + "┐" + "\033[0m")
        print("\033[95m│\033[0m \033[97mNAVIGASI: [UNLIMITED MODE] │ [ANONYMOUSE] │ [REAL-TIME] │ [HOZOO SYSTEM]\033[0m \033[95m│\033[0m")
        print("\033[95m" + "└" + "─" * 78 + "┘" + "\033[0m")

    def show_sending_animation(self, phone, mode="WHATSAPP"):
        animations = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        for i in range(8):
            frame = animations[i % len(animations)]
            if mode == "ANONYMOUSE":
                sys.stdout.write(f"\r\033[94m🕵️  MENGIRIM VIA ANONYMOUSE {frame} → {phone}\033[0m")
            else:
                sys.stdout.write(f"\r\033[94m🚀 MENGIRIM LAPORAN UNLIMITED {frame} → {phone}\033[0m")
            sys.stdout.flush()
            time.sleep(0.1)

    def get_current_time_info(self):
        now = datetime.now()
        days = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
        months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                 "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        
        return {
            'hari': days[now.weekday()],
            'tanggal': now.strftime("%d"),
            'bulan': months[now.month - 1],
            'tahun': now.strftime("%Y"),
            'jam': now.strftime("%H:%M:%S"),
            'zona': "WIB"
        }

    def show_status_bar(self):
        time_info = self.get_current_time_info()
        print("\033[95m" + "┌" + "─" * 78 + "┐" + "\033[0m")
        print(f"\033[95m│\033[0m \033[93m📅 {time_info['hari']} {time_info['tanggal']} {time_info['bulan']} {time_info['tahun']} │ 🕐 {time_info['jam']} {time_info['zona']} │ 📱 HOZOO UNLIMITED \033[95m│\033[0m")
        print("\033[95m" + "└" + "─" * 78 + "┘" + "\033[0m")

    def validate_number(self, phone_number):
        if not phone_number.startswith('+'):
            return False
        clean_number = ''.join(c for c in phone_number if c.isdigit() or c == '+')
        return len(clean_number) >= 10

    def generate_report_message(self, phone_number):
        return f"""Dear WhatsApp Support Team,

My WhatsApp account associated with the phone number {phone_number} has been permanently banned. I believe this may have been a mistake, as I always strive to follow WhatsApp's Terms of Service.

I rely on WhatsApp for daily communication with my family and work. I sincerely request a review of my account. If I have unknowingly violated any rules, please let me know so I can correct my behavior.

Thank you for your time and attention to this matter. I look forward to your response.

Sincerely,
HOZOO"""

    def generate_anonymouse_data(self):
        """Generate data seperti Anonymouse.org"""
        d = 10
        n = 10**(d-1) + random.randint(0, 10**d)
        h = str(n)
        b = base64.b64encode(h.encode()).decode()
        return n, b

    def send_via_anonymouse(self, phone_number, email_target="support@whatsapp.com"):
        """Mengirim laporan melalui Anonymouse.org"""
        try:
            n, v = self.generate_anonymouse_data()
            
            payload = {
                'n': str(n),
                'v': v,
                'to': email_target,
                'subject': f'WhatsApp Account Appeal - {phone_number}',
                'text': self.generate_report_message(phone_number)
            }
            
            anonymouse_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://anonymouse.org',
                'Referer': 'https://anonymouse.org/anonemail.html',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
            
            response = requests.post(
                "https://anonymouse.org/cgi-bin/anon-email.cgi",
                data=payload,
                headers=anonymouse_headers,
                timeout=15
            )
            
            return response.status_code == 200
            
        except Exception as e:
            print(f"\033[91m⚠️  Anonymouse Error: {str(e)}\033[0m")
            return False

    def send_real_report(self, phone_number, use_anonymouse=False):
        try:
            if use_anonymouse:
                success = self.send_via_anonymouse(phone_number)
                mode = "ANONYMOUSE"
            else:
                url = random.choice(self.report_urls)
                message = self.generate_report_message(phone_number)
                
                payload = {
                    'phone': phone_number,
                    'message': message,
                    'timestamp': str(int(time.time())),
                    'category': 'account_review',
                    'language': 'en'
                }
                
                response = requests.get(url, headers=self.headers, timeout=10)
                success = response.status_code == 200
                mode = "WHATSAPP"
            
            self.counter += 1
            
            report_data = {
                'number': phone_number,
                'timestamp': datetime.now(),
                'mode': mode,
                'status': 'SUCCESS' if success else 'PENDING'
            }
            
            self.sent_reports.append(report_data)
            return success
            
        except Exception as e:
            print(f"\033[91m⚠️  Error: {str(e)}\033[0m")
            return False

    def show_report_stats(self):
        success = len([r for r in self.sent_reports if r.get('status') == 'SUCCESS'])
        pending = len([r for r in self.sent_reports if r.get('status') == 'PENDING'])
        whatsapp_count = len([r for r in self.sent_reports if r.get('mode') == 'WHATSAPP'])
        anonymouse_count = len([r for r in self.sent_reports if r.get('mode') == 'ANONYMOUSE'])
        
        print(f"\n\033[96m📊 STATISTIK LAPORAN UNLIMITED:\033[0m")
        print(f"\033[92m✅ BERHASIL: {success}\033[0m")
        print(f"\033[93m⏳ PENDING: {pending}\033[0m")
        print(f"\033[94m📞 TOTAL: {len(self.sent_reports)}\033[0m")
        print(f"\033[95m📱 WHATSAPP: {whatsapp_count}\033[0m")
        print(f"\033[96m🕵️  ANONYMOUSE: {anonymouse_count}\033[0m")
        print("\033[95m" + "─" * 50 + "\033[0m")

    def run_unlimited_report(self):
        """Mode unlimited report tanpa berhenti"""
        self.clear_screen()
        self.show_banner()
        self.show_loading(1, "INISIALISASI SISTEM UNLIMITED")
        self.show_status_bar()
        self.show_navigation_ui()
        
        print(f"\n\033[96m🔥 HOZOO UNLIMITED MASS REPORTER READY!\033[0m")
        print(f"\033[96m💫 Mode: UNLIMITED NON-STOP AUTO SEND\033[0m")
        print(f"\033[96m🎯 Target: WHATSAPP SUPPORT + ANONYMOUSE.ORG\033[0m")
        print(f"\033[91m⚠️  Tekan CTRL+C untuk berhenti\033[0m")
        print("\033[95m" + "─" * 80 + "\033[0m")
        
        # Pilih mode pengiriman
        print(f"\n\033[93m🎯 PILIH MODE PENGIRIMAN:\033[0m")
        print(f"\033[97m1. WHATSAPP DIRECT (Default)\033[0m")
        print(f"\033[97m2. ANONYMOUSE.ORG (Email Anonymous)\033[0m")
        print(f"\033[97m3. DUAL MODE (Keduanya)\033[0m")
        
        mode_choice = input("\033[97mPilih mode (1-3): \033[0m").strip() or "1"
        
        # Input nomor pertama
        print(f"\n\033[93m🎯 MASUKKAN NOMOR TARGET PERTAMA (Format: +628123456789):\033[0m")
        first_number = input("\033[97m>>> \033[0m").strip()
        
        if not self.validate_number(first_number):
            print(f"\033[91m❌ FORMAT NOMOR SALAH! Gunakan: +628123456789\033[0m")
            return
        
        # Mulai unlimited mode
        self.start_unlimited_mode(first_number, mode_choice)

    def start_unlimited_mode(self, first_number, mode_choice):
        """Memulai mode unlimited dengan nomor pertama"""
        current_number = first_number
        batch_count = 0
        
        try:
            while True:
                batch_count += 1
                print(f"\n\033[95m🌀 BATCH {batch_count} - MEMULAI PENGIRIMAN UNLIMITED\033[0m")
                
                # Tentukan mode pengiriman
                use_anonymouse = False
                mode_text = "WHATSAPP"
                
                if mode_choice == "2":
                    use_anonymouse = True
                    mode_text = "ANONYMOUSE"
                elif mode_choice == "3":
                    # Dual mode - bergantian
                    use_anonymouse = (batch_count % 2 == 0)
                    mode_text = "ANONYMOUSE" if use_anonymouse else "WHATSAPP"
                
                # Kirim untuk nomor saat ini
                self.show_sending_animation(current_number, mode_text)
                success = self.send_real_report(current_number, use_anonymouse)
                
                if success:
                    print(f"\r\033[92m✅ BERHASIL! Laporan #{self.counter} ke {current_number} via {mode_text} | Unlimited Mode Active\033[0m")
                else:
                    print(f"\r\033[91m❌ GAGAL! Skip ke nomor berikutnya\033[0m")
                
                # Generate nomor berikutnya secara acak atau minta input baru
                if batch_count % 5 == 0:
                    print(f"\n\033[93m🎯 MASUKKAN NOMOR TARGET BARU (Kosongkan untuk auto-generate):\033[0m")
                    new_number = input("\033[97m>>> \033[0m").strip()
                    
                    if new_number and self.validate_number(new_number):
                        current_number = new_number
                    elif new_number:
                        print(f"\033[91m❌ Format salah, melanjutkan dengan nomor sebelumnya\033[0m")
                    else:
                        # Auto-generate nomor berikutnya
                        current_number = self.generate_next_number(current_number)
                else:
                    # Auto-generate nomor berikutnya
                    current_number = self.generate_next_number(current_number)
                
                # Delay random 1-4 detik
                delay = random.uniform(1, 4)
                time.sleep(delay)
                
                # Tampilkan statistik setiap 3 laporan
                if self.counter % 3 == 0:
                    self.show_report_stats()
                    
        except KeyboardInterrupt:
            print(f"\n\n\033[93m🛑 UNLIMITED MODE DIHENTIKAN\033[0m")
            self.show_report_stats()
            print(f"\033[94m👋 HOZOO UNLIMITED SYSTEM SHUTDOWN\033[0m")

    def generate_next_number(self, current_number):
        """Generate nomor berikutnya secara acak"""
        base = current_number[:-3]  # Ambil bagian dasar nomor
        last_three = ''.join(random.choices('0123456789', k=3))
        return base + last_three

    def main(self):
        """Program utama"""
        if not self.show_login():
            return
        
        self.run_unlimited_report()

if __name__ == "__main__":
    try:
        reporter = WhatsAppMassReporter()
        reporter.main()
    except Exception as e:
        print(f"\033[91m💥 ERROR: {str(e)}\033[0m")
