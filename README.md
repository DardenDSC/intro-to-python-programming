# Intro To Python Programming<img src="https://pydata.org/images/logo.png" width="270px" align="right" />
A repository of containing one script ([`script.py`](script.py)) that is a guide to begin 
learning how to perform data analysis in the Python programming language. The script 
covers how to read data, assign data to variables, analyze data, and plot data 
all using a Spotify user's songs played history that is in [`song-data.csv`](song-data.csv).

**Note**: This tutorial script is almost exactly the same as the one we have presented [here](https://github.com/DardenDSC/intro-to-r-programming/blob/master/script.R) in 
the tutorial on learning to perform data analysis in the R programming language.

## Table of Contents
 - [Following Along](#following-along)
 - [Installing Python](#installing-python)
 - [The Data](#the-data)
 - [Resources to Learn Python](#resources-to-learn-python)
 - [Source](#source)
 
### Following Along
The best way to learn Python is to try it out for yourself. After downloading Python and the 
RStudio development tool, open up RStudio and start running the code to see what it does. For this 
session: 
 - Open up RStudio, click File -> New File -> Text File
 - Go to [`script.py`](script.py) and copy/paste all the code into your new, blank script
 - Click Tools -> Terminal -> New Terminal
 - In the blinking Terminal window type: `ipython3`
 - Run commands by copy/pasting them into the Terminal window or by pressing CRTL+ALT+ENTER (CMD+OPTION+ENTER for Mac users)

Keep reading for more information on how to set up your computer with Python and RStudio. 
 
### Installing Python
First, you need to install Python. Python is an immensely popular general purpose 
programming language with many libraries. Fortunately, an organization called Anaconda, Inc. 
has made it easy to install just the libraries that we need for doing data analysis. Start 
by going to https://www.anaconda.com/download. You should see the options to download 
for Linux, Mac, or Windows. Follow the command prompts on your screen just like you 
would install any other software.

Next, you should install RStudio. Wait, Why should I install RStudio? I thought this 
was a Python programming tutorial! Yes, it's true 99.9% of Python developers don't use 
RStudio, but if you participated in our R programming workshop you should already have it installed 
and be familiar with how it looks. If you have it, then you're all set! If you haven't 
installed RStudio, then keep reading.

When you installed the Anaconda distribution, you only installed the software. It 
is hard to code directly to the software, so RStudio is an interface (other software) 
that makes it easier to write code and execute it. Go to https://www.rstudio.com/products/rstudio/download/#download and pick the installer 
for your operating system. Again, follow the prompts like you would install any 
other software on your computer. 

If you have trouble installing Python via the Anaconda distribution or RStudio, 
contact a member of the Darden Data Science club to help you by emailing us at: 
DataScienceClub@darden.virginia.edu

### The Data
The data contains 3,274 records on the songs played and 6 attributes about the songs. 
The attributes cover the basic data captured when playing a song on Spotify, such as 
the time played, track name, etc. Below are the data definitions: 

Variable | Data Type | Data Definition
---|---|---------
played_at | datetime | The date and time that the song was played
track_name | character | The name of the song played
explicit | logical | A `TRUE`/`FALSE` value indicating whether or not the song lyrics were the explicit version. `TRUE` means, yes, it was the explicit version
duration_ms | double | The length of the song played in milliseconds
type | character | One of three values indicating where the song was played from (`playlist`, `artist`, or `album`)
playlist_url | character | The URL of the Spotify playlist that the song was on. If missing, then the song was not played from a playlist.

### Resources to Learn Python
The best book to learn Python programming for data analysis is called the _Python Data Science Handbook_
by Jake VanderPlas. It is available for free online at: https://jakevdp.github.io/PythonDataScienceHandbook/

### Source
The data was taken from a blog that Tamas Szilagyi wrote about analyzing his 
spotify listening history: http://tamaszilagyi.com/blog/analyzing-my-spotify-listening-history/

[Top](#intro-to-python-programming)
