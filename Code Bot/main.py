import discord
from discord.ext import commands

# Define o prefixo para comandos tradicionais (ex: !comando)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento para indicar que o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    # Importante: sincroniza os comandos de barra (slash) com a API do Discord
    await bot.tree.sync()
    print("Comandos slash sincronizados!")

# Comando tradicional com prefixo, ex: !ping
@bot.command()
async def ping(ctx):
    # ctx = contexto do comando (quem enviou, onde, etc.)
    await ctx.send("Pong! 🏓 (comando por prefixo)") # Aqui o bot irá enviar essa mensagem, quando for utilizado !ping

# Comando do tipo "slash", ex: /ping
@bot.tree.command(name="ping", description="Responde com Pong! (comando slash)")
async def slash_ping(interaction: discord.Interaction):
    # interaction = interação do slash command 
    await interaction.response.send_message("Pong! 🏓 (comando slash)") # Aqui o bot irá enviar essa mensagem, quando for utilizado /ping

# Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot do Discord
# Para pegar o seu TOKEN, Acesse https://discord.com/developers/applications !
bot.run('SEU_TOKEN_AQUI')
