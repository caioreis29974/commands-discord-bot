@bot.command()
async def hora(ctx):
    now = datetime.now()
    embed = discord.Embed(
        title="Hora Atual",
        description=f"A hora atual é: {now.strftime('%H:%M:%S')}",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)
