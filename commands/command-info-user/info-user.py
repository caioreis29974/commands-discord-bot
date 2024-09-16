@bot.command()
async def info_user(ctx):
    user = ctx.author
    user_name = user.name
    user_id = user.id
    user_avatar_url = user.avatar.url if user.avatar else None
    user_created_at = user.created_at.strftime("%d/%m/%Y %H:%M:%S")
    member = ctx.guild.get_member(user.id)
    if member:
        roles = [role.name for role in member.roles if role.name != "@everyone"]
    else:
        roles = ["Não encontrado"]

    embed = discord.Embed(
        title="🧑‍💻 Informações do Usuário",
        description=f"Nome: **{user_name}**\nID: **{user_id}**\nCriado em: **{user_created_at}**\nCargos: **{', '.join(roles)}**",
        color=0x00376c
    )
    if user_avatar_url:
        embed.set_thumbnail(url=user_avatar_url)
    else:
        embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")

    await ctx.reply(embed=embed, mention_author=False)
