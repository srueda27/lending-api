class LoanDecision():
    def validate_loan(requested_amount):
        response = ''
        requested_amount = int(requested_amount) if requested_amount else 0

        if requested_amount > 50000:
            response = 'Declined'
        elif requested_amount == 50000:
            response = 'Undecided'
        elif requested_amount < 50000:
            response = 'Approved'

        return response
