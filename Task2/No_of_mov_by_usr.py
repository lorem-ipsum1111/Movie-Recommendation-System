from matplotlib import pyplot as plt
import numpy as np


dat_list = np.genfromtxt("no_movies_rated_by_user.csv",delimiter=',',skip_header=0)
plt.hist(dat_list, bins=2678)
plt.title("Histogram for number of movies rated by users")
plt.show()
