import disnake
import requests
from os import environ
from disnake.ext import commands
import flask

bot = commands.InteractionBot()
token = environ["token"]

@bot.slash_command(description="Sends messages anonymously")
async def send(inter, message):
    if len(message) < 2001:
     await inter.channel.send(message)


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


def run():
  app.run(host='0.0.0.0', debug=True)


def main():
  while True:
    requests.get("https://anon-bot-dev-fhqj.1.us-1.fl0.io")
    sleep(5)

if __name__ == '__main__':
  Process(target=run).start()
  Process(target=main).start()

bot.run(token)
