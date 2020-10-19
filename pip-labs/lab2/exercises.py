def exercise1():
    """
    Write a function to return a list of the first n numbers in the Fibonacci
    string.
    :return:
    """
    n = 7

    def solution1():
        fibList = []
        if n <= 0:
            return 'wrong input'
        if n == 1:
            fibList.append(0)
        if n == 2:
            fibList.append(0)
            fibList.append(1)
        if n > 2:
            fibList.append(0)
            fibList.append(1)
            a = 0
            b = 1
            i = 3
            while i <= n:
                fibList.append(a + b)
                aux = b
                b = a + b
                a = aux
                i += 1
        return fibList

    def solution2():
        fibonnaci = []
        fibonnaci.append(0)
        fibonnaci.append(1)
        for index in range(0, n - 2):
            fibonnaci.append((fibonnaci[index] + fibonnaci[index + 1]))
        return fibonnaci

    print(solution1())
    print(solution2())


def exercise2():
    """
    Write a function that receives a list of numbers and returns a list of
    the prime numbers found in it.
    :return:
    """
    numbers = [1, 5, 12, 58, 70, 11]

    def solution1():
        return [x for x in numbers if prime(x) == True]

    def prime(x):
        if x < 2:
            return False
        for d in range(2, int(x / 2)):
            if x % d == 0:
                return False
        return True

    print(solution1())


def exercise3():
    """
     Write a function that receives as parameters two lists a and b and
     returns: (a intersected with b, a reunited with b, a - b, b - a)
    :return:
    """
    a = [1, 2, 3, 5, 6]
    b = [4, 5, 6, 7]

    def solution1():
        intersect = [_a for _a in a if _a in b]
        union = list(set(a[:] + b[:]))
        diff1 = [_a for _a in a if _a not in b]
        diff2 = [_b for _b in b if _b not in a]
        return intersect, union, diff1, diff2

    def solution2():
        intersection = [x for x in a if x in b]
        union = a[:]
        union += [x for x in b if x not in a]
        a_b = [x for x in a if x not in b]
        b_a = [x for x in b if x not in a]

        return intersection, union, a_b, b_a

    print(solution1())
    print(solution2())


def exercise4():
    """
    Write a function that receives as a parameters a list of musical notes (
    strings), a list of moves (integers) and a start position (integer). The
    function will return the song composed by going though the musical notes
    beginning with the start position and following the moves given as
    parameter.
    Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will
    return ["mi", "fa", "do", "sol", "re"]
    :return:
    """
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start = 2

    def solution1():
        n = len(notes)
        current = start
        result = [notes[current % n]]
        for move in moves:
            current = current + move
            result = result + [notes[current % n]]
        return result

    print(solution1())


def exercise5():
    """
    Write a function that receives as parameter a matrix and will return the
    matrix obtained by replacing all the elements under the main diagonal
    with 0 (zero).
    :return:
    """
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    def solution1():
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i > j:
                    matrix[i][j] = 0

        return matrix

    print(solution1())


def exercise6():
    """
    Write a function that receives as a parameter a variable number of lists
    and a whole number x. Return a list containing the items that appear
    exactly x times in the incoming lists.
    Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists
    [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1
    and 2.
    :return:
    """
    x = 2
    args = ([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])

    def solution1():
        my_all = [el for my_list in args for el in my_list]
        return list(set(filter(lambda el: my_all.count(el) == x, my_all)))

    def solution2():
        big_list = []
        rs = []
        for i in args:
            big_list += i
        for i in big_list:
            if big_list.count(i) == x and i not in rs:
                rs.append(i)
        return rs

    print(solution1())
    print(solution2())


def exercise7():
    """
    Write a function that receives as parameter a list of numbers (integers)
    and will return a tuple with 2 elements. The first element of the tuple
    will be the number of palindrome numbers found in the list and the second
    element will be the greatest palindrome number.
    :return:
    """

    numbers = [111, 121, 1131, 131]

    def is_palindrome(number):
        return str(number) == str(number)[::-1]

    def solution1():
        palindromes = [x for x in numbers if is_palindrome(x)]
        n_of_palindromes = len(palindromes)
        max_palindrome = max(palindromes)
        return n_of_palindromes, max_palindrome

    print(solution1())


def exercise8():
    """
    Write a function that receives a number x, default value equal to 1,
    a list of strings, and a boolean flag set to True. For each string,
    generate a list containing the characters that have the ASCII code
    divisible by x if the flag is set to True, otherwise it should contain
    characters that have the ASCII code not divisible by x.
    Example: x = 2, ["test", "hello", "lab002"], flag = False will return ([
    "e", "s"], ["e" . Note: The function must return list of lists.
    :return:
    """
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = False

    def solution1():
        big_string = [c for string in strings for c in string]
        if flag:
            return [string for string in big_string if ord(string) % x == 0]
        return [string for string in big_string if ord(string) % x != 0]

    def solution2():
        chr_list = []
        for cuv in strings:
            for c in cuv:
                if c not in chr_list:
                    if flag:
                        if ord(c) % x == 0:
                            chr_list.append(chr)
                    else:
                        if ord(c) % x != 0:
                            chr_list.append(chr)

        return chr_list

    def solution3():
        def is_valid(char):
            return (ord(char) % x and not flag) or (not ord(char) % x and flag)

        return [[char for char in string if is_valid(char)] for string in
                strings]

    print(solution1())
    print(solution2())
    print(solution3())


def exercise9():
    """
    Write a function that receives as paramer a matrix which represents the
    heights of the spectators in a stadium and will return a list of tuples (
    line, column) each one representing a seat of a spectator which can't see
    the game. A spectator can't see the game if there is at least one taller
    spectator standing in front of him. All the seats are occupied. All the
    seats are at the same level. Row and column indexing starts from 0,
    beginning with the closest row from the field.
    Example:

    # FIELD

    [[1, 2, 3, 2, 1, 1],

    [2, 4, 4, 3, 7, 2],

    [5, 5, 2, 5, 6, 4],

    [6, 6, 7, 6, 7, 5]]

    Will return : [(2, 2), (3, 4), (2, 4)]
    :return:
    """

    matrix = [[1, 2, 3, 2, 1, 1],
              [2, 4, 4, 3, 7, 2],
              [5, 5, 2, 5, 6, 4],
              [6, 6, 7, 6, 7, 5]]

    def solution1():
        output = []
        for index_j in range(len(matrix[0])):
            last_big = matrix[0][index_j]
            for index_i in range(1, len(matrix)):
                if last_big >= matrix[index_i][index_j]:
                    output.append((index_i, index_j))
                else:
                    last_big = matrix[index_i][index_j]
        return output

    print(solution1())


def exercise10():
    """
    Write a function that receives a variable number of lists and returns a
    list of tuples as follows: the first tuple contains the first items in
    the lists, the second element contains the items on the position 2 in the
    lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(
    1.5, "a ") ,(5, 6, "b"), (3,7, "c")].

    Note: If input lists do not have the same number of items, missing items
    will be replaced with None to be able to generate max ([len(x) for x in
    input_lists]) tuples.
    :return:
    """
    args = ([1, 2, 3, 4], [5, 6, 7], ["a", "b", "c", 'd', 'e'])

    def solution1():
        max_length = max([len(arg) for arg in args])
        args2 = [arg + [None] * (max_length - len(arg)) for arg in args]

        return list(zip(*args2))

    print(solution1())


def exercise11():
    """
    Write a function that will order a list of string tuples based on the 3rd
    character of the 2nd element in the tuple. Example: ('abc', 'bcd'),
    ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
    :return:
    """
    my_lists = [('abc', 'bcd'), ('abc', 'zza')]

    def solution1():
        return list(sorted(my_lists, key=lambda x: x[1][2]))

    def solution2():
        def sort(el):
            return el[1][2]

        return sorted(my_lists, key=sort)

    print(solution1())
    print(solution2())


def exercise12():
    """
    Write a function that will receive a list of words  as parameter and will
    return a list of lists of words, grouped by rhyme. Two words rhyme if
    both of them end with the same 2 letters.

    Example:
    group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [
    ['ana', 'banana'], ['carte', 'parte'], ['arme']]
    :return:
    """
    rhymes = ['ana', 'banana', 'carte', 'arme', 'parte']

    def solution1():
        ret = []
        for el in rhymes:
            ok = 0
            for i in range(len(ret)):
                if el[-2:] == ret[i][0][-2:]:
                    ret[i] += [el]
                    ok = 1
            if ok == 0:
                ret += [[el]]
        return ret

    def solution2():
        rhyme_dict = dict()
        for word in rhymes:
            if word[-2:] in rhyme_dict:
                if word not in rhyme_dict[word[-2:]]:
                    rhyme_dict[word[-2:]].append(word)
            else:
                rhyme_dict[word[-2:]] = [word]
        return list(rhyme_dict.values())

    print(solution1())
    print(solution2())
