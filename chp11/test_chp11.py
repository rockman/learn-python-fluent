
import pytest
from collections import abc


def test_partial_interface():

    class Foo:
        def __init__(self, value):
            self.value = value

        def __getitem__(self, pos):
            return self.value[pos]

    foo = Foo("hello")

    assert foo[-1] == 'o'
    assert [i for i in foo]  # iteration works
    assert 'l' in foo
    assert 'x' not in foo


def test_no_need_to_register_abc():

    class Foo:
        def __len__(self):
            return 42

    assert isinstance(Foo(), abc.Sized)


def test_fail_to_implement_abc():

    class Foo(abc.Sized):
        pass

    with pytest.raises(TypeError):
        Foo()
