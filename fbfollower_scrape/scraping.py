
from playwright.sync_api import sync_playwright
import time
import random
import requests

base_url = "https://www.facebook.com/fabrizioromanoherewego"
api_url = "http://127.0.0.1:8000/api/fb-followers/"  # Your Django API

def parse_follower_count(text):
    """
    Converts strings like '26M', '1.2K', '345' to proper integers.
    """
    text = text.strip().upper().replace(",", "")
    if text.endswith("K"):
        return int(float(text[:-1]) * 1_000)
    elif text.endswith("M"):
        return int(float(text[:-1]) * 1_000_000)
    elif text.isdigit():
        return int(text)
    else:
        raise ValueError(f"Cannot parse follower count: {text}")

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=r"C:\Users\dell\OneDrive\Desktop\apiscrape\scraper\user",
        channel="chrome",
        no_viewport=True,
        headless=True,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        locale="en-US",
        args=["--start-maximized"]
    )

    context.add_init_script("""
        Object.defineProperty(navigator,'webdriver',{get:() => undefined});
        window.chrome = {runtime:{}};
        Object.defineProperty(navigator,'plugins',{get:() => [1,2,3,4,5]});
        Object.defineProperty(navigator,'languages',{get:() => ['en-US','en']});
    """)

    page = context.new_page()

    def get_follower_count():
        try:
            page.goto(base_url, wait_until="domcontentloaded")
            time.sleep(4)

            follower_1 = page.locator("a[href*='followers'] strong").inner_text()
            follower_int = parse_follower_count(follower_1)
            print("Follower count:", follower_int)

            # Send to API
            data = {
                "page_name": "fabrizioromanoherewego",
                "followers": follower_int
            }
            response = requests.post(api_url, json=data)
            print("Sent to API:", response.status_code)

        except Exception as e:
            print("Failed to fetch/send followers:", e)

    while True:
        get_follower_count()
        sleep_time = 30 + random.uniform(-5, 5)
        print(f"Waiting {round(sleep_time)} seconds...\n")
        time.sleep(sleep_time)
