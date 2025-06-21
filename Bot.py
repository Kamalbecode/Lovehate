
import telebot
import random
import re

# Your Telegram Bot API Token (REPLACE WITH YOUR NEW ONE)
API_KEY = "8164908656:AAEO1rvEaNHrXwZTrwTYf6Wqj5awopZnmrI"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! 👋 Send `/checklove Name1 & Name2` to get love and hate percentages.", parse_mode="Markdown")

@bot.message_handler(commands=['checklove'])
def check_love(message):
    text = message.text
    pattern = r"/checklove\s+(.+)\s*&\s*(.+)"
    match = re.match(pattern, text, re.IGNORECASE)

    if match:
        name1 = match.group(1).strip()
        name2 = match.group(2).strip()
        love = random.randint(50, 100)
        hate = 100 - love
        reply = f"❤️ *Love* between *{name1}* and *{name2}*: `{love}%`\n💔 *Hate*: `{hate}%`"
        bot.reply_to(message, reply, parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ Use the format: `/checklove Alice & Bob`")

# Keep the bot running
print("Bot is running...")
bot.infinity_polling()
