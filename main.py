'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  """
  Determina daca un numar este prim
  :param n: nr. intreg
  :return: True daca numarul e prim sau False daca numarul nu este prim
  """
  if n < 2:
    return False
  else:
    for i in range( 2 , n // 2 + 1 ):
      if n % i == 0:
        return False
  return True

assert is_prime(3) is True
assert is_prime(13) is True
assert is_prime(4) is False
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  """
  Returneaza produsul numerelor dintr-o lista
  :param lst:
  :return: un numar intreg care este produsul numerelor dintr-o lista
  """
  a = 1
  for i in lst:
    a = a * i
  return a
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  """
  Determina cmmdc a doua numere
  :param x: nr intreg
  :param y: nr intreg
  :return: cel mai mare divizor comun a doua numere care e o valoare intreaga
  """
  if x == y:
    return x
  while x != y:
    if x > y:
      x = x - y
    else:
      y = y -x
  return x

  assert get_cmmdc_v1(12 , 8) == 4
  assert get_cmmdc_v1(20 , 16) == 4
  assert get_cmmdc_v1(10 , 35) == 5
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  """
  Determina cmmdc a doua numere
  :param x: nr intreg
  :param y: nr intreg
  :return: o valoare intreaga care este cmmdc sau -1 in cazul in care ambele numere sunt egale cu 0
  """
  if x == 0:
    if y == 0:
      return -1
    else:
      return y
  else:
    r = x % y
    while r > 0:
      x = y
      y = r
      r = x % y
  return y

  assert get_cmmdc_v2(12, 8) == 4
  assert get_cmmdc_v2(20, 16) == 4
  assert get_cmmdc_v2(10, 35) == 5


  
  
def main():

  while True:
    print("1. Det daca un numar este prim")
    print("2. Calculati produsul numerelor dintr-o lista")
    print("3. Determinati cmmdc a doua numere")
    print("4. Determinati cmmdc a doua numere")
    print("5. Iesire")

    optiune = input("Selectati optiune: ")
    if optiune == "1":
      numar = int(input("Introduceti numarul: "))
      print(is_prime(numar))
    elif optiune == "2":
      lst = []
      n = int(input("Introduceti numarul de elemente: "))
      print("Introduceti elementele: ")
      for i in range(0,n):
        i = int(input())
        lst.append(i)
      print("Produsul elementelor din lista este egal cu: ")
      print(get_product(lst))
    elif optiune == "3":
      numar2 = int(input("Introduceti numarul: "))
      numar3 = int(input("Introduceti numarul: "))
      print("Cel mai mare divizor comun a celor doua numere este: ")
      print(get_cmmdc_v1(numar2 , numar3))
    elif optiune == "4":
      numar4 = int(input("Introduceti numarul: "))
      numar5 = int(input("Introduceti numarul: "))
      print("Cel mai mare divizor comun al celor doua numere este: ")
      print(get_cmmdc_v2(numar4 , numar5))
    elif optiune == "5":
      break
    else:
      print("Optiune gresita! Va rugam sa selectati alta optiune.")





if __name__ == '__main__':
  main()
