# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""WikiPedia.ORG
Syntax: .wikipedia Query"""
import wikipedia

from telegram import ChatAction
import html
import re
import json
from datetime import datetime
from typing import Optional, List
import time
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from tg_bot import dispatcher
from tg_bot.__main__ import STATS
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.extraction import extract_user
  @run_async
  def wikisearch(bot: Bot, update: Update, args):
    message = update.effective_message
  text = message.reply_to_message.text
    results = wikipedia.search(text)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
         message.reply_to_message.reply_text(result)

    __help__ = """
 - /wse:{word} Type the word or expression you want to search use. like /wse telegram Word: Telegram Definition: A once-popular system of telecommunications, in which the sender would contact the telegram service and speak their [message] over the [phone]. The person taking the message would then send it, via a teletype machine, to a telegram office near the receiver's [address]. The message would then be hand-delivered to the addressee. From 1851 until it discontinued the service in 2006, Western Union was the best-known telegram service in the world.
"""
    wikisearch_handler = DisableAbleCommandHandler("wse", wikisearch)
    dispatcher.add_handler(wikisearch)
