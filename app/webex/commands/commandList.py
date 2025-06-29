from webex_bot.models.command import Command
from webex_bot.formatting import quote_info
from webexteamssdk import WebexTeamsAPI
from webexteamssdk.models.immutable import Message
import logging
import os


class CommandList(Command):

    def __init__(self, api:WebexTeamsAPI):
        command = "list"
        super().__init__(
            command_keyword=command,
            help_message=f"{command}: Return the list of the available SOR file.",
        )
        self.api = api        
        self.open_route = "/data/host/SOR/"

    def execute(self, message, attachment_actions:Message, activity):    
        sor_files = []
        for f in os.listdir(self.open_route):
            if f.endswith('.json'):
                sor_files.append(f.replace('.json', '.sor'))
        logging.info(f"Found SOR files: {sor_files}")

        # Join sor_files into a single string, adding '\n' after every 2 elements
        sor_str = ""
        for i, f in enumerate(sor_files):
            sor_str += f"- {f}"
            if (i + 1) % 2 == 0 and i != len(sor_files) - 1:
                sor_str += '\n\n'
            elif i != len(sor_files) - 1:
                sor_str += ' '
            
                
        return f"***Available SOR :*** \n{sor_str}" if sor_str else "No SOR files found."

