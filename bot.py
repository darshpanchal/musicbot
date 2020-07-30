import pafy
import vlc
import json
from youtube_search import YoutubeSearch
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Paste your Api key of bot inside inverted comma.
apiKey = ""


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

Instance = vlc.Instance()
player = Instance.media_player_new()

def start(update, context):
    update.message.reply_text('Hi!! Tell me what you wanna play!!')

def echo(update, context):

    if (str(update.message.text).lower() == 'stop'):
        player.stop()

    elif (str(update.message.text[0]).lower() == 'a'):
        print('msg is: ' + str(update.message.text[1:]))
        results = YoutubeSearch(str(update.message.text[1:]), max_results=3).to_json()
        jresults = json.loads(results)
        jlink = jresults['videos'][0]['url_suffix']
        url = "https://www.youtube.com" + str(jlink)
        playsong(url, 'a')

    elif (str(update.message.text[0]).lower() == 'v'):
        if (str(update.message.text[0:3]).lower() == 'vol'):
            player.audio_set_volume(int(update.message.text[3:]))

        else:
            print(str(update.message.text[1:]))
            msg11 = str(update.message.text[1:])
            player.set_fullscreen(True)
            results = YoutubeSearch(msg11, max_results=5).to_json()
            jresults = json.loads(results)
            jlink = jresults['videos'][0]['url_suffix']
            url = "https://www.youtube.com" + str(jlink)
            playsong(url, 'v')

def error(update, context):
    logger.warning('"%s" threw error "%s"', update, context.error)


def playsong(url, avtype):
    player.pause()
    video = pafy.new(url)
    if (avtype == 'v'):
        bestvideo = video.getbest()
        streams = video.streams 
        for i in streams: 
            print(i) 
        besturl = bestvideo.url

    elif (avtype == 'a'):
        bestaudio = video.getbestaudio()
        besturl = bestaudio.url

    Media = Instance.media_new(besturl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()


def main():
    updater = Updater(apiKey, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()