import sys
import time
from megabox_open_push_function import *
from megabox_open_push_global_variable import *

# 영화 업데이트 내역 확인 로직
def dolby_cinema_main(url, cookies, headers, json_data, target_name, message_queue):
    try:
        # 첫 응답 저장
        response1 = extract_movie_date_from_megabox_api(get_request_to_megabox_api(url, cookies, headers, json_data))
        response2 = []
        while True:
            # 2번에 새 응답 저장
            response2 = extract_movie_date_from_megabox_api(get_request_to_megabox_api(url, cookies, headers, json_data))
            # log 저장
            save_log_info(f"{target_name} responsed.", True)
            # 날짜 추출
            set1 = {item['playDe'] for item in response1}
            set2 = {item['playDe'] for item in response2}
            # 새 응답과 저장된 이전 응답이 다르다면
            if set1 != set2:
                diff = set2 - set1
                # 추가된 변경사항이 있다면
                if len(diff) != 0:
                    added_result = ", ".join(diff)
                    save_log_info(f'{target_name} added item : {diff}, set1 : {set1}, set2 : {set2}, response1 : {response1}, response2 : {response2}')
                    # 추가된 변경사항 푸시알림 보내기
                    try:
                        message_queue.put([target_name, "**예매 오픈 알림** : " + str(added_result)])
                    except Exception as e:
                        save_log_error(f'{target_name} error when sending open push : {e}')
                        # 5초 대기 후 다시 알림 보내기 시도
                        time.sleep(5)
                        message_queue.put([target_name, "**예매 오픈 알림** : " + str(added_result)])
                # response1 값은 변경된 값으로 초기화
                response1 = response2
            # 5분마다 새로고침
            time.sleep(300)
    # 오류 발생 시
    except Exception as e:
        save_log_error(f'{target_name} error : {e}')
        # 다시 실행
        os.execl(sys.executable, sys.executable, *sys.argv)