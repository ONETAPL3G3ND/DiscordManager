import Text
import discord
import arg_core
import asyncio

class Bot:
    def __int__(self, bot):
        self.text = Text.Text()
        self.bot = bot
        self.interacted_users = set()

    async def OnReady(self):
        print('We have logged in as {0.user}'.format(self.bot))

    async def OnMessage(self, message):
        if isinstance(message.channel, discord.DMChannel) and message.author != self.bot.user:
            if message.author.id not in self.interacted_users:
                self.interacted_users.add(message.author.id)
                await message.channel.send(self.text.MainText)

                # Отправляем файл music.mp3
                with open('music.mp3', 'rb') as file:
                    await message.channel.send(file=discord.File(file))

        await self.bot.process_commands(message)

    async def Cls(self, ctx):
        self.interacted_users.clear()
        await ctx.send(self.text.Cls)

    async def SetAutoText(self, ctx):
        global text

        args = arg_core.get_arg(ctx)

        text = args[0]

        await ctx.send("Текст был установлен!")

    async def Sh(self, ctx):
        self.interacted_users.add(ctx.author.id)
        msg = await ctx.send("Успешно!")
        await asyncio.sleep(2)
        await ctx.message.delete()
        await msg.delete()

