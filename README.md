# Dit is Bouderrie

## installation

Install the requirements with the following command, (preferably in a virtual environment).
```
pip install -r requirements.txt
```

## install ffmpeg
The bot can play sounds over the voice channel, but it needs ffmpeg. Install ffmpeg with `brew` or your prefered package manager, or download it from the official website https://www.ffmpeg.org/download.html.
## token & environment variables
The discord bot initially tries to get the discord bot token from the `token` environment variable, if the token is not present as an environment variable it will look for the first line in the `.token` file and use that as the token.

Rename/copy the .token.example to .token and place the discord bot token on the first line in the file


## Starting the bot
start the bot with the following command, (in the virtual environment).
```
python main.py
```
