k = int(input('Please enter an integer k(1<=k<=1000): '))

powers = 1
for i in range(1001):
    # exit from the loop, to exclude unnecessary work of the loop
    if i > k:
        break
    if 10**powers < i:
        powers += 1
    # sum of narcissistic numbers
    narcissisticNumbSum = 0
    # a string showing the sum of the narcissistic numbers
    printList = []
    # whole part of division
    divWholePart = i

    while divWholePart > 0:
        # get remainder of division
        # last digit of numbers
        divRemainder = divWholePart % 10

        narcissisticNumbSum += divRemainder ** powers

        # conversion for rendering information
        listOfDivRemainderInPower = [divRemainder, "^", powers]

        # get the new integer part of the narcissistic number
        divWholePart //= 10

        if len(printList) > 0:
            listOfDivRemainderInPower.append(" + ")
            listOfDivRemainderInPower.extend(printList)

        printList = listOfDivRemainderInPower

    if i and i == narcissisticNumbSum:
        print("Narcissistic number: ", i, " = ", end='')
        for j in printList:
            print(j, end='')
        print("")
