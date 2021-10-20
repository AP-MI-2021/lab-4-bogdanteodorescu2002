def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def number_of_even (lst):
    '''
    Determina numarul de numere pare dintr-o lista
    :param lst: lista initiala de intregi
    :return: numarul de numere pare dintr-o lista
    '''
    num = 0
    for i in lst:
        if i % 2 == 0:
            num += 1
    return num

def intersection(lst1, lst2):
    '''
    Determina intersectia a doua liste
    :param lst1: prima lista de intregi
    :param lst2: a doua lista de intregi
    :return: a treia lista, care reprezinta intersectia dintre cele doua
    '''
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def palindrome(element):
    '''
    Determina daca un numar este palindrom sau nu
    :param element: numarul care se verifica
    :return: True, daca numarul este palindrom, False, daca nu
    '''
    n = len(element)
    for i in range(0, n//2):
        if element[i] != element[n-i-1]:
            return False
    return True

def concatenate(num1, num2):
    '''
    Functia concateneaza doi intregi, transformandu-i in str, si apoi rezultatul inapoi in intreg
    :param num1: primul intreg
    :param num2: al doilea intreg
    :return: Se returneaza intregul format in urma concatenarii
    '''
    z = int(str(num1) + str(num2))
    return z

def index_concatenate (lst1, lst2):
    '''
    Functia returneaza o lista
    :param lst1: prima lista de intregi
    :param lst2: a doua lista de intregi
    :return: lista concatenata
    '''
    maxim = 0
    iconcat = []
    if len(lst1) > len(lst2):
        maxim = len(lst1)
    else:
        maxim = len(lst2)
    for i in range (0, maxim):
        for j in range (0, maxim):
            if i == j:
                iconcat.append(concatenate(lst1[i], lst2[j]))
    return iconcat

def reverse (num):
    '''
    Functia returneaza inversul unui intreg
    :param num: intreg initial
    :return: intregul inversat
    '''
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

def div(lst1, lst2):
    lst3 = []
    for i in range(0, len(lst1)):
        for j in range (0, len(lst2)):
            if lst1[i] % lst2[j] == 0:
                lst3.append(reverse(lst1[i]))
            else:
                lst3.append(lst1[i])
    return lst3

if __name__ == '__main__':
    finish = False
    while not finish:
        print("0. Citire a doua liste")
        print("1. Numar de pare")
        print("2. Intersectia listelor")
        print("3. Concat")
        print("x. Iesiti din program")
        option = input("Dati optiunea: ")
        if option == '0'
            l1 = citireLista()
            l2 = citireLista()
        if option == '1':
            l1 = citireLista()
            l2 = citireLista()
            if number_of_even(l1) == number_of_even(l2):
                print("Listele au acelasi numar de elemente pare")
            else:
                print("Listele nu au acelasi numar de elemente pare")
            # test_get_largest_prime_below()
        elif option == '2':
            l1 = citireLista()
            l2 = citireLista()
            print("Intersectia celor doua liste este..")
            print(intersection(l1, l2))
        elif option == '3':
            l1 = citireLista()
            l2 = citireLista()
            print("Nu am reusit sa rezolv pana la final")
        elif option == '4':
            l1 = citireLista()
            l2 = citireLista()
            l3 = citireLista()
            print("Nu am reusit sa rezolv pana la final")
        elif option == 'x':
            finish = True
        else:
            print("Optiunea nu este valida")


