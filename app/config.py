#!/usr/bin/python3
import os

class Config:
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
