import requests
import random
import time
import scrapper

if __name__ == '__main__':
    path_to_key = 'secret.txt'
    scrapper = scrapper.Scrapper(path_to_key)
    scrapper.request_match_list('11121212122')
