
import pytest


def test_any_and_all():
    assert any([1, 2, 3])
    assert any(["hello", [], 42])
    assert not any([])

    assert all([1, 2, 3])
    assert not all(["hello", [], 42])
    assert all([])


def tag(name, *content, cls=None, **attrs):
    if cls:
        attrs['class'] = cls

    prefix = '<' + name + ''.join(f' {k}="{attrs[k]}"' for k in sorted(attrs))

    if content:
        return '\n'.join(f'{prefix}>{item}</{name}>' for item in content)
    else:
        return prefix + '/>'


def test_function_arguments():
    assert tag('a', cls='home') == '<a class="home"/>'
    assert tag('p', 'hello', 'world', cls='content') \
        == '<p class="content">hello</p>\n<p class="content">world</p>'
    assert tag('pre', 'alpha', 'beta', cls='python', a='a', z='z') == \
        r'''<pre a="a" class="python" z="z">alpha</pre>
<pre a="a" class="python" z="z">beta</pre>'''


def test_keyword_only_arguments():
    def f(a, *, b):
        return a + b

    with pytest.raises(TypeError):
        f(2, 3)

    assert f(2, b=3) == 5
    assert f(b=3, a=2) == 5


def test_function_annotations():
    def calc(name:str, value:'int > 0'=42) -> str: # noqa
        return f'{name}: {value}'

    from inspect import signature
    sig = signature(calc)

    assert sig.parameters['name'].annotation == str
    assert sig.parameters['value'].annotation == 'int > 0'
    assert sig.return_annotation == str


def test_itemgetter():
    data = (
        ('alice', 24, 'dogs'),
        ('bob', 50, 'cats'),
    )

    from operator import itemgetter

    first = itemgetter(0)
    second = itemgetter(1)
    last = itemgetter(-1)

    assert second(first(data)) == 24
    assert ','.join(first(i) for i in sorted(data, key=last)) == 'bob,alice'
    assert itemgetter(0, -1)(first(data)) == ('alice', 'dogs')


def test_attrgetter():
    from collections import namedtuple
    Fav = namedtuple('Fav', 'animal color')
    Person = namedtuple('Person', 'name age fav')

    data = Person('alice', 24, Fav('dogs', 'blue'))

    from operator import attrgetter

    assert attrgetter('name')(data) == 'alice'
    assert attrgetter('name', 'age')(data) == ('alice', 24)
    assert attrgetter('fav.color')(data) == 'blue'


def test_methodcaller():
    from operator import methodcaller

    upper = methodcaller('upper')
    hiphenate = methodcaller('replace', ' ', '-')

    assert upper('hello') == 'HELLO'
    assert hiphenate('home sweet home') == 'home-sweet-home'


def test_partial():
    from functools import partial
    p_content = partial(tag, 'p', cls='content')

    assert p_content('hello') == '<p class="content">hello</p>'
