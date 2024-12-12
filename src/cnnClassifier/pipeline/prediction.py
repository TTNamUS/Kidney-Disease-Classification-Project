import numpy as np
from cnnClassifier.constants import CONFIG_FILE_PATH
from cnnClassifier.utils.common import read_yaml
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename
        self.config = read_yaml(CONFIG_FILE_PATH)


    
    def predict(self):
        # load model
        model = load_model(os.path.join(self.config.training.trained_model_path))

        image_name = self.filename
        test_image = image.load_img(image_name, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]