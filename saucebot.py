import discord
import os
import json

import time, requests, random
from bs4 import BeautifulSoup as bs

link = 'https://nhentai.net/'

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
  
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
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if message.content.startswith('?sauce'):
      saucegen = sauceGen()
      await message.channel.send(saucegen)

client.run('TOKEN HERE')
