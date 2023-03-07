import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Replace YOUR_TOKEN with your bot token
bot = telegram.Bot(token='YOUR_TOKEN')

# Define the function to ban a user
def ban(update, context):
    user_id = update.message.from_user.id
    bot.kick_chat_member(chat_id=update.message.chat_id, user_id=user_id)

# Define the function to handle unknown commands
def unknown(update, context):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

# Create the handlers for the /banme and unknown commands
ban_handler = CommandHandler('banme', ban)
unknown_handler = MessageHandler(Filters.command, unknown)

# Create the updater and add the handlers to it
updater = Updater(token='YOUR_TOKEN', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(ban_handler)
dispatcher.add_handler(unknown_handler)

# Start the bot
updater.start_polling()
