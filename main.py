import Constants as Keys
from telegram.ext import *
import Responses as R

print("Bot is getting starting in few seconds...")


def start_command(update, context):
    # update.message.reply_text('WELCOME HACKER! YOUR BOTS ARE WAITING FOR YOU...')
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="Hello {yourname}! We are welcome to come in Dhruma's mam library".format(
        yourname=update.effective_user.first_name))
    update.message.reply_text('/register for register a new user')
    update.message.reply_text('/help for more → query')


def help_command(update, context):
    # update.message.reply_text('if you need help! you should ask for it on google')
    update.message.reply_text(f"""
/start → Welcome to the channel
/help → This get's instant help
/Register → register a new user to this bot
----------------------------------------------------------------------
/Subject → Here are lists of subject 
""")


def Subject_command(update, context):
    update.message.reply_text("Select your Subject (:")
    update.message.reply_text("1./SocialScience")
    update.message.reply_text("2./psychology")
    update.message.reply_text("3./English")

# ------------------------English ------------------------------------------


def English_command(update, context):
    update.message.reply_text("Select your Standard:-")
    update.message.reply_text("→/Eng_Standard_9")
    update.message.reply_text("→/Eng_Standard_10")
    update.message.reply_text("→/Eng_Standard_11")
    update.message.reply_text("→/Eng_Standard_12")
    # update.message.reply_text("Syntax : 's11' → '11' is for your standard")


def EnglishStandard9_command(update, context):
    update.message.reply_text('Standard 9 Study Material:')
    update.message.reply_text("Ch-1.")
    update.message.reply_text("Ch-2.")
    update.message.reply_text("Ch-3.")
    update.message.reply_text("Ch-4.")
    update.message.reply_text("Ch-5.")
    update.message.reply_text("Ch-6.")


def EnglishStandard10_command(update, context):
    update.message.reply_text('Standard 10 Study Material:')
    update.message.reply_text("Ch-1.")
    update.message.reply_text("Ch-2.")
    update.message.reply_text("Ch-3.")
    update.message.reply_text("Ch-4.")
    update.message.reply_text("Ch-5.")
    update.message.reply_text("Ch-6.")


def EnglishStandard11_command(update, context):
    update.message.reply_text('Select your Book:')
    update.message.reply_text("1./Snapshots")
    update.message.reply_text("2./Hornbill")
    
def EnglishStandard11_Snapshots_command(update, context):
    update.message.reply_text('Standard 11_Snapshots Study Material:')
    update.message.reply_text('---------------------------------------')
    update.message.reply_text("/1201 Ch-1.The summer of the beatiful..")
    update.message.reply_text("/1202 Ch-2.The address")
    update.message.reply_text("/1203 Ch-3.Ranga's marriage")
    update.message.reply_text("/1204 Ch-4.Albert Einstein school")
    update.message.reply_text("/1205 Ch-5.Mother's day")
    update.message.reply_text("/1206 Ch-6.The ghat of the only world")
    update.message.reply_text("/1207 Ch-7.The tale of melon city")

def EnglishStandard11_Hornbill_command(update, context):
    update.message.reply_text('Standard 11_Hornbill Study Material:')
    update.message.reply_text('#----------------------#----------------------#')
    update.message.reply_text("/1101 Ch-1.The portait of a lady")
    update.message.reply_text("/1111 poem-1.A photograph")
    update.message.reply_text("/1102 Ch-2.We're not afraid to die..")
    update.message.reply_text("/1103 Ch-3.Discovering Tut: the saga continues ")
    update.message.reply_text("/1113 poem-3. The Laburnum Top")
    update.message.reply_text("/1104 Ch-4.Landscape of the soul")
    update.message.reply_text("/1114 poem-4. The voice of the rain")
    update.message.reply_text("/1105 Ch-5.The Ailing planet: the green..")
    update.message.reply_text("/1106 Ch-6.The browning version")
    update.message.reply_text("/1116 poem-6.Childhood")
    update.message.reply_text("/1107 Ch-7.The adventure")
    update.message.reply_text("/1108 Ch-8.Silk Road")
    update.message.reply_text("/1118 poem-8.Father to son")


def EnglishStandard12_command(update, context):
    update.message.reply_text('Standard 12 Study Material:')
    update.message.reply_text("/1201 Ch-1.")
    update.message.reply_text("/1201 Ch-2.")
    update.message.reply_text("/1201 Ch-3.")
    update.message.reply_text("/1201 Ch-4.")
    update.message.reply_text("/1201 Ch-5.")
    update.message.reply_text("/1201 Ch-6.")
    update.message.reply_text("/1201 Ch-7.")
    update.message.reply_text("/1201 Ch-8.")
    update.message.reply_text("/1201 Ch-9.")
    update.message.reply_text("/1201 Ch-10.")
    update.message.reply_text("/1201 Ch-11.")
# ------------------------Psychology --------------------------------------------


def psychology_command(update, context):
    update.message.reply_text("Select your Standard:-")
    update.message.reply_text("→/Psy_Standard_11")
    update.message.reply_text("→/Psy_Standard_12")
    # update.message.reply_text("Syntax : 's11' → '11' is for your standard")

def PsychologyStandard11_command(update, context):
    update.message.reply_text('Standard 11 Study Material:')
    update.message.reply_text("Ch-1.")
    update.message.reply_text("Ch-2.")
    update.message.reply_text("Ch-3.")
    update.message.reply_text("Ch-4.")
    update.message.reply_text("Ch-5.")
    update.message.reply_text("Ch-6.")


def PsychologyStandard12_command(update, context):
    update.message.reply_text('Standard 12 Study Material:')
    update.message.reply_text("/0112 Ch-1.Variation in Psychological attributes ")
    update.message.reply_text("/0212 Ch-2.Self and Personality ")
    update.message.reply_text("/0312 Ch-3.Meeting life challenges ")
    update.message.reply_text("/0412 Ch-4.Psychological Disorders")
    update.message.reply_text("/0512 Ch-5.Therapeutic approaches ")
    update.message.reply_text("/0612 Ch-6.Attitude and Social cognition ")
    update.message.reply_text("/0712 Ch-7.Social Influences and Group processes")
    update.message.reply_text("/0812 Ch-8. Psychology and life ")
    update.message.reply_text("/0912 Ch-9.Developing Psychological Skills ")

# ------------------------SocialScience ------------------------------------------


def SocialScience_command(update, context):
    update.message.reply_text("Select your Standard:-")
    update.message.reply_text("→/SS_Standard_9")
    update.message.reply_text("→/SS_Standard_10")
    update.message.reply_text("→/SS_Standard_11")
    update.message.reply_text("→/SS_Standard_12")
    # update.message.reply_text("Syntax : 's11' → '11' is for your standard")

def SocialScienceStandard9_command(update, context):
    update.message.reply_text('Standard 9 Study Material:')
    update.message.reply_text("Ch-1.")
    update.message.reply_text("Ch-2.")
    update.message.reply_text("Ch-3.")
    update.message.reply_text("Ch-4.")
    update.message.reply_text("Ch-5.")
    update.message.reply_text("Ch-6.")


def SocialScienceStandard10_command(update, context):
    update.message.reply_text('Standard 10 Study Material:')
    update.message.reply_text("Ch-1.")
    update.message.reply_text("Ch-2.")
    update.message.reply_text("Ch-3.")
    update.message.reply_text("Ch-4.")
    update.message.reply_text("Ch-5.")
    update.message.reply_text("Ch-6.")


def SocialScienceStandard11_command(update, context):
    update.message.reply_text('Standard 11 Study Material:')
    update.message.reply_text("Ch-1.")
    update.message.reply_text("Ch-2.")
    update.message.reply_text("Ch-3.")
    update.message.reply_text("Ch-4.")
    update.message.reply_text("Ch-5.")
    update.message.reply_text("Ch-6.")


def SocialScienceStandard12_command(update, context):
    update.message.reply_text('Standard 12 Study Material:')
    update.message.reply_text("Ch-1.")
    update.message.reply_text("Ch-2.")
    update.message.reply_text("Ch-3.")
    update.message.reply_text("Ch-4.")
    update.message.reply_text("Ch-5.")
    update.message.reply_text("Ch-6.")


def register_command(update, context):
    update.message.reply_text
    (f"Your registration must be done otherwise you can't send this data to you..!")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(Keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("Subject", Subject_command))
    # English_command_call
    dp.add_handler(CommandHandler("English", English_command))
    dp.add_handler(CommandHandler("Eng_Standard_9", EnglishStandard9_command))
    dp.add_handler(CommandHandler("Eng_Standard_10", EnglishStandard10_command))
    dp.add_handler(CommandHandler("Eng_Standard_11", EnglishStandard11_command))
    dp.add_handler(CommandHandler("Hornbill", EnglishStandard11_Hornbill_command))
    dp.add_handler(CommandHandler("Snapshots", EnglishStandard11_Snapshots_command))
    dp.add_handler(CommandHandler("Eng_Standard_12", EnglishStandard12_command))

    # Psychology_command_call
    dp.add_handler(CommandHandler("psychology", psychology_command))
    dp.add_handler(CommandHandler("Psy_Standard_11", PsychologyStandard11_command))
    dp.add_handler(CommandHandler("Psy_Standard_12", PsychologyStandard12_command))
    # SocialScience_command_call
    dp.add_handler(CommandHandler("SocialScience", SocialScience_command))
    dp.add_handler(CommandHandler("SS_Standard_9", SocialScienceStandard9_command))
    dp.add_handler(CommandHandler("SS_Standard_10", SocialScienceStandard10_command))
    dp.add_handler(CommandHandler("SS_Standard_11", SocialScienceStandard11_command))
    dp.add_handler(CommandHandler("SS_Standard_12", SocialScienceStandard12_command))

    dp.add_handler(CommandHandler("register", register_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

#     update.message.reply_text("Ch-1.")
#     update.message.reply_text("Ch-2.")
#     update.message.reply_text("Ch-3.")
#     update.message.reply_text("Ch-4.")
#     update.message.reply_text("Ch-5.")
#     update.message.reply_text("Ch-6.")
