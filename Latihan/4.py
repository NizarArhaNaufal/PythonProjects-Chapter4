# diketahui

s1 = 125
s2 = 256
v1 = 62
v2 = 72
x = 6.00
z = 0.75

jarakAkeB = s1
jarakBkeC = s2
kecepatanAkeB = v1
kecepatanBkeC = v2
mulai = x
istirahat = z

# waktu A ke B

t1 = s1/v1
print(s1,'/',v1,'=',t1)

# waktu B ke C

t2 = s2/v2
print(s2,'/',v2,'=',t2)

# total waktu

totalwaktu = t1 + t2 + z 
print(t1,'+',t2,'+',z,'=',totalwaktu)
totalwaktu = 6.321684587813619

# sampai pada pukul
sampai = x + totalwaktu
print(x,'+',totalwaktu,'=',sampai)
