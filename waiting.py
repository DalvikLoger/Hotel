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

x = df['days_in_waiting_list']  # abscisses des points des deux nuages
x1 = df['arrival_date_year']
y1 = df['lead_time']     # ordonnées des points du premier nuage
y2 = df['company']   # ordonnées des points du second nuage

fig = plt.figure(figsize=(20,10))

plt.subplot(221)
plt.scatter(x, y1, label = "Arrival date Year ")
plt.legend()

plt.subplot(222)
plt.bar(x1, y2, label = "lead time",)
plt.legend()