from telegram import ReplyKeyboardMarkup

meet_keyboard = [['Кто ты?']]
meet_markup = ReplyKeyboardMarkup(meet_keyboard, one_time_keyboard=True)

reply_keyboard = [['Какова моя миссия?', 'Как мне подготовиться к приключению?'],
                  ['Где и когда искать мудреца?', "Прости, кто ты еще раз?"],
                  ['Я все понял, прощай.']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

start_keyboard = [['Go to the Stage 1']]
start_markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=True)

reset_keyboard = [['Reset the state']]
reset_markup = ReplyKeyboardMarkup(reset_keyboard, one_time_keyboard=True)

stage_1_keyboard = [['Go to the Stage 2.1','Go to the Stage 2.2'], ['Reset the state']]
stage_1_markup = ReplyKeyboardMarkup(stage_1_keyboard, one_time_keyboard=True)

stage_2_1_keyboard = [['Go to the Stage 3.1','Go to the Stage 3.2'], ['Reset the state']]
stage_2_1_markup = ReplyKeyboardMarkup(stage_2_1_keyboard, one_time_keyboard=True)

stage_2_2_keyboard = [['Go to the Stage 3.3'], ['Reset the state']]
stage_2_2_markup = ReplyKeyboardMarkup(stage_2_2_keyboard, one_time_keyboard=True)

stage_3_1_keyboard = [['Go to the Stage 1'], ['Reset the state']]
stage_3_1_markup = ReplyKeyboardMarkup(stage_3_1_keyboard, one_time_keyboard=True)

stage_3_2_keyboard = [['Go to the Stage 4'], ['Reset the state']]
stage_3_2_markup = ReplyKeyboardMarkup(stage_3_2_keyboard, one_time_keyboard=True)