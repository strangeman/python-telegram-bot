#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import logging

import config, keyboards, replies
from saver import save_thread, loadData

logging.basicConfig(format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s',
            level=config.LOG_LEVEL, filename=config.LOG_FILE)

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(config.LOG_LEVEL)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, error)


def main():
    def kill_threads(signum, frame):
        saver.kill_received = True
    # Create the Updater and pass it your bot's token.

    #test bot
    updater = Updater(token=config.TOKEN, user_sig_handler=kill_threads)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', replies.start)],

        states={
            replies.START:    [RegexHandler(u'^Go to the Stage 1$',
                                    replies.stage_1),
                               MessageHandler(Filters.text,
                                    replies.default_response),
                       ],
            replies.STAGE_1:  [RegexHandler(u'^Go to the Stage 2\.1$',
                                    replies.stage_2_1),
                               RegexHandler(u'^Go to the Stage 2\.2$',
                                    replies.stage_2_2),
                               RegexHandler(u'^Reset the state$',
                                    replies.reset),
                               MessageHandler(Filters.text,
                                    replies.default_response),
                       ],
            replies.STAGE_2_1: [RegexHandler(u'^Go to the Stage 3\.1$',
                                    replies.stage_3_1),
                                RegexHandler(u'^Go to the Stage 3\.2$',
                                    replies.stage_3_2),
                                RegexHandler(u'^Reset the state$',
                                    replies.reset),
                                MessageHandler(Filters.text,
                                    replies.default_response),
                       ],
            replies.STAGE_2_2: [RegexHandler(u'^Go to the Stage 3\.3$',
                                    replies.stage_3_3),
                                RegexHandler(u'^Reset the state$',
                                    replies.reset),
                                MessageHandler(Filters.text,
                                    replies.default_response),
                       ],
            replies.STAGE_3_1: [RegexHandler(u'^Go to the Stage 1$',
                                    replies.stage_1),
                                RegexHandler(u'^Reset the state$',
                                    replies.reset),
                                MessageHandler(Filters.text,
                                    replies.default_response),
                       ],
            replies.STAGE_3_2: [RegexHandler(u'^Go to the Stage 4$',
                                    replies.stage_4),
                                RegexHandler(u'^Reset the state$',
                                    replies.reset),
                                MessageHandler(Filters.text,
                                    replies.default_response),
                       ],
            replies.STAGE_4:   [RegexHandler(u'^Reset the state$',
                                    replies.reset),
                                MessageHandler(Filters.text,
                                    replies.default_response),
                       ],
        },

        fallbacks=[RegexHandler(u'^Reset the state$', replies.done)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    loadData(conv_handler, dp)

    saver = save_thread(conv_handler, dp)
    saver.start()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()