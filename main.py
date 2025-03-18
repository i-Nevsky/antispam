from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TRADING_WORD = "трейдинг"

async def delete_trading_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.text:
        if TRADING_WORD in update.message.text.lower():
            await context.bot.delete_message(
                chat_id=update.effective_chat.id,
                message_id=update.message.message_id
            )

if __name__ == '__main__':
    app = ApplicationBuilder().token("7712516662:AAECNpqvIMy1OszmAAQxrBEuHYhQc52v4kQ").build()  # вставь токен
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_trading_message))
    app.run_polling()
