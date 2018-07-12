# Reddit - NSFW
Detection of potential nudity in images using Convolutional Neural Networks in Python with Keras

## 0. Preface
'NSFW' stands for 'Not Safe for Work', synonymous to images containing nudity, gore, violence, drugs etc. However, for the purpose of this article, 'NSFW' refers solely to images containing nudity.
'SFW' refers to images or objects which are 'Safe for Work', in other words, which do not contain any of the above stated subjects whatsoever.

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

###### N.B. : If you plan to test run this program, then after extracting the images using RipMe , make sure to filter out images from videos and remove the empty .gitkeep file I have placed as a placeholder in each of the folders just to upload the basic structure to GitHub.

## 2. Running the Convolutional Neural Network

If you would personally like to run the program, I suggest installing [Anaconda](https://www.anaconda.com/download/) and installing Theano, Tensorflow and Keras using the following commands in the Anaconda Prompt

```
conda create -n py35 python=3.5 anaconda

activate py35

conda install theano
conda install tensorflow
conda install keras
```

After that, open Spyder in the environment we set up as py35 using the following commands in the Anaconda Prompt
```
activate py35

spyder --show console
```

Open the *cnn.py* file inside Spyder and set the working directory as the parent directory of 'dataset' folder.
Adjust the parameters according to your wish and run *cnn.py* and wait for the training to complete.

###### N.B. If you are not using Anaconda for your python environment I suggest creating a virtualenv before installing Theano, Keras and Tensorflow to prevent corrupting your entire python installation if an error occurs.

## 3. Analysing the results
The results of the training can be found in the file named *training_transcript* in the home directory of this repository. Error analysis and related data were taken from the above mentioned file.

Values stated below are averages which were taken over the last 5 epochs of training.

Set | Accuracy
--- | -------- 
Training Data |  90.1 % 
Test Data | 80.2 % 


