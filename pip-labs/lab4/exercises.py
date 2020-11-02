import collections
import os
import sys


def exercise1():
    """
    Să se scrie o funcție ce primeste un singur parametru, director,
    ce reprezintă calea către un director.
    Funcția returnează o listă cu extensiile unice sortate crescator (in
    ordine alfabetica) a fișierelor din directorul dat ca parametru.
    Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
    :return:
    """
    director = r"C:\Python39\DLLs"

    def solution1():
        extensions = {
            os.path.splitext(item)[1].strip(".")
            for item in os.listdir(director)
            if os.path.isfile(os.path.join(director, item)) and "." in item}

        return list(sorted(extensions))

    def solution2():
        extensions = {
            item.name.split(".")[-1]
            for item in os.scandir(director)
            if item.is_file() and "." in item.name}

        return list(sorted(extensions))

    print(solution1())
    print(solution2())


def exercise2():
    """
    Să se scrie o funcție ce primește ca argumente două căi: director si
    fișier.
    Implementati functia astfel încât în fișierul de la calea fișier să fie
    scrisă pe câte o linie, calea absolută a fiecărui fișier din interiorul
    directorului de la calea folder, ce incepe cu litera A.
    :return:
    """
    director = r"C:\Python39\DLLs"
    fisier = "fisere"

    def solution1():
        paths = [
            item.path for item in os.scandir(director)
            if item.is_file() and item.name.lower().startswith("a")]

        with open(fisier, 'w') as fd:
            for path in paths:
                fd.write(f"{os.path.abspath(path)}\n")

    print(solution1())


def exercise3():
    """
    Să se scrie o funcție ce primește ca parametru un string my_path.
    Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele
    20 de caractere din conținutul fișierului. Dacă parametrul reprezintă
    calea către un director, se va returna o listă de tuple (extensie,
    count), sortată descrescător după count, unde extensie reprezintă
    extensie de fișier, iar count - numărul de fișiere cu acea extensie.
    Lista se obține din toate fișierele (recursiv) din directorul dat ca
    parametru.
    :return:
    """
    my_path = r"C:\Python39\LICENSE.txt"

    def solution1():
        if os.path.isfile(my_path):
            to_read = min([20, os.stat(my_path).st_size])
            with open(my_path, 'rb') as fd:
                # there can be negative 'seeks' if the file is open in 'rb' mode
                fd.seek(-to_read, os.SEEK_END)
                return fd.read().decode()  # make the result a string

        extensions = collections.defaultdict(lambda: 0)
        for (root, _, file_names) in os.walk(my_path):
            for filename in file_names:
                ext = os.path.splitext(filename)[1]
                extensions[ext] += 1

        return list(sorted(extensions.items(), key=lambda x: 1 / x[1]))

    print(solution1())


def exercise4():
    """
    Să se scrie o funcție ce returnează o listă cu extensiile unice a
    fișierelor din directorul dat ca argument la linia de comandă (
    nerecursiv). Lista trebuie să fie sortată crescător.
    Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu
    are extensie, deci nu va apărea în lista finală.
    :return:
    """
    director = sys.argv[1]

    def solution1():
        extensions = set()
        for name in os.listdir(director):
            if not os.path.isfile(os.path.join(director, name)):
                continue

            extensions.add(os.path.splitext(name)[1])

    print(solution1())


def exercise5():
    """
    Să se scrie o funcție care primește ca argumente două șiruri de
    caractere, target și to_search și returneaza o listă de fișiere care
    conțin to_search. Fișierele se vor căuta astfel: dacă target este un
    fișier, se caută doar in fișierul respectiv iar dacă este un director se
    va căuta recursiv in toate fișierele din acel director. Dacă target nu
    este nici fișier, nici director, se va arunca o excepție de tipul
    ValueError cu un mesaj corespunzator.
    :return:
    """
    target = r"C:\Python39\Lib\urllib"
    to_search = "User-Agent"

    def search_in_file(file, to_search):
        if not isinstance(to_search, bytes):
            to_search = to_search.encode()

        with open(file, 'rb') as fd:
            chunk_size = len(to_search)
            first_chunk = fd.read(chunk_size)

            while first_chunk:
                second_chunk = fd.read(chunk_size)
                if to_search in first_chunk + second_chunk:
                    return True
                first_chunk = second_chunk

    def solution1():
        abs_target = os.path.abspath(target)
        if not (os.path.isfile(abs_target) or os.path.isdir(abs_target)):
            raise Exception("Invalid target file/folder")

        if os.path.isfile(target) and search_in_file(abs_target, to_search):
            return [abs_target]

        output = []
        for (root, directories, files) in os.walk(abs_target):
            for file in files:
                fpath = os.path.join(root, file)
                if search_in_file(fpath, to_search):
                    output.append(fpath)

        return output

    print(solution1())


def exercise6():
    """
    Să se scrie o funcție care are același comportament ca funcția de la
    exercițiul anterior, cu diferența că primește un parametru în plus: o
    funcție callback, care primește un parametru, iar pentru fiecare eroare
    apărută în procesarea fișierelor, se va apela funcția respectivă cu
    instanța excepției ca parametru
    :return:
    """
    target = r"C:\Python39\\Lib\urllib"
    to_search = "User-Agent"

    def custom_callback(exception):
        print(f"This is custom exception handling: {exception}")

    def search_in_file(file, to_search):
        if not isinstance(to_search, bytes):
            to_search = to_search.encode()

        with open(file, 'rb') as fd:
            chunk_size = len(to_search)
            first_chunk = fd.read(chunk_size)

            while first_chunk:
                second_chunk = fd.read(chunk_size)
                if to_search in first_chunk + second_chunk:
                    return True
                first_chunk = second_chunk

    def solution1(callback):
        abs_target = os.path.abspath(target)
        if not (os.path.isfile(abs_target) or os.path.isdir(abs_target)):
            raise Exception("Invalid target file/folder")

        try:
            if os.path.isfile(target) and search_in_file(abs_target, to_search):
                return [abs_target]

            output = []
            for (root, directories, files) in os.walk(abs_target):
                for file in files:
                    fpath = os.path.join(root, file)
                    if search_in_file(fpath, to_search):
                        output.append(fpath)

            return output
        except Exception as e:
            callback(e)

    print(solution1(custom_callback))


def exercise7():
    """
    Să se scrie o funcție care primește ca parametru un șir de caractere care
    reprezintă calea către un fișer si returnează un dicționar cu următoarele
    cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea
    fisierului in octeti, file_extension = extensia fisierului (daca are) sau
    "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.
    :return:
    """
    file_path = r"readonly.txt"

    def solution1():
        return {
            'full_path': os.path.abspath(file_path),
            'file_size': os.stat(file_path).st_size,
            'file_extenison': os.path.splitext(file_path)[1],
            'can_read': os.access(file_path, os.R_OK),
            'can_write': os.access(file_path, os.W_OK),
        }

    print(solution1())


def exercise8():
    """
    Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest
    parametru reprezintă calea către un director aflat pe disc. Funcția va
    returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina
    directorului dir_path.

    Exemplu apel funcție: functie("C:\\director") va returna [
    "C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]

    Calea "C:\\director" are pe disc următoarea structură:

    C:\\director\\fisier1.txt <- fișier

    C:\\director\\fisier2.txt <- fișier

    C:\\director\\director1 <- director

    C:\\director\\director2 <- director
    :return:
    """
    dir_path = r"C:\Python39"

    def solution1():
        abs_path = os.path.abspath(dir_path)
        return [item.path for item in os.scandir(abs_path) if item.is_file()]

    print(solution1())
