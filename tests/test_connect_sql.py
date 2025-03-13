# 📂 tests/test_connect_sql.py - Pruebas de conexión a SQL Server

import unittest
from src.connect_sql import connect_sql

class TestSQLConnection(unittest.TestCase):
    def test_connection(self):
        data = connect_sql()
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()