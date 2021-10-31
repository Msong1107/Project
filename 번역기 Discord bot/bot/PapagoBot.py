
import discord
import yaml
from asyncio import *
from discord.ext import commands
from urllib.error import HTTPError, URLError
from translator import dataProcessStream

client_id = "client_id"
client_secret = "client_secret"
token = "토큰"


streamInstance = dataProcessStream(client_id,client_secret)


client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!도움말"))
    print("{0.user}".format(client))

@client.event
async def on_message(message):
    def sendmsg(resultPackage) -> discord.Embed:
        if resultPackage['status']["code"] < 300:
            embed = discord.Embed(title=f"번역기 | {resultPackage['data']['ntl']['name']} > {resultPackage['data']['tl']['name']}",description="", color=0x5CD1E5)
            embed.add_field(name=f"전 {resultPackage['data']['ntl']['name']}", value=resultPackage['data']['ntl']['text'],inline=False)
            embed.add_field(name=f"후 {resultPackage['data']['tl']['name']}", value=resultPackage['data']['tl']['text'],inline=False)
            embed.set_thumbnail(url="")
            embed.set_footer(text="네이버 Papago Api",icon_url='')
            return embed
        else:
            embed = discord.Embed(title="Error Code", description=resultPackage['status']['code'],color=0x5CD1E5)
            return embed
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith("!한영번역"):
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("번역 완료!", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send(f"번역 실패! 다시 해주세요 : {e}")

    if message.content.startswith("!영한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("번역 완료!", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("번역 실패! 다시 해주세요")

    if message.content.startswith("!한일번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("번역 완료!", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("번역 실패! 다시 해주세요")

    if message.content.startswith("!일한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("번역 완료!", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("번역 실패! 다시 해주세요")

    if message.content.startswith("!한중번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("번역 완료!", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("번역 실패! 다시 해주세요")

    if message.content.startswith("!중한번역"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        trsText = message.content.split(" ")
        try:
            if len(trsText) == 1:
                await message.channel.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send("번역 완료!", embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("번역 실패! 다시 해주세요")
client.run(token)
