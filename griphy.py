from discord.ext.commands import Bot
import random

token = 'Njk3NDQ2MjAxNTgyNDE5OTg4.Xo3Zhw.3N0yZl4MOLirxQoURbTFmQiwS3U'
bot = Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Login as")
    print(bot.user.name)
    print("-------")
    
@bot.command(name='g')
async def magic_eight_ball(ctx):
    response =[
        'Without a doubt.', 
        'Outlook good.', 
        'Better not tell you now.', 
        'Cannot predict now.',
        'My reply is no.', 
        'Outlook not so good.',
    ]

    await ctx.send(random.choice(response))

bot.run(token)