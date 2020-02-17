class LoanDecision():
    """
    Validates the loan decision according to the requested amount
        Parameters:
            requested_amount: requested amount for the loan
        Return:
            response:   'Approved' if requested_amount < 50000
                        'Declined' if requested_amount > 50000
                        'Undecided' if requested_amount = 50000
    """
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
