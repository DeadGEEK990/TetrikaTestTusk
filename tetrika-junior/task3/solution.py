def to_intervals(lst):
    return [(lst[i], lst[i + 1]) for i in range(0, len(lst), 2)]

def clip_interval(interval, bounds):
    start, end = interval
    return max(start, bounds[0]), min(end, bounds[1])

def intersect(a, b):
    start = max(a[0], b[0])
    end = min(a[1], b[1])
    if start < end:
        return (start, end)
    return None

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals['lesson']
    pupil_intervals = [clip_interval(p, lesson) for p in to_intervals(intervals['pupil'])]
    tutor_intervals = [clip_interval(t, lesson) for t in to_intervals(intervals['tutor'])]

    pupil_intervals = [p for p in pupil_intervals if p[0] < p[1]]
    tutor_intervals = [t for t in tutor_intervals if t[0] < t[1]]

    overlaps = []
    for p in pupil_intervals:
        for t in tutor_intervals:
            o = intersect(p, t)
            if o:
                overlaps.append(o)

    merged = merge_intervals(overlaps)
    total = sum(end - start for start, end in merged)
    return total


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        print(f'i:{i}|test_answer: {test_answer}')
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'