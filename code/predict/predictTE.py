import sys

#import PIL
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import load_model
##https://stackoverflow.com/questions/1707780/call-python-function-from-matlab
from keras_preprocessing.image import ImageDataGenerator

def predictTE(modelName = '../models/model_te.h5'):
    model = load_model(modeName)
    test_data = []
    for fname in sorted(os.listdir('testing')):
        if fname == '.DS_Store' : continue
        subject_data_path = os.path.join('testing' , fname)
        if not os.path.isfile(subject_data_path): continue
        test_data.append(fname)
    df = pd.DataFrame(test_data, columns = ['fnames'])
    df['fnames'] = df['fnames'].astype(str)
    test_datagen = ImageDataGenerator(rescale=1./255.)
    test_g=test_datagen.flow_from_dataframe(
                                       dataframe= df,
                                       directory="./testing",
                                       x_col="fnames",
                                       batch_size=1,
                                       seed=42,
                                       shuffle=False,
                                       class_mode=None,
                                       target_size=(224,224))
    STEP_SIZE_TEST=test_g.n//test_g.batch_size
    pred = model.predict_generator(test_g,
                                   steps=STEP_SIZE_TEST,
                                   verbose=1)
    pred_bool = (pred >0.5)
    predictions=[]
    labels = {0: '0',
              1: '1',
              2: '2',
              3: '3',
              4: '4',
              5: '5',
              6: '6',
              7: '7',
              8: '8',
              9: '9'}
    for row in pred_bool:
        l=[]
        for index,cls in enumerate(row):
            if cls:
                l.append(labels[index])
        predictions.append(",".join(l))
    result = float (predictions[0] ) 
    return result





if __name__ == '__main__':
    x = str(sys.argv[1])
    sys.stdout.write(str(predictTE(x)))