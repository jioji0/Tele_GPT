from openai import OpenAI
client = OpenAI(
    api_key="apiKey"
)
import api

from telegram import ForceReply, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

token = "5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0"

# Define a few command handlers. These usually take the two arguments update and
# context.
# /start로 대화방을 가동시키는 경우 봇의 첫 메세지
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"HI {user.mention_html()}!, 나는 chatgpt 메신저야",
        reply_markup=ForceReply(selective=True),
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

'''
application = ApplicationBuilder().token("5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0").build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
application.run_polling(allowed_updates=Update.ALL_TYPES)
'''

#입력된 메세지로,  modgpt4 (gpt4 api를 호출하여 답변을 얻은 모듈) 모듈을 사용
async def gpt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """gpt모듈을 호출하는것."""
    print (update.message.text)
    await update.message.reply_text("......") #gpt 모듈이 응답을 준비하는동한 메세지로 ......을 보냄
    userPrompt = update.message.text
    gptresult = api.Command(userPrompt)
    await update.message.reply_text(gptresult) #gpt모듈의 답변을 메세지로 보냄


#위의 함수들을 종합하여 텔레그램에 커맨드와 답변을 처리하는 영역

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token("5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0").build()

    # on different commands - answer in Telegram   # /start등 /어쩌고로 지정된 액션을 받아들여, 해당 함수(start)를 호출 동작실행 시키는 커맨드 핸들러
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gpt)) #텔레그램 user messager를 받아 해당 함수(gpt)에 메세지 input을 넣을수 있는 메세지 핸들러

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
