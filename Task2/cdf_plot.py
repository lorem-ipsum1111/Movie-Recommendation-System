from matplotlib import pyplot as plt
import numpy as np


dat_list = np.genfromtxt("no_movies_rated_by_user.csv",delimiter=',',skip_header=0)

plt.hist(dat_list, bins=2678, normed=True, cumulative=True, label='CDF of No. of ratings by users', 
         histtype='step', alpha=0.55, color='purple')
