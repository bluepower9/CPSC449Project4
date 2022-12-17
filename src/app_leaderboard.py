from venv import create
from quart_schema import QuartSchema
from quart import Quart, g, request
from api.leaderboard.leaderboard import app_leaderboard
import toml
import logging
import asyncio
import os
import socket
from api.util.util import register_webhook
import httpx

app = Quart(__name__)
QuartSchema(app)

app.logger.setLevel(logging.INFO)

app.register_blueprint(app_leaderboard)
#app.register_blueprint(app_users)

#config app here
app.config.from_file(f'./config/config.toml', toml.load)

callback = socket.getfqdn('http://' + 'localhost'+ ':' + os.environ['PORT'] + '/leaderboard/update')

asyncio.run(register_webhook(app.config['WEBHOOK']['URL'], callback))


if __name__ == '__main__':
    
    app.run(debug=True)