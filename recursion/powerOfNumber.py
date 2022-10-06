def powerOfNumber(base, exp):
    assert exp >= 0 and int(exp) == exp, 'Number must be + integer only.'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * powerOfNumber(base, exp-1)

print(powerOfNumber(-2,2))