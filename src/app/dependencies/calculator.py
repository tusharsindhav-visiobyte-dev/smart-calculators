from app.domain.calculator.arithmetic import ArithmeticCalculator
from app.services.calculator import CalculatorService


def get_calculator_service() -> CalculatorService:
    calculator = ArithmeticCalculator()

    return CalculatorService(calculator)

