import doctest


def test():
    return doctest.testfile("README.rst", optionflags=doctest.REPORT_ONLY_FIRST_FAILURE + doctest.ELLIPSIS)

if __name__ == '__main__':
    print test()
