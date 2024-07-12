import discord
from discord.ext import commands
import random
import datetime

# 봇 인스턴스 생성
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# 봇이 준비되었을 때 실행되는 이벤트
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content == "바보":
        await message.channel.send("바보라는 사람이 바보임 ㅇㅇ")
    elif message.content == "안녕":
        await message.channel.send("ㅎㅇ")
    elif message.content == "롤":
        await message.channel.send("이거 정신병임")
    elif message.content == "슬더스":
        await message.channel.send("이거 게임 아님 ㅇㅇ")
    elif message.content == "운동":
        await message.channel.send(f"{message.author.display_name}야 운동해라")
    elif message.content == "오늘":
        today = datetime.datetime.now()
        if today.weekday() == 0:
            await message.channel.send("월요일 조아")
        elif today.weekday() in [5,6]:
            await message.channel.send("주말 개꿀")
        else:
            await message.channel.send("아 나가기 싫어!")
    elif message.content == "내일":
        today = datetime.datetime.now()
        if today.weekday() == 6:
            await message.channel.send("월요일 조아")
        elif today.weekday() in [4,5]:
            await message.channel.send("주말 개꿀")
        else:
            await message.channel.send("아 나가기 싫어!")
    elif message.content == "어제":
        await message.channel.send("난 너가 어제 뭐 한지 알고 있다.")
        
    await bot.process_commands(message)


@bot.command()
async def 선택(ctx,usr_choice:str):
    choices = ['가위','바위','보']
    bot_choice = random.choice(choices)
    await ctx.send('가위 바위 보!')
    if usr_choice not in choices:
        await ctx.send('님 쫄?')

    result = determine_winner(usr_choice, bot_choice)
    await ctx.send(f'{result}')


def determine_winner(usr_choice, bot_choice):
    choices = ['가위','바위','보']
    if usr_choice == bot_choice:
        return "아 짜치네!"
    elif (usr_choice == 'rock' and bot_choice == 'scissors') or \
            (usr_choice == 'paper' and bot_choice == 'rock') or \
            (usr_choice == 'scissors' and bot_choice == 'paper'):
        return "님이 이김!"
    elif usr_choice not in choices:
        return "님이 안냈으니 내가 이긴거임 ㅇㅇ"
    else:
        return "내가 이김!"

@bot.command()
async def 로또(ctx):
    await ctx.send('추첨을 시작하겠습니다.')
    random_ball = [random.randint(1,10) for _ in range(3)]
    ball_select = [random.randint(1,10) for _ in range(3)]
    if random_ball == ball_select:
        await ctx.send('오 당첨인데?')
    else:
        await ctx.send('응 꽝이야')
    
    



@bot.command()
async def 훈수(ctx):
    await ctx.send('아 그거 그렇게 하는 거 아닌데')
    ## 여기다가 해당 내용에 대한 API나 검색엔진을 활용해서 크롤링하여 훈수를 두는 형식으로 작동
    ### input your code!

# 디스코드 봇 토큰
TOKEN = 'INPUT TOKEN!!!!!'

# 봇 실행
bot.run(TOKEN)
