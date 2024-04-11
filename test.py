import json
from first_task import convolve
import numpy as np

def convolve_from_file(file_name):
    with open(file_name, 'rb') as f:
        data = json.load(f)

    test_cases = data.get('examples', [])
    results = []

    for idx, case in enumerate(test_cases, start=1):
        input_data = case.get('input')
        expected_output = case.get('expected_output')
        function_name = case.get('function_name')

        if function_name is None:
            raise ValueError(f"Function name is missing for test case {idx}")

        # Получение функции по имени
        func = getattr(np, function_name) if hasattr(np, function_name) else globals().get(function_name) #проверяем на наличие функции в библиотеке numpy или уже в "глобальном" поиске

        if func is None:
            raise ValueError(f"Function '{function_name}' is not defined for test case {idx}")

        try:
            result = convolve(input_data, func)
            error = None

            # Проверка на соответствие ожидаемому результату
            if result != expected_output:
                raise ValueError("Expected output does not match actual output")
                
        except Exception as e:
            result = None
            error = str(e)

        results.append((result, error))

    return results

if __name__ == "__main__":
    test_file = 'examples.json'
    results = convolve_from_file(test_file)
    for idx, (result, error) in enumerate(results):
        print(f"Test case {idx}:")
        if error is not None:
            print(f"Error occurred: {error}")
        else:
            print(f"Test completed. Result: {result}")
        print()
