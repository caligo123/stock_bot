#-*- coding:utf-8 -*-

import discord



######################################################################################################## ----------------셀레늄
from selenium import webdriver  # 1
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#한화3우B, cj대한통운, LG유플러스, NH투자증권우
#체크할 종목명들 리스트
stocks = [];
stocks.append('한화3우B')
stocks.append('CJ대한통운')
stocks.append('LG유플러스')
stocks.append('NH투자증권우')

#네이버 증권 주소
url = 'https://finance.naver.com/'

#초기설정
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# 사람처럼 보이게 하는 옵션들
options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정
# 2========================================================================================================================================================================
# 오류 시 chromedriver 경로 바꾸기 (c드라이브부터 .exe까지)#1
driver = webdriver.Chrome("C:/Users/bigla/OneDrive/문서/개인/프로젝트/주식알림봇/Stock_Bot/stock_bot/chromedriver87.exe")  # 1
# ========================================================================================================================================================================
######################################################################################################## ----------------셀레늄



#디코 시작
######################################################################################################## ----------------디코 시작
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} 에 로그인하였습니다.')


@client.event
async def on_message(message):
    s = message.content.split()
    if s[0]=='Ping' : 
        print('pong')
        await message.channel.send('pong')
    
    elif s[0]=='activate':
        while(1):
            #루프의 해당 종목명 검색=============================================================================================
            for stock in stocks: #stocks 내의 주식 종목 갯수만큼 반복
                driver.get(url)  # 1
                #루프의 해당 종목명 검색=============================================================================================
                search_box = driver.find_element_by_xpath("//*[@id='stock_items']")  # 로그인 아이디 입력 박스 검사해서 따온 xpath 넣기 
                search_box.click()
                search_box.clear()
                search_box.send_keys(stock)
                #기다리기
                driver.implicitly_wait(1)
                WebDriverWait(driver, 10)
                #해당 종목 급등/급락 확인하는 작업=========================================================================================
                

                
            #루프의 해당 종목명 검색=============================================================================================


    
            



client.run('ODAyMDE1MzA3NDQ3MDA5Mjgw.YApE9g.8iikYwHwGZ_p_UygmHM_-NEGRNc')
