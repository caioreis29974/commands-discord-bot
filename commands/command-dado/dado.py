@bot.command()
async def dado(ctx, numero: int = None):
    if numero is None:
        embed = discord.Embed(
            title="🎲 Dado",
            description="Por favor, forneça um número para rolar o dado.\nExemplo: `>dado 6`",
            color=0x00376c
        )
        await ctx.reply(embed=embed, mention_author=False)
        return

    variavel = random.randint(1, numero)
    embed = discord.Embed(
        title="🎲 DADO 🎲",
        description=f"O número que saiu no dado é **{variavel}**",
        color=0x00376c
    )
    await ctx.reply(embed=embed, mention_author=False)
