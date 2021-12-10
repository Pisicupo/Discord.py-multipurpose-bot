import discord
from discord.ext import commands, tasks
import DiscordUtils 
import json
import emoji
import os
import asyncio

intents=intents=discord.Intents.all()
client = commands.Bot(command_prefix = '!!', owner_id =694809454465777685)
music = DiscordUtils.Music()

@client.event
async def on_ready():
    print('Bot is online')
    activity = discord.Activity(type=discord.ActivityType.listening, name='SkullCenter Community')
    await client.change_presence(status=discord.Status.dnd, activity=activity)

#ZONA EMBED

@client.command(aliases=['Regole'])
async def regole(ctx):
    embed=discord.Embed(title='**REGOLE DEL SERVER**', description='''
    ● È severamente vietata ogni forma di razzismo sulla base di attributi come razza, orientamento sessuale o religioso e disabilità.
    ● Non eludere il ban o le misure di moderazione del server usufruendo di account alternativi e non nascondere la tua identità.
    ● Non sessualizzare in alcun modo immagini raffiguranti minori, inclusi i contenuti illustrati come lolicon o shotacon. Non pubblicare contenuti espliciti (NSFW) di alcun tipo.
    ● Non sono assolutamente consentiti contenuti espliciti quali gore e immagini di violenza su persone ed animali.
    ● Non organizzare o trattare attività illegali quali terrorismo, traffico di sostanze illecite, di armi o di prodotti contraffatti. Anche la compravendita di account o risorse in game è vietata.
    ● Non incitare al suicidio o all'autolesionismo, il bullismo non è tollerato ed è vietata la pubblicazione non consenziente di contenuti espliciti o immagini intime di altre persone (revenge porn), nel tentativo di umiliarle o screditarle.
    ● Non pubblicizzare altri youtubers ed evita l'autopromozione e i link di invito a server esterni.
    ● Non trollare gli altri membri, non condividere malware o virus e non minacciare o fingere di essere un hacker.''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(aliases=['Sito'])
async def sito(ctx):
    embed=discord.Embed(title='Sito ufficiale di SkullCenter', url='https://www.skullcenter.net', color=0xFF0000)
    embed.set_author(name='Sito')
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(aliases=['Partner'])
async def partner(ctx):
    embed=discord.Embed(title='**Come diventare partner**', description='''
    Requisiti Twitch:
     ● Avere minimo 1000 follower
     ● Avere minimo 15 spettatori medi
     ● Rispettare il regolamento di Twitch e non avere sanzioni da quest ultimo.

    Requisiti Youtube:
     ● Avere minimo 5000 follower
     ● Portare contenuti di qualità
     ● Fare almeno 400-500 visualizzazioni medie in 1-2 giorni.

    Vantaggi di essere affiliati con SkullCenter:
     ● Targhetta partner sul discord
     ● Supporto tecnico e configurazionale per server discord
     ● Vignetta sul sito ufficiale di SkullCenter
     ● Opportunità di formare team e collaborazioni con altri partner di SkullCenter
     ● SMP privato e supportato da SkullCenter
     ● Supporto e setup per video editing e live
     
    Confermatosi i requisiti aprire un ticket sul discord e aspettare la risposta di un amministratore''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(aliases=['Staff'])
async def staff(ctx):
    embed=discord.Embed(title='**STAFF**', description='''
    **AMMINISTRATORI**:
     ● Yuvi#2432
     ● 𝗛𝗲𝗮𝗿𝘁𝗹𝗲𝘀𝘀#4067
    **TECNICI**:
     ● Pisicupo#1705
     ● NeM#7562
     ● minisbiri#5676
     ● Fr3zez#1672''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(aliases=['Developer'])
async def developer(ctx):
    embed=discord.Embed(title='**DEVELOPER BOT**', description='''
    Pisicupo#1705
    Pisicupo su Telegram
    NeM#7562
    zNeMx su Telegram''', color=0xFF0000)
    embed.set_footer(text='By Pisicupo#1705')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(aliases=['Aiuto'])
async def aiuto(ctx):
    embed = discord.Embed(title='Aiuto', description='''
    Sei hai bisogno di aiuto contatta o apri
    un ticket affinchè un **admin** o **staffer** ti 
    possa aiutare.''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)

@client.command(aliases=['Comandi'])
async def comandi(ctx):
    embed = discord.Embed(title='Comandi', description='''
    ● Regole: Esegui questo comando per visualizzare le regole del server
    ● Sito: Esegui questo comando per sapere il link del sito
    ● Partner: Esegui questo comando per conoscere i requisiti di affiliazione 
    ● Staff: Esegui questo comando per una lista dei membri dello staff
    ● Aiuto: Esegui questo comando per sapere come ricevere assistenza
    ● Social: Esegui questo comando per conoscere i social ufficiali di SkullCenter''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()
#STANZE
@client.command(alisaes=['Stanza'])
async def stanza(ctx):
    embed = discord.Embed(title='**Come fare stanze private**', description='''
    ━━━━━━━━━━━━━━━━
    Private Rooms
    ● Prefix= !pb
    Lock = Chiudi la stanza
    Rename = Cambia nome alla stanza
    Unlock = Apri la stanza

    es. !pbLock

    N.B. le stanze si eliminano dopo che
         l'ultima persona rimasta esce
            le stanze permanenti si potranno 
            avere in futuro.
    ━━━━━━━━━━━━━━━━''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()
#SOCIAL
@client.command(aliases=['Social'])
async def social(ctx):
    embed = discord.Embed(title='**Social**', description='''
    ● TikTok: **SkullCenterOfficial**
    ● Instagram: **SkullCenterOfficial**''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()
#MUSICA
@client.command(aliases=['Musica'])
async def musica(ctx):
    embed = discord.Embed(title='**Musica**', description='''
    
    ━━━━━━━━━━━━━━━
      Musica
     ● Manda il titolo o link del tuo brano
        preferito e il bot si unirà a te
        riproducendolo
    ━━━━━━━━━━━━━━━''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()
#RUOLI
@client.command(aliases=['Ruoli'])
@commands.has_role('👑')
async def ruoli(ctx):
    embed = discord.Embed(title='**Ruoli**', description='''
    ● **🤵 | Amministratori**: Gestore community e staff
    ● **👨‍💻 | Tecnici**: Gestore di sito web e bot discord
    ● **🤖 | Skull Center**: Bot discord ufficiali''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()

#COMANDI STAFF
@client.command(aliases=['Comandistaff'])
@commands.has_role('👑')
async def comandistaff(ctx):
    embed = discord.Embed(title='**Comandi per gli staff**', description='''
    ● **Mute** (@utente) serve per mutare una persona perma
    ● **Unmute** (@utente) serve per smutare una persona
    ● **Kick** (@utente) serve per cacciare una persona
    ● **Ban** (@utente) serve per bannare una persona
    ● **Unban** (@utente) serve per unbannare una persona
    ● **ClearChat** serve per cancellare tutti i messaggi di una chat, massimo 100 messaggi (solo per chi ha 👑)''', color=0xFF0000)
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()

#FINE ZONA EMBED

#ZONA COMANDI CON PERMESSI
#MUTE

@client.command(aliases=['m'])
@commands.has_permissions(kick_members = True)
async def mute(ctx, member : discord.Member, *, reason='**Infrazione regole della community**'):
    muted_role = ctx.guild.get_role(YOUR ID MUTED ROLE)

    await member.add_roles(muted_role)
    embed = discord.Embed(title='**Mute**', description=f'''
    {member} è stato mutato da
    **Moderatore**: {ctx.author.name}
    **Motivo**: ''' +reason, color=0xFF0000)
    embed.set_author(name='SkullCenter Security')
    embed.set_thumbnail(url='https://media0.giphy.com/media/4tQw3rAfoVZf5kMUVZ/giphy.gif?cid=790b7611e426c1fd6036683897a5b51905fd5ffea1a8746c&rid=giphy.gif&ct=g')
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()
#UNMUTE
@client.command(aliases=['um'])
@commands.has_permissions(kick_members = True)
async def unmute(ctx, member : discord.Member, *, reason=None):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title='**Unmute**', description=f'''
    {member} è stato smutato da
    **Moderatore**: {ctx.author.name}''', color=0xFF0000)
    embed.set_author(name='SkullCenter Security')
    embed.set_thumbnail(url='https://media0.giphy.com/media/4tQw3rAfoVZf5kMUVZ/giphy.gif?cid=790b7611e426c1fd6036683897a5b51905fd5ffea1a8746c&rid=giphy.gif&ct=g')
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await ctx.message.delete()



#KICK
@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*,reason= '**Infrazione regole della community**'):
    embed = discord.Embed(title='**Kick**', description=f'''
    {member} è stato cacciato dal server da
    **Moderatore**: {ctx.author.name}
    **Motivo**: ''' +reason, color=0xFF0000)
    embed.set_author(name='SkullCenter Security')
    embed.set_thumbnail(url='https://media0.giphy.com/media/4tQw3rAfoVZf5kMUVZ/giphy.gif?cid=790b7611e426c1fd6036683897a5b51905fd5ffea1a8746c&rid=giphy.gif&ct=g')
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await member.kick(reason=reason)
    await ctx.message.delete()
#BAN
@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*,reason= '**Infrazione regole della community**'):
    embed = discord.Embed(title='**Ban**', description=f'''
    {member} è stato bannato dal server da
    **Moderatore**: {ctx.author.name}
    **Motivo**: ''' +reason, color=0xFF0000)
    embed.set_author(name='SkullCenter Security')
    embed.set_thumbnail(url='https://media0.giphy.com/media/4tQw3rAfoVZf5kMUVZ/giphy.gif?cid=790b7611e426c1fd6036683897a5b51905fd5ffea1a8746c&rid=giphy.gif&ct=g')
    embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
    await ctx.send(embed=embed)
    await member.ban(reason=reason)
    await ctx.message.delete()
#UNBAN
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    bannedUsers = await ctx.guild.bans()
    name, discrimator = member.split('#')

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discrimator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title='**Unban**', description=f'''
            {user.mention} è stato unbannato da
            **Moderatore**: {ctx.author.name}''', color=0xFF0000)
            embed.set_author(name='SkullCenter Security')
            embed.set_thumbnail(url='https://media0.giphy.com/media/4tQw3rAfoVZf5kMUVZ/giphy.gif?cid=790b7611e426c1fd6036683897a5b51905fd5ffea1a8746c&rid=giphy.gif&ct=g')
            embed.set_footer(text='SkullCenter| ● Chill | ● Gaming | ● Service')
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return

#CLEARCHAT
@client.command(aliases=['purge'])
@commands.has_role('👑')
async def clear(ctx, amount=9):
    ammount = amount+1
    if amount > 101:
        await ctx.send('Non posso eliminare più di 100 messaggi')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Messaggi eliminati')
        
#ZONA JOIN
@client.event
async def on_member_join(member):
    await member.send(f'''
    {member} benvenuto nel server discord ufficiale di **SkullCenter**.
    Perfavore leggi il regolameno facendo !!regole oppure nella apposita stanza #「📙」regolamento''')
#ZONA VOCALE
@client.command()
async def entra(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('Non sei in un canale vocale, per fare questo comando entra in un canale vocale')

@client.command()
async def esci(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Sono uscito nel canale vocale')
    else:
        await ctx.send('Non sono in un canale vocale')

@client.command()
async def play(ctx, *, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    player[server.id] = player


client.run('YOUR TOKEN BOT')
