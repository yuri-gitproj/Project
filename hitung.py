#kalkulator

in1 = int(input ("Masukkan Angka Pertama :"))
in2 = int(input ("Masukkan Angka Kedua :"))
in3 = input ("Pilih Operator :1.* 2.+ 3.- 4./")

if in3=="1":
    in4 = in1 * in2
    print (in1," x ",in2,"=",in4)

elif in3=="2":
    in4 = in1 + in2
    print (in1," + ",in2,"=",in4)

elif in3=="3":
    in4 = in1 - in2
    print (in1," - ",in2,"=",in4)

elif in3=="4":
    in4 = in1 / in2
    print (in1," / ",in2,"=",in4)

else:
    print ("Angka yang anda masukkan tidak ada")


    

