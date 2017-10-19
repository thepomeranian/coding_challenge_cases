from unittest import TestCase
from app import app


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_cases_get(self):
        """/cases endpoint testing

        Testing GET
        """

        result = self.client.get("/cases")
        self.assertEqual(result.status_code, 200)
        self.assertIn('{}', result.data)

    def test_cases_post(self):
        """/cases endpoint testing

        Testing POST
        **When I load the json as a file and by pasting it directly, I get this error:
        result = self.client.post("/cases", data=test)
  File "/Users/fl186024/Desktop/cases/venv/lib/python2.7/site-packages/werkzeug/test.py", line 801, in post
    return self.open(*args, **kw)
  File "/Users/fl186024/Desktop/cases/venv/lib/python2.7/site-packages/flask/testing.py", line 122, in open
    builder = make_test_environ_builder(self.application, *args, **kwargs)
  File "/Users/fl186024/Desktop/cases/venv/lib/python2.7/site-packages/flask/testing.py", line 37, in make_test_environ_builder
    return EnvironBuilder(path, base_url, *args, **kwargs)
  File "/Users/fl186024/Desktop/cases/venv/lib/python2.7/site-packages/werkzeug/test.py", line 344, in __init__
    for key, value in _iter_data(data):
  File "/Users/fl186024/Desktop/cases/venv/lib/python2.7/site-packages/werkzeug/test.py", line 205, in _iter_data
    for key, values in iteritems(data):
  File "/Users/fl186024/Desktop/cases/venv/lib/python2.7/site-packages/werkzeug/_compat.py", line 28, in <lambda>
    iteritems = lambda d, *args, **kwargs: d.iteritems(*args, **kwargs)
AttributeError: 'list' object has no attribute 'iteritems'
        """

        result = self.client.post("/cases", data=[{"case_id": 100, "state": {"from": None, "to": "open"}, "timestamp": "2017-01-01T00:00:00Z"},
                                                  {"case_id": 100, "assignee": "Otter", "team": "Support",
                                                      "timestamp": "2017-01-01T00:00:00Z"},
                                                  {"case_id": 100, "assignee": "Rabbit", "team": "Runtime",
                                                      "timestamp": "2017-01-02T15:00:00Z"},
                                                  {"case_id": 100, "state": {"from": "open", "to": "pending"},
                                                   "timestamp": "2017-01-02T16:00:00Z"},
                                                  {"case_id": 100, "state": {"from": "pending", "to": "open"},
                                                   "timestamp": "2017-01-07T06:00:00Z"},
                                                  {"case_id": 100, "state": {"from": "open", "to": "closed"}, "timestamp": "2017-01-08T06:00:00Z"}]
                                  )
        self.assertEqual(result.status_code, 200)
        self.assertIn('{ "case_id": 100, "hours": 25}', result.data)


class CasesUnitTest(TestCase):

    def test_isRuntime(self, case_id):
        assert Cases.is_Runtime(case_id) == True

if __name__ == "__main__":
    unittest.main()
