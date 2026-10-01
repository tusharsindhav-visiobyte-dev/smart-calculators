from pydantic import BaseModel, Field, model_validator
from typing import Optional

class CalculationRequest(BaseModel):
    operation: str = Field(..., examples=["add", "evaluate"])
    a: Optional[float] = None
    b: Optional[float] = None
    expression: Optional[str] = None

    @model_validator(mode="after")
    def validate_inputs(self):
        operation = self.operation.lower()
        
        if operation == "evaluate":
            if not self.expression:
                raise ValueError("Field 'expression' is required when operation is 'evaluate'.")
        else:
            if self.a is None or self.b is None:
                raise ValueError(f"Fields 'a' and 'b' are required for operation '{operation}'.")
        return self


class CalculationResponse(BaseModel):
    operation: str
    a: Optional[float] = None
    b: Optional[float] = None
    expression: Optional[str] = None
    result: float
