import discord
from discord.ext import commands
import Bot as bt

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='>', intents=intents, self_bot = True)
Bot = bt.Bot(bot)


@bot.event
async def on_ready():
    await Bot.OnReady()

@bot.event
async def on_message(message):
    await Bot.OnMessage(message)

@bot.command()
async def cls(ctx):
    await Bot.Cls(ctx)

@bot.command()
async def set_auto_text(ctx):
    await Bot.SetAutoText(ctx)


@bot.command()
async def sh(ctx):
    await Bot.Sh(ctx)



if __name__ == "__main__":
    bot.run('token', bot = False)