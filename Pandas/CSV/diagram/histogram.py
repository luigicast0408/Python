import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('data.csv')

df["Duration"].plot(kind='hist')
plt.show()
