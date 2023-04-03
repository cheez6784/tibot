'''

The full code for Tibytes V1.0, fully commented.
External files exist, and for privacy purposes, are not included. Bot token is in a seperate environment variable for the same reasons.
Do not run. This code is dependent on other files and resources.

'''


# Basic imports of all needed modules
import discord
import os
import requests, random
from discord.utils import get
import asyncio
import re
from urllib.parse import urlparse







#This is youtube channel data that is used to get videos.
channel = "https://www.youtube.com/@Tibytes"
blUIDLink = "https://beatleader.xyz/u/"
html = requests.get(channel + "/videos").text
info = re.search('(?<={"label":").*?(?="})', html).group()
videoUrl = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
#Poll command variables
twovotes = 0
onevotes = 0
#These are a list of moderators with access to moderator features (Me for testing purposes)
mods = ["Tibytes#2121", "Cheez#5224"]
#Basic discord client and intent stuff
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
#A list of "favorite songs"
favsong = ["https://www.youtube.com/watch?v=KouvBEP0PgI", "https://www.youtube.com/watch?v=JjRWh3TW_ms", "https://www.youtube.com/watch?v=VrxX3BCPjIo", "https://www.youtube.com/watch?v=8vaB_7Hzn40", "https://www.youtube.com/watch?v=FmLzfYBHfuY", "https://www.youtube.com/watch?v=8SnNVJVdqo8", "https://www.youtube.com/watch?v=w0AOGeqOnFY", "https://www.youtube.com/watch?v=kJQP7kiw5Fk", "https://www.youtube.com/watch?v=BTs5FS66IUI", "https://www.youtube.com/watch?v=5ngWIDkPP3o", "https://www.youtube.com/watch?v=QX43QTYyV-8", "https://www.youtube.com/watch?v=v_cr-QAddzc","https://www.youtube.com/watch?v=zKJ6xGVzrnI", "https://www.youtube.com/watch?v=4-UbHw8eDzM", "https://www.youtube.com/watch?v=YRvOePz2OqQ", "https://www.youtube.com/watch?v=dMXJHw2z8s4", "https://www.youtube.com/watch?v=e5Pu24Ve-vo", "https://www.youtube.com/watch?v=nXT70ZPRT6w", "https://www.youtube.com/shorts/YuQdicHRlSY", "https://www.youtube.com/watch?v=adkPu9A3bVs", "https://www.youtube.com/watch?v=Xa6PEyj5Uo4", "https://www.youtube.com/watch?v=pvuN_WvF1to"]
#Release notes
release = "Tibot V1.0\nTibot is released! Includes API features, account linking, custom commands, and more!"
#All the text for the help command
help = "COMMANDS:\n^test: tests if the bot works\n^pick: follow this command with 2 options seperated by spaces and the bot will chose one (ex: ^pick tibytes tibby)\n^kat: random cat image\n^randomnum: a random number\n^whisper: follow this with a mention and your message seperated by a |, and the bot will send the message. (ex: ^whisper @Tibytes, hello)\n^help: :/\n^latestvideo: gives you the link to the latest Tibytes video\n^lvdata: gives you info about the latest Tibytes video\n^badjoke: gives you a bad joke\n^poke: gives you a random pokemon\n^poll: follow up with 2 options and a seconds wait seperated by spaces. The poll will continue for the amount of seconds you input. (ex: ^poll tibytes tibby 30)\n^opendms: the bot sends you a message in dms\n^minion: follow up with | and then the text, and it will be translated into minion language! (ex: ^minion | i like tibytes videos very much)\n^shakespeare: same thing as the minion, but it translates text to shakespeare.\n^linkBL: follow this up with your beatleader user id to link it. (ex: ^linkBL 1234)\nNOTE: The Link Feature Is In Development And May Have Bugs\n^bl: follow this up with a mention of a user to get their beatleader link if it is linked.\n^stats: follow up with a user mention to get that user's beatleader stats.\n^n: No\n^y: Yes\n^favsong: gives you a great song\n^bsmg: gives you the link to the bsmg discord\n^suggestion: use this command, followed with | and a suggestion for the bot. Cheez will check this and implement some.\n^bug: same thing as suggestions but for bugs.\n^dog: random dog image\n^kquest: kanye quest\n^release: Gives you release notes and the version.\n^recentsong: gives you a beatleader replay link to the most recent song you played.\n^settings: gives you Tibytes controller settings.\n^hsv: gives you Tibytes hitscore visualizer settings.\n^mods: gives you Tibytes mods.\n^sabers: Gives you Tibytes sabers.\n"
#Determines if the bot is... On
on = 1
#This function runs when the bot goes online in discord
@client.event
async def on_ready():
  #Lets me know the bot is online
  print ('We have logged in as {0.user}'.format(client))
  #Sets the bots activity to "Watching your every move"
  activity = discord.Activity(name='your every move', type=discord.ActivityType.watching)
  await client.change_presence(activity=activity)
 
#Runs when a message is sent
@client.event
async def on_message(message):
    #Making some stuff global so I can use it in a function.
    global help, userIds
    #Just makes sure that the bot doesn't detect it's own messages.
    if message.author == client.user:
        return
    #Test command
    if message.content.startswith("^test"):
      await message.channel.send("Tibot works!")
    #Pick command
    if message.content.startswith("^pick"):
      #Makes a list containing all the message split by a space
      picksplit = message.content.split(" ")
      #Picks a random number (Either 1 or 2)
      choicevar = random.randint(1, 2)
      #Sends certain parts of the split message depending on the random number
      if choicevar == 1:
        await message.channel.send(picksplit[1])
      else:
        await message.channel.send(picksplit[2])
    #Random cat image!
    if message.content.startswith("^kat"):
      #Gets a response from the api server
      rawCatApiOutput = requests.get("https://api.thecatapi.com/v1/images/search")
      #Turns the response into text
      cat = rawCatApiOutput.json()
      #Makes a dictionary out of the text
      responseDictCat = dict(cat[0])
      #Sends the cat url provided (In discord it will show as an image)
      await message.channel.send(responseDictCat['url'])
    #Gets a random number and sends it
    if message.content.startswith("^randomnum"):
      await message.channel.send(random.randint(0, 99999999999999999999999999999))
    #Whisper command
    if message.content.startswith("^whisper"):
      #message.mentions[0] gets the first user mention in the message
      whisperUser = message.mentions[0]
      #Splits the message by |
      MessageSplit = message.content.split("|")
      #Sends the message provided to the mentioned user
      await whisperUser.send("From "+str(message.author)+": "+str(MessageSplit[1]))
    #Sends the help text from earlier
    if message.content.startswith("^help"):
      await message.channel.send(help)
    #Gets Tibytes latest video
    if message.content.startswith("^latestvideo"):
      #Sends the video url data from earlier
      await message.channel.send(videoUrl)
    #Sends the video data from earlier
    if message.content.startswith("^lvdata"):
      await message.channel.send(info)
    #Bad joke
    if message.content.startswith("^badjoke"):
      #Gets the response from the api
      joke = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt")
      #joke.text also turns the response into text.
      await message.channel.send(joke.text)
    #"Poke" is short for pokemon. Gets a random pokemon  
    if message.content.startswith("^poke"):
      #Gets a api response
      Pokelink = str("https://pokeapi.co/api/v2/pokemon?limit=1&offset="+str(random.randint(0, 999)))
      #Makes a dicitonary 
      rawPokeResponse = dict(requests.get(Pokelink).json())
      #Gets the results
      PokeResults = rawPokeResponse['results']
      #Gets a dictionary of the first item
      PokeResultsDict = dict(PokeResults[0])
      #Sends the name of the pokemon
      await message.channel.send(str(PokeResultsDict['name']))
    #Makes a poll  
    if message.content.startswith("^poll"):
      #Splits the message
      arguments = message.content.split(" ")
      #Makes sure there are 2 options
      if len(arguments) < 2:
        await message.channel.send("Please provide 2 options for the poll")
        return
      #Makes a string with the question
      pquestion = arguments[1] + " (1️⃣) or " + arguments[2]+" (2️⃣)"
      #Gets the poll length
      secondsWait = int(arguments[3])
      #Sends the question
      pmessage = await message.channel.send(pquestion)
      #Adds reactions to the message with the poll so users can vote
      await pmessage.add_reaction("1️⃣")
      await pmessage.add_reaction("2️⃣")
      #Checks if someone reacts to the message
      def reactioncheck(reaction, user):
        return user != client.user and str(reaction.emoji) in ["1️⃣", "2️⃣"]
      #while True runs until stopped
      while True:
        #Globals the variables
        global twovotes
        global onevotes
        #Try "tries" to execute the code, and if there is an error, you can do something.
        try:
          #Waits for a reaction
          reaction, user = await client.wait_for("reaction_add", check= reactioncheck, timeout=secondsWait)
        except asyncio.TimeoutError:
          #Breaks the loop
          break
        else:
          #Adds votes 
          if str(reaction.emoji) == "1️⃣":
            onevotes = onevotes + 1
          elif str(reaction.emoji) == "2️⃣":
            twovotes += 1
      #Gets total votes      
      votes = onevotes + twovotes
      #Makes sure there are votes
      if onevotes < 1 and twovotes < 1:
        await message.channel.send("No votes where added in the provided time. Please try again!")
        return
      #Gets the percentages
      onepercent = (onevotes / votes) * 100
      twopercent = (twovotes / votes) * 100
      #Gets the results
      results = "1 was "+str(onepercent)+"%, while 2 was "+str(twopercent)+"%"
      #Sends them
      await message.channel.send(results)
      #Sends a simplified "who won"
      if onepercent > twopercent:
        await message.channel.send(arguments[1]+" won!")
      elif twopercent > onepercent:
        await message.channel.send(arguments[2]+" won!")
      else:
        await message.channel.send("It was a tie!") 
    #Sends a message to the user to open the dms    
    if message.content.startswith("^opendms"):
      await message.author.send("Hello there")
      await message.add_reaction("<:HappyPing:1051800606622355507> ")
    #Minion translator
    if message.content.startswith("^minion"):
      TextForLink = ""
      #The minion api link
      beforeLink = "https://api.funtranslations.com/translate/minion.json?text="
      
      varthingy = 0
      #Splits the message
      messageSplit = message.content.split("|")
      #Splits the text to translate
      textsplit = messageSplit[1].split(" ")
      #Makes a string with each word seperated by %20
      for i in textsplit:
        TextForLink = TextForLink+textsplit[varthingy]+"%20"
        varthingy = varthingy + 1
        if varthingy == len(textsplit):
          break
      #Gets the final link
      finalLink = beforeLink+TextForLink
      #Api request
      translatedJson = requests.get(finalLink)
      #Making it text
      dictResponse = dict(translatedJson.json())
      contents = dict(dictResponse['contents'])
      #Sending the translated text
      await message.channel.send(contents['translated'])
    #Same thing as the minion translator but for shakespeare  
    if message.content.startswith("^shakespeare"):
      TextForLink = ""
      beforeLink = "https://api.funtranslations.com/translate/shakespeare.json?text="
      
      varthingy = 0
      messageSplit = message.content.split("|")
      textsplit = messageSplit[1].split(" ")
      for i in textsplit:
        TextForLink = TextForLink+textsplit[varthingy]+"%20"
        varthingy = varthingy + 1
        if varthingy == len(textsplit):
          break
          
      finalLink = beforeLink+TextForLink
      translatedJson = requests.get(finalLink)
      dictResponse = dict(translatedJson.json())
      contents = dict(dictResponse['contents'])
      await message.channel.send(contents['translated'])
    #Links your beatleader account   
    if message.content.startswith("^linkBL"):
      #Opens the userid text file in read mode
      Tfile = open("uids.txt", "r")
      #Runs for every line
      for line in Tfile:
          #Splits the line at :
          splitline = line.split(":")
          #Happens if the splitline is the messages author
          if splitline[0] != str(message.author):
              #Splits the message
              messageSplit = message.content.split(" ")
              #Happens if the user is not already registered
              if messageSplit[1] != splitline[1]:
                  print("Link")
                  #Closes the file
                  Tfile.close()
                  #Opens the file again in a different mode. "r" just reads the file and "a", writes new lines to the file
                  with open("uids.txt", "a") as Tfile:
                    #Writes the id and user to the file. \n creates a new line.
                    Tfile.write("\n" + str(message.author) + ":" + str(messageSplit[1]))
                    print("Account Linked")
                  await message.reply("Account Linked")
              else:
                  await message.reply("Account Already Linked")
      #Closes the file.            
      Tfile.close()
        
    #Sends a users beatleader account
    if message.content.startswith("^bl"):
      #Opens the file
      Tfile = open("uids.txt", "r")
      #Gets the mention
      blUser = message.mentions[0]
      #Sets userdetected to false
      user_detected = False 
      #For every line in the file
      for line in Tfile:
        #Splits the line
        splitline = line.split(":")
        #If the user in the file is the mentioned user
        if splitline[0] == str(blUser):
          #Send the beatleader link witht the id
          await message.reply(blUIDLink+str(splitline[1]))
          #User detected
          user_detected = True  
          #Breaks out of the loop
          break  
      #If the user is not detected  
      if not user_detected:
        await message.reply("User's Account Not Linked")
    #Shows the user's stats.
    if message.content.startswith("^stats"):
      #This is temporary
      await message.channel.send("At the moment, stats is not working due to something that I, and multiple other people cannot figure out. I will try to fix this asap!")
      #Opens the file
      fileT = open("uids.txt", "r")
      print("stats")
      #Gets the mention
      statuser = message.mentions[0]
      #Again, userdetected
      user_detected = False  
      #For every line
      for line in fileT:
        #Split the line
        splitline = line.split(":")
        #If the user is detected
        if str(statuser) == splitline[0]:
          #Get the beatleader id
          blID = splitline[1]
          print(blID)
          #Gets the response from the beatleader api
          rawResponse = requests.get("https://api.beatleader.xyz/player/"+str(blID))
          #Jsons it
          responseBLJson = dict(rawResponse.json())

          print(rawResponse.text)

          print(requests.get("https://api.beatleader.xyz/player/"+str(blID)))
          #Gets the beatleader stats. Some data is on the responseBLJson and other is in the BLstats
          BLstats = responseBLJson['scoreStats']
          print(BLstats)
          #Compiles a message with the data
          userStatsMessage = str("PP: "+str(responseBLJson['pp'])+"\nRank: "+str(responseBLJson['rank'])+"\nTop PP: "+str(BLstats['topPp'])+"\nCountry: "+str(responseBLJson['country'])+"\nCountry Rank: "+str(responseBLJson['countryRank']))
          print(userStatsMessage)
          #Sends it
          await message.reply(userStatsMessage)
          print(str(responseBLJson['pp']))
          print(str(responseBLJson))
          #Userdetected
          user_detected = True  
          #Breaks out of the loop
          break  
      if not user_detected:
        await message.reply("User's Beatleader Account Not Yet Linked")
      #Closes the file  
      fileT.close()
        
    
          
        
          
    #Simple no and yes commands
    if message.content.startswith("^n"):
      #Deletes the message
      await message.delete()  
      #Sends a new one
      await message.channel.send("No")
    if message.content.startswith("^y"):
      await message.delete()  
      await message.channel.send("Yes")  
    #Detects if a message is a rickroll
    if "https://www.youtube.com/watch?v=dQw4w9WgXcQ" in message.content or "https://www.youtube.com/watch?v=xvFZjo5PgG0" in message.content:
      await message.channel.send("It's a rickroll!")
    #Sends a favorite song  
    if message.content.startswith("^favsong"):
      #random.choice gets a random item from a list or dictionary
      await message.channel.send(random.choice(favsong))
    #Sends the bsmg link
    if message.content.startswith("^bsmg"):
      await message.reply("https://discord.gg/beatsabermods")
    #Suggestions for the bot  
    if message.content.startswith("^suggestion"):
      #Message split
      suggestionSplit = message.content.split("|")
      #Opens the text file
      suggestions = open("suggestions.txt", "w")
      #Writes the suggestion into the file
      suggestions.write(str(str(message.author)+":"+str(suggestionSplit[1])))
      #Closes the file
      suggestions.close()
      #Says "Suggestion recorded!"
      await message.channel.send("Suggestion recorded!")
    #Same thing for suggestion but for bugs
    if message.content.startswith("^bug"):
      suggestionSplit = message.content.split("|")
      suggestions = open("bugs.txt", "w")
      suggestions.write(str(str(message.author)+":"+str(suggestionSplit[1])))
      
      suggestions.close()
      await message.channel.send("Bug Report Has Been Recorded")  
    #Same proccess as kat but for a dog image  
    if message.content.startswith("^dog"):
      dogResponseRaw = requests.get("https://random.dog/woof.json")
      dogDict = dict(dogResponseRaw.json())
      await message.channel.send(str(dogDict['url']))
    #Shows you an image of kanye quest  
    if message.content.startswith("^kquest"):
      await message.channel.send("https://cdn.discordapp.com/attachments/917159518352326689/1076841066029916170/kanje.jpg")
    #Sends a image if you say u got games on ur phone  
    if "u got games on ur phone" in message.content.lower():
      await message.reply("https://cdn.discordapp.com/attachments/1052608920453124186/1076634682231365803/FpOL6WwXoAAEmJD.jpg")
    #Shows you the release data from earlier  
    if message.content.startswith("^release"):
      await message.channel.send(release)
    #Gets your most recent song from beatleader. This took me 3 days.
    if message.content.startswith("^recentsong"):
      #Another temporary message
      await message.channel.send("For an unknown reason, stats and recentsong just stopped working. I changed no code, and it is nobodys fault. I will try to fix this, but all other comands should work for now. - Cheez")
      #Opens the file
      uidFile = open("uids.txt", "r")
      #Again, for every line
      for line in uidFile:
        #Split the line
        splitline = line.split(":")
        #If the user is detected
        if splitline[0] == str(message.author):
          #Gets the api request with the users id
          HistoryRawlink = str("https://api.beatleader.xyz/player/"+str(splitline[1])+"/scores")
          RawResponseHistory = requests.get(HistoryRawlink)
          #.jsons() it
          allScores = dict(RawResponseHistory.json())
          print(str(allScores))
          #Gets the list called "data"
          dataList = list(allScores['data'])
          print(str(allScores['data']))
          #Gets a dictionary inside data
          dataDict = dict(dataList[0])
          #Gets the id of the play
          playID = dataDict['id']
          #Gets a beat saber replay link with the score id
          replayLink = str("https://replay.beatleader.xyz/?scoreId="+str(playID))
          #Sends it
          await message.channel.send(replayLink)
          #User is detected
          user_detected = True  
          #Breaks from the loop
          break  
      #If the user is not linked
      if not user_detected:
        await message.reply("Account Not Linked!")
    #Sends Tibytes faq question materials    
    if message.content.startswith("^settings"):
      await message.reply("https://cdn.discordapp.com/attachments/1024300305489330176/1024300305623556116/unknown.png   and  https://cdn.discordapp.com/attachments/1024300305489330176/1024300305992663100/unknown.png")
    if message.content.startswith("^hsv"):
      await message.reply("https://cdn.discordapp.com/attachments/1024246926432030811/1024246926520107048/HitScoreVisualizerConfig_poopy.json")
    if message.content.startswith("^sabers"):
      await message.reply("https://cdn.discordapp.com/attachments/1024247927624966154/1024247927750807562/BigThinSabre_2.saber.meta  &  https://cdn.discordapp.com/attachments/1024247927624966154/1024247928056975360/BigThinSabre_2.trail     If you want the latest sabers Tibytes is using in his videos, they are behind a patreon paywall. For anyone interested, https://www.patreon.com/beatleader/posts")
    if message.content.startswith("^mods"):
      await message.reply("These mods are for 1.26.0. It is not advised to use these exact files for any other version. https://cdn.discordapp.com/attachments/1038499135759847485/1043121023211552768/Tibytes_Plugins2.zip")
    #Custom commands!
    if message.content.startswith("%"):
      #If a moderator wants to add a command
      if message.content.startswith("%addcommand") and str(message.author) in mods:
        #Basic settings
        commandExists = False
        Commandsplit = message.content.split("|")
        #File open
        commands = open("customcommands.txt", "a+")
        #For line in the file
        for line in commands:
          #Split the line
          LineSplit = line.split("|")
          #If the command the user provided exists
          if str(Commandsplit[1]) == LineSplit[0]:
            #Set the exists to true and break from the loop
            commandExists = True
            break
        #If the command exists, else write the command   
        if commandExists == True:
          await message.channel.send("Command Already Exists")
        else:
          commands.write("\n"+str(Commandsplit[1])+"|"+str(Commandsplit[2]))
          await message.channel.send("Command created!")
        #File close  
        commands.close()  
      else:  
        #This happens if a command is being used, not created
        #File open
        commandsDoc = open("customcommands.txt", "r")
        #Split the message every character
        args = message.content.split()
        #Removes the prefix (%) from the message
        commandMat = args[0][1:]
        #Sets iscommand
        IsCommand = False
        #For line in the custom commands document
        for line in commandsDoc:
          #Split the line
          SpitLine = line.split("|")
          #If the command the user is using exists
          if str(commandMat) == str(SpitLine[0]):
            #Set the response to the response in the file
            commandResponse = str(SpitLine[1])
            #Sets the command to true and breaks out of the loop
            IsCommand = True
            break
        #If the command does not exist, say so, else, send the response  
        if IsCommand == False:
          await message.channel.send("Command Does Not Exist")
        else:
          
          await message.channel.send(str(commandResponse))
    #Send the hosting status page      
    if message.content.startswith("^hostingstats"):
      await message.reply("https://stats.uptimerobot.com/MAXDxs2Aom")

#Again, "try" will try to run but if fails, except can run      
try:
    
    
    
    #Runs a script called "keep_alive", shown in the file
    keep_alive()
    #Runs the bot with the token
    client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException:
    #This except happens when the bot is blocked by rate limits
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    #Runs the restarter.py file and restarts the project
    os.system("python restarter.py")
    os.system('kill 1')


  