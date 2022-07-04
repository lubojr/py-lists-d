from homework1.pets_letter import pets_begin_d

def test_hw1_empty():
    input_f = []
    result = pets_begin_d(input_f)
    assert result == []


def test_hw1_contains_d():
    input_f = ['d', 'dd', 'tiger']
    result = pets_begin_d(input_f)
    assert result == ['d', 'dd']

def test_hw1_standard_input():
    input_f = ['Dog', 'cat', 'dolphin', 'rabbit', 'snake']
    result = pets_begin_d(input_f)
    assert result == ['dolphin']

# def test_hw1_heterogenous_input():
#     input_f = ['', 183, None, True, 'dog']
#     result = pets_begin_d(input_f, 'd')
#     assert result == ['dog']


