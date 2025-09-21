# Extended Features Documentation

This document describes the new features added to the miniPython compiler.

## New Features Added

### 1. Proper Boolean Literals
- **True** and **False** (capitalized) instead of **true** and **false**
- Can be assigned to variables and used in expressions
- Type checking recognizes BOOLEAN type

Example:
```python
x = True
y = False
print x  # prints True
print y  # prints False
```

### 2. Additional Built-in Functions

#### abs(expression)
Returns the absolute value of a number
```python
print abs(-5)     # Valid
print abs(3.14)   # Valid
```

#### len(identifier) 
Returns the length of a list
```python
arr = [1, 2, 3]
print len(arr)    # Valid
```

#### round(expression)
Rounds a number to the nearest integer
```python
print round(3.14)  # Valid
print round(2.7)   # Valid
```

### 3. String Concatenation with + Operator
- Strings can now be concatenated using the + operator
- Both operands must be strings (enforced by type checker)
- Mixed type addition (number + string) produces an error

Example:
```python
x = "Hello"
y = " World"
z = x + y     # Valid: string concatenation
print z       # prints "Hello World"

# Error cases:
a = 5
b = "test"
c = a + b     # Error: mixed types not allowed
```

## Type System Updates
- Added BOOLEAN type for True/False values
- Enhanced ADD operation to support both:
  - NUMBER + NUMBER = NUMBER
  - STRING + STRING = STRING
- Type checking prevents mixed-type addition

## Backward Compatibility
All existing miniPython code remains compatible. The changes are purely additive and don't break existing functionality.

## Testing
All new features have been tested and work correctly with the existing semantic analysis framework.