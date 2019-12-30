from matplotlib import pyplot as plt
import numpy as np


dat_list = np.genfromtxt("No_of_ratings_for_movie.csv",delimiter=',',skip_header=0)
plt.hist(dat_list, bins=278)
plt.title("Histogram for number of ratings for movies")
plt.show()
