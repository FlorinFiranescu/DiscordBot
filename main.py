import discord
import json
import Scrapping
from Scrapping import getLegendary
#async lib, uses callbacks
import random
def getBotKey():
    with open('.key', 'r') as f:
        str = f.readlines()
        str = str[0].strip()
        return str

def getCommands():
    with open('commands.json', 'r') as json_file:
        commands = json.load(json_file)
    return commands
client = discord.Client()

def returnUtil(user, util):
    user = str(user)
    user = user[:-5]
    listOfMessages = [
        #"Here you go, {}".format(user),
        #"Well.. well.. {}, you are a picky one!".format(user),
        #"Not your best week, ain't it {}?".format(user),
        #"So you finally got that nice trinket, {}?".format(user),
        #"{}.. I swear to god, if you are asking me again for the same site i am going to.....".format(user),
        #"Bwonsamdi been expectin' ya, {} :> ".format(user),
        "Hello there, {}!".format(user)
    ]
    return '{}\n{}'.format(random.choice(listOfMessages), util)

@client.event
async def on_ready():
    print("Your best friend, WowHelperBOT is here {}".format(client.user))


@client.event
async def on_message(message):
    bot_mention = f'<@!{client.user.id}>'
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello there, partner!")

    if bot_mention in message.content:
        content = message.content.split()
        commandList = content[1].split('-')
        commands = getCommands()
        #decode the message
        for k,v in commands.items():

            if k == "!affixes" and k in commandList:
                spec = None
                print(commandList)
                if len(commandList) == 1:
                    await  message.channel.send(returnUtil(message.author, Scrapping.getAffixes(v)))
                elif len(commandList) == 2:
                    spec = commandList[1]
                    await  message.channel.send(returnUtil(message.author, Scrapping.getAffixes(v, spec)))
                elif(len(commandList) >2 ):
                    spec = commandList[1]
                    await  message.channel.send("Your command does not match my expectations.\nWhen talking about affixes, the format is !affixes-spec , where spec -> (dungeon, melee, range, healer))\n{}"
                    .format(returnUtil(message.author, Scrapping.getAffixes(v, spec))))
            elif k == "!legendary" and k in commandList:
                if len(commandList) == 1:
                    await message.channel.send("What do you want to know about your legendaries? I know only about sould ash required for craft or upgrade.")
                elif len(commandList) == 2:
                    subCommand = commandList[1]
                    await message.channel.send(getLegendary(subCommand))




client.run(getBotKey())

