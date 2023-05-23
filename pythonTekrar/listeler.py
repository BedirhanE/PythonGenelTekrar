#python liste işlemleri.
"""
-bileşik veri türüdür ve çok yönlüdür
-liste , köşeli parantez içine alınmış ve virgülle ayrılmış ögeler içerir
-[1,2,5,"elma","armut",12.8]
-farklı veri tiplerini içerisinde barındırabilir.
"""
#görüntü işlemede resimlerimizi bir listede depolayabiliriz, görüntülere nesne tespiti yapabiliriz.
liste=[1,2,3,4,5,6]
print(type(liste))

haftanın_günleri=["pazartesi","salı","çarşamba","perşembe","cuma","cumaretsi","pazar"]
print(haftanın_günleri[0]) #ilk eleman.
print(haftanın_günleri[0:7:1])#listedeki tüm elemanları getirme.
print(haftanın_günleri[0:7:2])#başlangıç,bitiş ve artış miktarı.
print(haftanın_günleri[6]) #son eleman.
print(len(haftanın_günleri))#listenin boyutu.
print(haftanın_günleri[7:0:-1])#tersten yazdırma işlemi.
print(haftanın_günleri[-1])#listenin sonundaki eleman.
print(haftanın_günleri[1:4:1])#haftanın 2., 3. ,4. günlerini yazdırma işlemi.

#sayı listesi işlemleri (ekleme , çıkarma )
sayı_listesi=[1,2,3,4,5,6]
sayı_listesi.append(7) #listeye eleman ekleme.
print(sayı_listesi)
sayı_listesi.remove(4) #listeden eleman çıkarma
print(sayı_listesi)


sayı_listesi.reverse() #listeyi ters cevirme.
print(sayı_listesi)
liste=[1,5,87,41,11]
liste.sort() #listeyi sıralama işlemi (küçükten büyüğe sıralama).
print(liste)
liste.sort(reverse=True)#listeyi büyükten küçüğe sıralama işlemi.
print(liste)