'''
Nama : Fadhil Anwar Ahsani
Kelas : 1A - RPL
NIM : 2407136
'''

name = str(input("Name: "))
gender = input("Gender (L/P): ").lower()
age = int(input("Age (Number): "))
height = float(input("Height (in cm): "))
iq = int(input("IQ: "))

success = name + " diprediksi dapat menjadi Model Catwalk"
fail = name + " Tidak dapat menjadi Model Catwalk"

if(gender == "l" and 18 <= age <= 25):
    print("L")

    if(height > 175):

        if(iq >= 130):
            print(success)
        else:
            print(f"IQ({iq}), {fail}. Karena IQ anda tidak memenuhi persyaratan yaitu IQ 130++")

    else:
            print(f"Tinggi({height}cm), {fail} Karena Tinggi anda tidak memenuhi persyaratan yaitu min.175cm untuk Pria")

        
elif(gender == "p" and 18 <= age <= 25):

    if(height > 170):

        if(iq >= 130):
            print(success)
        else:
            print(f"IQ({iq}), {fail}. Karena IQ anda tidak memenuhi persyaratan yaitu IQ 130++")

    else:
        print(f"Tinggi({height}cm), {fail} Karena Tinggi anda tidak memenuhi persyaratan yaitu min.170cm untuk Wanita")

else:
    print(f"Umur anda({age}) tidak memenuhi persyaratan minimum yaitu 18-25th")

     

    

