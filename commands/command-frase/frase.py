#Lembre-se de utilizar o comando "import json" dentro do seu código.
@bot.command(name='frase')
async def send_quote(ctx):
    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes = json.load(file)
    
    quote = random.choice(quotes)
    embed = discord.Embed(
        title="Frase Inspiradora 🚀",
        description=f'"{quote["quote"]}"\n- {quote["author"]}',
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)
