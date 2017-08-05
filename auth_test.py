
import oauth2 as oauth
import urlparse
import requests

# from wordpress import API
# from wordpress_json import WordpressJsonWrapper

url = 'https://public-api.wordpress.com/oauth2/authorize?client_id=45998&response_type=token&client_secret=Z9wnBuKVZMS9yXKCvn31SrljBOxmi9p1tfGGPSoODcviyYRd2cltuBIDjm5NCxfq'

url_base = 'https://public-api.wordpress.com/oauth2/token'
url = 'https://public-api.wordpress.com/oauth2/token'
data = {
	'client_id':'45998',
	'client_secret':'Z9wnBuKVZMS9yXKCvn31SrljBOxmi9p1tfGGPSoODcviyYRd2cltuBIDjm5NCxfq',
	'grant_type':'password',
    'username':'cmh3258',
    'password':'ball06',
}


# https://public-api.wordpress.com/rest/v1.1/me/sites
# url = 'https://public-api.wordpress.com/oauth2/authorize?client_id=45998&response_type=token&redirect_uri=https://oauth.io/auth&blog=108370734'
url = 'https://public-api.wordpress.com/rest/v1.1/sites/108370734' #this
# r = requests.get(url, params=data)
url = 'https://public-api.wordpress.com/oauth2/authorize?client_id=45998&response_type=token&redirect_uri=http://localhost:8000&blog=108370734&scope=global'

url = 'https://public-api.wordpress.com/oauth2/token?client_id=45998&client_secret=Z9wnBuKVZMS9yXKCvn31SrljBOxmi9p1tfGGPSoODcviyYRd2cltuBIDjm5NCxfq&grant_type=password&username=cmh3258&password=ball06'



# url = 'https://api.twitter.com/oauth/request_token?oauth_callback=http://localhost:8000/'
# r = requests.get(url)
# print r.url
url = 'https://public-api.wordpress.com/oauth2/token'
data = {
    'client_id':'45998',
    'redirect_uri':'http://localhost:8000',
    'client_secret':'Z9wnBuKVZMS9yXKCvn31SrljBOxmi9p1tfGGPSoODcviyYRd2cltuBIDjm5NCxfq',
    'code':'bzLLz4LxNN',
    'grant_type':'authorization_code'
}
r = requests.post(url, data=data)

print r
print r.text
# print r.headers


# wpapi = API(
#     url="https://pondersimple.com/",
#     consumer_key="45998",
#     consumer_secret="Z9wnBuKVZMS9yXKCvn31SrljBOxmi9p1tfGGPSoODcviyYRd2cltuBIDjm5NCxfq",
#     api="wp-json",
#     version="wp/v2",
#     wp_user="cmh3258",
#     wp_pass="ball06"
# )
# # r = wpapi.get("posts")
# # print r
# print dir(wpapi)
# print dir(wpapi.auth)


# wp = WordpressJsonWrapper('https://public-api.wordpress.com/rest/v1.1/', 'cmh3258', 'ball06')
# print wp.get_posts()
