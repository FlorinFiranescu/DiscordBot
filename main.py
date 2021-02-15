import discord
import json
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
        "Here you go, {}".format(user),
        "Well.. well.. {}, you are a picky one!".format(user),
        "Not your best week, ain't it {}?".format(user),
        "So you finally got that nice trinket, {}?".format(user),
        "{}.. I swear to god, if you are asking me again for the same site i am going to.....".format(user),
        "Bwonsamdi been expectin' ya, {} :> ".format(user),
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
        commands = getCommands()
        #decode the message
        for k,v in commands.items():
            if k in message.content.split():
                await message.channel.send(returnUtil(message.author, v))



client.run(getBotKey())

