import pytest

# function to be tested
def fuzzy_math(num1, operator, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception("we need to do fuzzy math on ints")
    
    if operator == "+":
        result = num1 + num2
    elif operator == "*":
        result = num1 * num2
    else:
        raise Exception(f"I dont know to do math with '{operator}'")
    
    if result < 0:
        return "a negative number"
    elif result < 10:
        return "a small number"
    elif result < 20:
        return "a medium number"
    else:
        return "a large number"
    
print(fuzzy_math(3, "+", 4))

# unit tests
class TestFuzzyMath:
    
    def test_non_int_input_for_num1_A(self):
        error = None
        try:
            fuzzy_math('hi', '+', 2)
        except Exception as e:
            error = e
        assert error is not None

    def test_non_int_input_for_num1_B(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math('hi', '+', 2)
        assert 'fuzzy math on ints' in str(exc_info)

    def test_non_int_input_for_nusm2(self):
        pass

    def test_addition_with_negative_result(self):
        pass

    def test_addition_with_small_result(self):
        assert fuzzy_math(2, '+', 2) == "a small number"
        # both are similar
        assert 'small number' in fuzzy_math(2, '+', 2)
        
    def test_addition_with_medium_result(self):
        assert fuzzy_math(7, '+', 8) == "a medium number"
        # # both are similar
        assert 'medium number' in fuzzy_math(7, '+', 8)

    def test_addition_with_large_result(self):
        assert fuzzy_math(17, '+', 18) == "a large number"
        # # both are similar
        assert 'large number' in fuzzy_math(17, '+', 18)

    def test_multiplication_with_negative_result(self):
        pass

    def test_multiplication_with_small_result(self):
        pass

    def test_multiplication_with_medium_result(self):
        pass

    def test_multiplication_with_large_result(self):
        pass

    def test_invalid_operator(self):
        pass
