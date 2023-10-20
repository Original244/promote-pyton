import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    await client.process_commands(message)







#-----------------------------------------------------



#------------------------ DEMOTED -----------------------
@client.command()
@commands.has_any_role("Staff Management")
async def demote(ctx, member: discord.Member = None, *, reason=None):
    await ctx.channel.purge(limit=1)
    if member is None:
        await ctx.send('Recuerda que tienes que etiquetar a alguien al usar el comando.')
        return

    if not any(role.name == "Staff Management" for role in ctx.author.roles):
        await ctx.send('Lo siento, no tienes permiso para usar este comando.')
        return

    highest_role = member.top_role
    await member.kick(reason=reason)
    canal_log = client.get_channel(942241059654737952)
    await canal_log.send(f'**DEMOTED** {member.mention} {highest_role} > User')


#------------------------------- RESIGN -------------------------------


@client.command()
@commands.has_any_role("Staff Management")
async def resign(ctx, member: discord.Member = None, *, reason=None):
    await ctx.channel.purge(limit=1)
    if member is None:
        await ctx.send('Recuerda que tienes que etiquetar a alguien al usar el comando.')
        return

    if not any(role.name == "Staff Management" for role in ctx.author.roles):
        await ctx.send('Lo siento, no tienes permiso para usar este comando.')
        return

    highest_role = member.top_role
    await member.kick(reason=reason)
    canal_log = client.get_channel(942241059654737952)
    await canal_log.send(f'**RESIGN** {member} {highest_role} > User')


#------------------------------REJECT --------------------------------------------




@client.command()
@commands.has_any_role("Staff Management")
async def reject (ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    if member is None:
        
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=1)
        await ctx.send('Recuerda que tienes que etiquetar a alguien al usar el comando.')
        return
    
    if ctx.author.id == 630248424985591811 or ctx.author.id == 555457054832197673 or ctx.author.id == 970756137811062784:
        await member.kick(reason=reason)
        canal_log = client.get_channel(942241059654737952)
        await canal_log.send(f'**REJECT** {member.mention} Learner > User')
    else:
        await ctx.send('Lo siento, no tienes permitido usar este comando')


#---------------------- INVITES ----------------------------
@client.command()
@commands.has_any_role("Staff Management")
async def invite(ctx):
        
    await ctx.channel.purge(limit=1)
    invite = await ctx.channel.create_invite(max_uses=1, max_age=86400)
    
    embed = discord.Embed(color=discord.Color.blue())
    embed.set_author(name="Invitación generada")
    embed.add_field(name="Generada por", value=ctx.author.name, inline=False)
    embed.add_field(name="Fecha y hora", value=ctx.message.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    embed.add_field(name="Invitación", value=invite.url, inline=False)
    
    await ctx.author.send(embed=embed)

    registro_channel_id = 942241059440848982
    registro_channel = client.get_channel(registro_channel_id)
    if registro_channel:
        await registro_channel.send(embed=embed)
    else:
        print(f"No se pudo encontrar el canal con ID {registro_channel_id}")



#------------------------------- PROMOTE -------------------------------
@client.command()
@commands.has_any_role("Staff Management")
async def promote(ctx, member: discord.Member=None):
     await ctx.channel.purge(limit=1)

     if member == None:
         await ctx.send(f"{ctx.author.mention}, debes mencionar a un miembro")
         return

     ############################################################
     #                                                          #
     #                     Rank Id`s                            #
     #                                                          #
     ############################################################
     learner = ctx.guild.get_role(942241058912342020)
     trialmod = ctx.guild.get_role(942241058912342021) 
     mod = ctx.guild.get_role(942241058912342022)
     srmod = ctx.guild.get_role(942241058912342025)

     admin = ctx.guild.get_role(942241058929147938)
     headadmin = ctx.guild.get_role(942241058929147939)
     platformadmin = ctx.guild.get_role(942241058945908776)
     lowstaff = ctx.guild.get_role(942241058912342019)
     mediumstaff = ctx.guild.get_role(942241058912342023)
     highstaff = ctx.guild.get_role(942241058929147936)
     trainer = ctx.guild.get_role(942241058891374655)
     management = ctx.guild.get_role(942241058929147940)
     staff = ctx.guild.get_role(942241058912342018)
     ############################################################
     #                                                          #
     #                     Rank Id`s                            #
     #                                                          #
     ############################################################
     channel = client.get_channel(942241059654737952)

     if learner in member.roles:
         oldrank = "Learner"
         newrank = "Staff"
         await member.remove_roles(learner)
         await member.add_roles(staff)
         await member.add_roles(lowstaff)
         await member.add_roles(trialmod)

     elif trialmod in member.roles:
         oldrank = "Staff"
         newrank = "Mod"
         await member.remove_roles(trialmod)
         await member.add_roles(mod)
         
     elif mod in member.roles:
         oldrank = "Mod"
         newrank = "Senior-Mod"
         await member.remove_roles(mod)
         await member.remove_roles(lowstaff)
         await member.add_roles(mediumstaff)
         await member.add_roles(srmod)

     elif srmod in member.roles:
         oldrank = "Senior-Mod"
         newrank = "Admin"
         await member.remove_roles(srmod)
         await member.remove_roles(mediumstaff)
         await member.add_roles(highstaff)
         await member.add_roles(trainer)
         await member.add_roles(admin)

     elif admin in member.roles:
         oldrank = "Admin"
         newrank = "Head-Admin"
         await member.remove_roles(admin)
         await member.add_roles(headadmin)

     elif headadmin in member.roles:
         oldrank = "Head-Admin"
         newrank = "Platform-Admin"
         await member.remove_roles(headadmin)
         await member.remove_roles(highstaff)
         await member.add_roles(platformadmin)

     else:
         await ctx.send("Ocurrio un error, asegurate de que el miembro tenga un rol de staff")
    
     await channel.send(f"**PROMOTED** {member.mention} {oldrank} > {newrank}")




#Asignar rol a los learner/  (Nuevos miembros)
@client.event
async def on_member_join(member):
    rol = discord.utils.get(member.guild.roles, name="Learner")  # Obtener el rol por su nombre
    await member.add_roles(rol)  # Asignar el rol al miembro
    mensaje = f'**NEW** {member.mention} Learner'  # Mensaje de bienvenida
    await client.get_channel(942241059654737952).send(mensaje)


#Mensaje borrados
@client.event
async def on_message_delete(message):
    canal_log = client.get_channel(942241059440848982)  # Reemplaza 942241059440848982 con el ID del canal de logs donde se enviará el mensaje

    # Construye el cuadro del mensaje borrado
    log_message = f"```\nMensaje borrado en #{message.channel.name}\n\n"
    log_message += f"Autor: {message.author.name} ({message.author.id})\n"
    log_message += f"Contenido: {message.content}\n"
    log_message += f"Fecha: {message.created_at}\n```"

    await canal_log.send(log_message)




#------------------------------------- /HELP -----------------------------------------
client.remove_command('help')

@client.command()
async def help(ctx):
    # Verifica si el autor del mensaje tiene el rol "staff management"
    if discord.utils.get(ctx.author.roles, name="Staff Management"):
        embed = discord.Embed(title="Comandos de Ayuda", description="Lista de comandos disponibles:", color=0x00ff00)

        # Añade los comandos y sus descripciones
        embed.add_field(name="/demote", value="Cada que uses este comando se expulsara del **discord del staff** al usuario que menciones al usar este comando y dejando logs en **#staff-changes** y al que use el comando le toca expulsarlo del discord del staff o quitar los roles", inline=False)
        embed.add_field(name="/invite", value="Cada que uses este comando te enviará una invitación unica de un solo uso con un uso de 24hrs al privado", inline=False)
        embed.add_field(name="/promote", value="Cada que uses este comando se subirá de rango al staff que pongas, recuerda que solo se le agrega el promote en el **discord del staff** y el que use el comando le toca editar los roles del staff", inline=False)
        embed.add_field(name="/reject", value="Este comando lo usarás cada que hagas staff applies para el rango Staff y haya fallado los 2 intentos para que se le expulse del server y deje logs en #staff-changes", inline=False)
        embed.add_field(name="/resing", value="Este comano lo usarás cada que un staff no quiera ser mas staff ya por cualquier razón", inline=False)
        # ...

        await ctx.send(embed=embed)
    else:
        await ctx.send("¡No tienes permisos para usar este comando!")