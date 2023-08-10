import unittest
from spreadsheet.core import Spreadsheet

class TestSpreadsheetCore(unittest.TestCase):
    def test_set_and_get_cell_value(self):
        """
        Test the functionality of the set_cell_value() and get_cell_value() methods in the Spreadsheet class.

        This test case creates a new instance of the Spreadsheet class and sets the values of two cells using the set_cell_value() method. The values are then retrieved using the get_cell_value() method and compared to the expected values using the assertEqual() method.

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        spreadsheet = Spreadsheet()
        spreadsheet.set_cell_value("A1", 13)
        spreadsheet.set_cell_value("A2", 14)
        self.assertEqual(spreadsheet.get_cell_value("A1"), 13)

    def test_evaluated_expression(self):
        """
        Evaluate an expression in the spreadsheet and assert the result.

        This function creates a new spreadsheet object and sets the values of cells A1, A2,
        and A3. It then sets the value of cell A3 to the sum of the values in cells A1 and A2.
        Finally, it asserts that the value of cell A3 is equal to 27.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        spreadsheet = Spreadsheet()
        spreadsheet.set_cell_value("A1", 13)
        spreadsheet.set_cell_value("A2", 14)
        spreadsheet.set_cell_value("A3", "=A1+A2")
        self.assertEqual(spreadsheet.get_cell_value("A3"), 27)

    def test_nested_expression(self):
        """
        Test the evaluation of nested expressions in the spreadsheet.

        This function creates a new instance of the Spreadsheet class and sets the values of four cells.
        The value of cell A1 is set to 13, the value of cell A2 is set to 14, the value of cell A3 is set to the sum of A1 and A2,
        and the value of cell A4 is set to the sum of A1, A2, and A3.

        The function then asserts that the value of cell A4 is equal to 54.

        This test is verifying that the spreadsheet correctly evaluates nested expressions and returns the expected results.

        Parameters:
        - self: The current instance of the test class.

        Return: None
        """
        spreadsheet = Spreadsheet()
        spreadsheet.set_cell_value("A1", 13)
        spreadsheet.set_cell_value("A2", 14)
        spreadsheet.set_cell_value("A3", "=A1+A2")
        spreadsheet.set_cell_value("A4", "=A1+A2+A3")
        self.assertEqual(spreadsheet.get_cell_value("A4"), 54)

if __name__ == '__main__':
    unittest.main()
