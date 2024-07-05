#!/usr/bin/python3
import sys
import os
import unittest

# Ensure the app directory is in the path for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import Articles, Source

class TestArticles(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles(
            author="John Doe",
            title="Test Article",
            description="This is a description of the test article.",
            url="http://example.com/article",
            urlToImage="http://example.com/image.jpg",
            publishedAt="2024-07-04T12:34:56Z",
            content="This is the content of the test article."
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_initialization(self):
        self.assertEqual(self.new_article.author, "John Doe")
        self.assertEqual(self.new_article.title, "Test Article")
        self.assertEqual(self.new_article.description, "This is a description of the test article.")
        self.assertEqual(self.new_article.url, "http://example.com/article")
        self.assertEqual(self.new_article.urlToImage, "http://example.com/image.jpg")
        self.assertEqual(self.new_article.publishedAt, "2024-07-04T12:34:56Z")
        self.assertEqual(self.new_article.content, "This is the content of the test article.")

class TestSource(unittest.TestCase):
    def setUp(self):
        self.new_source = Source(
            id="test-id",
            name="Test Source",
            description="This is a description of the test source.",
            url="http://example.com/source",
            category="general"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_initialization(self):
        self.assertEqual(self.new_source.id, "test-id")
        self.assertEqual(self.new_source.name, "Test Source")
        self.assertEqual(self.new_source.description, "This is a description of the test source.")
        self.assertEqual(self.new_source.url, "http://example.com/source")
        self.assertEqual(self.new_source.category, "general")

if __name__ == '__main__':
    unittest.main()
