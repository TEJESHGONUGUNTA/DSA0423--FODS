import pandas as pd
import numpy as np
from scipy import stats

data = {'rating':[4,5,3,4,5,4,3,5,4,5]}

df = pd.DataFrame(data)

ratings = df['rating']

mean_rating = np.mean(ratings)

std_error = stats.sem(ratings)

confidence_interval = stats.t.interval(0.95, len(ratings)-1, loc=mean_rating, scale=std_error)

print("Average Rating:", mean_rating)
print("95% Confidence Interval:", confidence_interval)
