import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

from random import *

API_TOKEN = '549381528:AAEB8ZJ9MPtTmPf2V5ok1Mk6GAd3ACVwZgk'
WEBHOOK_URL = 'https://45ee1cb6.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'init',
        'goal_L',
        'goal_H',
        'goal_C',
        'goal_E',
        'goal_LH',
        'goal_LC',
        'goal_LE',
        'goal_HC',
        'goal_HE',
        'goal_CE',
        'goal_LHC',
        'goal_LHE',
        'goal_LCE',
        'goal_HCE',
        'goal_LHCE'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'goal_L',
            'conditions': 'goto_L'
        },
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'goal_H',
            'conditions': 'goto_H'
        },
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'goal_C',
            'conditions': 'goto_C'
        },
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'goal_E',
            'conditions': 'goto_E'
        },
        {
            'trigger': 'advance',
            'source': 'goal_L',
            'dest': 'goal_LH',
            'conditions': 'goto_LH'
        },
        {
            'trigger': 'advance',
            'source': 'goal_L',
            'dest': 'goal_LC',
            'conditions': 'goto_LC'
        },
        {
            'trigger': 'advance',
            'source': 'goal_L',
            'dest': 'goal_LE',
            'conditions': 'goto_LE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_H',
            'dest': 'goal_LH',
            'conditions': 'goto_LH'
        },
        {
            'trigger': 'advance',
            'source': 'goal_H',
            'dest': 'goal_HC',
            'conditions': 'goto_HC'
        },
        {
            'trigger': 'advance',
            'source': 'goal_H',
            'dest': 'goal_HE',
            'conditions': 'goto_HE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_C',
            'dest': 'goal_LC',
            'conditions': 'goto_LC'
        },
        {
            'trigger': 'advance',
            'source': 'goal_C',
            'dest': 'goal_HC',
            'conditions': 'goto_HC'
        },
        {
            'trigger': 'advance',
            'source': 'goal_C',
            'dest': 'goal_CE',
            'conditions': 'goto_CE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_E',
            'dest': 'goal_LE',
            'conditions': 'goto_LE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_E',
            'dest': 'goal_HE',
            'conditions': 'goto_HE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_E',
            'dest': 'goal_CE',
            'conditions': 'goto_CE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LH',
            'dest': 'goal_LHC',
            'conditions': 'goto_LHC'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LH',
            'dest': 'goal_LHE',
            'conditions': 'goto_LHE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LC',
            'dest': 'goal_LHC',
            'conditions': 'goto_LHC'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LC',
            'dest': 'goal_LCE',
            'conditions': 'goto_LCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LE',
            'dest': 'goal_LHE',
            'conditions': 'goto_LHE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LE',
            'dest': 'goal_LCE',
            'conditions': 'goto_LCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_HC',
            'dest': 'goal_LHC',
            'conditions': 'goto_LHC'
        },
        {
            'trigger': 'advance',
            'source': 'goal_HC',
            'dest': 'goal_HCE',
            'conditions': 'goto_HCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_HE',
            'dest': 'goal_LHE',
            'conditions': 'goto_LHE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_HE',
            'dest': 'goal_HCE',
            'conditions': 'goto_HCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_CE',
            'dest': 'goal_LCE',
            'conditions': 'goto_LCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_CE',
            'dest': 'goal_HCE',
            'conditions': 'goto_HCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LHC',
            'dest': 'goal_LHCE',
            'conditions': 'goto_LHCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LHE',
            'dest': 'goal_LHCE',
            'conditions': 'goto_LHCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_LCE',
            'dest': 'goal_LHCE',
            'conditions': 'goto_LHCE'
        },
        {
            'trigger': 'advance',
            'source': 'goal_HCE',
            'dest': 'goal_LHCE',
            'conditions': 'goto_LHCE'
        },
		{
            'trigger': 'advance',
            'source': ['goal_L',
						'goal_H',
						'goal_C',
						'goal_E',
						'goal_LH',
						'goal_LC',
						'goal_LE',
						'goal_HC',
						'goal_HE',
						'goal_CE',
						'goal_LHC',
						'goal_LHE',
						'goal_LCE',
						'goal_HCE',
						'goal_LHCE'
						],
            'dest': 'init',
            'conditions': 'goto_init'
        }
        #{
        #    'trigger': 'go_back',
        #    'source': [
        #        'state1',
        #        'state2'
        #    ],
        #    'dest': 'user'
        #}
        #{
        #    'trigger': 'advance',
        #    'source':['goal_L','goal_H','goal_C'],
        #    'dest': 'init',
        #    'conditions': 'goto_init'
        #}
    ],
    initial='init',
    auto_transitions=False,
    show_conditions=True,
    ignore_invalid_triggers = True
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run(port=8443)
