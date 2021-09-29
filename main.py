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
  # codul vostru aici
  return True
  
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
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  """
  Determina cmmdc a doua numere
  :param x: nr intreg
  :param y: nr intreg
  :return: o valoare intreaga care este cmmdc
  """
  return True
  
  
def main():
  # interfata de tip consola aici

  n=int(input("Introduceti numar: "))
  print(is_prime(n))

if __name__ == '__main__':
  main()
