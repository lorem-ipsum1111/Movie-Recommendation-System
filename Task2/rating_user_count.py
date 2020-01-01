import csv
import numpy as np
import pandas as pd

movies = 9724
users = 610
movies_rated = np.zeros(users,dtype = int) 

with open('ratings.csv') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',')
	for row in csv_reader:
		movies_rated[int(row[0])-1]+=1
			
pd.DataFrame(movies_rated).to_csv("no_movies_rated_by_user.csv",header=None,index=None)
