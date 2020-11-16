def hammingEncoder(data):
    """
    Function to encode a stream of data bits using Hamming code
    :param data:
    :return:
    """
    if all(char in '01' for char in data) and data != "":
        # Initialize encoded string
        print("Data to be encoded = ", data)
        datalist = list(data)
        result = ""
        datalistcopy = list(data)

        pwr = 0
        exp = 0
        count = 0
        length = len(datalist)
        while pwr < length:
            pwr = 2 ** exp
            exp += 1
            count += 1
            length += 1

        checkbits = count - 1
        for i in range(checkbits):
            pos = (2 ** i) - 1
            datalist.insert(pos, '*')
            datalistcopy.insert(pos, '*')

        check = 1
        # parity_list = []
        checkbits = []
        while check <= len(datalist):
            lst = []
            for i in range(check - 1, len(datalist), 2 * check):
                lst.extend(datalist[i:i + check])
            check *= 2
            # parity_list.extend(lst)
            print("Before parity:")
            print(lst)
            counter = 0
            for u in range(1, len(lst)):
                if lst[u] == "1":
                    counter += 1
            if counter % 2 == 0:
                lst[0] = "0"
                checkbits += "0"
            else:
                lst[0] = "1"
                checkbits += "1"
            print("After parity:")
            print(lst)

        print("Printing checkbits: ")
        print(checkbits)

        c = 0
        for e in range(0, len(datalist)):
            if datalist[e] == "*":
                result += checkbits[c]
                c += 1
            else:
                result += datalist[e]
        print(datalistcopy)
        return result

    else:
        return "Error: Input must be binary!"


# hammingEncoder('01001111')
print(hammingEncoder('10'))
