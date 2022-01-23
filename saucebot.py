import discord
import os
import time, requests, random
from bs4 import BeautifulSoup as bs

link = 'https://nhentai.net/'

client = discord.Client()

help_message = '''
>>> SauceGenBot reacts to these commands:
 
`?help` - display this message
`?anime` - recommend random anime
`?hentai` - recommend random hentai
`?sauce` - generate random sauce
'''

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
      await message.channel.send('UNDER CONSTRUCTION!')    

client.run('OTM0NDQzMzA4MDk5NDYxMTQw.YewKJQ.3fln12k8GDItI3E_wu68dOV7oQA')