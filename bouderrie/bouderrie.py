from bouderrie.helpers import HelperMethods
from bouderrie.commandregistry import CommandRegistry
import discord
import asyncio


class Boudrerrie(discord.Client):
    def __init__(self, **kwargs):
        intents = discord.Intents.default()
        intents.members = True
        self.CommandRegistry = CommandRegistry()
        self.HelperMethods = HelperMethods()
        self.audiofiles = []
        self.playing_audio = False
        self.voice_client = None
        super().__init__(intents=intents)

    AT_DRERRIE_ID = '<@!822801078914908172>'

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def speak(self, message, file):
        if not hasattr(message.author.voice, 'channel'):
            await message.author.send("You're not in the voice channel")
            return

        voice_channel = message.author.voice.channel

        if self.voice_client is None:
            self.voice_client = await voice_channel.connect()
        elif not self.voice_client.is_connected():
            self.voice_client = await voice_channel.connect()

        self.audiofiles.append(file)

        if not self.playing_audio:
            self.playing_audio = True
            while len(self.audiofiles) >= 1:
                if self.voice_client.is_playing():
                    while self.voice_client.is_playing():
                        await asyncio.sleep(0.1)
                    self.voice_client.stop()

                popped_audio = self.audiofiles.pop(0)
                self.voice_client.play(
                    discord.FFmpegPCMAudio(popped_audio))
            self.playing_audio = False

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        if message.content.startswith(self.AT_DRERRIE_ID + " !"):
            contentremainder = message.content.lower()[
                len(self.AT_DRERRIE_ID + " !"):]
            command = contentremainder.split(" ")[0]

            if len(command) <= 2:
                await message.channel.send("command is too short")
                return

            if len(command) > 10:
                await message.channel.send("command is too long")
                return

            if str(message.attachments) == "[]":
                await message.channel.send("please attach a file")
                return

            filename = str(message.attachments).split(
                "filename='")[1].split("' ")[0].lower()
            if filename.endswith(".mp3") or filename.endswith(".wav"):
                completefilename = command + "-" + filename
                await message.attachments[0].save(fp="command-sounds/{}".format(completefilename))
                self.CommandRegistry.add(
                    command, completefilename)
                await message.author.send("!" + command + "command added")
            return

        if message.content.lower().startswith('!zeg mop'):
            await message.delete()
            mop = await self.HelperMethods.getmop()
            filename = self.HelperMethods.text_to_soundfile(mop)
            return await self.speak(message, filename)

        if message.content.lower().startswith('!zeg'):
            text = message.content.lower()[4:]
            await message.delete()
            filename = self.HelperMethods.text_to_soundfile(text=text)
            return await self.speak(message, filename)

        if message.content.lower().startswith('!sounds'):
            embed = discord.Embed(
                title="Bouderrie command registry:", description="sound commands en de files", color=discord.Colour.random())

            for commandkey, commandvalue in self.CommandRegistry.commands.items():
                embed.add_field(name="!" + commandkey,
                                value=commandvalue, inline=False)
            await message.channel.send(embed=embed)
            return

        if message.content.lower().startswith('!'):
            await message.delete()
            command = message.content.lower()[1:]
            filename = self.CommandRegistry.get(command=command)
            if filename != None:
                file = "command-sounds/" + str(filename)
                return await self.speak(message, file)
            else:
                await message.author.send("Nou sound is bound to this command \n" +
                                          "You can add new commands if you send a soundfile in general with @boudrerrie !command \n" +
                                          "If you want a list of commands you can say !sounds in general")
