#!/usr/bin/python3
import sys
import os
import unittest
from app import create_app
from flask import url_for

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_index_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'News Highlight', response.data)

    def test_article_page(self):
        response = self.client.get(url_for('main.article'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Articles', response.data)

if __name__ == '__main__':
    unittest.main()
