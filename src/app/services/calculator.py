from app.domain.calculator.arithmetic import ArithmeticCalculator
from app.schemas.calculator import CalculationRequest, CalculationResponse

class CalculatorService:
    def __init__(self, calculator: ArithmeticCalculator):
        self.calculator = calculator

    def calculate(self, request: CalculationRequest) -> CalculationResponse:
        operation = request.operation.lower()

        # Handle string evaluation dynamically
        if operation == "evaluate":
            result = self.calculator.evaluate(request.expression)
            return CalculationResponse(
                operation=operation,
                expression=request.expression,
                result=result
            )

        # Map basic standard two-variable math operations
        operations = {
            "add": self.calculator.add,
            "subtract": self.calculator.subtract,
            "multiply": self.calculator.multiply,
            "divide": self.calculator.divide,
        }

        if operation not in operations:
            raise ValueError(f"Unsupported operation: {request.operation}")

        # Execute standard math actions safely
        result = operations[operation](request.a, request.b)

        return CalculationResponse(
            operation=operation,
            a=request.a,
            b=request.b,
            result=result,
        )
