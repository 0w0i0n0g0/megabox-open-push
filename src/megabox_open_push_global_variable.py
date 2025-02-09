import os

##################################################
# ENV
discord_bot_token = os.environ["DISCORD_BOT_TOKEN"]



##################################################
# discord channel id

discord_channel_id_dictionary = {
    "LOG": 1309139853631557632,
    "ANNOUNCEMENT": 1309141746978131988,
    "COEX-DOLLBY": 1311285423208792075,
}



##################################################
# megabox_open_push_dolby_cinema.py

dolby_cinema_url = 'https://www.megabox.co.kr/on/oh/ohb/SimpleBooking/selectBokdList.do'

dolby_cinema_cookies = {
    'WMONID': 'DiWiTYLVOiT',
    '_ga': 'GA1.1.1370743338.1720490451',
    'JSESSIONID': '5fVi4pXp3VEzlT0UW1BHIYfwEydfWyGQZMQ3mX6eDPfFwe78z1uiXEBLBxvuetH6.b25fbWVnYWJveF9kb21haW4vbWVnYS1vbi1zZXJ2ZXIy',
    'SESSION': 'ZWUzYTQxYTMtNzJhNy00YWI0LTkyYmUtZjVjZWM1ZGI2NTQ5',
    '_ga_5JL3VPLV2E': 'GS1.1.1720511739.2.1.1720511743.56.0.0',
    '_ga_LKZN3J8B1J': 'GS1.1.1720511739.2.1.1720511744.0.0.0',
}

dolby_cinema_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://www.megabox.co.kr',
    'Pragma': 'no-cache',
    'Referer': 'https://www.megabox.co.kr/on/oh/ohb/SimpleBooking/simpleBookingPage.do?rpstMovieNo=&theabKindCode1=&brchNo1=&sellChnlCd=&playDe=&naverPlaySchdlNo=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

dolby_cinema_json_data = [
    {
        # 코엑스 돌비시네마
        'arrMovieNo': '',
        'playDe': '20240709',
        'brchNoListCnt': 1,
        'brchNo1': '1351',
        'brchNo2': '',
        'brchNo3': '',
        'areaCd1': 'DBC',
        'areaCd2': '',
        'areaCd3': '',
        'spclbYn1': 'Y',
        'spclbYn2': '',
        'spclbYn3': '',
        'theabKindCd1': 'DBC',
        'theabKindCd2': '',
        'theabKindCd3': '',
        'brchAll': '',
        'brchSpcl': 'DBC',
        'movieNo1': '',
        'movieNo2': '',
        'movieNo3': '',
        'sellChnlCd': '',
    },
]

dolby_cinema_target_name = [
    "COEX-DOLLBY",
]