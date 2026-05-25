def calculate_tax(amount, tax_percent):
    return (tax_percent / 100) * amount

def apply_late_fee(amount, days_late):
    if days_late > 30:
        return amount + (0.10 * amount)
    return amount
