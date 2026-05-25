from app import calculate_tax, apply_late_fee

def test_calculate_tax_standard():
    result = calculate_tax(1000, 18)
    assert result == 180.0

def test_calculate_tax_zero():
    result = calculate_tax(1000, 0)
    assert result == 0.0

def test_apply_late_fee_charged():
    result = apply_late_fee(1000, 31)
    assert result == 1100.0

def test_apply_late_fee_not_charged():
    result = apply_late_fee(1000, 15)
    assert result == 1000.0
