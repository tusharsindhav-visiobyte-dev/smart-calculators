from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies.calculator import get_calculator_service
from app.domain.calculator.exceptions import DivisionByZeroError
from app.schemas.calculator import (
    CalculationRequest,
    CalculationResponse,
)
from app.services.calculator import CalculatorService


router = APIRouter()

@router.post(
    "/calculate",
    response_model=CalculationResponse,
    status_code=status.HTTP_200_OK,
)
def calculate(
    request: CalculationRequest,
    service: CalculatorService = Depends(get_calculator_service),
):
    try:
        return service.calculate(request)

    except DivisionByZeroError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )
