def main():
    l = [0] * 11
    sign = -1
    n = 1
    while n < 11:
        l[n] = sign * (n*2+1)
        sign = sign * -1
        n = n + 1

    n = 1
    while n < 11:
        print(l[n])
        n = n + 1

    i = 1
    while i < 11:
        j = i
        min_index = i
        while j < 11:
            if l[j] < l[min_index]:
                min_index = j
            j = j + 1

        temp = l[i]
        l[i] = l[min_index]
        l[min_index] = temp

        i = i + 1

    print("*****")
    n = 1
    while n < 11:
        print(l[n])
        n = n + 1


main()
