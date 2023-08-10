from typing import Dict


class BankStatementFinalResultResponse:
    def __init__(self, period: Dict[str, str], account_name: str, account_number: str, total_turn_over_credit: float,
                 total_turn_over_debits: float,
                 opening_balance: float, closing_balance: float, average_monthly_balance: float, excel_file_path: str):
        self.account_number = account_number
        self.excel_file_path = excel_file_path
        self.average_monthly_balance = average_monthly_balance
        self.closing_balance = closing_balance
        self.opening_balance = opening_balance
        self.total_turn_over_debits = total_turn_over_debits
        self.total_turn_over_credit = total_turn_over_credit
        self.account_name = account_name
        self.period = period
