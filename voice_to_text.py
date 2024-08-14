from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
import json
from config import Config

deepgram = DeepgramClient(Config.DG_API_KEY)

def translate(audio_url: str):

    with open(audio_url, "rb") as file:
            buffer_data = file.read()

    payload: FileSource = {
        "buffer": buffer_data,
    }

    options = PrerecordedOptions(
        model="nova-2",
        smart_format=True,
    )

    response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
    result = response.to_json(indent=4)
    result = json.loads(result)
    try:
        text_list = result['results']['channels'][0]['alternatives'][0]['words']
        text = " ".join([word['word'] for word in text_list])
    except KeyError:
         return "Sorry, I couldn't understand that."
    except TypeError:
         return "Sorry, I couldn't understand that."
    return text