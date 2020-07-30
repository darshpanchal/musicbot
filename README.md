# musicbot
Takes song name from telegram bot and plays it on device.

It uses telegram bot python api for getting text from bot and uses youtube search under the hood to get link of playback and plays it on VLC.

Dependencies: (Install using pip)
- youtube-search
- youtube_dl
- telegram bot python api
- pafy
- VLC python wrappers

Paste your API key from botfather in file and then use.

It has 2 modes, Audio and Audio/video,
Specify mode in your message using 'A' for audio or 'V' for audio/video.
eg message for audio: Adespacito by luis fonsi
eg message for video: Vdespacito by luis fonsi

other commands are:
- Vol (to adjust volume, use it with number between 0 to 100, like Vol100 gives full volume)
- Stop (stops existing playback)
