API_KEY = 'YOUR_API'

@bot.command()
async def clima(ctx, *, cidade: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': cidade,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['cod'] != 200:
        await ctx.send(f"Erro: {data['message']}")
        return

    cidade = data['name']
    temperatura = data['main']['temp']
    descricao = data['weather'][0]['description']
    umidade = data['main']['humidity']
    vento = data['wind']['speed']

    embed = discord.Embed(
        title=f"Clima em {cidade}",
        description=f"Descrição: {descricao.capitalize()}",
        color=discord.Color.blue()
    )
    embed.add_field(name="Temperatura", value=f"{temperatura}°C", inline=True)
    embed.add_field(name="Umidade", value=f"{umidade}%", inline=True)
    embed.add_field(name="Velocidade do Vento", value=f"{vento} m/s", inline=True)

    await ctx.send(embed=embed)
