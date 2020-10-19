def exercise1():
    """
    Find The greatest common divisor of multiple numbers read from the console.
    :return:
    """
    numbers = input("Insert numbers:")  # numbers separated by spaces

    def gcd(number1, number2):
        while number1 != number2:
            if number1 > number2:
                number1 -= number2
            else:
                number2 -= number1
        return number1

    def solution1(numbers):
        numbers = [int(i) for i in numbers.split(" ")]

        return max([i for i in range(1, numbers[0] + 1) if (
                len([x for x in numbers if (x % i == 0)]) == len(numbers))])

    def solution2(numbers):
        numbers = [int(i) for i in numbers.split(" ")]

        current_gcd = gcd(numbers[0], numbers[1])
        for number in numbers[2:]:
            current_gcd = gcd(current_gcd, number)

        return current_gcd

    print(solution1(numbers))
    print(solution2(numbers))


def exercise2():
    """
    Write a script that calculates how many vowels are in a string.
    :return:
    """

    string = "Ana are MERE!"

    def solution1():
        return len([chr for chr in string if chr in "aeiouAEIOU"])

    def solution2():
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        count = 0
        for c in string:
            if c in vowels:
                count += 1

        return count

    def solution3():
        word = string.lower()
        return word.count('a') + word.count('e') + word.count('i') + word.count(
            'o') + word.count('u')

    print(solution1())
    print(solution2())
    print(solution3())


def exercise3():
    """
    Write a script that receives two strings and prints the number of
    occurrences of the first string in the second.
    :return:
    """
    first_string = "abbabb"
    second_string = "abbabbabbabb"

    def solution1():
        return second_string.count(first_string)

    def solution2(first_string, second_string):
        val = second_string.find(first_string)
        nr = 0
        while val != -1:
            nr = nr + 1
            second_string = second_string[val + len(first_string):]
            val = second_string.find(first_string)

        return nr

    print(solution1())
    print(solution2(first_string, second_string))


def exercise4():
    """
    Write a script that converts a string of characters written in
    UpperCamelCase into lowercase_with_underscores.
    :return:
    """
    string = "HelloWorldCup"

    def solution1():
        my_string = string
        for char in my_string:
            if not char.isupper():
                continue

            if my_string.index(char) != 0:
                my_string = my_string.replace(char, '_{}'.format(char.lower()))
            else:
                my_string = my_string.replace(char, char.lower())

        return my_string

    def solution2():
        new_string = ""
        nr_of_letters = 1

        for i in range(0, len(string)):
            if string[i].isupper():
                new_string += string[i - nr_of_letters:i].lower()
                if i != 0:
                    new_string += "_"

                nr_of_letters = 1
            else:
                nr_of_letters = nr_of_letters + 1

        new_string += string[len(string) - nr_of_letters:len(string)].lower()
        return new_string

    def solution3():
        result = ''.join(
            ["_" + chr.lower() if chr.isupper() else chr for chr in string])

        return result[1:] if result[0] == '_' else result

    def solution4():
        converted_string = ""
        for i in range(0, len(string)):
            if 'A' <= string[i] <= 'Z' and i > 0:
                converted_string = converted_string + '_' + string[i].lower()
            else:
                converted_string = converted_string + string[i].lower()
        return converted_string

    print(solution1())
    print(solution2())
    print(solution3())
    print(solution4())


def exercise5():
    """
    Given a square matrix of characters write a script that prints the string
    obtained by going through the matrix in spiral order (as in the example):
    firs      1  2  3  4    =>   first_python_lab
    n_lt      12 13 14 5
    oba_      11 16 15 6
    htyp      10 9  8  7
    :return:
    """

    matrix = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p']
    ]

    def first_line(matrix):
        return matrix[1:], matrix[0]

    def last_line(matrix):
        return matrix[:-1], (matrix[-1])[-1::-1]

    def left_row(matrix):
        new_matrix = []
        output = ""
        for line in matrix:
            output += line[0]
            new_matrix.append(line[1:])
        return new_matrix, output[-1::-1]

    def right_row(matrix):
        new_matrix = []
        output = ""
        for line in matrix:
            output += line[-1]
            new_matrix.append(line[:-1])
        return new_matrix, output

    def solution1():
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        dirrection = 0

        while top <= bottom and left <= right:
            if dirrection == 0:
                for i in range(left, right + 1):
                    print(matrix[top][i], end=" ")
                top += 1
            elif dirrection == 1:
                for i in range(top, bottom + 1):
                    print(matrix[i][right], end=" ")
                right -= 1
            elif dirrection == 2:
                for i in range(right, left - 1, -1):
                    print(matrix[bottom][i], end=" ")
                bottom -= 1
            elif dirrection == 3:
                for i in range(bottom, top - 1, -1):
                    print(matrix[i][left], end=" ")
                left += 1

            dirrection = (dirrection + 1) % 4

    def solution2(matrix):
        output_string = ""
        index = 0
        while matrix is not None:
            if index == 0:
                matrix, word = first_line(matrix)
            elif index == 1:
                matrix, word = right_row(matrix)
            elif index == 2:
                matrix, word = last_line(matrix)
            else:
                matrix, word = left_row(matrix)
            index = (index + 1) % 4
            output_string += word
            if not matrix:
                break
        return output_string

    print(solution1())
    matrix = "firs,n_lt,oba_,htyp"
    print(solution2(matrix.split(",")))


def exercise6():
    """
    Write a function that validates if a number is a palindrome.
    :return:
    """
    number = 123432

    def solution1():
        x = str(number)
        return x == x[::-1]

    print(solution1())


def exercise7():
    """
    Write a function that extract a number from a text (for example if the
    text is "An apple is 123 USD", this function will return 123, or if the
    text is "abc123abc" the function will extract 123). The function will
    extract only the first number that is found.
    :return:
    """
    string = "An apple is 123 USD. 3"

    def solution1():
        n = len(string)
        i = 0
        while i < n:
            if '0' <= string[i] <= '9':
                ans = ""
                while i < n and '0' <= string[i] <= '9':
                    ans += string[i]
                    i += 1
                print(ans)
                break
            else:
                i += 1

    print(solution1())


def exercise8():
    """
    Write a function that counts how many bits with value 1 a number has. For
    example for number 24, the binary format is 00011000, meaning 2 bits with
    value "1"
    :return:
    """
    number = 24

    def solution1():
        bit_index = 0
        count = 0
        while (1 << bit_index) <= number:
            if ((1 << bit_index) & number) != 0:
                count = count + 1
            bit_index = bit_index + 1
        return count

    def solution2():
        x = bin(number)
        return x[2:].count('1')

    print(solution1())
    print(solution2())


def exercise9():
    """
    Write a functions that determine the most common letter in a string. For
    example if the string is "an apple is not a tomato", then the most common
    character is "a" (4 times). Only letters (A-Z or a-z) are to be
    considered. Casing should not be considered "A" and "a" represent the
    same character.
    :return:
    """
    string = "an apple is not a tomatoaa"

    def solution1():
        letter_dict = dict()
        current_most_common_letter = string[0]
        for letter in string:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
            if letter_dict[letter] > letter_dict[current_most_common_letter]:
                current_most_common_letter = letter
        print(current_most_common_letter)
        return current_most_common_letter

    print(solution1())


def exercise10():
    """
    Write a function that counts how many words exists in a text. A text is
    considered to be form out of words that are separated by only ONE space.
    For example: "I have Python exam" has 4 words.
    :return:
    """
    string = "I have Python exam"

    def solution1():
        return len(string.split(' '))

    print(solution1())
