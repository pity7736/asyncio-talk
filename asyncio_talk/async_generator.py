
async def generator(to):
    print('init generator')
    for i in range(to + 1):
        yield i
