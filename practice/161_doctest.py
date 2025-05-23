class Cal():
    def add_num_and_double(self, x ,y):
        """ add and double
        >>> c = Cal()
        >>> c.add_num_and_double(1, 1)
        4

        >>> c.add_num_and_double('1', '1')
        Traceback (most recent call last):
        ...
        TypeError
        """
        # テスト結果から引数はintで受け取る必要があるとわかるため条件を追加
        if type(x) is not int or type(y) is not int:
            raise TypeError
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # cal = Cal()
    # r = cal.add_num_and_double(1,'1')
    # print(r)