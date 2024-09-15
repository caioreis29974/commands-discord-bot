@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"O tempo de resposta do bot é de {latency:.2f} ms.",
        color=0x00376c
    )
    await ctx.send(embed=embed)
