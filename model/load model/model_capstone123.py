import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Read dataset
df = pd.read_csv('dataset_capstone123.csv', delimiter=";")

# Kamus untuk penerjemahan teks ke angka
translation_table = {'important': 0, 'not important': 1}
translation_table2 = {'urgent': 0, 'not urgent': 1}
translation_table3 = {'rendah': 0, 'sedang': 1, 'tinggi': 2}

# Menggunakan metode map untuk penerjemahan
df['Tingkat Important'] = df['Tingkat Important'].replace(translation_table)
df['Tingkat Urgent'] = df['Tingkat Urgent'].replace(translation_table2)
df['Kompleksitas'] = df['Kompleksitas'].replace(translation_table3)

feature =  df.drop(['Prioritas'],axis=1)
target = df['Prioritas'].values

# Encode target data using LabelEncoder
label_encoder = LabelEncoder()
target_data_encoded = label_encoder.fit_transform(target)

# Perform one-hot encoding on the encoded target data
target_data_encoded_onehot = tf.keras.utils.to_categorical(target_data_encoded, num_classes=4)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(feature, target_data_encoded_onehot, test_size=0.3, random_state=42)

# Build the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(16, input_dim=4, activation='relu'))
model.add(tf.keras.layers.Dense(8, activation='relu'))
model.add(tf.keras.layers.Dense(4, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=8, verbose=1)

# Predict on the test data
predictions = model.predict(X_test)
predicted_labels = np.argmax(predictions, axis=1)
predicted_y = np.argmax(y_test, axis=1)

# Decode the predicted labels
predicted_labels_decoded = label_encoder.inverse_transform(predicted_labels)
y_target = label_encoder.inverse_transform(predicted_y)

# Generate classification report
report = classification_report(y_target, predicted_labels_decoded)
print("Classification Report:")
print(report)

# Calculate accuracy
accuracy = accuracy_score(y_target, predicted_labels_decoded)
print("Accuracy: {:.2f}%".format(accuracy * 100))

# Generate classification report
report = classification_report(y_target, predicted_labels_decoded)
print("Classification Report:")
print(report)

# Compute confusion matrix
cm = confusion_matrix(y_target, predicted_labels_decoded)

model.save("model.h5")
loaded_model = tf.keras.models.load_model("model.h5")

predicted_labels = np.argmax(predictions, axis=1)

# Decode the predicted labels
predicted_labels_decoded = label_encoder.inverse_transform(predicted_labels)

# Create Flask app
app = Flask(__name__)

# Run the Flask app
if __name__ == '__main__':
    app.run()