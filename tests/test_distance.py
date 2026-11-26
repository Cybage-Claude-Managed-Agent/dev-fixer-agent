from src.distance import trip_miles


def test_single_leg():
    assert trip_miles([16.09344]) == 10.0


def test_total_of_all_legs():
    assert trip_miles([8.04672, 8.04672]) == 10.0
