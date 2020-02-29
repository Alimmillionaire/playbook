import wikipedia as wiki
import requests
import argparse
from colored import fg, attr
from gtts import gTTS

G = fg("grey_70")
Y = fg("yellow")
R = fg("red")
E = attr("reset")


parser = argparse.ArgumentParser(prog="", description=None)
parser.add_argument("words", nargs="+", help="Words to search")
parser.add_argument("-l", "--language", help="your preferred language Ex: pt, fr, ru")
parser.add_argument("-ns", "--sentences", type=int, default=5, help="Number of sentences")
args = parser.parse_args()

word = " ".join(args.words)
language = args.language
no_of_sentences = args.sentences

if language:
    wiki.set_lang(language)

try:
    result = wiki.summary(word, sentences=no_of_sentences)
except wiki.exceptions.PageError:
    print(f"{Y}Language probably not available, please try a diffrerent language!{E}")
except wiki.exceptions.DisambiguationError:
    print(f"{Y}Conflict of word and choice of language.{E}")
except requests.exceptions.ConnectionError:
    print(f"{R}Unable to connect to the internet.{E}")
else:
    print(f"{G}{result}{E}")
    # import reprlib
    # print(reprlib.repr(result))
    # tts = gTTS(result)
    # tts.save("wiki.mp3")

#
