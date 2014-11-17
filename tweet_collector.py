import tweepy
import time
import unicodedata
import sys
import os
from tweet_processor import get_tweets


valid = False
while (not valid):
	try:
		file_name = raw_input('Enter a file name: ')
		input_file_dir = file_name
		if os.path.isfile(input_file_dir):
			print file_name + " is loaded."
			valid = True
	except:
		print "Invalid Input"

get_keywords = True
keywords = []
get_word = ""
print "Enter keyword that you want the output tweet to have."
print "Enter #Done to finish input or enter #None to have no keywords.\n"
while get_keywords:
	get_word = raw_input("Keyword Number " + str(len(keywords) + 1) + ": ")
	if get_word == "#Done":
		get_keywords = False
	elif get_word == "#None":
		keywords = []
		get_keywords = False
	else:
		try:
			keywords.append(str(get_word).upper())
		except:
			print "Invalid Input, the keyword must be a string"		

print "The Analysis is progress..."
time.sleep(2)

start_time = time.time()
def load_ID(filename):
	lines = []
	f = open(filename, 'r')
	for line in f:
		line = line.rstrip('\n')
		lines.append(line)
	return lines
input_length = len(load_ID(input_file_dir))

for i in range (input_length):
	get_tweets(i, file_name, keywords)
	time.sleep(2)

elapsed_time = time.time() - start_time
print("Process Time: " + str(int(elapsed_time)) + " seconds")