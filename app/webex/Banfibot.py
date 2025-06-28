from config import Config
from webexpythonsdk import WebexAPI
from webex_bot.webex_bot import WebexBot
import webex.commands.commands as commands

class BanfiBot(object):
    def __init__(self):

        #create a Config object
        self.configuration=Config()
        self.bot = WebexBot(teams_bot_token=self.configuration.get_token(),
                   approved_domains=['cisco.com', 'liceobanfi.eu'],
                   bot_name=self.configuration.get_name(),
                   proxies=self.configuration.get_proxies())
        token = self.configuration.get_token()
        self.api = WebexAPI(access_token=token)
        commands.add_commands(self.bot, self.api)


    def start(self):
        print("before run")
        self.bot.run()
        print("after run")

        

    