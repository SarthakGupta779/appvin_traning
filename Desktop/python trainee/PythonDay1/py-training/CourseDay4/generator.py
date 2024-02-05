def geb():
    for i in range(3):
        yield i
        print("hello")
a1=geb()
for i in a1:
    print(i)
    