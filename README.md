# Reddit - NSFW
Detection of potential nudity in images using Convolutional Neural Networks in Python with Keras

## 0. Preface
'NSFW' stands for 'Not Safe for Work', synonymous to images containing nudity, gore, violence, drugs etc. However, for the purpose of this article, 'NSFW' refers solely to images containing nudity.
'SFW' refers to images or objects which are 'Safe for Work', in other words, which do not contain any of the above stated negatives whatsoever.

Owing to GitHub's terms of service, I can neither upload the dataset containing nudity nor directly link to any such dataset. However, if you wish to run this model yourself, clone the repository and manually download the dataset as specified below.

## 1. Collecting the images
Reddit was selected as the main source of the images used for this project as it contained the largest database and was easily extractable.

Primary thoughts on extracting the data included using a web scraping script in Python using Scrapy but I found a much easier way to do so thanks to [RipMeApp](https://github.com/ripmeapp/ripme) (Credits to the creator). Using ripme, I extracted data from close to 5 subreddits each for the NSFW and SFW categories. (SFW ones were /r/Art, /r/Dogs, /r/EarthPorn, /r/pics, /r/cats). 

#### Summary of the number of images collected

Category | Training Set | Test Set
-------- | ------------ | ---------
NSFW | 300 | 50
SFW | 300 | 50
Total | 600 | 100

###### N.B. : If you plan to test run this script, then after extracting the images using RipMe , make sure to filter out images from videos and remove the empty .gitkeep file I have placed as a placeholder in each of the folders just to upload the basic structure to GitHub.

