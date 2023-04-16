import discord
from discord.ext import commands 
import os

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@client.event
async def on_ready():
  await client.tree.sync()

@client.command(aliases = ['hi'])
async def hello(ctx):
 await ctx.send("Hi there, Gator here for surveys. Use !feedback for feedbacks and !bugreport for... yeah you guessed it, bugreports.")


class TestButtons(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label = "test")
  async def test(self, button: discord.ui.Button, interaction: discord.Interaction):
    await interaction.channel.send("RRRRR Gator")

@client.tree.command(name = "test")
async def testnut(interaction: discord.Interaction):
  await interaction.response.send_message(content = "Gator here!", view = TestButtons())


@client.tree.command(name="feedback", description = "for feedbacks")
async def feedback(interaction: discord.Interaction):
  await interaction.response.send_message(content = "Hey")

@client.command()
async def terminationcommand(ctx):
  await ctx.send("Terminating the bot :(")
  await client.close()

client.run(os.getenv("TOKEN"))


