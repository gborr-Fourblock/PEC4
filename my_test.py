import unittest
from concern import sumsample, econconcern, infeconcern
from regex import app_times
from graph_pre_and_post import concernsafterbefore
from data_extr import dataconcern, dataapproval, datapollster
from approve_disapp import graf_appr
from pollnumber import pollnumber


pollster = datapollster("data/pollster_ratings.xlsx")
concern_polls = dataconcern("data/covid_concern_polls.csv")
approval_polls = dataapproval("data/covid_approval_polls.csv")

concern_polls2 = concern_polls[concern_polls.text.str.contains('coronavirus', case=False)]
approval_polls2 = approval_polls[approval_polls['text'].str.contains('Trump', case=False)]


class TestDataExpl(unittest.TestCase):

    def test_app_times(self):
        print("Starting test_app_times")
        with open("data/covid_approval_polls.csv") as f:
            data = f.read().strip()
        huff = app_times('Huffington Post', data)
        url = app_times('^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])|.pdf', data)
        print("Starting test_app_times")
        self.assertEqual(huff, 112)
        self.assertEqual(url, 1366)

    def test_graf_appr(self):
        print("Starting test_graf_appr")
        appdis = graf_appr(approval_polls2)
        self.assertEqual(int(appdis.iloc[0, 0]), 3109)
        self.assertEqual(int(appdis.iloc[1, 0]), 9053)
        self.assertEqual(int(appdis.iloc[2, 0]), 22040)
        self.assertEqual(int(appdis.iloc[3, 0]), 12804)
        self.assertEqual(int(appdis.iloc[0, 1]), 22277)
        self.assertEqual(int(appdis.iloc[1, 1]), 13070)
        self.assertEqual(int(appdis.iloc[2, 1]), 3713)
        self.assertEqual(int(appdis.iloc[3, 1]), 16095)

    def test_sumsample(self):
        print("Starting test_sumsample")
        sumasample = sumsample(concern_polls2)
        self.assertEqual(sumasample, 1271783 )

    def test_econconcern(self):
        print("Starting test_econconcern")
        very, not_very = econconcern(concern_polls2)
        self.assertEqual(very, 4898.0)
        self.assertEqual(not_very, 265.0)

    def test_infeconcern(self):
        print("Starting test_infeconcern")
        very1, not_very1 = infeconcern(concern_polls2)
        self.assertEqual(not_very1, "11.71")
        self.assertEqual(very1, "26.97")

    def test_pollnumber(self):
        print("Starting test_pollnumber")
        a, b, c, d = pollnumber(pollster)
        self.assertEqual(a, 14)
        self.assertEqual(b, 66)
        self.assertEqual(c, 312)
        self.assertEqual(d, 51)

    def test_concernsafterbefore(self):
        print("Starting test_concernsafterbefore")
        antes, despues = concernsafterbefore(concern_polls2)
        self.assertEqual(antes.iloc[0], 859.0)
        self.assertEqual(antes.iloc[1], 436.0)
        self.assertEqual(antes.iloc[2], 138.0)
        self.assertEqual(antes.iloc[3], 50.0)
        self.assertEqual(despues.iloc[0], 548.0)
        self.assertEqual(despues.iloc[1], 257.0)
        self.assertEqual(despues.iloc[2], 63.0)
        self.assertEqual(despues.iloc[3], 26.0)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDataExpl))
unittest.TextTestRunner(verbosity=2).run(suite)
