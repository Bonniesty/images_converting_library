import tweetAPIexample
import textDetectAndGenerate
import sys
import dbc

def entryLib(youTwitterAccount):
    tweetAPIexample.get_all_tweets(youTwitterAccount)
    textDetectAndGenerate.generateVideo(youTwitterAccount)


if __name__ == '__main__':
    try:
        inputAccount = sys.argv[1]
    except:
        print("Oops! There is no twitter account!")
    else:
        entryLib(inputAccount)

    #database operation
    print("1:search\n")
    print("2:show statistics\n")
    print("3:exit\n")
    while True:
        x = input("please select an operation:\n")
        if int(x) == 1:
            k = input("please enter an keyword:\n")
            dbc.search(k)
        if  int(x)==2:
            dbc.stat()
        if int(x)==3:
            break
