import unittest
from src.controller import run_backend
import json

class TestCases(unittest.TestCase):
    def test_run_backend(self):
        edges_list = []
        papers_list = []
        queries = ["ai", "data science", "343dad|?_", "<script>alert('!')</script>"]
        for i in range(len(queries)):
            edges_list[i], papers_list[i] = run_backend(queries[i])
            edges_list[i] = dict(json.loads(edges_list[i]))
        for i in range(len(queries)):
            self.assertTrue(len(papers_list[i] > 0))
            self.assertEqual(type(papers_list[i]), type([]))
            self.assertTrue(len(edges_list[i].keys()) > 0)
            self.assertEqual(type(papers_list[i][0]), type([]))


if __name__ == '__main__':
    unittest.main()