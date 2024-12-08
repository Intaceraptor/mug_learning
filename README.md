# Introduction
This is one of my first personal project with regards to studying machine learning methods. However, as it wasn't very well documented at the time due to limited knowledge, I am essentially coming back to clean it up a little, fill in some of the gaps, and document my learnings and results properly. I am pretty proud of this project at the time and to be honest even now, so I hope you enjoy this little thing I worked on. 

# About the dataset
The dataset used for this project was obtained from multiple different sources (which is generally bad practice I know, but I wanted more data to work with at the time.). The datasets were split before hand, rather than within the main notebook, into three different folders: mug_test_orig, mug_train_orig, and non_mug_train_orig. (orig here standing for original, non_mug_test doesnt't exist because non_mug_train was a much larger dataset than mug_train, hence the latter of non_mug_train was used as the non_mug_test set) 

# About the files
There are multiple files included in this repository besides the folders containing the testing/training data. Including:
1. augment_image.py
This was used as a little test to augment the images of mugs to create a larger dataset. It did not go very well however and the model was not able to learn much from the extra data. I have left it there regardless as it might be useful for when I need a template for writing a data augmentation algorithm, but for now it does not serve much purpose in this project.

2. mug_cleaning.ipynb
This is a Jupyter notebook containing the code I used to clean the dataset. specifially it does multiple things. Taking a folder containing images, it resizes and normalizes the images, and creates a new folder containing these images. This process is repeated three times for the three different datasets mentioned above. 

3. mug_Training_utils.py
This python script contains multiple helper functions used in the main notebook. This was pretty useful as it prevented having to run these functions everytime I ran the notebook, and simply makes the notebook shorter hence easier to follow. 

4. mug_training.ipynb
This Jupyter notebook contains the main parts of the code. I started by creating a fairly basic model containing a couple stacked dense layers with a sigmoid activated output layer, which gave an approximately 70% accuracy on the test set. I then constructed a convolutional neural network containing two blocks of convolution layers followed by max pooling layers, followed by a dense layer, a dropout layer, and a dense output layer. This model was able to perform much better than the previous one, achieving a 94% accuracy on the test set. 

# Conclusion:
I went go into too much about this project as it was just a little for fun thing I did as a start. I did however, learn some basics of constructing datasets, as well as constructing convolutional neural networks and using them for image classification. Overall this should be pretty easy to follow, and I stuck to using the most basic methods of the tensorflow library. 