import time
num=int(input("A number from which the count down will start:"))
while num > 0:
    print(num)
    time.sleep(1)
    num -= 1

print ("Time's up")
