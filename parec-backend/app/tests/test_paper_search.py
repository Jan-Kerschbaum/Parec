import unittest
from src.paper_seach import run_paper_search, get_paper_relevance, construct_relevance_metric
from math import log as ln

class TestCases(unittest.TestCase):
    def test_run_paper_search(self):
        term_graph = { # Simulates search depth 1, words per search 3
            "TeSt": ["test", "test environment", "test suite"],
            "test": ["test suite", "testing", "unittest"],
            "test environment": ["environment", "test suite", "test"],
            "test suite": ["suite", "test", "noideawhattoputhere"], 
            }
        query = "TeSt"
        max_relevance = 10
        papers = run_paper_search(term_graph, query, max_relevance)
        self.assertEqual(type(papers), type([]))
        self.assertEqual(type(papers[0]), type([]))
        self.assertEqual(type(papers[0][0]), type(""))
        self.assertEqual(type(papers[0][1]), type(""))
        self.assertEqual(type(papers[0][2]), type(""))
        


    def test_construct_relevance_metric(self):
        term_graph = { # Simulates search depth 1, words per search 3
            "TeSt": ["test", "test environment", "test suite"],
            "test": ["test suite", "testing", "unittest"],
            "test environment": ["environment", "test suite", "test"],
            "test suite": ["suite", "test", "noideawhattoputhere"], 
            }
        query = "TeSt"
        max_relevance = 10
        metric = construct_relevance_metric(term_graph, query, max_relevance)
        self.assertEqual(type(metric), type({}))
        keys = list(metric.keys())
        vals = list(metric.values())
        vals = [val for sublist in vals for val in sublist]
        self.assertEqual(type(keys[0]), type(""))
        self.assertEqual(type(vals[0]), type(1))
        for v in vals:
            self.assertTrue(v > 7) # max relevance is 10, every other term in graph is either found from query (mr - 1), or found from term found from query (mr - 2)


    def test_get_paper_relevance(self):
        relevance_list = {
            "query": 10,
            "q0": 9,
            "q1": 9,
            "q2": 9,
            "q00": 8,
            "q01": 8,
            "q010": 7,
            "q011": 7,
            "q02": 8,
        }
        paper = "q010 q02 na query"
        relevance = get_paper_relevance(relevance_list, paper)
        relevance_test = relevance_list["q010"] + relevance_list["q02"] + relevance_list["query"] # = (ln(1) + 1) * (rl["q010"] + rl["q02"] + rl["query"])
        self.assertTrue(relevance - relevance_test < 0.01)


if __name__ == '__main__':
    unittest.main()
