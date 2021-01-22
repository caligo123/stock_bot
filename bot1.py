#-*- coding:utf-8 -*-

import discord

def get_num(s):
    return float(''.join(ele for ele in s if ele.isdigit() or ele == '.'))



######################################################################################################## ----------------셀레늄
from selenium import webdriver  # 1
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import re

class Stock:
    code = ' '
    name = ' '
    per = 0
    def __init__(self, name,code):
        self.name = name
        self.code = code

    def update_per(self,per):
        self.per = per    

#한화3우B, cj대한통운, LG유플러스, NH투자증권우
#체크할 종목명들 리스트





stocks = [];
stocks.append('A00088K')#한화3우B
stocks.append('A000120')#CJ대한통운
stocks.append('A032640')#LG유플러스
stocks.append('A005945')#NH투자증권우



#네이버 증권 주소
url = 'https://finance.daum.net/quotes/'

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
        await message.channel.send('activated')
        while(1):
            #루프의 해당 종목명 검색=============================================================================================
            for stock in stocks: #stocks 내의 주식 종목 갯수만큼 반복
                url1 = url + stock + '#home'
                driver.get(url1)  # 1
                
                #종목명 찾기
                #name = WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/span/div/span[1]/span[1]/span[1]/a/text()"))
                

                #해당 종목 급등/급락 확인하는 작업=========================================================================================
                percent = WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/span/div/span[1]/span[1]/span[3]/p[2]"))
                perNum = re.findall('\d+',percent.text)
                
                print(percent.text[1])
                print(percent.text[1]+1)

                if(get_num(percent.text)>0.5):
                    await message.channel.send(name.text + "의 급변화 감지!")
                    
                    if(percent.text[0]=='+'):
                        await message.channel.send(name.text + " 이/가 급등 중 입니다!")
                    if(percent.text[0]=='-'):
                        await message.channel.send(name.text + " 이/가 급락 중 입니다!")
                       


                driver.implicitly_wait(1)
                WebDriverWait(driver, 10)

                
            #루프의 해당 종목명 검색=============================================================================================


    
            



client.run('ODAyMDE1MzA3NDQ3MDA5Mjgw.YApE9g.8iikYwHwGZ_p_UygmHM_-NEGRNc')
