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
dataFrance = df[df.country == 'FRA']

x = df['is_repeated_guest']  # abscisses des points des deux nuages
x1 = df['previous_cancellations']
y1 = df['previous_bookings_not_canceled']     # ordonnées des points du premier nuage
y2 = df['previous_cancellations']   # ordonnées des points du second nuage

fig = plt.figure(figsize=(20,10))

plt.subplot(221)
plt.bar(x, y1, label = "Is Repeated guest ")
plt.legend()

plt.subplot(222)
plt.bar(x1, y1, label = "Previous_Cancellations / Previous booking not canceled",)
plt.legend()

plt.subplot(223)
plt.scatter(x, y2, label = "Is repeated guest / Previous cancellations",)
plt.legend()