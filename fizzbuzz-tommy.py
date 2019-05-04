fizz = 5
buzz = 7
pop = 9
done = False

for i in range(1,100):
    done = False
    if i % fizz == 0:
        print("Fizz")
        done = True
    if i % buzz == 0:
        print("Buzz")
        done = True
    if i % pop == 0:
        print("Pop")
        done = True
    if not done:
        print(i)
