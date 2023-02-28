import unittest
from src.related_terms import get_term_graph, find_related_terms, find_related_terms_query

class TestCases(unittest.TestCase):
    def test_get_term_graph(self):
        query = "query"
        depth = 2
        words_per_search = 2
        graph = get_term_graph(query, depth, words_per_search)
        self.assertEqual(type(graph), type({}))
        self.assertEqual(type(list(graph.keys())[0]), type(""))
        self.assertEqual(type(list(graph.values())[0]), type([]))
        self.assertEqual(type(list(graph.values())[0][0]), type(""))

    def test_find_related_terms_query(self):
        res = find_related_terms_query("query", 3)
        self.assertEqual(type(res), type([]))
        self.assertEqual(type(res), type(""))

    def test_find_related_terms(self):
        query = find_related_terms_query("query", 1)[0] # Making sure that query is an embedded term
        res = find_related_terms(query, 3)
        self.assertEqual(type(res), type([]))
        self.assertEqual(type(res), type(""))


if __name__ == '__main__':
    unittest.main()
