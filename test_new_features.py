# Test file for new features
def testbooleans():
    x = True
    y = False
    return x

def testbuiltins(num):
    return abs(num)

def testlen():
    arr = [1, 2, 3]
    return len(arr)

def testround():
    return round(3.14)

print testbooleans()
print testbuiltins(-5)
print testlen()
print testround()