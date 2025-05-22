class Cal():
    def add_num_and_double(self, x ,y):
        """ add and double
        >>> c = Cal()
        >>> c.add_num_and_double(1,1)
        4
        """
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # cal = Cal()
    # r = cal.add_num_and_double(1,1)
    # print(r)