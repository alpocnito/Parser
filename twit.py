from time import sleep
import tweepy
from tweepy import Stream
import json
import requests
from tweepy import OAuthHandler
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
def init():
    global lmtzr, negative_words, positive_words, emotion_map, stream, all_words, bad_words, data
    bad_words = ["http", "@", ",", "!", "#", "-", ".", "$", ":", "the", "a", "`", "?", ";", "/", "\\", "%", "and", "or",
                 "a", "the", "rt", "on", "of", "it", "at", "(", ")", "i", "bitcoin", "to", "in", "is", "for", "about",
                 "like", "this", "out", "mineifiwildout", "you", "next", "their", "btc", "-n…", "'s", "’", "that", "here"
                 "blockchain", "will", "``", "we", "are", "now", "with", "''", "be", "one", "by", "price", "have", "been",
                 "cryptocurrency", "today", "", "s", "if", "day", "crypto", "xvg", "ico", "'m", "&", "…", "n't", "mcm"]
    consumer_key = 'rkUIdEidORMaCGIRB8yrqM2Wi'
    consumer_secret = 'tIrTg4Yv6VnBZsiXkGFeJQpfTQCQcYDTBeXGpvxleiTgjGJY2K'
    access_token = '936879767277547520-HiwscBn80UUHAfXNmhEntm962kNQwyV'
    access_secret = 'fek6M0g9K7jIt5xOcfQBuTdx9Lvy0BzRGiGzG7C6tkTv0'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    myStreamListener = MyStreamListener()
    stream = Stream(auth, myStreamListener)
    lmtzr = WordNetLemmatizer()
    data = list()

    with open('materials/all_words.json') as file:
        new_d = json.load(file)
        all_words = eval(str(new_d))

    negative_file = open("materials/negative-words.txt", 'r')
    positive_file = open("materials/positive-words.txt", 'r')
    senti_words_file = open("materials/output.txt", 'r')

    negative_words = set(eval(negative_file.read()))
    positive_words = set(eval(positive_file.read()))
    emotion_map = dict(eval(senti_words_file.read()))

    negative_file.close()
    positive_file.close()
    senti_words_file.close()

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.followers_count:
            analyze_tweet(status)
def analyze_tweet(tweet):
    global lmtzr, negative_words, positive_words, emotion_map, all_words, bad_words, data
    simpleDict_neg = simpleDict_pos = 0
    emotionMap_pos = emotionMap_neg = 0
    senti = 0
    token = word_tokenize(tweet.text)
    tagging = nltk.pos_tag(token)
    for word in tagging:
        l_word = lmtzr.lemmatize(word[0]).lower()
        if l_word in bad_words or l_word.find("//") != -1 or l_word.find(r"\\") != -1:
            continue
        if l_word[-3:] == "...":
            l_word = l_word[:-3]

        if l_word in negative_words:
            simpleDict_neg += tweet.user.followers_count
        if l_word in positive_words:
            simpleDict_pos += tweet.user.followers_count
        if l_word in emotion_map.keys():
            emotionMap_pos += emotion_map[l_word][0] * tweet.user.followers_count
            emotionMap_neg += emotion_map[l_word][1] * tweet.user.followers_count
        if l_word not in all_words.keys():
            url = "http://www.sentic.net/api/en/concept/" + l_word + "/polarity/intensity"
            try:
                r = str(requests.get(url).content)
            except:
                with open('materials/Fuck.txt', 'a') as file:
                    print(l_word, file=file)
                continue
            if int(r.find('ERROR')) == -1 and int(r.find("400 Bad Request")) == -1:
                r = r[360:r.find("</intensity>")]
                r = r[r.find(">") + 1:]
                r = float(r)
                all_words[l_word] = r
            else:
                all_words[l_word] = 0
        senti += all_words[l_word] * tweet.user.followers_count
        data.append((tweet.created_at, simpleDict_neg, simpleDict_pos, emotionMap_neg, emotionMap_pos, senti))
        print(data)

init()
stream.filter(track=['bitcoin' or 'BTC' or 'Bitcoin' or "btc"], languages=["en"])
