import unittest
import answer


class TestAnswer(unittest.TestCase):
    # unsure what to put here
    # {'name': '', 'edges': []}
    def test_graph_simple(self):
        graph = {"A": {'name': 'A', 'edges': ['B']}, "B": {'name': 'B', 'edges': ['A', 'C']},
                 "C": {'name': '', 'edges': ['D']}, "D": {'name': 'D', 'edges': ['C']}}
        self.assertEqual(answer.bot_find_dr_bart(graph['A'], graph['B'], graph), 'A, B')

    def test_graph_complex(self):
        graph = {"A": {'name': 'A', 'edges': ['B', 'C', 'E']}, "B": {'name': 'B', 'edges': ['A', 'C', 'D', 'E']},
                 "C": {'name': 'C', 'edges': ['B', 'D']}, "D": {'name': 'D', 'edges': ['C', 'E']}, 'E':{'name': 'E', 'edges': ['F','G']},
                  'F':{'name': 'F', 'edges': ['A', 'B', 'E']}, 'G':{'name': 'G', 'edges': ['E']}}
        self.assertEqual(answer.bot_find_dr_bart(graph['C'], graph['E'], graph), 'C, B, E')
        self.assertEqual(answer.bot_find_dr_bart(graph['C'], graph['G'], graph), 'C, B, E, G')

    def test_graph_line(self):
        graph={"A":{'name':'A', 'edges': ['B']},'B':{'name': 'B', 'edges': ['A', 'C']}, 'C':{'name': 'C', 'edges': ['B']}}
        self.assertEqual(answer.bot_find_dr_bart(graph['A'], graph['C'], graph), 'A, B, C')
        self.assertEqual(answer.bot_find_dr_bart(graph['B'], graph['C'], graph), 'B, C')

    def test_graph_big(self):
        graph={'A':{'name': 'A', 'edges': ['B','H']}, 'B':{'name': 'B', 'edges': ['A','C','D']}, 'C':{'name': 'C', 'edges': ['B','D','G']},
                'D':{'name': 'D', 'edges': ['C']}, 'E':{'name': 'E', 'edges': ['G','F']}, 'F':{'name': 'F', 'edges': ['E']},
               'G':{'name': 'G', 'edges': ['E','C']},'H':{'name': 'H', 'edges': ['A']}}
        self.assertEqual(answer.bot_find_dr_bart(graph['C'], graph['E'], graph), 'C, G, E')
        self.assertEqual(answer.bot_find_dr_bart(graph['A'], graph['D'], graph), 'A, B, D')

    def test_graph_figure_eight(self):
        graph={'D':{'name': 'D', 'edges': ['A', 'C', 'E', 'G']}, 'C':{'name': 'C', 'edges': ['B', 'D']}, 'B': {'name': 'B', 'edges': ['A','C']},
               'A':{'name': 'A', 'edges': ['B', 'D']}, 'E':{'name': 'E', 'edges': ['D','F']}, 'F':{'name': 'F', 'edges': ['E', 'G']},
               'G':{'name': 'G', 'edges': ['D', 'F']}}
        self.assertEqual(answer.bot_find_dr_bart(graph['D'], graph['F'], graph), 'D, E, F')
        self.assertEqual(answer.bot_find_dr_bart(graph['D'], graph['B'], graph), 'D, A, B')
        self.assertEqual(answer.bot_find_dr_bart(graph['D'], graph['B'], graph), 'D, A, B')


if __name__ == "__main__":
    unittest.main()
