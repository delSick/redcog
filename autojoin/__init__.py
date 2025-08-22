from .autojoin import AutoJoin

def setup(bot):
    bot.add_cog(AutoJoin(bot))
