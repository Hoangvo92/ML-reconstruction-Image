import sys

#import PIL
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import load_model
##https://stackoverflow.com/questions/1707780/call-python-function-from-matlab
from keras_preprocessing.image import ImageDataGenerator

def predictT2(modelName = '../models/model_t2.h5', labelText="../labels/T2_labels.txt"):
    model = load_model(modelName)
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
    labels = {}
    file1 = open(labelText, 'r')
    Lines = file1.readlines()
 
    count = 0
    # Strips the newline character
    for line in Lines:
        labels[count] = line.strip()
        count += 1
    
    for row in pred_bool:
        l=[]
        for index,cls in enumerate(row):
            if cls:
                l.append(labels[index])
        predictions.append(",".join(l))
    result = 0
    
    if predictions[0] == '':
        result = 0
    else:
        listValue  = list(map(float, predictions[0].split(',')))
        result = max(listValue) 
    return result





#if __name__ == '__main__':
#    x = str(sys.argv[1])
 #   sys.stdout.write(str(predictTE(x)))