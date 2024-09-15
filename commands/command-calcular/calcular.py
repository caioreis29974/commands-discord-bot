@bot.command(name="calcular")
async def calcular(ctx, *expression):
    expression = "".join(expression)
    
    print(expression)
    
    try:
        response = eval(expression)
    except Exception as e:
        await ctx.send(f"Erro ao calcular a expressão: {e}")
        return
    
    calcular_embed = discord.Embed(
        title="⚡ Calculadora ⚡",
        description=f"A resposta do cálculo é: {response}",
        color= discord.Color.yellow()
    )
    
    await ctx.send(embed=calcular_embed)
