from discord.ext.commands import Bot

from yaml import safe_load

class ModMailBot(Bot):
    
    async def setup_hook(self) -> None:
        with open('config.yaml') as file:
            file = safe_load(file)['ModMail']
            self.log_channel_id = file['log_channel_id']
            self.response_channel_id = file['response_channel_id']
            
        
    
