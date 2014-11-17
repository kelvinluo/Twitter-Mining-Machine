import tweepy
import time
import unicodedata
import sys

def get_tweets(index, company, get_keywords):
  CONSUMER_KEY = 'trkMRaTjXXvwDhDEJlDlSif95'
  CONSUMER_SECRET = 'KBiPp4qd4o2nDeYiCQevGua1557cAz2WJuO49jHXd4hcVZ4dVj'
  OAUTH_TOKEN = '2880393485-6fbVCYeTK3gBucWlizFWZ8RsjrBpVxkX2O7scqi'
  OAUTH_TOKEN_SECRET = 'nm8ii2A5xhNel6FJ09ONace0Fchcthbd7SriCLHKPok75'
  
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.secure = True
  auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
  api = tweepy.API(auth)
  
  #Any change on the keywords? Just replace or add more on this list.
  keywords = get_keywords
  
  def load_ID(filename):
	  lines = []
	  f = open(filename, 'r')
	  for line in f:
		  line = line.rstrip('\n')
		  lines.append(line)
	  return lines
  
  valid = False
  company_names = load_ID(company)
  company_index = index
  
  
  all_tweets = []
  key = company_names[company_index]
  tweet_page = tweepy.Cursor(api.user_timeline, screen_name=key, count=200).pages(16)
  count = 0
  try:
	  for page in tweet_page:
		  for tweet in page:
			  count += 1
			  date_time = str(tweet.created_at.year) + "/" + \
			          str(tweet.created_at.month) + "/" + \
			          str(tweet.created_at.day) + " " + \
			          str(tweet.created_at.hour) + ":" + \
			          str(tweet.created_at.minute) + ":" +\
			          str(tweet.created_at.second)
			  outtweets = [date_time, unicodedata.normalize('NFKD', tweet.text).\
			               encode('ascii','ignore')]
			  all_tweets.append(outtweets)	
	  early_break = False
	  
	  if keywords != []:
	    filtered_tweetes = []
	    for tweet in all_tweets:
		    info = tweet[1].upper()
		    early_break = False
		    for keyword in keywords:
			    if "#" in info:
				    all_words = info.split(' ')
				    for word in all_words:
					    if word != "" and word[0] == '#' and keyword in word:
						    filtered_tweetes.append(tweet)
						    early_break = True
						    break
					    elif word == keyword:
						    filtered_tweetes.append(tweet)
						    early_break = True
						    break
				    if early_break:
					    break
			    else:
				    keyword = keyword + " "
				    if keyword in info:
					    filtered_tweetes.append(tweet)
					    break	    
	  else:
	    filtered_tweetes = all_tweets
					  
	  file = open("output/" + key + "_tweets.txt", "w")
	  file.write("Total Number of Tweets: " + str(len(filtered_tweetes)) + "\n\n")
	  for tweets in filtered_tweetes:
		  
		  
		  file.write(tweets[0] + "\n")
		  file.write(tweets[1] + "\n")
		  file.write("\n")
	  print(count)
	  print("Cheers!!! Tweets for " + key + " is processed.")
	  time.sleep(4)
	  
  
  except:
	  print key + " is not a valid key."
	  time.sleep(10)  
