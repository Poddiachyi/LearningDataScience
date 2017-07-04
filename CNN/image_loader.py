from keras.preprocessing.image import array_to_img, img_to_array, load_img
import numpy as np
import os
from zipfile import ZipFile

def load(zipfilename, ratio=4, task='classification'):

    image_width = 640
    image_height = 480
    channels = 3

    image_width = int(image_width / ratio)
    image_height = int(image_height / ratio)

    with ZipFile(zipfilename) as archive:
        X = np.ndarray(shape=(len(archive.infolist()), image_height,
                        image_width, channels), dtype=np.float32)
        y = []
        i = 0
        for entry in archive.infolist():
            with archive.open(entry) as file:
                index = file.name.find("_")
                y.append(int(file.name[:index]))
                img = load_img(file)
                img.thumbnail((image_width, image_height))
                x = img_to_array(img)
                x = (x - 128.0) / 128.0
                X[i] = x
                i += 1
                if i % 250 == 0:
                    print("{} images to array".format(i))

        if task == 'classification':
            print('vectorization')
            y = vectorize_labels(y)

        print('Loaded!')
        return X, np.array(y)

def vectorize_labels(labels):
    classes = sorted(list(set(labels)))
    n_classes = len(classes)
    results = []
    for label in labels:
        result = np.zeros(n_classes)
        result[classes.index(label)] = 1
        results.append(result)
    return results
