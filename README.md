# Fake News Identification

The goal is to build a Machine Learning model that can classify a given news headline as real or fake. To achieve the task, we will be using a few popular news datasets as well as scraping data from sites for fake news(if the need arises). The first step to solving the problem is the creation of a dataset containing headlines and their respective class labels
## Dataset(s)

The dataset used is the [Name of the Dataset](Download link) from (source of download e.g Kaggle). If the task is a classification task, then you must specify the number of classes and give a 1 line description of each class as follows(example of Iris Dataset). 

The 2 class labels are:
<br>

**1. Real:** The news headline provided is real
<br>

**2. Fake:** The news headline provided is fake


## Model(s) Used

This needs to be a description of the model used and a brief overview of how it works in theory (e.g taken of a CNN Model): 

The network architecture used was a basic CNN model, with Max Pooling and ReLU Activation functions. Input images are resized to an optimal size and then fed into the **Convolutional layer**. These images are converted to their pixel values, which can be imagined as a three-dimensional matrix for the purpose of visualization. The **Convolutional layer** has a kernel. This kernel is generally a small matrix of specified kernel size mxnx3 (3 for RGB images). 
<br>

**Rectified Linear Unit (ReLU)** is the activation layer used in CNNs.The activation function is applied to increase non-linearity in the CNN. Images are made of different objects that are not linear to each other.


**Max Pooling:** A limitation of the feature map output of Convolutional Layers is that they record the precise position of features in the input. This means that small movements in the position of the feature in the input image will result in a different feature map. This can happen with re-cropping, rotation, shifting, and other minor changes to the input image. A common approach to addressing this problem from signal processing is called down sampling. This is where a lower resolution version of an input signal is created that still contains the large or important structural elements, without the fine detail that may not be as useful to the task.

## Future Work
Good ideas or strategies that you were not able to implement which you think can help  improve performance.


## Running The Application
As of now we do not have an application but an example flask application 

it is based on the modular structure to serve as an example of the same..

It can be launched by first init the VirtualEnv and then running the run.py in the home folder

The App folder contains all the information regarding the server