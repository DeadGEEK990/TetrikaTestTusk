import pytest
from .solution import to_intervals, clip_interval, intersect, merge_intervals, appearance


def test_to_intervals():
    assert to_intervals([1, 2, 3, 4]) == [(1, 2), (3, 4)]
    assert to_intervals([5, 10]) == [(5, 10)]
    assert to_intervals([]) == []

def test_clip_interval():
    assert clip_interval((5, 15), (0, 10)) == (5, 10)
    assert clip_interval((0, 20), (5, 15)) == (5, 15)
    assert clip_interval((5, 15), (10, 12)) == (10, 12)

def test_intersect():
    assert intersect((1, 5), (3, 7)) == (3, 5)
    assert intersect((1, 5), (6, 7)) is None

def test_merge_intervals():
    assert merge_intervals([(1, 3), (2, 4)]) == [(1, 4)]
    assert merge_intervals([(5, 6), (7, 8)]) == [(5, 6), (7, 8)]
    assert merge_intervals([(1, 2)]) == [(1, 2)]

@pytest.mark.parametrize("intervals, expected", [
    (
        {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702807, 1594704542],
            'tutor': [1594702749, 1594705148]
        },
        1735
    ),
    (
        {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395],
            'tutor': [1594663290, 1594663430]
        },
        54
    ),
    (
        {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066]
        },
        33
    )
])
def test_appearance(intervals, expected):
    assert appearance(intervals) == expected
