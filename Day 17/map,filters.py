#Maps()
numbers = [1,2,3,4,5,6]
result = map(lambda x:x*2,numbers)
print(list(result))

#Filters()
numbers = [1,2,3,4,5,6]
result1 = filter(lambda x:x%2==0,numbers)
print("All the even numbers are:",list(result1))

#map()   → Transform data
#filter() → Select data