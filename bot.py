import discord
from discord.ext import commands
import os
import time
import threading
import asyncio
from youtube_dl.utils import ytdl_is_updateable
from youtubesearchpython import VideosSearch
import json
from ast import literal_eval
import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})


from youtubesearchpython.internal.constants import ResultMode
def search(url):
    global st
    videosSearch = VideosSearch(url, limit = 1)
    #print(videosSearch.result()['result'][0]['link'])
    print(videosSearch.result()['result'][0]['link'])
    st = videosSearch.result()['result'][0]['link']

    return st
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def download(url, filename):
    if os.path.isfile(filename) == False: 
        os.system('youtube-dl --extract-audio --audio-format mp3  --external-downloader aria2c -o  "'+ filename+'" ' + url)    
        
def getcachetitle(url):
    global ct
    videosSearch = VideosSearch(url, limit = 1)
    #print(videosSearch.result()['result'][0]['id'])
    ct = (videosSearch.result()['result'][0]['id'])
    return ct

client = commands.Bot(command_prefix=".")
arr = []
context = None
st = str
ct = str
index = 1 
pause_thread = False


@client.event
async def on_ready():
    print('Ready to Rock!')

def q_push(url):
    arr.append(url)

def q_pop():
    if len(arr) > 0:
        return arr.pop(0)

    return None

@client.command()
async def play(ctx, *url : str):
    #url = ""
    global pause_thread 
    global context
    global index 
    pause_thread = False


    context = ctx
    voice = discord.utils.get(client.voice_clients, guild=context.guild)    
 
    if voice == None or not voice.is_connected:
        await connect(context)

    print(url)
    if url == ():
        await ctx.reply("can't download this, please specify a song")
        return
    #urlj = ''.join(url).replace("'", "\\'")
    urls = str(url)
    urln = urls.replace("'", "\\'")
    print(urln)
    search(urln)
    getcachetitle(urln)
    await ctx.reply(":thumbsup: Downloading your wonderful song, it may take a while, depending on the size :100: \n Link:paperclip::computer: = " + st)
    filename = "./songs/"+str(ct)+".mp3"
    download(st, filename)

    if os.path.exists(filename):
            q_push(filename)
    else:
        await ctx.reply("can't download this song")

async def connect(ctx):
    channel = ctx.author.voice.channel
    try:
        await channel.connect()
    except:
        print("already connected!")
    
async def playaudio(ctx, filename):
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio(filename))
    
def dele(filename):
    os.system('rm ' + filename)

@client.command()
async def sendmess(ctx):
    await ctx.reply("ciao")
    
@client.command()
async def pause(ctx):
    global pause_thread

    server = ctx.message.guild
    voice_channel = server.voice_client                
    voice_channel.pause()
    pause_thread = True
    print('pause')

@client.command()
async def resume(ctx):
    global pause_thread
    server = ctx.message.guild
    voice_channel = server.voice_client                
    voice_channel.resume()
    pause_thread = False

    
@client.command()
async def skip(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
 
        await ctx.reply("if i'm downloading a song i'll play it as soon as it gets downloaded")
        voice.stop()
       
@client.command()
async def leave(ctx):
    global pause_thread 
    global index    
    global arr

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        voice.is_connected = False
        #os.system('rm ./songs/*.mp3')
        arr = []
        index = 1
        pause_thread = True


async def mainloop():
    global arr 
    global context
    global client

    while True:
#        print(pause_thread)
        if pause_thread == True:
           time.sleep(0.5)
           continue

        if context != None:
            #print(pause_thread)
            voice = discord.utils.get(client.voice_clients, guild=context.guild)

            #if voice == None or not voice.is_connected:
                #await connect(context)
            if voice != None and context != "" and voice.is_connected():
                if not voice.is_playing():
                    song = q_pop()
                    if song != None:
                        await playaudio(context, song)

                        #try:
                        #    time.sleep(0.4)
                        #    os.remove(song)
                        #except UnboundLocalError: 
                        #    print("")
        time.sleep(1)

def ans(ctx):
    ctx.reply(":thumbsup:The Download is :100: OVER :100: ")


x = threading.Thread(target=asyncio.run, args=(mainloop(),))
x.start()


client.run('token')
