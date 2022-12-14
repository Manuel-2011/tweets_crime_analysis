import api.twitter_secrets as twitter_secrets
import requests
from datetime import datetime


def auth():
  return twitter_secrets.BEARER_TOKEN

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent"

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def make_request(keyword, start_time, max_results=100):
  bearer_token = auth()
  headers = create_headers(bearer_token)
  start_time = start_time
  end_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:00.000z')

  url = create_url(keyword, start_time,end_time, max_results)
  json_response = connect_to_endpoint(url[0], headers, url[1])

  # if (save):
  #   append_tweets_to_csv(json_response, fileName)

  return json_response