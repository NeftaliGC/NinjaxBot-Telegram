#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Bot simple para responder a los mensajes de Telegram.
Primero, se definen algunas funciones de controlador. Luego, esas funciones se pasan a
el Despachador y registrados en sus respectivos lugares.
Luego, el bot se inicia y se ejecuta hasta que presionamos Ctrl-C en la línea de comando.
Uso:
Ejemplo básico de Echobot, repite mensajes.
Presione Ctrl-C en la línea de comando o envíe una señal al proceso para detener el
Bot.
"""

import logging
from typing import ContextManager

from telegram import Update, ForceReply, update
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Envíe un mensaje cuando se emita el comando /start."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hola, soy NinjaxBot {user.mention_markdown_v2()}\!' + '\nUsa /help para conocer mis funciones',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Envie un mensaje cuando el comando /help sea usado."""
    update.message.reply_text('Esto es lo que puedo hacer: \n /start \n /help \n /qr')
    


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1617542737:AAH7z4NNv8SPQyj5tV1ill6bXhcPNagOa_Y")

    # Consiga que el despachador registre a los mesajes
    dispatcher = updater.dispatcher

    # en diferentes comandos - responde en Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Si un mensaje es Hola respode Hola
    dispatcher.add_handler(MessageHandler(Filters.text("Hola") & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.text("hola") & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.text("Ola") & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.text("ola") & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()