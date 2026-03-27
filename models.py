from pydantic import BaseModel
from typing import List, Optional

class BankOffer(BaseModel):
    bank_name: str
    max_amount: float
    roi: float

class LoanState(BaseModel):
    income: float
    credit_score: int
    loan_amount: float
    age: int
    available_offers: List[BankOffer] = []
    is_fraud: bool = False

class LoanAction(BaseModel):
    decision: int  # 0: Reject, 1: Approve
    justification: str  # Naya Field: AI ka reason



# from pydantic import BaseModel
# from typing import List, Optional

# class LoanState(BaseModel):
#     income: float
#     credit_score: int
#     loan_amount: float
#     age: int
#     is_fraud: Optional[bool] = False  

# class LoanAction(BaseModel):
#     decision: int  # 0: Reject, 1: Approve


# class BankOffer(BaseModel):
#     bank_name: str
#     max_amount: float
#     roi: float  # Rate of Interest

# class LoanState(BaseModel):
#     income: float
#     credit_score: int
#     loan_amount: float
#     age: int
#     available_offers: List[BankOffer] = [] 

#     is_fraud : bool = False