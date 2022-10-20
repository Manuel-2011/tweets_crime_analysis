import csv
import dateutil.parser

# Create file
def create_csv_file_for_tweets(fileName):
  csvFile = open(fileName, "a", newline="", encoding='utf-8')
  csvWriter = csv.writer(csvFile, delimiter=';')

  #Create headers for the data you want to save, in this example, we only want save these columns in our dataset
  csvWriter.writerow(['author id', 'created_at', 'geo', 'id','lang', 'like_count', 'quote_count', 'reply_count','retweet_count','source','tweet'])
  csvFile.close()

def append_tweets_to_csv(json_response, fileName):
  #A counter variable
  counter = 0

  #Open OR create the target CSV file
  csvFile = open(fileName, "a", newline="", encoding='utf-8')
  csvWriter = csv.writer(csvFile, delimiter=';')
  csvFile.write('\n')

  #Loop through each tweet
  for tweet in json_response['data']:
        
    # We will create a variable for each since some of the keys might not exist for some tweets
    # So we will account for that

    # 1. Author ID
    author_id = tweet['author_id']

    # 2. Time created
    created_at = dateutil.parser.parse(tweet['created_at'])

    # 3. Geolocation
    if ('geo' in tweet):   
      geo = tweet['geo']['place_id']
    else:
      geo = " "

    # 4. Tweet ID
    tweet_id = tweet['id']

    # 5. Language
    lang = tweet['lang']

    # 6. Tweet metrics
    retweet_count = tweet['public_metrics']['retweet_count']
    reply_count = tweet['public_metrics']['reply_count']
    like_count = tweet['public_metrics']['like_count']
    quote_count = tweet['public_metrics']['quote_count']

    # 7. source
    source = tweet['source']

    # 8. Tweet text
    text = tweet['text']

    # 9. Context
        
    # Assemble all data in a list
    res = [author_id, created_at, geo, tweet_id, lang, like_count, quote_count, reply_count, retweet_count, source, text]
        
    # Append the result to the CSV file
    csvWriter.writerow(res)
    counter += 1

    # When done, close the CSV file
  csvFile.close()

  # Print the number of tweets for this iteration
  print("# of Tweets added from this response: ", counter) 