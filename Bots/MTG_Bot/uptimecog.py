from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()
  

status = cycle(['with Python','MTG: Card Bot'])


@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=nextcord.Game(next(status)))
