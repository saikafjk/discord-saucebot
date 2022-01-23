import discord
import os
import time, requests, random
from bs4 import BeautifulSoup as bs

link = 'https://nhentai.net/'

anidir = 'DIR HERE'
hendir = 'DIR HERE'

client = discord.Client()

help_message = '''
>>> SauceGenBot reacts to these commands:
 
`?help` - display this message
`?anime` - recommend random anime
`?hentai` - recommend random hentai
`?sauce` - generate random sauce
`?version` - displays SauceGenBot version
'''

version = 'SauceGenBot is currently v0.6'

def initial():
    #open anime list file
    f = open(anidir,'r+')
    
    #create new list
    global anilist
    anilist = []
    
    #Count how many titles
    while True:
        line = f.readline()
        
        #store titles to list
        anilist.append(line)
        
        if not line:
            break
            
    f.close();

def animeGen():
    anicount = 0;
    
    #open anime list file
    f = open(anidir,'r+')
    
    #Count how many titles
    while True:
        anicount += 1
        
        line = f.readline()
        
        if not line:
            break
    
    #close file
    f.close()

    #Generate random value
    val = random.randint(0,anicount)
    
    #Generate random title based on list
    title = anilist[val]
    
    #Generate MAL search link
    #rpl = title.replace(" ","%20")
    #search = 'https://myanimelist.net/search/anime?q=' + title.replace(' ','%20') + '&cat=anime'
    #search1 = search.replace('\n','')
    
    #print(search1)
    #r = requests.get(search1)
    #print(r.status_code)
    
    return(title)

def sauceGen():
    r = requests.get(link)
    soup = bs(r.content, 'html.parser')

    # Find "New Uploads" div
    divtag = soup.find_all('div', class_="container index-container")

    # Get the latest
    for tag in divtag:
        a = tag.find_all('a', class_='cover', href=True)

        for i in a[:1]:
            text = i['href']
            set0 = text

    # Extract number
    set1 = set0.replace('/g/', '')
    set2 = set1.replace('/','')

    page = int(set2)
    
    for i in range(10):
        val = random.randint(000000, page)
        sauce = 'From Nhentai: ' + str(val) + ' \n\nLink: https://nhentai.net/g/' + str(val)
    
    return(sauce)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #print(str(message) + '\n');
  
  if message.author == client.user:
    return
        
  if message.content.startswith('!STOP'):
      await message.channel.send('Stopped bot.')
      exit()
  
  if message.content.startswith('?help'):
      await message.channel.send(help_message)
  
  if message.content.startswith('?sauce'):
      saucegen = sauceGen()
      await message.channel.send(saucegen)
      
  if message.content.startswith('?hentai'):
      await message.channel.send('UNDER CONSTRUCTION!')
      
  if message.content.startswith('?anime'):
      await message.channel.send('Anime Recommendation: ' + animeGen())    
  
  if message.content.startswith('?version'):
      await message.channel.send(version)   

initial()
client.run('TOKEN HERE')