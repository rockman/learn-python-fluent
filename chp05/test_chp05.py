
def test_any_and_all():
    assert any([1, 2, 3]) == True
    assert any(["hello", [], 42]) == True
    assert any([]) == False

    assert all([1, 2, 3]) == True
    assert all(["hello", [], 42]) == False
    assert all([]) == True


