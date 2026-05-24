# Homework-1-Python-Basics-and-Unit-Testing-with-Pytest
This repository contains the solution for Homework 1 of Course Testing and Implementation of IS, focusing on writing basic Python functions and testing them using the `pytest` framework.

## Author Information
* **Name:** Nyoman Adi Arya Subakti
* **NIM:** 2415091013
* **Class:** SI4IKI

---

## Files Included

1. **`homework1_2415091013.ipynb`**
   The main Jupyter/Colab notebook for the assignment. This file contains the complete workflow for Homework 1, including the creation of the functions, the implementation of the test cases, and the test execution results.
2. **`my_math_testing.ipynb`**
   A practice notebook completed together with the lecturer during a Zoom session. This file serves as a learning material exploring `pytest` concepts, such as testing basic math functions, handling exceptions (`pytest.raises`), and using parameterized tests (`@pytest.mark.parametrize`).
3. **`homework1.py`** The core Python script generated from the homework notebook, containing the required logical functions.
4. **`test_homework1.py`** The test script generated from the homework notebook, containing the unit tests to verify the accuracy of the functions in `homework1.py`.

---

## Implemented Functions in Homework 1

The `homework1.py` file includes the following functions:

* `calculate_average(numbers)`: Calculates the average of a list of numbers. Returns `0` if the list is empty.
* `find_max(numbers)`: Finds and returns the maximum value in a list of numbers. Returns `None` if the list is empty.
* `count_vowels(text)`: Counts the total number of vowels (a, i, u, e, o, A, I, U, E, O) in a given string.
* `is_prime(n)`: Determines whether a given integer `n` is a prime number. Returns `True` if prime, otherwise `False`.

---

## Testing Coverage

The `test_homework1.py` covers multiple test scenarios based on the assignment instructions:

* **List Operations (`calculate_average`, `find_max`):** Tested against normal lists, empty lists, lists with a single element, and lists containing negative numbers.
* **String Operations (`count_vowels`):** Tested with lowercase words (`hello`, `bacod`), uppercase words (`HELLO`), empty strings (`""`), and all-vowel strings (`aiueoAIEOU`).
* **Math Operations (`is_prime`):** Tested with specific edge cases and numbers: 2, 3, 4, 17, 1, 0, -2, and -5.

---

## How to Run the Tests

To run the unit tests on your local machine, follow these steps:

1. Ensure Python is installed on your system.
2. Install the `pytest` library if you haven't already:
   ```bash
   pip install pytest
