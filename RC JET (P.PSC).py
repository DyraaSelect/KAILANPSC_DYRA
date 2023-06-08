jenis_komponen = ["mmpf form 5*1000*500mm","control horn","push rod wire","linkage stopper","esc (sw50a)","servo 9g","rc upo battery","propeller","brushless motor","carpon fiber rod 3mm","receiver (ia10b rx)","flysky-16x remote control"]
harga_komponen = [23,3,2,12,67,5.20,57.56,5.50,15.79,25.30,61,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]
   
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("***************************UNIVERSE******************************")
print("~~~~~~~~~~~~~~~~~~~~~~ZIERA,DANNY,HANNA~~~~~~~~~~~~~~~~~~~~~~~")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print("HARGA MMPF FORM 5*1000*500mm=RM23,CONTROL HORN=RM3,PUSH ROD WIRE=RM2,LINKAGE STOPPER=RM12,ESC (SW50A)=RM67,SERVO 9g=RM5.20,RC UPO BATTERY=RM57.56,PROPELLER=RM5.50,BRUSHLESS MOTOR=RM5.79,CARPON FIBER ROD 3mm=RM25.30,RECEIVER (IA10B RX)=RM61,FLYSKY-16X REMOTE CONTROL=RM161")
a=int(input("Masukkan kuantiti untuk mmpf form 5*1000*500mm:"))
b=int(input("Masukkan kuantiti untuk control horn:"))
c=int(input("Masukkan kuantiti untuk push rod wire:"))
d=int(input("Masukkan kuantiti untuk linkage stopper:"))
e=int(input("Masukkan kuantiti untuk esc (sw50a):"))
f=float(input("Masukkan kuantiti untuk servo 9g:"))
g=float(input("Masukkan kuantiti untuk rc upo battery:"))
h=float(input("Masukkan kuantiti untuk propeller:"))
i=float(input("Masukkan kuantiti untuk brushless motor:"))
j=float(input("Masukkan kuantiti untuk carpon fiber rod 3mm:"))
k=int(input("Masukkan kuantiti untuk receiver (ia10b rx):"))
l=int(input("Masukkan kuantiti untuk flysky-16x remote control:"))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,l]

def jumlah_harga ():
    for i in range(4):
        jumlah[i] = harga_komponen[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nKuantiti anda ialah:")
    print(a,"komponen", jenis_komponen[0])
    print(b,"komponen", jenis_komponen[1])
    print(c,"komponen", jenis_komponen[2])
    print(d,"komponen", jenis_komponen[3])
    print(e,"komponen", jenis_komponen[4])
    print(f,"komponen", jenis_komponen[5])
    print(g,"komponen", jenis_komponen[6])
    print(h,"komponen", jenis_komponen[7])
    print(i,"komponen", jenis_komponen[8])
    print(j,"komponen", jenis_komponen[9])
    print(k,"komponen", jenis_komponen[10])
    print(l,"komponen", jenis_komponen[11])

    print("\n Jumlah harga untuk komponen ialah RM",sum (jumlah))
jumlah_harga()
cetak()
