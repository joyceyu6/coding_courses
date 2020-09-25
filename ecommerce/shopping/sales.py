# executing modules as scripts
# load once and cache
print("sales initialized", __name__)  # __name__
# command + p or cntl + p windows
print("Sales")


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":  # if run by this own module
    print("sales started")
    calc_tax()
'''return:
sales initialized __main__
Sales
sales started
'''
