import logging
import telegram
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Updater
from telegram.ext.filters import TextFilter


import transformers
from transformers import GPT2Tokenizer, GPT2LMHeadModel


#Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('name')


#Load pre-trained model tokenizer and model

tokenizer = GPT2Tokenizer.frompretrained("gpt2")
model = GPT2LMHeadModel.frompretrained("gpt2")


def answerquestion(question):
    # Encode the input sequence
    
    inputids = tokenizer.encode(question, return_tensors="pt")
    # Generate a response to the input
    response = model.generate('input_ids')

    # Decode the response to text
    response_text = tokenizer.decode(response[0], skip_special_tokens=True)
    return response_text


def start(bot, update):
    update.message.reply_text(
        "Hi there! I am Jarvis, a language model created by OpenAI. I can answer almost any question. What would you like to ask?")


def askquestion(bot, update):
    question = update.message.text
    response = answerquestion(question)
    update.message.reply_text(response)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    bot = Bot(token="yourtokenhere")
    updater = Updater(bot=bot)


dp = updater.dispatcher

# Add handlers
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(TextFilter(), ask_question))
dp.add_error
