

Highest number of ratings of a movie: 279

Lowest number of ratings of a movie: 1


Histogram: 

	On X axis: No. of users who have rated a movie.
	On Y axis: No. of movies
	
We see that a large number of movies have very less number of ratings. This is represented by the high peak of the histogram
at the start. The histogram peak diminishes as we move away from Y axis, representing that there are a few movies which are very
famous and have been rated by a large number of users.

CDF:
	On X axis: No. of users who have rated a movie
	On Y axis: The total fraction of the movies included upto that point

We observe that the graph is steep at the beginning, showing that majority of movies have very few ratings. As we move away from
the Y-axis, the graph becomes steeper, showing that a very less fraction of movies have significant ratings.


The graph resembles an exponential distribution.

Note: Although the highest movie index is 193609, there are only 9724 movies in the dataset, meaning that a lot of movie indices
are empty, and thus have been excluded.


File description: 

blank_indices.csv: CSV file containing indices which do not refer to any movie

cdf_plot.py : Python code used to plot the cdf
no_of_ratings.py : Python code used to plot the histogram
No_of_ratings_for_movie.csv: Data extracted to plot the histogram.
