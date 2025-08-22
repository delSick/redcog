import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.commands import Context 

class AutoJoin(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot
        self.target_channel_id = 783093706189701151

    @commands.command()
    async def setchannel(self, ctx: Context, channel: discord.VoiceChannel):
        """Setzt den Ziel-Voice-Channel für AutoJoin."""
        self.target_channel_id = channel.id
        await ctx.send(f"Ziel-Channel gesetzt: {channel.name} ({channel.id})")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Prüfen, ob der User einem Channel beigetreten ist
        if after.channel and after.channel.id == self.target_channel_id:
            voice = discord.utils.get(self.bot.voice_clients, guild=member.guild)
            if voice and voice.is_connected():
                return  # Bot ist schon verbunden

            # Bot dem Channel joinen lassen
            try:
                await after.channel.connect()
            except discord.ClientException as e:
                print(f"Fehler beim Verbinden: {e}")

            # Optional: Musik starten (wenn du z. B. Audio-Cog nutzt)
            # Du kannst hier z. B. `await self.bot.get_cog("Audio").play(ctx, "URL")` verwenden
