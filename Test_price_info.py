from price_info import total_cost_shopping, cost_of_fruits

def test_total_cost_shopping():
    expected_total = 46.75
    result = total_cost_shopping()
    assert round(result, 2) == expected_total

def test_cost_of_fruits():
    result = cost_of_fruits('apple', 10)
    assert result is not None
    assert round(result, 2) == 12.00
    assert round(cost_of_fruits('pear', 3), 2) == 2.70
    assert cost_of_fruits('banana', 5) is None  # Fruit not in list
