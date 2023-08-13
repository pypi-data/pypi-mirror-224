import unittest
from spreadsheet.core import Spreadsheet

class TestSpreadsheetCore(unittest.TestCase):
    def setUp(self):
        """
        Common cell values used throughout the test cases.
        """
        self.spreadsheet = Spreadsheet()
        self.spreadsheet.set_cell_value("A1", 13)
        self.spreadsheet.set_cell_value("A2", 14)

    def test_set_and_get_cell_value(self):
        """
        Test the functionality of the set_cell_value() and get_cell_value() methods in the Spreadsheet class.
        """
        self.assertEqual(self.spreadsheet.get_cell_value("A1"), 13)

    def test_evaluated_expression(self):
        """
        Evaluate an expression in the spreadsheet and assert the result.
        """
        self.spreadsheet.set_cell_value("A3", "=A1+A2")
        self.assertEqual(self.spreadsheet.get_cell_value("A3"), 27)

    def test_nested_expression(self):
        """
        Test the evaluation of nested expressions in the spreadsheet.
        """
        self.spreadsheet.set_cell_value("A3", "=A1+A2")
        self.spreadsheet.set_cell_value("A4", "=A1+A2+A3")
        self.assertEqual(self.spreadsheet.get_cell_value("A4"), 54)

    def test_invalid_expression(self):
        """
        Test handling of invalid expressions.
        """
        with self.assertRaises(ValueError):
            self.spreadsheet.set_cell_value("A5", "=A1+A6")  # A6 is not defined

        with self.assertRaises(ValueError):
            self.spreadsheet.set_cell_value("A6", "=A5+A2")  # A5 is not defined

        with self.assertRaises(ValueError):
            self.spreadsheet.set_cell_value("A9", "=A1**A2")  # Unsupported operation

if __name__ == '__main__':
    unittest.main()
