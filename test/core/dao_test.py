import unittest
from a_la_romana_services.core.dao import DAO


class DAOTestCase(unittest.TestCase):

    dao = None
    db_name = "a_la_romana_test_db"
    users = "test_users"
    activities = "test_activities"
    events = "test_events"
    config = {
        "db_name": db_name,
        "users": users,
        "activities": activities,
        "events": events
    }

    def setUp(self):
        self.dao = DAO(self.config)

    def test_setup(self):
        self.assertIsNotNone(self.dao)
        self.assertEquals(self.dao.db_name, self.db_name)
        self.assertEquals(self.dao.users, self.users)
        self.assertEquals(self.dao.activities, self.activities)
        self.assertEquals(self.dao.events, self.events)