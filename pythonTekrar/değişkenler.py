
#değişkenler
tamsayı_değişken =10  #tamsayı değişkenim.
ondalıklı_sayı=12.8  #double değişkenim.

print(tamsayı_değişken)
print(ondalıklı_sayı)

#dört işlemler temelden.
pi_sayısı=3.14
katsayı=2

toplam=pi_sayısı + 1
fark=pi_sayısı - 1
çarpma=pi_sayısı*2
bölme=pi_sayısı/katsayı

#print fonksiyonunu kullanarak 4 işlemi ekrana yazdırıyoruz.
print("Toplam:",toplam)
print("Farkları:",fark)
print("Çarpma:",çarpma)
print("Bölme:",bölme)


print(f"Toplam {toplam} ve fark {fark} değerleri")
print("Çarpma: %.3f , bölme: %4f" %(çarpma,bölme) )



#değişkenler arası dönüşüm işlemleri

int_çarpma=int(çarpma)#float to int
print(int_çarpma)

float_tamsayı_değişken=float(tamsayı_değişken)#int to float
print(float_tamsayı_değişken)

#Stringler : karakter dizileri

string="Merhaba Dünya"
print(string)

resim_yolu="veri" +"\\" + "image"+ ".png"
print("png uzantılı resim yolu: ",resim_yolu)