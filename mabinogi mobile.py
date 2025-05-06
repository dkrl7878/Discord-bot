import discord
import asyncio

# 인텐트 설정 (메시지 콘텐츠 읽기 포함)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():  # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇의 상태메시지"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # 봇 자신이 보낸 메시지는 무시

    if message.content == "테스트":  # 메시지 감지
        await message.channel.send(f"{message.author} | {message.author.mention}, Hello")
        await message.author.send(f"{message.author} | {message.author.mention}, User, Hello")

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('MTM2OTI0NTIyNzAxMzExMTkyOA.GWWrK7.4sCJvzse7fJBthcdy0F1QzFycBNjJvUKRnskjw')