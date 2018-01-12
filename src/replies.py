import keyboards
import logging
from telegram.ext import ConversationHandler

START, STAGE_1, STAGE_2_1,  STAGE_2_2, STAGE_3_1, STAGE_3_2, STAGE_4 = range(7)

def start(bot, update):
    logging.info('New user arrived! His update info: %s', update)
    if update.message.chat.type == 'private':
        update.message.reply_text("Hi dude! Let's test state machine! Here is the 'START' location.",
            reply_markup=keyboards.start_markup)
    else:
        update.message.reply_text(
            "Sorry, I work only in one-to-one conversations")
        return ConversationHandler.END

    return START

def stage_1(bot, update):
    update.message.reply_text("Welcome to the Stage 1! Let's go futher. What variant you're choose?",
        reply_markup=keyboards.stage_1_markup)

    return STAGE_1

def stage_2_1(bot, update):
    update.message.reply_text("Stage 2.1? Nice choice! What's next?",
        reply_markup=keyboards.stage_2_1_markup)

    return STAGE_2_1

def stage_2_2(bot, update):
    update.message.reply_text("Stage 2.2? Not so bad. Let's go to the next stage!",
        reply_markup=keyboards.stage_2_2_markup)

    return STAGE_2_2

def stage_3_1(bot, update):
    update.message.reply_text("Oh. Stage 3.1 was wrong choice. Go back to the Stage 1",
        reply_markup=keyboards.stage_3_1_markup)

    return STAGE_3_1

def stage_3_2(bot, update):
    update.message.reply_text("Stage 3.2! You're made the right choice!",
        reply_markup=keyboards.stage_3_2_markup)

    return STAGE_3_2

def stage_3_3(bot, update):
    update.message.reply_text("Stage 3.3! Great! You're almost finished!",
        reply_markup=keyboards.stage_3_2_markup)

    return STAGE_3_2

def stage_4(bot, update):
    update.message.reply_text("Stage 4! Congratulations! Now you can restart the state. :)",
        reply_markup=keyboards.reset_markup)

    return STAGE_4

def reset(bot, update):
    update.message.reply_text("Okay, resetting the state machine.",
        reply_markup=keyboards.start_markup)

    return START


def default_response(bot, update):
    update.message.reply_text(
        "What you need? I don't understand you. Try to reset the state.",
        reply_markup=keyboards.reset_markup)

    return STAGE_1


def done(bot, update):
    update.message.reply_text("Bye-bye. See you later!")

    return ConversationHandler.END