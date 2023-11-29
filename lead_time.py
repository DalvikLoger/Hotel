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

x = df['arrival_date_day_of_month']      # abscisses des points des deux nuages
y1 = df['arrival_date_week_number']     # ordonnées des points du premier nuage
y2 = df['lead_time']   # ordonnées des points du second nuage

fig = plt.figure(figsize=(20,10))

plt.subplot(221)
plt.bar(x, y1, label = "Arrival date week number ")
plt.legend()

plt.subplot(222)
plt.scatter(x, y2, c = 'm', label = "lead time",)
plt.legend()

