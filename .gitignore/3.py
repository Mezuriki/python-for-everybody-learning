summ = int(0)
count = int(0)
list = []

while True:
    try:
        a = input("enter a number or Enter to finish: ")
        if a:
            summ = summ + int(a)
            count += 1
            list.append(a)
        else:
            print("numbers: ", list)
            print("count = ", count)
            print("summ = ", summ)
            print("lowest = ", min(list))
            print("highest = ", max(list))
            print("mean = ", summ / count)
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break