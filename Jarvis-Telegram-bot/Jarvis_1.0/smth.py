import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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


def start(update, context):
    update.message.reply_text(
        "Hello, I'm a Telegram AI bot. My name is Jarvis and I was developed by Asado. How can I help you today?")


def chat(update, context):
    question = update.message.text
    answer = generate_answer(question, model, tokenizer)
    update.message.reply_text(answer)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
