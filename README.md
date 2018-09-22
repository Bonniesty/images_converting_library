# images_converting_library :octocat:

This libaray aims to build a python library which downloads images from a twitter feed, convert them to a video and describe the content of the images in the video. :+1:
Using and needed to be installed:
  - [Tweepy](http://docs.tweepy.org/en/v3.5.0/)  - to get API data response
  - [FFMPEG](https://www.ffmpeg.org/) - to convert images to video
  - [Google Vision API](https://cloud.google.com/vision/) - to label products in the picture


# demo 
Some images of twitter account **SelenaActivity** are downloaded through Tweepy in ```pics``` file.

The final demo video is named as ```outputVedio.mp4``` and the pictures with annotation on it are in  ```labeledPics``` file.



# how to use
There are two APIs as ```tweetAPIexample``` and ```textDectectAndGenerate```. You can use the first API to download pictures from selected twitter acount, and the second API to add described annotations and generate video. You have to get twitter API credentials to use the first API. If you don't have credentials, submit a issue to get a API credentials for a try. 


* To download images from twitter account, you can fill in the credentials, and run the following code:
```python
python tweetAPIexample.py
```
  Then you can run the second API to generat video. 
```python
python textDetectAndGenerate.py
```
* If you would like to use images from your own sources, just add your pictures in the ```pics``` file, then simply run:
```python
python textDetectAndGenerate.py
```
  Then, pictures with annotations will be generated in ```labeledPics``` file and a video will be generated as ```outputVedio.mp4```
  
* To get a faster start, run the folling code. You only need to fill the Twitter account, and this library will generate the video for you.  
```python
python libraryEntry.py youTwitterAccount(eg. @SelenaActivity)
```
 


