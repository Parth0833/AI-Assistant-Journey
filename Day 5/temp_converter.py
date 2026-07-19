def celcius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    print("celcius to fahrenhit is:", f)
    return f
def fahernhite_to_celcius(f):
    c = (f - 32) * 5/9
    print("fahrenheit to celcius is:", c)
    return c

celcius_to_fahrenheit(200)
fahernhite_to_celcius(500)
