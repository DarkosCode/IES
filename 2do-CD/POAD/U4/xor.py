import numpy
import tensorflow as tf
tf.keras.utils.set_random_seed(73)
x = numpy.array([[0, 0],[0, 1],[1, 0],[1, 1]], dtype="float32")
y = numpy.array([[0], [1], [1], [0]], dtype="float32")
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)), # entrada
    # activaciones: linear, tanh, sigmoid, relu, softmax
    tf.keras.layers.Dense(2, "tanh"), # oculta
    tf.keras.layers.Dense(2, "tanh"), # oculta
    tf.keras.layers.Dense(1, "sigmoid") #salida
])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.03),
              loss="binary_crossentropy",
              metrics=["accuracy"])
model.fit(x, y, epochs=5000, verbose=0)
probabilidades = model.predict(x, verbose=0)
predicciones = (probabilidades >= 0.5).astype(int)
for entrada, probabilidad, prediccion, salida in zip(x, probabilidades, predicciones, y):
    print(f"{entrada.astype(int)} -> prob {probabilidad[0]:.3f} pred {prediccion[0]} -> {salida.astype(int)}")
