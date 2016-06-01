#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from os import environ
from sys import argv
from urllib import urlretrieve as download
from json import loads
import requests

def main():
    nombre = argv[1]
    api_key = environ['TMDBAPI']
    payload = { 'api_key' : api_key, 'query' : nombre, 'language' : 'es' }
    r = loads(requests.get('http://api.themoviedb.org/3/search/movie', params=payload ).text)
    titulo = r['results'][0]['title']
    poster_path = r['results'][0]['poster_path']
    download("https://image.tmdb.org/t/p/original/%s" % poster_path, "%s.jpg" %titulo)

if __name__ == '__main__':
    main()
