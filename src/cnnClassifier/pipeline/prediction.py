import numpy as np
from cnnClassifier.constants import CONFIG_FILE_PATH
from cnnClassifier.utils.common import read_yaml
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self, image):
        self.image = image
        self.config = read_yaml(CONFIG_FILE_PATH)


    
    def predict(self):
        # load model
        model = load_model(os.path.join(self.config.trained_model.trained_model_path))

        img_array = np.array(self.image.resize((224, 224))) / 255.0
        test_image = np.expand_dims(img_array, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]