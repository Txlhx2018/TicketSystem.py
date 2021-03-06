import discord
from discord.ext import commands
from discord import Activity, ActivityType
from discord.utils import get

client = commands.Bot(command_prefix ='.')
client.remove_command('help')

@client.event
async def on_ready():
        await client.wait_until_ready()
        await client.change_presence(activity=Activity(name="Playing Ticket System by Talha2018#0001",
                                                type=ActivityType.playing))
        print('Bot is ready')

@client.command()
async def new(ctx):
     
        ticket_channel = await ctx.guild.create_text_channel(name=f":ticket-{ctx.author}") 
        await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)  
        
        guild = ctx.guild 
        rolesearch = discord.utils.get(guild.roles,  name="Ticket-Helper")
        await ticket_channel.set_permissions(rolesearch, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True, manage_channels=True)  
        
        await ticket_channel.set_permissions(guild.default_role, send_messages=False, read_messages=False) 
   
        embed=discord.Embed(color=0xff8103)
        embed.add_field(name="Support Ticket", value=f"Ticket by {ctx.author.mention}", inline=False)
        embed.add_field(name="Option:", value=":lock: - ```.close - <#ticket>```", inline=False)
        embed.set_footer(text=f"Ticket | {ctx.author}")
        await ticket_channel.send(embed=embed)
        await ticket_channel.send(f"Hello, {ctx.author.mention}! Please describe your problem as well as you can, that a Ticket-Helper can help you.") 

@client.command()
@commands.has_permissions(manage_channels=True)
async def close(ctx, channel: discord.TextChannel): 

         await ctx.channel.delete()      

@client.command()
@commands.has_permissions(administrator=True) 
async def setup(ctx):
           
        guild = ctx.guild
        await ctx.guild.create_role(name="Ticket-Helper", colour=discord.Colour(0xE03400)) 
        em=discord.Embed(title="Information", description="Ticket System was successfully installed. | Attention If you run ```.setup``` again, the ticket system will no longer work and report an error. Since there are there 2 roles of ticket helper you have to delete one then, This code is still in development for problems/questions contact me on Discord : Talha2018#0001", color=0x00ff00)                                    
        await ctx.send(embed=em) 
           
@client.command() 
async def support(ctx):
	       
        embed=discord.Embed(title="Support", description="Contact me for Support, Discord : ```Talha2018#0001```", color=0x00ff00)                                                                                  
                                                   
        await ctx.send(embed=embed) 
        
@client.command() 
async def help(ctx):
	       
        embed=discord.Embed(title="Help", description="```.new``` - Ticket create, ```.setup``` - Install Ticket System, ```.support``` - support ```.close <#ticket>``` - delete a Ticket", color=0x00ff00)                                                                                  
                                                   
        await ctx.send(embed=embed) 
	
client.run('Your BOT TOKEN FROM DISCORD DEVELOPER PORTAL')
#Talha2018 - For Help Contact me on Discord : Talha2018#0001
