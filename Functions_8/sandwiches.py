def items(*args):
    print('\nYour sandwich is preparing using')
    for arg in args:
        print(f"\t-{arg}")

items('chicken', 'extra cheese', 'chille')
items('beef', 'yogurt')


