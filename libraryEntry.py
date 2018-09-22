import tweetAPIexample
import textDetectAndGenerate
import sys

def entryLib(youTwitterAccount):
    tweetAPIexample.get_all_tweets(youTwitterAccount)
    textDetectAndGenerate.generateVideo()

if __name__ == '__main__':
    entryLib(sys.argv[1])
