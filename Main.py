import discord
import cohere
import random 
import os
from gtts import gTTS
#pip install discord.py==1.7.3 [use this version]

token = "Discord_Bot_Token" #use your Discord Bot Token Here
co = cohere.Client('Cohere_api_key') #use your Co:here api key here
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():print(f"Bot logged in as {client.user}")#checking if bot is upor not
  
@client.event
async def on_message(message):   
  if message.author != client.user:
    if message.content.startswith('!h'):
      x=co.generate(  model='xlarge',prompt=message.content+':',max_tokens=50,temperature=0.9,k=0,p=0.75,frequency_penalty=1,presence_penalty=0,stop_sequences=["-"],return_likelihoods='NONE')
      g=str(x.generations[0].text)
      await message.reply(g)
    elif message.content.startswith("!tts"):
      xo=message.content
      xo=xo[4:]
      language = 'te'
      myobj = gTTS(text=xo, lang=language, slow=False)
      myobj.save("welcome.mp3")
      await message.reply(file=discord.File('welcome.mp3'))
    elif message.content.startswith('!cancer'):
      x=co.generate(  model='xlarge',prompt=message.content+':',max_tokens=50,temperature=0.9,k=0,p=0.75,frequency_penalty=1,presence_penalty=0,stop_sequences=["-"],return_likelihoods='NONE')
      g=str(x.generations[0].text)
      await message.reply(g)
    
    elif message.content.startswith("!poll"):
      lns=0
      emjs=['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','⏸️']
      po=message.content
      qo = po.split("\n")
      for i in qo:
        if i:
          lns += 1
      if lns>1 and lns<12:
        emjs1=emjs[1:lns]
        ro=random.choice(emjs1)	  
        await message.add_reaction(ro)
      else:
        await message.reply(random.choice(range(0, lns))	)
    elif message.content.startswith('!'):
      y=message.content
      p=y.replace('!',' ')
      q=p.split(" ")
      ls=['health','vitamin','vitamins','Proteins','Protein','biotin','Nutrients']
      jk=['is','is/are best for','are in','are good for','are bad for','can be extracted from']
      check = False
      for m in q:
        for n in ls:
          if m == n:
            check = True
            t=m
            if check:
              x=co.generate(  model='xlarge',prompt=message.content+':',max_tokens=50,temperature=0.9,k=0,p=0.75,frequency_penalty=1,presence_penalty=0,stop_sequences=["-"],return_likelihoods='NONE')
              g=str(x.generations[0].text)
              await message.reply(g)    
    elif message.content.startswith('!'):
      x=co.generate(  model='xlarge',prompt=message.content+':',max_tokens=50,temperature=0.9,k=0,p=0.75,frequency_penalty=1,presence_penalty=0,stop_sequences=["-"],return_likelihoods='NONE')
      g=str(x.generations[0].text)
      await message.reply(g)
client.run(token)
