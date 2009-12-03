Python Code Completation
========================

1. Dado um contexto, a inicial da linha ou variavel e o número da linha - Retorna as opções para completar código python:
    >>> from pycodecompletation import complete
    >>> complete("""#teste.py
    ... class Testando:
    ...     "class 'dummy' de teste"
    ... """, "Test", line=3)
    [{'info': 'class  dummy  de teste', 'word': 'ando', 'abbr': 'Testando'}]
    >>> complete("""#teste.py
    ... class Testando:
    ...     "class 'dummy' de teste"
    ...     def foo(self):
    ...         "Foo"
    ...     def bar(self):pass
    ... """, "Testando.f", 6)
    [{'info': 'Foo', 'word': 'oo(', 'abbr': 'foo()'}]

2. Deveria completar um import de um módulo:
    >>> complete("""import os.path""", "os.path.getsi", 2)
    [{'info': 'Return the size of a file, reported by os.stat().', 'word': 'ze(', 'abbr': 'getsize(filename)'}]

3. Não completa código utilizando from:
    >>> complete("""from os.path import""", "from os.path import get", 2)
    []

