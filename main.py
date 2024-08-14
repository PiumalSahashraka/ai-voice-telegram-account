from telethon import TelegramClient, events
import os
from config import Config
import voice_to_text



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
        text = voice_to_text.translate(filepath)
        await client.send_message(event.chat_id, text)


async def main():
    # Create a new instance of the client
    await client.start(phone = Config.PHONE_NUMBER)
    print("listening for new voice messages...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
 