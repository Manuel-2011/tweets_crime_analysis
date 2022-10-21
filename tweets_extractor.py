from api.twitter import make_request
from utils.file_utilities import append_tweets_to_csv

if __name__ == "__main__":
  keyword = "(robaron OR asaltaron OR secuestraron OR apuñalaron OR raponearon) lang:es -is:retweet -is:reply (has:media OR has:images OR has:video_link)"
  start_time = "2022-10-21T02:07:00.000Z"
  response = make_request(keyword, start_time)
  append_tweets_to_csv(response, 'data.csv')