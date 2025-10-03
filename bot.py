import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"スラッシュコマンド {len(synced)} 個を同期しました")
    except Exception as e:
        print(f"同期エラー: {e}")

@bot.tree.command(name="hello", description="挨拶を返します")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"こんにちは、{interaction.user.mention}！")

# Renderの環境変数からTOKENを読み込む
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
