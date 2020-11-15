num=float(input("enter a number"))
last_two= num%100
ones_digit=last_two%10
tens_digit=(last_two-ones_digit)//10
sum_of_the_last_two_digits = ones_digit+tens_digit
print(sum_of_the_last_two_digits)
