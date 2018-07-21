
# This script is available online at: 
#   https://github.com/DardenDSC/intro-to-python-programming/blob/master/script.py

# If you are using RStudio to run the code below, then go to "Tools" -> "Terminal" 
# and you should see a window pop open next to the console tab in the lower left pane 
# of RStudio that says "Terminal". All of your Python commands will be rendered there. 

# In the terminal type: python -V 
# This will tell you which version of Python you are running. If you don't see anything 
# close RStudio and go to ... to install the Anaconda, scientific computing distribution 
# of Python
#
# Once you have Python installed, in the terminal type: ipython3  

# This allows you to run code interactively. Use your cursor to highlight 
# the lines you would like to run and then press CRTL+ALT+ENTER or CMD+OPTION+ENTER for Mac users.

#  DO I BOTHER WITH THIS SINCE THEY HAVE CONDA?
# how to install a library (only need to install a library once) ---------------


# how to load a library (need to load a each new R session) --------------------

# Run "import LIBRARY_NAME" to load a library. You must load the library every 
# time that you start running your Python script (start a new session) so that the 
# functions become available for use to use during the session. 
import numpy 

# A lot of times people will abbreviate the name of the library to make their code 
# shorter and easier to read. So you can load the numpy library using a made up alias "np"
import numpy as np

# Here we will additional libraries that makes it easier to manipulate data
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
%matplotlib qt

# reading in data --------------------------------------------------------------

# Read the CSV (comma-seperated values) file called "song-data.csv" from our project folder
# The dataset actually comes from a blog that Tamas Szilagyi wrote about analyzing his 
# spotify listening history: http://tamaszilagyi.com/blog/analyzing-my-spotify-listening-history/

# The command "read_csv()" will read the data and assign it to an object called "df_tracks"
# The " = " operator means take the result from the right-hand side and put it into a 
# variable by the name of what is on the left-hand side of the operator.
df_tracks = pd.read_csv("https://raw.githubusercontent.com/DardenDSC/intro-to-r-programming/master/song-data.csv")


# an example where variable is not assigned (just printed to console) ----------

# You don't always have to assign data to a variable. If you don't include the 
# assignment operator, the result will just print it in the Console window.
1 + 1

# an example where you want to delete a variable -------------------------------

# Variables occupy memory during your session. If you create one and no longer 
# need it, then you can delete it using "del" to free up memory.
y = 1 + 1
y
del y
y


# writing out data -------------------------------------------------------------

# It's great to read the data and have it in your Python session, but what if you'd like 
# to save the data for another time? You can save a CSV file to your computer by 
# using the "to_csv()" command. This command takes 1 arguments: 
#   1. The name of the file you'd like to create and store the data in.
# Here we are saving the data in df_tracks to a file called "songs.csv"
df_tracks.to_csv("songs.csv")


# figuring out the rows and columns of a dataset -------------------------------

# Python uses the "pandas" library to store data in a "tabular" format. In other words, a format 
# that keeps the data in a rectangle shape of rows and columns. There are functions 
# as part of the pandas library specifically designed to work with the data in this form.
# For example, every dataframe has a "shape" attribute that contains the rows and 
# column counts of the data. In our case, that is 3274 rows by 6 columns.
df_tracks.shape


# referencing specific data points using their indices -------------------------

# Because dataframes is typically based on rectangles which are a collection of rows and columns
# you can reference specific parts of the rectangle using "indices". The indices are the 
# row and column numbers that point to a specific value. The "iloc" attribute stands 
# for integer location, which allows you to specify by integer index different parts 
# of the dataframe.
#
# For example, to reference the 1st row, 2nd column, you just need to put that information 
# in square brackets separated by a comma. Remember Python is a zero-based indexing language 
# the first item in a list is indicated by the 0 index. In this case "0,1" referencess 
# the first and second column.
df_tracks.iloc[0,1]

# If you'd like to reference just the first row, then put a colon for the column index
df_tracks.iloc[0,:]

# If you'd like to reference just the fourth column, then put a colon for the row index
df_tracks.iloc[:,3]

# Rectangular data where the columns have names can be referenced using their name and the "loc"
# attribute of the dataframe.
# For example, if you want the 1st observation in the "track_name" column, just put ".iloc[0]" on the
# end of df_tracks referencing the column name instead of its index, like this:
df_tracks['track_name'].iloc[0]

# Again, you can confirm this is the same as using the row-column indices.
df_tracks.iloc[0, 1]

# If you ever forget the names of your dataframe or want to look at its structure
# just reference the attribute "dtypes" which provides the column names and their 
# data types
df_tracks.dtypes
 
# Why should I worry about how to pull pieces of data out of a data.frame? Let's 
# say that you wanted to find the difference in duration between the first and 
# second song in the dataset. You can pull out those two pieces of data and subtract 
# to find the difference.
first_song_duration = df_tracks.iloc[0, 3]
second_song_duration = df_tracks.iloc[1, 3]
second_song_duration - first_song_duration

# You can confirm that the second song is shorter by looking at the dataset.
df_tracks[['track_name','duration_ms']].iloc[:2]

# Assigning variables is really important in Python because you can take many different 
# data objects and perform operations on them to do even more analysis.


# the different data structures in Python --------------------------------------

# In Python there are more than just rectangles of data. There are a few data structures: 
#  - List/Array (a collection of values of the same data type, e.g. a bunch of numbers, or a bunch of words)
#  - Dictionaries (a collection of values that could be of different data types, e.g. a bunch of numbers and words)
#  - Tuple (a collection of values of different data types, e.g. numbers and words)
#  - DataFrames (a rectangle of rows and columns of different data types, e.g. numbers and words)

# You can check if a variable is a certain type of data structure by using "isinstance()". 
# In our case df_tracks is not a list or tuple, it's a pandas DataFrame and that can be 
# confirmed by using the "type()" function
isinstance(df_tracks, list)
isinstance(df_tracks, tuple)
type(df_tracks)


# the different primitive data types in Python ---------------------------------

# In Python there are even simpler types of data called primitive data types. They 
# make up a larger structure, such as a DataFrame:
# The primitive different types are: 
#  - String (str) - a single letter or words 
#  - Integer (int) - whole numbers (no decimals) from neg infinity to infinity
#  - Float - real numbers (with decimals) from neg infinity to infinity
#  - Boolean (bool) - values that only take on TRUE or FALSE

# Again you can check if a variable is a certain type by using "isinstance()" or the "type()" function
isinstance(3.14, str)
isinstance(3.14, int)
isinstance(3.14, float)
type(3.14)
y = int(3.14)
y
isinstance(y, int)
isinstance(False, bool)
isinstance("FALSE", bool)
isinstance("FALSE", str)

# Wait! How do we know about all these functions. You can Google them and see 
# examples of other people's code which is a good step, but if you need a reminder 
# on the definition of a function and you already know the name, then you can 
# find the documentation by typing help() in the console like this: 
help()
# type "q" to quit the help

# You can also directly search for a function like this: 
help(pd.read_csv)

# You can browse an entire package like this:  
help(pd)
dir(pd)

# Pro Tip: You can quickly scroll to the top/bottom and page throughout the 
# help documentation by using the HOME and END functions on Windows or by using the following: 
# FN+UP (page up), FN+DOWN (page down), FN+LEFT (top of doc), FN+RIGHT (bottom of doc)

# working with missing data in Python ------------------------------------------

# Python keeps track of missing values as well, the absence of a value. 
# The function "isna()" returns a vector of logical values that indicate whether 
# or not the value in the vector at that position is missing
# For example, if we would like to check the missing values in a column of the 
# dataset we can do it like this: 
pd.isna(df_tracks['playlist_url'].head(2))

# Note that we've used the head() function to only look at the first 2 values, otherwise 
# we would see the entire vector (one element for each row in the dataset).

# The interesting thing about the logical data type is that Python considers FALSE = 0 
# and TRUE = 1 when you convert a vector of logicals to numeric, so if you want to 
# count the number of missing values in the playlist_url column, then all you have 
# to do is calculate the "sum()"
sum(pd.isna(df_tracks['playlist_url']))


# finding the proportion of missing values in a column -------------------------

# A neat trick is that if the FALSE/TRUE values are coded 0/1, then if you take the 
# average, it will represent the proportion of rows that have missing values
# For example, in this dataset, the proportion of rows (observations) that have a 
# missing playlist url is: 
round(np.mean(pd.isna(df_tracks['playlist_url'])),4)
# the mean (average) function comes from the numpy package, that is why we had to 
# reference it using the prefix "np".

# This tells you that 69.64% of the songs played have a missing value for playlist_url. 
# This makes sense because not all songs are going to be played from a playlist.

# This is all very fun exploring different columns, but what about some more complex 
# analyses? Let's say you wanted to determine if the duration of songs is longer or 
# shorter depending on if it is played from a playlist or an album on Spotify. 
# Python has the tools to easily answer this question! Let's first take a look at the syntax. 


# filtering data and counting rows using filter() ------------------------------

# The pandas library is one of the most important libraries when doing data analysis 
# Python. It has a number of handy functions. The first we'll talk about is the "query()" 
# function to select certain records. Let's say you only wanted to work with the rows 
# where the the song was played on a playlist and then count the number of 
# rows in that filtered dataset. Just combine the logic like this: 
df_tracks \
  .query('type == "playlist"') \
  .shape[0]

# Here the backslash tells Python that the command is not done, go to the next line 
# to continue evaluating it. We split the command across multiple lines so that it 
# is easier to read each step.

# The "shape()" function should be familiar. It counts the rows and columns in a dataset. 
# The "query()" function is new. We are taking the df_tracks dataset and using the "query()" 
# function to select the rows type == "playlist", then we use that result's shape attribute to 
# get the row count.


# summarizing data using group_by() and summarize() ----------------------------

# Let's get back to the question about calculating the duration of tracks played on a 
# playlist or an album. The pandas library has the function "group_by()" that will 
# split the data into all the possible values in a column and calculate a summary for 
# each value. The "agg()" function will calculate a summary statistic, such as the average, 
# for each of the grouped values (i.e. song type playlist or album). To make the data 
# more digestable we convert the song duration in milliseconds to seconds by dividing by 
# 1000 and then calculating the mean to get average seconds, and then dividing by 60 
# to convert the average song seconds to minutes.
df_tracks \
  .fillna({'type': ''}) \
  .groupby('type') \
  .agg({'duration_ms': lambda x: np.mean(x / 1000) / 60})


# a summary of what has been shown so far --------------------------------------

# To summarize you have learned the following:
# - How to load a library for analysis using "import PACKAGE_NAME as ALIAS" (need to load a library each Python session)
# - How to load data using the "pd.read_csv()" function
# - How to assign data to a variable using the assignment operator (" = "). In this case we called it "df_tracks"
# - How to remove a variable using the "del"
# - The different primitive data types in Python: string, integer, float, boolean
# - The different data structures in R: array/list, dictionary, tuple, DataFrame
# - How to check the data type of a variable using functions like: "isinstance()" and "type()"
# - How to reference specific data points in a data.frame using indices df_tracks.iloc[1,1] or df_tracks['column'].iloc[1]
# - How to pull up the documentation using the help() function with a keyword, a function name or a library
# - How to count rows, columns, dimensions of dataset using the "shape" attribute
# - How to count the missing values in a column using "pd.isna()"
# - How to calculate the average using "np.mean()"
# - How to chain together data operations using the backslash (\) and period (.) for each new line
# - How to summarize data using "query()", "groupby()", and "agg()"


# plotting data in R using the seaborn library ---------------------------------

# A lot of work in data analysis is formatting the data and computing summary 
# statistics like the ones we've been running, but it is important to supplement 
# that analysis with plots to get a better feel for what's happening in the dataset. 
# For example, let's say we wanted to know the distribution of songs played by the 
# hour of the day.
sns.distplot(
  pd.to_datetime(df_tracks['played_at']) \
    .dt.hour,
  kde=False
)
# Here the seaborn library, aliased using "sns",  has a function called "distplot()" 
# that generates a histogram. Prior to plotting we had to convert the "played_at" column 
# to a datetime format and extract the hour component. The extra argument "kde=False" 
# is telling the plotting function to plot the counts, not the kernal density function 
# which is a statistical term for the estimated probability of an outcome. Here we 
# care less about probabilities and just the raw counts of what happened.


# adding more elements to a histogram ------------------------------------------

# What's interesting is there is a peak around 8am and 7pm. The chart above is missing 
# some important components like axis labels and a title, but it is easy to add these elements.
# We can use the "set()" function for a seaborn plot that gives us access to setting 
# elements like the x-axis, y-axis, and title.
sns.distplot(
  pd.to_datetime(df_tracks['played_at']) \
    .dt.hour, 
  kde=False
).set(xlabel='Hour of Day (0-24)',
      ylabel='Count of Songs Played', 
      title="Distribution of Songs Played by Hour of Day")
 
     
# creating a line plot ---------------------------------------------------------

# In the example above we created a histogram, but more typically users want to 
# see a line plot. Let's plot the number of songs played each day and plot them 
# over time to see the trend. 
sns.tsplot(
  df_tracks \
    .apply(lambda df: pd.to_datetime(df_tracks['played_at']).dt.date) \
    .groupby('played_at') \
    .size()
).set(xlabel='Date',
      ylabel='Count of Songs Played', 
      title="Trend of Songs Played over Time")
