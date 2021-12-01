from day1 import load_data, count_growth, part_b


def test_load_data():
    data = load_data('test_data.txt')
    assert data == [199,
                    200,
                    208,
                    210,
                    200,
                    207,
                    240,
                    269,
                    260,
                    263]

def test_count_growth():
    data = load_data('test_data.txt')
    count = count_growth(data)
    assert count == 7

def test_part_b():
    data = load_data('test_data.txt')
    count = part_b(data, 3)
    assert count == 5
