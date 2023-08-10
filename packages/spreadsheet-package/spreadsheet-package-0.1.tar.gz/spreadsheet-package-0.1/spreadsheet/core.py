from typing import Dict
import re

class Spreadsheet:
    def __init__(self):
        self.cells: Dict[str, object] = {}

    def set_cell_value(self, cell_id: str, value: object) -> None:
        """
        Set the value of a cell in the dictionary.

        Args:
            cell_id (str): The ID of the cell.
            value (object): The value to be set.

        Returns:
            None
        """
        self.cells[cell_id] = value

    def get_cell_value(self, cell_id: str) -> object:
        """
        Get the value of a cell from the dictionary.

        Args:
            cell_id (str): The ID of the cell.

        Returns:
            object: The value of the cell.

        Raises:
            ValueError: If the cell is not found.
        """
        if cell_id in self.cells:
            value = self.cells[cell_id]
            if isinstance(value, str) and value.startswith('='):
                value = self.evaluate_expression(value[1:])
            return value
        else:
            raise ValueError("Cell not found")

    def evaluate_expression(self, expression: str) -> object:
        """
        Evaluate an expression containing cell IDs.

        Args:
            expression (str): The expression to be evaluated.

        Returns:
            object: The result of the evaluation.
        """
        cell_ids = re.findall(r'[A-Z]+\d+', expression)
        for cell_id in cell_ids:
            expression = expression.replace(cell_id, str(self.get_cell_value(cell_id)))
        return eval(expression)

