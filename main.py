import discord
import asyncio

token = 'BOT TOKEN HERE'
dmcontent = "DESU WA"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Ready.')
    print('------------')

@client.event
async def on_guild_join(server):
    print ("Connected to " + str(server.name))
    memberdmlist = []
    for channel in server.channels:
        if channel.type == discord.ChannelType.text:
            chan = channel
    for member in server.members:
        memberdmlist.append(member)
    for member in memberdmlist:
        perms = chan.permissions_for(member)
        if member.bot == True:
            continue
        if perms.kick_members:
            print (str(member)+ " can kick, not DMing.")
            continue
        if perms.ban_members:
            print (str(member)+ " can ban, not DMing.")
            continue
        if perms.administrator:
            print (str(member)+ " is admin, not DMing.")
            continue
        else:
            print ("DMing "+str(member))
            try:
                await member.send(content=dmcontent)
            except Exception as e:
                print ("Unable to DM " + str(member))
    try:
        await server.leave()
        print ("Left " + server.name)
    except Exception:
        print ("Unable to Leave the server.")
        
client.run(token)
