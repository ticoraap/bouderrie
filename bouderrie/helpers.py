
import os
from gtts import gTTS
import urllib3
import json


class HelperMethods:
    def get_token():
        try:
            return os.environ['discord_token']
        except KeyError:
            try:
                with open('.token', 'r') as f:
                    return f.readline().strip()
            except Exception as e:
                print(e)

    def text_to_soundfile(self, text, lang='nl'):
        folder = './gtts-sounds/'
        filename = str(hash(text)) + '.wav'
        file = folder + filename

        if os.path.isfile(file):
            return file

        tts = gTTS(text, lang=lang)
        tts.save(file)
        return file

    async def getmop(self):
        http = urllib3.PoolManager()
        req = http.request(
            'GET',
            'https://www.moppenbot.nl/api/random/?nsfw=true',
            headers={
                'Content-Type': 'application/json',
            }
        )
        jsondata = json.loads(req.data.decode('utf-8'))
        return jsondata.get('joke').get('joke')
