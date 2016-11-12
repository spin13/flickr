
import env
import json
import requests


def to_url(json_data):
    return 'https://farm%s.staticflickr.com/%s/%s_%s.jpg' % (i['farm'], i['server'], i['id'], i['secret'])


def get_picts(word, N):
    opts = {
        'sort': 'relevance',
        'privacy_filter': 1,
        'content_type': 1,
        'per_page': N,
        'format': 'json',
        'nojsoncallback': 1,
        'api_key': env.API_KEY,
        'method': 'flickr.photos.search',
        'text': word
    }
    url = env.API_BASE
    res = requests.get(url, params=opts)
    return res.json()['photos']['photo']

if __name__ == '__main__':
    a = get_picts('cat', 3)
    for i in a:
        print(to_url(i))


