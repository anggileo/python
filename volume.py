print("jalan normal di python3")
print("halo selamat datang di VOLUME")
x = input("mau dibuat encer atau pekat? jawab: [encer:1|pekat:2]")


class warna:
	biru='\033[94m'
	cyan='\033[96m'
	hijau='\033[92m'
	bold='\033[1m'
	underline='\033[4m'
	tutup='\033[0m'
print(x)
if (x=='1'):
	encerkonsentrasiawal = float(input("masukkan konsentrasi awal: "))
	print (encerkonsentrasiawal)
	encerkonsentrasiingin = float(input("masukkan konsentrasi yang diinginkan: "))
	print (encerkonsentrasiingin)
	encervolumeingin = float(input("masukkan volume yang diinginkan: "))
	print (encervolumeingin)
	encerjawab=(encerkonsentrasiingin*encervolumeingin)/encerkonsentrasiawal
	print(f"{warna.hijau}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{warna.tutup}")
	print("ambil bahan awal sebanyak ", encerjawab, " lalu tambah air sampai volume akhirnya 	", encervolumeingin )
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	encerperluair= encervolumeingin-encerjawab
	print("perlu tambahan air sebanyak ", encerperluair)
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	encerbanding1=encerjawab/encerjawab
	encerbanding2=encerperluair/encerjawab
	print(encerbanding1," bahan awal		:	 ",encerbanding2," air")	
	print(f"{warna.hijau}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{warna.tutup}")

if (x=='2'):
	print("kasus untuk melarutkan nadcc 1 tabletnya 1000 ppm, agar menjadi x ppm perlu air berapa?")
	pekatkonsentrasiawal=float(input("masukkan konsentrasi awal: "))
	print(pekatkonsentrasiawal)
	pekatvolumeawal=float(input("masukkan volume awal: "))
	print(pekatvolumeawal)
	pekatkonsentrasiingin=float(input("masukkan konsentrasi yang diinginkan: "))
	print(pekatkonsentrasiingin)
	pekatjawab=(pekatkonsentrasiawal*pekatvolumeawal)/pekatkonsentrasiingin
	print("diperlukan air sebanyak " ,pekatjawab, "untuk membuat bahan akhir dengan konsentrasi " ,pekatkonsentrasiingin )

