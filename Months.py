months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    try:
        number = int(input("Enter a number from 1 to 12: "))
    except:
        number = 0
    if 1 <= number <= 12:
        print(months[number - 1])
        break
