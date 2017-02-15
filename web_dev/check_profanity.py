import os

def read_text():
	quotes = open('/home/francois/practice/web_dev/movie_quotes.txt')
	contents_of_files = quotes.read()
	print(contents_of_files)
	quotes.close()
read_text()