

import calculator

def setup_module(module):
    print("\nsetup_module called")

def teardown_module(module):
    print("\nteardown_module called")

def setup_function(function):
    print("\nsetup_function called")

def teardown_function(function):
    print("\nteardown_function called")

def test_add(numbers, resource):
    a, b = numbers
    assert calculator.add(a, b) == 15

def test_sub(numbers):
    a, b = numbers
    assert calculator.sub(a, b) == 5
