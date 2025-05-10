import numpy as np
from tensorflow.keras import datasets, utils, layers, models
from matplotlib import pyplot as plt

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# Load the MNIST dataset, split into training and test sets
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

# Normalize the pixel values to the [0, 1] range (originally 0-255)
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Ensure the images have a shape of (28, 28, 1) by adding an extra dimension for "channels"
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# Display information about the training set
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# Display the first 9 images in the training set to verify the data
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))
plt.show()

# Convert class vectors to binary class matrices
y_train = utils.to_categorical(y_train, num_classes)
y_test = utils.to_categorical(y_test, num_classes)

# Define a simple Convolutional Neural Network (CNN)
model = models.Sequential([
    layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

model.summary()

batch_size = 128
epochs = 1  # Increase this to 5–10 for higher accuracy

# Compile the model with loss function, optimizer, and metrics
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model to the training data, with a validation split
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Evaluate the model on the test set
score = model.evaluate(x_test, y_test, verbose=0)

print("Test loss:", score[0])
print("Test accuracy:", score[1])

