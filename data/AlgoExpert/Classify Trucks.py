import tensorflow as tf

def classify_trucks():
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Conv2D(16, 3, activation="relu", input_shape=(224, 224, 3), kernel_initializer="he_normal"),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Conv2D(32, 3, activation="relu", kernel_initializer="he_normal"),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Conv2D(64, 3, activation="relu", kernel_initializer="he_normal"),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(20, activation="relu", kernel_initializer="he_normal"),
            tf.keras.layers.Dense(1, activation="sigmoid", kernel_initializer="glorot_normal"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
        loss=tf.keras.losses.BinaryCrossentropy(),
        metrics=['binary_accuracy']
    )
    return model
