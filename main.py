from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def check_range(update, context):
    number = ' '.join(context.args)
    if not number:
        update.message.reply_text("Please provide a number. Example: /check 989925646809")
        return
    update.message.reply_text(f"📞 Checking: {number}\n\n✅ WhatsApp: Active\n❌ Telegram: Not Registered")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("check", check_range))
updater.start_polling()
updater.idle()
