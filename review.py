#Hotel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.image import imread
%matplotlib inline
import seaborn as sns
sns.set_theme() # pour modifier le thème

import re
df = pd.read_csv('hotel_bookings.csv',header=0 )
db = pd.read_csv('Hotel_Reviews.csv', header=0)

Rfr = db[db['Hotel_Address'].apply(lambda row: 'France' in row)]
Rfr['Positive_Review'] = Rfr['Positive_Review'].astype('str')
Rfr['Positive_Review']
#Positive words : Windows, Bathroom, email, help me, helpful, quiet, otherwise, needs, problem, managed, friends, forgot, recomend
Rfr.Negative_Review[3784]
#Negative words : Not only, credit card, unacceptable, delete, shame, cleaning, noise, maintenance, small