import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
import sys
import time
import os
import glob
import numpy
import math
from scipy.fftpack import fft
from scipy.fftpack.realtransforms import dct
from scipy.signal import lfilter, hamming
from ctc.code.utilities.features import *
import pandas as pd
import pickle


files = [f for f in os.listdir('./wav') if os.path.isfile(os.path.join("wav", f))]
berlin=[]
emo_dict={"W":"Anger","L":"Boredom","E":"Disgust","A":"Anxisty/Fear","F":"Happiness","T":"Sadness","N":"Neutral"}
for i,f in enumerate(files):
    samplerate, data = wavfile.read(os.path.join("./wav",f))
    wavfile.write("input_file.wav",samplerate,data)
    command = "SMILExtract -C demo1.conf -I input_file.wav -O output_file.csv"
    os.system(command)
    emo=emo_dict[f[5]]
    speaker=f[:2]
    sentence=f[2:5]
    version=f[6]
    data=pd.read_csv("output_file.csv",sep=";")
    tp=(data,emo,speaker,sentence,version,samplerate)
    berlin.append(tp)

with open('berlin.pickle', 'wb') as handle:
    pickle.dump(berlin, handle, protocol=pickle.HIGHEST_PROTOCOL)

 
