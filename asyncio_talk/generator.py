
def generator(items):
    print('init generator')
    for item in items:
        print('item', item)
        yield item
