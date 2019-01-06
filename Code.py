answers = []
possible = []

for prime in range(2, 101):
    is_prime = True
    for i in range(2, prime):
        if prime % i == 0:
            is_prime = False
    if is_prime:
        print("Prime number to test: " + str(prime))

        string_prime = str(prime)

        prime_length = len(string_prime)
        print("Prime_length: " + str(prime_length))

        if prime_length == 2:

            list_digits_prime = list(string_prime)

            print("The list of digits in current prime: " + str(list_digits_prime))

            product_prime = 1

            for digit_prime in list_digits_prime:
                product_prime = product_prime * int(digit_prime)

            print("Product of digits of product_prime: " + str(product_prime))

            not_qualified = False
            print("Setting not_qualified to: " + str(not_qualified))

            for smaller_num in range(1, prime):
                print("Now testing smaller_num: " + str(smaller_num))

                string_smaller_num = str(smaller_num)
                list_digits_smaller_num = list(string_smaller_num)

                product_smaller_num = 1

                for digit_smaller_num in list_digits_smaller_num:
                    product_smaller_num = product_smaller_num * int(digit_smaller_num)

                print("Product of digits of smaller_num: " + str(product_smaller_num))

                if product_prime != product_smaller_num:
                    print("Appending prime to possible: " + str(prime))
                    possible.append(prime)
                else:
                    not_qualified = True
                    print("Prime did not qualify. \n")
                    possible.clear()
                    break

            if not not_qualified:
                possible = list(dict.fromkeys(possible))
                answers.append(str(possible))
                print("Appending prime to answers: " + str(possible) + "\n")
                possible.clear()

        else:
            print("Prime did not qualify. \n")

print(answers)
