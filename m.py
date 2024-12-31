from telethon import TelegramClient
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Telegram API credentials for Telethon
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

# Admin user ID to whom we send the data (replace with actual admin's Telegram ID)
admin_id = '6135948216'

# Create a Telethon client for accessing user data
client = TelegramClient('session_name', api_id, api_hash)

# Set up logging for the bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_user_data(user_id):
    """Collect user data using Telethon."""
    user = await client.get_entity(user_id)
    user_data = {
        'User ID': user.id,
        'Username': user.username,
        'First Name': user.first_name,
        'Last Name': user.last_name,
        'Phone Number': user.phone,
    }
    return user_data

def start(update: Update, context: CallbackContext):
    """Handle /start command from the user in the bot."""
    user_id = update.message.from_user.id
    user_name = update.message.from_user.full_name

    # Send a welcome message to the user
    update.message.reply_text(f"Hello {user_name}, your data is being collected!")

    # Collect user data using Telethon
    user_data = client.loop.run_until_complete(get_user_data(user_id))

    # Prepare the data to send to the admin
    user_data_str = "\n".join([f"{key}: {value}" for key, value in user_data.items()])

    # Send collected user data to the admin
    context.bot.send_message(chat_id=admin_id, text=f"User Data:\n{user_data_str}")

def main():
    """Start the Telegram Bot."""
    # Start the Telethon client
    client.start(phone_number)

    # Create the bot updater and dispatcher
    updater = Updater('7735159098:AAHB_Gb97ItiyiYqf2FEAnQeZYaAH6pntBI', use_context=True)

    # Register the /start command handler
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Start the bot
    updater.start_polling()
    updater.idle()

# Run the main function to start the bot and Telethon client
if __name__ == '__main__':
    main()
