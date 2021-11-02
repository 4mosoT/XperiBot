from xperibot.xperibot import ExpBot
import numpy as np
import logging
import os
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
token = os.environ['TELE_BOT']

# bot = ExpBot(token, allowed_users=['@marco_formoso'])
# bot.start_bot()

with ExpBot(token, allowed_users=['@marco_formoso']) as bot:
    bot.in_experiment("Example1")
    for x in bot.loop(range(100), report_status_every=30):
        bot.add_scalar("loss_train", np.random.rand(), x)
        bot.add_scalar("loss_val", np.random.rand(), x)
        bot.update_loop(x)
    bot.out_experiment()