import discord
from discord.ext import commands

# Intents allow the bot to interact with users' messages and other events
intents = discord.Intents.default()
intents.message_content = True

# Define the bot with command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

# Create a dictionary to store user data
user_data = {}

# This function will handle the command that starts the data collection
@bot.command()
async def start(ctx):
    await ctx.send("Welcome to the data collection bot! Let's start by collecting some basic information.")
    await ctx.send("Please provide your name:")

# This will handle the user's response and store it
@bot.command()
async def collect(ctx, *, answer: str):
    user_id = ctx.author.id

    # Create a new entry for the user if it does not exist
    if user_id not in user_data:
        user_data[user_id] = {}

    # Store the user's data
    if "name" not in user_data[user_id]:
        user_data[user_id]["name"] = answer
        await ctx.send(f"Got your name: {answer}. What is your age?")
    elif "age" not in user_data[user_id]:
        user_data[user_id]["age"] = answer
        await ctx.send(f"Got your age: {answer}. What's your favorite color?")
    elif "color" not in user_data[user_id]:
        user_data[user_id]["color"] = answer
        await ctx.send(f"Got your favorite color: {answer}. Thank you for participating!")
        await ctx.send("Your data has been collected successfully!")

# This is an event that runs when the bot starts up
@bot.event
async def on_ready():
    print(f'Bot is logged in as {bot.user}')

# Run the bot with the token
bot.run('8009823215:AAFyzYFIvjvMTvS1454tJ1kp3kGh72TtgZY')
