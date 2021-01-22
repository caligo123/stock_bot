#-*- coding:utf-8 -*-

import discord

import bs4
import requests



#한화3우B, cj대한통운, LG유플러스, NH투자증권우
#체크할 종목명들 리스트
stocks = [];
stocks.append('A00088K')#한화3우B
stocks.append('A000120')#CJ대한통운
stocks.append('A032640')#LG유플러스
stocks.append('A005945')#NH투자증권우

#다음 증권 주소
url = 'https://finance.daum.net/'

url1 = 'https://finance.daum.net/quotes/'
url2 = '#home'



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
        #while(1):
        for stock in stocks:
                page = requests.get(url1+stock+url2)
                soup = bs4.BeautifulSoup(page.content,"html.parser")

                box = soup.find_all(attrs={'class':'currentStk'})
                
                


                percent = soup.p['data-realtime-change-ratio']
                percent2 = soup.find_all()
            
                print(soup.p)
                soup.find_all("p")
                ps = soup.find_all("p")

                for p in ps:
                    print(p)

            



client.run('ODAyMDE1MzA3NDQ3MDA5Mjgw.YApE9g.8iikYwHwGZ_p_UygmHM_-NEGRNc')
