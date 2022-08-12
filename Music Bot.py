import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = "!")

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    if voice_client:
        await voice_client.disconnect()
        print("Bot left the voice channel")
    else:
        print("Bot was not in channel")











bot.run("MTAwNTE2MzAyMDE5Mzg5ODYwNg.G3PE9B.aqa1Bav9m9Irl9ff7CyDqEASPKmj88qI67GRDc")