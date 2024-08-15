from telethon import TelegramClient, events
import os
from config import Config
import generator.voice_to_text as voice_to_text
import generator.response_generator

download_path = 'downloads'
client = TelegramClient(Config.PHONE_NUMBER, Config.API_ID, Config.API_HASH)

@client.on(events.NewMessage)
async def handle_message(event: events.NewMessage.Event):
    if event.message.voice and event.is_private:
        print("Received a voice message!")
        file = event.message.voice

         # Define a filename
        filename = f"voice_message_{event.message.id}.ogg"
        filepath = os.path.join(download_path, filename)
        
        # Download the file
        await event.message.download_media(file=filepath)
        text = voice_to_text.translate(filepath, event.message.sender.first_name)
        await client.send_message(event.chat_id, text)


async def main():
    await client.start(phone = Config.PHONE_NUMBER)
    print("listening for new voice messages...")
    await client.run_until_disconnected()

with client:
    try:
        task = client.loop.run_until_complete(main()) 
    except KeyboardInterrupt:
        task.cancel()
        print("Exiting...") 
 