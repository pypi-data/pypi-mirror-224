from typing import Dict
import re


class Spreadsheet:
    def __init__(self):
        self.cells: Dict[str, object] = {}
        self.supported_operations = ['+', '-']

    def set_cell_value(self, cell_id: str, value: object) -> None:
        """
        Sets the value of a cell in the spreadsheet.

        Parameters:
            cell_id (str): The ID of the cell to set the value for.
            value (object): The value to set for the cell.

        Returns:
            None

        Raises:
            ValueError: If the value contains unsupported operators or references undefined cells.
        """
        if isinstance(value, str) and value.startswith('='):
            operators = re.findall(r'[+\-*/]', value)
            unsupported_operators = [operator for operator in operators if operator not in self.supported_operations]
            if unsupported_operators:
                raise ValueError(f"Unsupported operators {unsupported_operators} found")

            referenced_cells = re.findall(r'[A-Z]+\d+', value)
            undefined_cells = [cell_reference for cell_reference in referenced_cells if cell_reference not in self.cells]
            if undefined_cells:
                raise ValueError(f"Referenced cells {undefined_cells} are not defined")

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
        
        if cell_id not in self.cells:
            raise ValueError("Cell not found")
        
        value = self.cells[cell_id]
        if isinstance(value, str) and value.startswith('='):
            value = self.evaluate_expression(value[1:])
        return value

    def evaluate_expression(self, expression: str) -> object:
        """
        Evaluate a mathematical expression and return the result.

        Args:
            expression (str): The mathematical expression to evaluate.

        Returns:
            object: The result of the evaluation.

        Raises:
            ValueError: If the expression contains an unsupported or invalid token,
                        or if the expression is invalid.
        """
        operators = self.supported_operations
        tokens = re.findall(r'[A-Z]+\d+|[+\-()]|\d+\.\d+|\d+', expression)
        stack = []

        def perform_operation(op, op1, op2):
            """
            Perform a mathematical operation on two operands.

            Args:
                op (str): The operator to perform.
                op1 (float): The first operand.
                op2 (float): The second operand.

            Returns:
                float: The result of the operation.
            """
            if op == '+':
                return op1 + op2
            elif op == '-':
                return op1 - op2
            else:
                raise ValueError("Unsupported operation")

        for token in tokens:
            if token in operators:
                while stack and stack[-1] in operators:
                    if len(stack) < 3:
                        raise ValueError("Unsupported or invalid token")
                    op2, op, op1 = stack.pop(), stack.pop(), stack.pop()
                    stack.append(perform_operation(op, op1, op2))
                stack.append(token)
            elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(float(token))
            elif token in self.cells:
                stack.append(self.get_cell_value(token))
            else:
                raise ValueError("Unsupported or invalid token")

        while len(stack) > 1:
            if len(stack) < 3:
                raise ValueError("Unsupported or invalid token")
            op2, op, op1 = stack.pop(), stack.pop(), stack.pop()
            stack.append(perform_operation(op, op1, op2))

        if len(stack) != 1:
            raise ValueError("Invalid expression")

        return stack[0]
