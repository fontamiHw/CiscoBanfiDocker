from webex_bot.webex_bot import WebexBot
from webexpythonsdk import WebexAPI
from webex.commands.commandImage import CommandImage
from webex.commands.commandList import CommandList

def add_commands(bot:WebexBot, api:WebexAPI):
    bot.add_command(CommandImage(api))    
    bot.add_command(CommandList(api))