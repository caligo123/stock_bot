#-*- coding:utf-8 -*-

import discord



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
            await message.channel.send('activated')
    
            



client.run('ODAyMDE1MzA3NDQ3MDA5Mjgw.YApE9g.8iikYwHwGZ_p_UygmHM_-NEGRNc')
