class Cal():
    def add_num_and_double(self, x ,y):
        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    cal = Cal()
    r = cal.add_num_and_double(1,1)
    print(r)