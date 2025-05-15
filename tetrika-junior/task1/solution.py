def strict(func):
    def wrapper(*args, **kwargs):
        ann = func.__annotations__

        for i,(name, expected_type) in enumerate(ann.items()):
            if name == 'return':
                continue
            if i >= len(args):
                break
            if not isinstance(args[i], expected_type):
                raise TypeError(f'Ожидаются: {name} типа: {expected_type}, получено: {type(args[i])}')

        result = func(*args, **kwargs)
        return result
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))

