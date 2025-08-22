from .autojoin import AutoJoin

async def setup(bot):
    await bot.add_cog(AutoJoin(bot))
