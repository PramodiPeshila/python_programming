#Play FizzBuzz game.print Fizz for numbers divide by 3.Print Buzz for Numbers divide by 5.Print FizzBuzz for numbers divide by both 3 and 5 and else print the number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
