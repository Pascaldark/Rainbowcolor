import discord
import asyncio
import random
from discord import Member, Guild, User
from discord.ext import commands

client = commands.Bot(command_prefix='!')

autoroles = {
    698853138441961472: {'memberroles': [698856534670704672], 'botroles': [699217366986260480]}
}


@client.event
async def on_ready():
    print('Wir sind eingeloggt als User {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(),
              discord.Colour.blue(), discord.Colour.purple()]
    while True:
        await client.change_presence(activity=discord.Game('discord.gg/zdMtRH8'), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('Zasino-Gang | Dein Casino Server'), status=discord.Status.online)
        await asyncio.sleep(5)
        guild: Guild = client.get_guild(698853138441961472)
        if guild:
            role = guild.get_role(699548996364140574)
            if role:
                if role.position < guild.get_member(client.user.id).top_role.position:
                    await role.edit(colour=random.choice(colors))


def is_not_pinned(mess):
    return not mess.pinned


@client.event
async def on_member_join(member):
    guild: Guild = member.guild
    if not member.bot:
        embed = discord.Embed(title='Willkommen auf ZasinoGang {} <a:tut_herz:662606955520458754>'.format(member.name),
                              description='Wir heißen dich herzlich Willkommen auf unserem Server!', color=0x22a7f0)
        try:
            if not member.dm_channel:
                await member.create_dm()
            await member.dm_channel.send(embed=embed)
        except discord.errors.Forbidden:
            print('Es konnte keine Willkommensnachricht an {} gesendet werden.'.format(
                member.name))
        autoguild = autoroles.get(guild.id)
        if autoguild and autoguild['memberroles']:
            for roleId in autoguild['memberroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)
    else:
        autoguild = autoroles.get(guild.id)
        if autoguild and autoguild['botroles']:
            for roleId in autoguild['botroles']:
                role = guild.get_role(roleId)
                if role:
                    await member.add_roles(role, reason='AutoRoles', atomic=True)


@client.event
async def on_message(message):
    if message.channel.id == 699563424824295474:
        await message.add_reaction("👍")
        await message.add_reaction("👎")
        await message.add_reaction("❓")
    elif message.channel.id == 698855070850351146:
        await message.add_reaction("<a:RainbowCoin:699522326844276746>")

@client.command()
async def laden(ctx):
    try:
        message = await ctx.send('lädt...')
        await asyncio.sleep(3)
        await message.edit('fertig')
    except Exception as e:
        print(e)


client.run("Njk5NTUxMTcyMDQ1OTYzMzA0.XpXOog.P35Po03GkEHSn4okG7gzLyD2hww")
