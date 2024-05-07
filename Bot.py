import Text
import discord
import arg_core
import asyncio
import AI

class Bot:
    def __init__(self, bot):
        self.text = Text.Text()
        self.bot = bot
        self.InteractedUsers = set()
        self.FullInteractedUsers = set()
        self.Ai = AI.AI()

    async def OnReady(self):
        print('We have logged in as {0.user}'.format(self.bot))

    async def OnMessage(self, message):
        if isinstance(message.channel, discord.DMChannel) and message.author != self.bot.user:
            if message.author.id not in self.InteractedUsers and message.author.id not in self.FullInteractedUsers:
                await message.channel.send(self.text.MainText)
                self.InteractedUsers.add(message.author.id)

                with open('music.mp3', 'rb') as file:
                    await message.channel.send(file=discord.File(file))
                await message.channel.send(await self.Ai.CreateMessage(message.author.id, message.content))

            elif message.author.id in self.InteractedUsers and message.author.id not in self.FullInteractedUsers:
                await message.channel.send(await self.Ai.CreateMessage(message.author.id, message.content))
        await self.bot.process_commands(message)

    async def Cls(self, ctx):
        self.InteractedUsers.clear()
        self.FullInteractedUsers.clear()
        await self.SendDisappearingmMessage(ctx, self.text.Cls)

    async def SendDisappearingmMessage(self, ctx, text):
        msg = await ctx.send(text)
        await asyncio.sleep(2)
        await ctx.message.delete()
        await msg.delete()


    async def SetAutoText(self, ctx):

        args = arg_core.get_arg(ctx)

        self.text = args[0]

        await ctx.send("Текст был установлен!")


    async def Sh(self, ctx):
        self.InteractedUsers.add(ctx.channel.recipient.id)
        await self.SendDisappearingmMessage(ctx, "Успешно!")

    async def Stop(self, ctx):
        self.FullInteractedUsers.add(ctx.channel.recipient.id)
        self.InteractedUsers.add(ctx.channel.recipient.id)
        await self.SendDisappearingmMessage(ctx, "Успешно!")
