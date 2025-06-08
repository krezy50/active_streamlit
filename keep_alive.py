# keep_alive.py
import requests
import os
import datetime

# Streamlit 앱 URL을 환경 변수에서 가져옵니다.
# Render Cron Job 설정 시 'STREAMLIT_APP_URL'이라는 환경 변수를 추가할 것입니다.
STREAMLIT_APP_URL = os.environ.get("STREAMLIT_APP_URL")

if not STREAMLIT_APP_URL:
    print("Error: STREAMLIT_APP_URL environment variable is not set.")
    exit(1)

try:
    response = requests.get(STREAMLIT_APP_URL, timeout=10) # 10초 타임아웃
    if response.status_code == 200:
        print(f"[{datetime.datetime.now()}] Successfully pinged Streamlit app: {STREAMLIT_APP_URL}. Status Code: {response.status_code}")
    else:
        print(f"[{datetime.datetime.now()}] Failed to ping Streamlit app: {STREAMLIT_APP_URL}. Status Code: {response.status_code}")
        print(f"Response content: {response.text[:200]}...") # 에러 내용 일부 출력
except requests.exceptions.RequestException as e:
    print(f"[{datetime.datetime.now()}] An error occurred while pinging Streamlit app {STREAMLIT_APP_URL}: {e}")