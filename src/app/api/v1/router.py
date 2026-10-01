from fastapi import APIRouter

from app.api.v1.calculators import router as calculator_router


api_router = APIRouter()

api_router.include_router(
    calculator_router,
    prefix="/calculators",
    tags=["Calculators"],
)

