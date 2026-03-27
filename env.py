import random
from models import LoanState, LoanAction, BankOffer

class LoanApprovalEnv:
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty
        self.current_state = None
        # Bank Database
        self.banks = [
            {"name": "HDFC", "min_score": 750, "roi_base": 8.5},
            {"name": "SBI", "min_score": 700, "roi_base": 9.0},
            {"name": "ICICI", "min_score": 650, "roi_base": 10.5},
            {"name": "Axis", "min_score": 600, "roi_base": 12.0}
        ]

    def get_bank_offers(self, score, income):
        offers = []
        for bank in self.banks:
            if score >= bank["min_score"]:
                max_amt = income * random.uniform(5, 12)
                roi = bank["roi_base"] - (score - bank["min_score"]) * 0.01
                offers.append(BankOffer(
                    bank_name=bank["name"],
                    max_amount=round(max_amt, 2),
                    roi=round(max(roi, 7.0), 2)
                ))
        return offers

    def reset(self) -> LoanState:
        income = random.uniform(20000, 150000)
        score = random.randint(300, 850)
        
        offers = self.get_bank_offers(score, income)
        
        self.current_state = LoanState(
            income=income,
            credit_score=score,
            loan_amount=random.uniform(5000, 50000),
            age=random.randint(18, 70),
            available_offers=offers,
            is_fraud=random.random() < 0.1 if self.difficulty == "hard" else False
        )
        return self.current_state

    def step(self, action: LoanAction):
        # Ground truth kya hona chahiye tha?
        should_approve = len(self.current_state.available_offers) > 0 and not self.current_state.is_fraud
        
        reward = 0.0
        
        # 1. Sabse bada gunah: Fraud ko Approve kar diya!
        if action.decision == 1 and self.current_state.is_fraud:
            reward = -2.0  
            
        # 2. Perfect Decision: Sahi time pe approve kiya
        elif action.decision == 1 and should_approve:
            reward = 1.0
            
        # 3. Perfect Decision: Sahi time pe reject kiya (No offers or Fraud)
        elif action.decision == 0 and not should_approve:
            reward = 1.0
            
        # 4. Partial Penalty: Eligible bande ko reject kar diya (Bank ka loss hua)
        elif action.decision == 0 and should_approve:
            reward = -0.5  
            
        done = True
        return self.current_state, reward, done




# import random
# from models import LoanState, LoanAction, BankOffer

# class LoanApprovalEnv:
#     def __init__(self, difficulty="easy"):
#         self.difficulty = difficulty
#         self.current_state = None
#         # Bank Database
#         self.banks = [
#             {"name": "HDFC", "min_score": 750, "roi_base": 8.5},
#             {"name": "SBI", "min_score": 700, "roi_base": 9.0},
#             {"name": "ICICI", "min_score": 650, "roi_base": 10.5},
#             {"name": "Axis", "min_score": 600, "roi_base": 12.0}
#         ]

#     def get_bank_offers(self, score, income):
#         offers = []
#         for bank in self.banks:
#             if score >= bank["min_score"]:
#                 max_amt = income * random.uniform(5, 12)
#                 # Jitna acha score, utna kam ROI (Interest Rate)
#                 roi = bank["roi_base"] - (score - bank["min_score"]) * 0.01
#                 offers.append(BankOffer(
#                     bank_name=bank["name"],
#                     max_amount=round(max_amt, 2),
#                     roi=round(max(roi, 7.0), 2)
#                 ))
#         return offers

#     def reset(self) -> LoanState:
#         income = random.uniform(20000, 150000)
#         score = random.randint(300, 850)
        
#         # Offers generate karna
#         offers = self.get_bank_offers(score, income)
        
#         self.current_state = LoanState(
#             income=income,
#             credit_score=score,
#             loan_amount=random.uniform(5000, 50000),
#             age=random.randint(18, 70),
#             available_offers=offers,
#             is_fraud=random.random() < 0.1 if self.difficulty == "hard" else False
#         )
#         return self.current_state

#     def _get_ground_truth(self) -> int:
#         # Agar koi bank offer de raha hai, toh technically approve hona chahiye
#         return 1 if len(self.current_state.available_offers) > 0 and not self.current_state.is_fraud else 0

#     def step(self, action: LoanAction):
#         correct_decision = self._get_ground_truth()
#         reward = 1.0 if action.decision == correct_decision else -1.0
#         done = True 
#         return self.current_state, reward, done