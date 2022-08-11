from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import date
import os

async def discord(desp, x):
    discord_url = os.environ.get("discord")
    webhook = DiscordWebhook(url=discord_url)
    title = f"""
    Genshin Daily Sign-In 
    -Number of successful sign-ins: {x}
    -Number of failed sign-ins: 0
    """
    today = date.today()
    datetoday = today.strftime("%B %d, %Y")
    embed = DiscordEmbed(title=title , description=desp, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()
    if (response.status_code == 200):
        print(f'Discord Message SUCCESS')
    else:
        print(f'Discord Message FAILED\n{response}')