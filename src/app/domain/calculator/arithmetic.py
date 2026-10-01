from app.domain.calculator.exceptions import DivisionByZeroError
import ast

class ArithmeticCalculator:
    def __init__(self):
        self._operators = {
            ast.Add: self.add,
            ast.Sub: self.subtract,
            ast.Mult: self.multiply,
            ast.Div: self.divide,
            ast.USub: lambda a: -a,  # Handles negative numbers like -5
            ast.UAdd: lambda a: a,   # Handles positive signs like +5
        }

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return a / b

    def evaluate(self, expresssion: str) -> float:
        try:
            tree = ast.parse(expresssion, mode='eval')
            return self._eval_node(tree.body)
        except (TypeError, ValueError, KeyError) as e:
            raise ValueError(f"Invalid  mathematical expression: {expresssion}") from e 

    def _eval_node(self, node):
        if isinstance(node, ast.Constant):
            if not isinstance(node.value, (int, float)):
                raise TypeError("Only numbers are allowerd.")
            return float(node.value)

        elif isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            # This line works now because self._operators exists above!
            op_func = self._operators[type(node.op)]
            return op_func(left, right)

        elif isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            op_func = self._operators[type(node.op)]
            return op_func(operand)

        else:
            raise TypeError(f"Unsupported operator: {type(node).__name__}")
