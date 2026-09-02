numbers =[5, 12, 8, 21, 30, 7, 18]

filtered_numbers=filter(lambda x: x>10, numbers)

squared_numbers = map(lambda x: x**2,filtered_numbers)

sorted_numbers = sorted(squared_numbers,key=lambda x: x)

def result_generator(data_list):
    for num in data_list:
        yield num

gen = result_generator(sorted_numbers)

for result in gen:
    print(result)
    