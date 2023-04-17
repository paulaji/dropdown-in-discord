import discord
from discord.ext import commands 
import os

class SelectMenu(discord.ui.Select):
  def __init__(self):
    options = [discord.SelectOption(label = "feedback"), discord.SelectOption(label = "bug-report")]
    super().__init__(placeholder = "Tell Gator what form to provide", options = options)

  async def callback(self, interaction:discord.Interaction):
    await interaction.response.send_message(content = f"Providing you with **{', '.join(self.values)} form**")

class Select(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.add_item(SelectMenu())

client = commands.Bot(command_prefix = "/", intents = discord.Intents.all())

CHANNEL_ID = #blahblahblacksheep
channel = client.get_channel(CHANNEL_ID)

@client.event
async def on_ready():
  await client.tree.sync()

@client.tree.command(name="select", description="this is a sample menu")
async def select(interaction: discord.Interaction):
    view = Select()
    await interaction.response.send_message(content="Gator here to help!", view=view)


@client.command(aliases = ['hi'])
async def hello(ctx):
 await ctx.send("Hi there, Gator here for surveys. Use !feedback for feedbacks and !bugreport for... yeah you guessed it, bugreports.")

@client.tree.command(name="feedback", description = "for feedbacks")
async def feedback(interaction: discord.Interaction):
  await interaction.response.send_message(content = "Hey")

@client.command()
async def johnwickhasapencil(ctx):
  await ctx.send("Terminating the bot :(")
  await client.close()

client.run(os.getenv("TOKEN"))


