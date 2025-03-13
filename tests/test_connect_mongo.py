# 📂 tests/test_connect_mongo.py - Pruebas de conexión a MongoDB

import unittest
from src.connect_mongo import connect_mongo

class TestMongoConnection(unittest.TestCase):
    def test_connection(self):
        data = connect_mongo()
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()