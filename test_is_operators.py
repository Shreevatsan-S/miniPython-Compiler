# Test new comparison operators
x = 5
y = 5
z = 10

# Test is operator
if x is y:
    print "x is y"

# Test is not operator  
if x is not z:
    print "x is not z"

# Test existing comparisons still work
if x == y:
    print "x equals y"

if x != z:
    print "x not equals z"