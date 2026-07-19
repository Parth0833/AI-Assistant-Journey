# Accept inputs from the user
a = int(input("Enter sub 1 marks: "))
b = int(input("Enter sub 2 marks: "))
c = int(input("Enter sub 3 marks: "))
d = int(input("Enter sub 4 marks: "))
e = int(input("Enter sub 5 marks: "))

# Pass marks as arguments to calculate total
def calc_total(a, b, c, d, e):
    total = a + b + c + d + e
    print("Total Marks Scored are:", total)
    return total

# Pass the total score to calculate average
def calc_avg(total):
    avg = total / 5
    print("Average marks are:", avg)
    return avg

# Pass the total score to calculate percentage (assuming max 100 marks per subject)
def calc_percentage(total):
    percent = (total / 500) * 100
    print("The percent obtained is:", percent)
    return percent

# Main display function coordinates data flow
def display_result(a, b, c, d, e):
    total_score = calc_total(a, b, c, d, e)
    calc_avg(total_score)
    calc_percentage(total_score)

# Run the display function
display_result(a, b, c, d, e)
