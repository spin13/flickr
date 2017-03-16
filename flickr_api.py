import env
import json
import requests
import random
from time import sleep


def to_url(json_data):
    print(json_data)
    print("#####################")
    return 'https://farm%s.staticflickr.com/%s/%s_%s.jpg' % (json_data['farm'], json_data['server'], json_data['id'], json_data['secret'])


def get_picts(word='', N=1, sort_algo=''):
    opts = {
        'sort': sort_algo,
        'privacy_filter': 1,
        'content_type': 1,
        'per_page': N,
        'format': 'json',
        'nojsoncallback': 1,
        'api_key': env.FLICKR_API_KEY,
        'method': 'flickr.photos.search',
        'text': word
    }
    url = env.FLICKR_API_BASE
    res = requests.get(url, params=opts)
    return res.json()['photos']['photo']


def random_url():
    ''' 
    sort:
        
        date-posted-desc    アップロード日時の新しい順
        date-posted-asc アップロード日時の古い順
        date-taken-asc  撮影日時の古い順
        date-taken-desc 撮影日時の新しい順
        interestingness-desc    人気の高い順
        interestingness-asc 人気の低い順
        relevance   関連度の高い順
    '''
    words = [
        'cat', 'cat cute', 'kitten', 'kitten cute'
    ]
    algos = [
        'date-posted-desc', 'date-taken-desc', 'interestingness-desc', 'relevance'
    ]

    res = get_picts(word=random.choice(words), N=10, sort_algo=random.choice(algos))
    ret = to_url(random.choice(res))
    if ret == 'https://farm7.staticflickr.com/6168/6153055212_a4c67ef37c.jpg':
        ret = to_url(random.choice(res))
    
    return ret

