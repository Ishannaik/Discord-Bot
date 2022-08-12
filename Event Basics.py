import discord
from discord.ext import commands
import pytesseract
import cv2
import numpy as np
from PIL import Image
import requests
intents = discord.Intents.all()
bot = discord.Client(intents = intents)

@bot.event
async def on_ready():
    print("BOT IS ONLINE")

@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "hello":
         await msg.channel.send("Hello " + username)
@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}!")

############################################################ DISCORD OCR
def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite("removed_noise.png", img)
    cv2.imwrite(img_path, img)

    # Uncomment the BELOW LINE when deploying on HEROKU
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  
    
    result = pytesseract.image_to_string(Image.open(img_path))
    return result
    
bot = commands.Bot(command_prefix='.', description="This is an OCR-Bot named Sigma")

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Sigma"))
    print("Lessa GO!! It's Sigma Time!!!!")

@bot.event
async def on_message(message):
    try:
        url = message.attachments[0].url
        r = requests.get(url)
        filename = "img.png"
        with open(filename, 'wb') as out_file:
            out_file.write(r.content)
        print(url)
        context = await bot.get_context(message)
        ocr = get_string("img.png")
        try:
            await context.send(ocr)
        except:
            await context.send("Sigma couldn't find any text in your image please retry")
    except:
        pass
    await bot.process_commands(message)
############################################################ DISCORD OCR

###@bot.event
###async def on_raw_reaction_add(payload):
    #on_reaction_add













bot.run("MTAwNTE2MzAyMDE5Mzg5ODYwNg.G3PE9B.aqa1Bav9m9Irl9ff7CyDqEASPKmj88qI67GRDc")