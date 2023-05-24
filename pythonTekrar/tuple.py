#Tuple konu tekrarı

""" Python tuple (demet), değiştirilemez ve sıralı bir veri koleksiyonudur.
Tuple, parantezler içinde virgülle ayrılmış öğelerden oluşur.
Tuple'lar, listelere benzer, ancak farkları, tuple'ların değiştirilemez olmasıdır.
Yani, bir tuple oluşturduktan sonra, öğeleri değiştiremez veya ekleyemezsiniz.
"""

"""" değiştirilemez ve sıralı bir veri tipidir
(1,2,3) bir Tuple örneğidir..

"""

tuple_veritipi = (1,2,3,3,4,5,6)
#ilk elemanı bulma.
print(tuple_veritipi[0])

# 2. indeksten sonraki elemanları yazdır.
print(tuple_veritipi [2:])

#tuple içerisinde 3 den kaçtane var.

print(tuple_veritipi.count(3))

tuple_xyz = (1,2,3)
x,y,z=tuple_xyz
print(x,y,z)
