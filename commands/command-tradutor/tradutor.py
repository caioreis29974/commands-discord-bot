@bot.command(name='traduzir')
async def traduzir(ctx, *, text: str):
    try:
        translation = translator.translate(text, dest='en')
        embed = discord.Embed(
            title="💧 Tradução 💧",
            description=f"Texto original: {text}\n\nTradução: {translation.text}",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send('Erro na tradução.')
