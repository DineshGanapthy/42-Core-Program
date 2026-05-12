def input_temperature(temp_str: str) -> int:
    """ Just Inputs """
    print(f"Input data is '{temp_str}'")
    temp_str = int(temp_str)
    return temp_str

def test_temperature() -> None:
    """Test The previous function with diffrent values"""
    tests = ["25", "abc"]
    try:
        print("=== Garden Temperture ===\n")
        for t in tests:
            try:
                num = input_temperature(t)
                print(f"Temperture is now {num}℃")    
                print()    
            except ValueError as e:
                print("Caught input_temperature error:", e)
    finally:
        print()
        print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()


#def input_temperature(temp_str: str) -> int:
  #  """ Just Inputs """
  #  print(f"Input data is '{temp_str}'")
  #  temp_str = int(temp_str)
  #  try: 
  #      int(temp_str)
 #   except ValueError as exc:
  #      raise ValueError(f"Caught input_temperature error: invalid literal for int() with base 10: '{temp_str}'\n")
  #  else:
  #   print(f"Temperture is now {temp_str}℃")    
 #   print()
 #   return temp_str