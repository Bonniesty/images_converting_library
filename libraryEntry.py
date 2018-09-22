import tweetAPIexample
import textDetectAndGenerate
import sys

def entryLib(youTwitterAccount):
    tweetAPIexample.get_all_tweets(youTwitterAccount)
    textDetectAndGenerate.generateVideo()

if __name__ == '__main__':
    try:
        inputAccount = sys.argv[1]
    except:
        print("Oops! There is no twitter account!")
    else:
        entryLib(inputAccount)

    
