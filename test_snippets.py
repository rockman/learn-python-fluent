
# testing Python features from various snippets of the book


def test_for_else():
    flag = False
    for _ in range(10):
        pass
    else:
        flag = True

    assert flag

    for i in range(10):
        if i > 5:
            break
    else:
        assert False


def test_while_else():
    flag = False
    i = 10
    while i > 5:
        i -= 1
    else:
        flag = True

    assert flag

    i = 10
    while i > 5:
        if i % 7 == 0:
            break
        i -= 1
    else:
        assert False


def test_try_else():
    flag = False
    try:
        "hello" + "world"
    except TypeError:
        pass
    else:
        flag = True

    assert flag

    try:
        "hello" + 42
    except TypeError:
        pass
    else:
        assert False
