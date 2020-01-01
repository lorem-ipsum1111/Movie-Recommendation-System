

Highest No of movies rated by a user: 2698
Lowest number of movies rated by a user: 20

Histogram: 
	On X axis: No. of movies rated by the users
	On Y axis: No. of users who have rated a particular no. of movies
	
We see that a significant number of users(about 14) have rated only about 20 movies. As the number of movie count goes up, the number of users who have rated that much count goes drastically down. In mid region, the no. of users goes to zero. Later we again find some users who have rated about 2200 or 3000 movies, showing that those users are movie enthusiasts.

CDF: 
	The CDF is quite steep in the beginning showing that a large portion of users have rated only a few movies. This shows that the rating matrix generated is very sparse. The graph flattens out later showing that a very small portion of users rate a significant count of movies.
	
	The graph resembles that of a modification of exponential distribution.
	
File description: 

cdf_plot.py: Python code used to plot the cdf

no_of_movies_rated_by_user.csv: Raw data used to plot the histogram and cdf

No_of_mov_by_usr.py : Python code used to plot histogram

rating_user_count: Python code used to generate the raw data
