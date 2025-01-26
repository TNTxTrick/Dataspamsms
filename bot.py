import os
import requests
import re
from time import sleep, time
from datetime import datetime
from telebot import TeleBot
from concurrent.futures import ThreadPoolExecutor

# Cấu hình bot Telegram
TELEGRAM_BOT_TOKEN = "7296526311:AAFProE6bBnY_kZU1LBF9WGp83BG4kyg4i8"
CHAT_ID = "6602753350"  # ID của nhóm hoặc người nhận
bot = TeleBot(TELEGRAM_BOT_TOKEN)

# Danh sách các website đào proxy
listwebsite = [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", 
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all",
]

# Tên tệp proxy live ban đầu
proxy_file = "live_proxies.txt"

def clear():
    """Xóa màn hình console."""
    os.system("cls" if os.name == "nt" else "clear")

def get_proxies_from_website(url):
    """Đào proxy từ website."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            pattern = r'\b(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\b'
            proxy_matches = re.findall(pattern, response.text)
            return proxy_matches
    except Exception:
        pass
    return []

def check_proxy(proxy):
    """Kiểm tra tính khả dụng của proxy."""
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    try:
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        if response.status_code == 200:
            return proxy
    except requests.exceptions.RequestException:
        pass
    return None

def process_proxy(proxy):
    """Xử lý và lưu proxy live."""
    result = check_proxy(proxy)
    if result:
        with open(proxy_file, 'a') as live_file:
            live_file.write(result + '\n')
        print(f"\033[1;32m[Live] {result}")
    else:
        print(f"\033[1;31m[Dead] {proxy}")

def scrape_proxies():
    """Đào proxy từ danh sách website và kiểm tra proxy live."""
    proxies = []
    for web in listwebsite:
        proxies.extend(get_proxies_from_website(web))
    print(f"\033[1;34mĐã đào được {len(proxies)} proxy từ các nguồn.\033[0m")

    # Sử dụng ThreadPoolExecutor để kiểm tra proxy song song
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(process_proxy, proxies)

    print(f"\033[1;32mProxy live đã được lưu vào {proxy_file}.\033[0m")

def send_file_to_telegram():
    """Gửi tệp proxy tới Telegram và tạo tệp mới sau khi gửi."""
    global proxy_file
    try:
        if os.path.exists(proxy_file) and os.path.getsize(proxy_file) > 0:
            with open(proxy_file, 'rb') as file:
                bot.send_document(CHAT_ID, file, caption="🔗 Proxy Live: Đây là danh sách proxy hiện tại.")
            print("\033[1;32mTệp proxy đã được gửi thành công tới Telegram.\033[0m")
            
            # Xóa tệp sau khi gửi
            os.remove(proxy_file)
            print("\033[1;33mTệp proxy đã được xóa.\033[0m")
            
            # Tạo tệp mới với thời gian
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            proxy_file = f"live_proxies_{current_time}.txt"
            print(f"\033[1;34mTạo tệp mới: {proxy_file}\033[0m")
        else:
            print("\033[1;31mKhông có proxy live để gửi.\033[0m")
    except Exception as e:
        print(f"\033[1;31mLỗi khi gửi tệp proxy: {e}\033[0m")

# Hàm đào liên tục trong 15 phút và gửi tệp sau đó
def continuous_scrape_and_send():
    start_time = time()
    while True:
        # Kiểm tra nếu đã đủ 15 phút (900 giây)
        if time() - start_time >= 900:
            # Gửi tệp proxy
            send_file_to_telegram()
            # Reset thời gian bắt đầu
            start_time = time()

        # Đào proxy trong vòng 15 phút
        scrape_proxies()
        
        # Đợi 10 giây giữa các lần đào
        sleep(10)

# Chạy chương trình
clear()
print("\033[1;34mChương trình sẽ tự động đào proxy, kiểm tra và gửi tệp proxy live tới Telegram mỗi 15 phút.\033[0m")

continuous_scrape_and_send()  # Bắt đầu đào và gửi liên tục