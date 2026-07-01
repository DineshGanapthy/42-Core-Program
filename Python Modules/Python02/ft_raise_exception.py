def input_temperature(temp_str: str) -> int:
    """ Just Inputs """
    print(f"Input data is '{temp_str}'")
    temp_int = int(temp_str)
    if temp_int >= 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    if temp_int <= 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    return temp_int


def test_temperature() -> None:
    """Test The previous function with diffrent values"""
    tests = ["25", "abc", "100", "-50"]
    try:
        print("=== Garden Temperture Checker ===\n")
        for t in tests:
            try:
                num = input_temperature(t)
                print(f"Temperture is now {num}°C")
            except ValueError as e:
                print("Caught input_temperature error:", e)
            print()
    finally:
        print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
