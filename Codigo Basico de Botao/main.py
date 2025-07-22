import discord
from discord.ext import commands

# Define o prefixo para comandos tradicionais (ex: !comando)
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento para indicar que o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    bot.add_view(TesteBotao()) # Isso serve para que se o bot ficar off-line, quando ele voltar o botão irá está funcionando normalmente.
    # Importante: sincroniza os comandos de barra (slash) com a API do Discord
    await bot.tree.sync()
    print("Comandos slash sincronizados!")

# Classe do botão
class TesteBotao(discord.ui.View):
    def __init__(self):
        # timeout=None significa que o botão não irá expirar enquanto o bot estiver online
        super().__init__(timeout=None)

    # Evento de clique no botão
    @discord.ui.button(label="Testar botão", style=discord.ButtonStyle.primary, custom_id="botao_teste_123")
    async def teste_botao_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Você clicou no botão! ✅", ephemeral=True)

# Comando slash /botao
@bot.tree.command(name="botao", description="Envia uma embed com um botão interativo")
async def botao(interaction: discord.Interaction):
    guild = interaction.guild

    # Criação da embed
    embed = discord.Embed(
        title="Exemplo de Embed com Botão",
        description="Clique no botão abaixo para testar a interação!",
        color=discord.Color.blue()
        # Você pode utilizar o método mais fácil de achar a cor que você deseja que é usando cor Hexadecimal, ex: color=discord.Color(0xFF0000)
        # Utilize o site abaixo para pegar cores em hexadecimal:
        # https://www.google.com/search?q=cor+em+hexadecimal&oq=cor+em+&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPNIBCDE4NjlqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8&sei=aWx_aI-FDqqy5OUP8dTcuA0
    )
    embed.set_author(name=guild.name, icon_url=guild.icon.url if guild.icon else discord.Embed.Empty) # Colocar o author da embed, com icone do servidor.
    embed.set_footer(text="Footer do servidor", icon_url=guild.icon.url if guild.icon else discord.Embed.Empty) # Colocar o footer da embed, com icone do servidor

    await interaction.response.send_message(embed=embed, view=TesteBotao()) # Esse view ele está adicionando o botão "Testar botão" junto da embed.

# Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot do Discord
# Para pegar o seu TOKEN, Acesse https://discord.com/developers/applications !
bot.run('SEU_TOKEN_AQUI')
