import logging
from telegram import Bot
from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import Updater
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace with your own token
TOKEN = "6199626067:AAH0H-CHS5XXbY68BMmWjs4VkF-miROzfMo"

# Load the pre-trained GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define AI model


def generate_answer(question, model, tokenizer):
    input_ids = tokenizer.encode(question, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(input_ids)
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer

# Define Telegram bot functions


def start(bot: Bot, update: Update):
    update.message.reply_text(
        "Hello, I'm a Telegram AI bot. How can I help you today?")


def chat(bot: Bot, update: Update):
    question = update.message.text
    answer = generate_answer(question, model, tokenizer)
    update.message.reply_text(answer)


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(None, chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
