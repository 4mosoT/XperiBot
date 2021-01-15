from experibot.experibot import ExpBot
import numpy as np
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
token = os.environ['TELE_BOT']

with ExpBot(token, allowed_users=['@marco_formoso']) as b:
    for x in range(100):
        b.add_scalar("loss_train", np.random.rand(), x)
        b.add_scalar("loss_val", np.random.rand(), x)
