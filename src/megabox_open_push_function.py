import json
import time
import subprocess
import requests
import logging
import datetime
from datetime import datetime

def run_megabox_open_push_status():
    while True:
        save_log_info("megabox_open_push_status.py restarted.")
        process = subprocess.Popen(['python', 'megabox_open_push_status.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(3600)
        process.kill()

# 로그 저장
def save_log_info(log, is_log_file=False):
    if is_log_file:
        logging.info(log)
    print(f"[{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')}] {log}", flush=True)

def save_log_error(log, is_log_file=True):
    if is_log_file:
        logging.error(log)
    print(f"[{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')}] {log}", flush=True)

def get_request_to_megabox_api(url, cookies, headers, json_data):
    
    response = requests.post(
        url = url,
        cookies = cookies,
        headers = headers,
        json = json_data,
        verify = False,
    )
    # 응답 본문 추출
    response_body = response.content
    # UTF-8 디코딩
    response_text = response_body.decode('utf-8-sig')
    # JSON 데이터 파싱
    data = json.loads(response_text)
    # 응답결과 리턴
    return data

def extract_movie_date_from_megabox_api(data):
    movie_date = data.get("movieFormDeList")
    return movie_date