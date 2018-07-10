
# Importing libraries
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator

# Initialising the CNN
classifier = Sequential()

# 1st Convolution Layer
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))# Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# 2nd Convolution Layer
# Uncomment the below layer if you want a deeper convolutional layer
# classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
# classifier.add(MaxPooling2D(pool_size = (2, 2)))

# 3rd Convolution Layer
# Uncomment the below layer if you want a deeper convolutional layer
# classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
# classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Flattening
classifier.add(Flatten())

# Output
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

# Compiling the classifier
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting images
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

# Label - 1
training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')
# Label - 2
test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

# Debugging truncated image error - Uncomment if you experience a truncated image error
# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True

# Fitting the data and training the neural network
classifier.fit_generator(training_set,
                         samples_per_epoch = 614, #Modify this value to number of training samples returned from Label - 1
                         nb_epoch = 25,
                         validation_data = test_set,
                         nb_val_samples = 100) #Modify this value to number of test samples returned from Label - 2