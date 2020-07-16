import os
import json
import unittest
import datetime
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, db, Speaker, Event


class EventSpeakTestCase(unittest.Testcase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ["DATABASE_URL"]
        setup_db(self.app, self.database_path)
        db.create_all()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.new_event = {
            "subject": "exampleSubject",
            "event_date": datetime.date(2020, 9, 1),
        }

        self.new_speaker = {
            "name": "exampleName",
            "expertise": "exampleExpertise",
            "event_id": "1",
        }

    def tearDown(self):
        pass

    # ========================================#
    # Test GET Request Endpoints
    # ========================================#

    # =v= Test GET request for retrieving events  =v= #

    def test_get_events(self):
        res = self.client().get("/events")
        self.assertEqual(res.status_code, 200)

    def test_404Error_get_events(self):
        res = self.client().get("/events")
        self.assertEqual(res.status_code, 404)

    # =v= Test GET request for retrieving speakers  =v= #

    def test_get_speakers(self):
        res = self.client().get("/speakers")
        self.assertEqual(res.status_code, 200)

    def test_404Error_get_speakers(self):
        res = self.client().get("/speakers")
        self.assertEqual(res.status_code, 404)

    # ========================================#
    # Test POST Request Endpoints
    # ========================================#

    # =v= Test POST for events  =v= #

    def test_add_events(self):
        res = self.client().post("/events", json=self.new_event)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(["new_event"]["subject"], "exampleSubject")

    def test_422Error_add_events(self):

        test_add_422 = {
            "subject": "event add error",
            "event_date": "invalid",
        }

        res = self.client().post("/events", json=test_add_422)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)

    # =v= Test POST for speakers  =v= #

    def test_add_speakers(self):
        res = self.client().post("/speakers", json=self.new_speaker)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(["new_speaker"]["name"], "exampleName")

    def test_422Error_add_speakers(self):

        test_add_422 = {
            "name": "name add error",
            "expertise": "invalid",
            "event_id": "invalid",
        }

        res = self.client().post("/speakers", json=test_add_422)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)

    # ========================================#
    # Test PATCH Request Endpoints
    # ========================================#

    # =v= Test PATCH for events  =v= #

    def test_update_events(self):
        res = self.client().patch("/events/2", json=self.new_event)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404Error_update_events(self):
        res = self.client().patch("/events/9000", json=self.new_event)
        self.assertEqual(res.status_code, 404)

    # =v= Test PATCH for speakers  =v= #

    def test_update_speakers(self):
        res = self.client().patch("/speakers/2", json=self.new_speaker)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404Error_update_speakers(self):
        res = self.client().patch("/speakers/9000", json=self.new_speaker)
        self.assertEqual(res.status_code, 404)

    # ========================================#
    # Test DELETE Request Endpoints
    # ========================================#

    # =v= Test DELETE for events  =v= #

    def test_delete_events(self):
        res = self.client().delete("/events/1", json=self.new_event)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404Error_delete_events(self):
        res = self.client().delete("/events/9000", json=self.new_event)
        self.assertEqual(res.status_code, 404)

    # =v= Test DELETE for speakers  =v= #

    def test_delete_speakers(self):
        res = self.client().delete("/speakers/1", json=self.new_speaker)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404Error_delete_speakers(self):
        res = self.client().delete("/speakers/9000", json=self.new_speakers)
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
