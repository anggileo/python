import pandas as pd
from decimal import Decimal as D
import numpy as np
import scipy.stats

print("halo selamat datang di ANOVA")
print("silahkan masukkan rancangan acakmu, RAL, RAKL")
model = input("model rancanganmu?:[ral],[rakl]: ")
print("model acakmu memakai: ", model)

namafile = input("impor data csv, nama filenya?: ")
data = pd.read_csv(namafile)
print(data)


perlakuan = pd.unique(data.perlakuan.values)
b_anggota = (len(data.values))
b_perlakuan = (len(perlakuan))
b_ulangan = (b_anggota/b_perlakuan)


print(perlakuan)
print("_______________________________________________________________")
print(b_anggota, " anggota, ",b_perlakuan," perlakuan, ",D(b_ulangan), " ulangan")
print("_______________________________________________________________")




if(model == 'rakl'):
	print("analis varians: ")
	gt = (data['hasil'].sum())
	gt2 = (gt**2)
	p_u = (b_perlakuan * b_ulangan)
	fk =  gt2/p_u
	print("FK: ", fk)
	yktotal = (data['hasil'].values**2).sum() - fk
	print("YK total: ", yktotal)
	t_perlakuan = data.groupby(['perlakuan']).sum()
	ykperlakuan = ((t_perlakuan.values**2).sum()/b_ulangan) - fk
	print("YK perlakuan: ", ykperlakuan)
	sum_kelompok = data.groupby(['ulangan']).sum()
	pindahvariabel = sum_kelompok
	ykulangan = ((pindahvariabel['hasil'].values**2).sum()/b_perlakuan) - fk
	print("YKulangan: ", ykulangan)
	ykerror = yktotal-ykperlakuan-ykulangan
	print("YKerror: ", ykerror)
	bulangan = int(b_ulangan - 1)
	bperlakuan = int(b_perlakuan - 1)
	berror = int((bulangan)*(bperlakuan))
	btotal = (b_ulangan*b_perlakuan)-1
	ktulangan = ykulangan/bulangan
	ktperlakuan = ykperlakuan/bperlakuan
	kterror = ykerror/berror
	fhitperlakuan = ktperlakuan/kterror
	print("FhitPerlakuan: ",fhitperlakuan)
	ftab5 = scipy.stats.f.ppf(q=1-0.05, dfn=bperlakuan, dfd=berror)
	ftab1 = scipy.stats.f.ppf(q=1-0.01, dfn=bperlakuan, dfd=berror)
	print("Ftabel tingkat kesalahan 5%: ", ftab5)
	print("Ftabel tingkat kesalahan 1%: ", ftab1)
	if(fhitperlakuan > ftab5):
		print("dengan tingkat kepercayaan 95%, perlakuan ini berpengaruh nyata")
	if(fhitperlakuan > ftab1 ):
		print("dengan tingkat kepercayaan 99%, perlakuan ini berpengaruh nyata")
	if(fhitperlakuan < ftab5):
		print("dengan tingkat kepercayaan 95%, perlakuan ini tidak berpengaruh nyata")
	if(fhitperlakuan < ftab1):
		print("dengan tingkat kepercayaan 99%, perlakuan ini tidak berpengaruh nyata")





elif(model == 'ral'):
	print("analis varians: ")
	gt = (data['hasil'].sum())
	gt2 = (gt**2)
	p_u = (b_perlakuan * b_ulangan)
	fk =  gt2/p_u
	print("FK: ", fk)
	yktotal = (data['hasil'].values**2).sum() - fk
	print("YK total: ", yktotal)
	t_perlakuan = data.groupby(['perlakuan']).sum()
	ykperlakuan = ((t_perlakuan.values**2).sum()/b_ulangan) - fk
	ykerror = yktotal-ykperlakuan
	print("YK error: ", ykerror)
	bulangan = int(b_ulangan - 1)
	bperlakuan = int(b_perlakuan - 1)
	berror = int((b_ulangan-1)*b_perlakuan)
	btotal = (b_ulangan*b_perlakuan)-1
	ktperlakuan = ykperlakuan/bperlakuan
	kterror = ykerror/berror
	fhitperlakuan = ktperlakuan/kterror
	print("FhitPerlakuan: ",fhitperlakuan)
	ftab5 = scipy.stats.f.ppf(q=1-0.05, dfn=bperlakuan, dfd=berror)
	ftab1 = scipy.stats.f.ppf(q=1-0.01, dfn=bperlakuan, dfd=berror)
	print("Ftabel tingkat kesalahan 5%: ", ftab5)
	print("Ftabel tingkat kesalahan 1%: ", ftab1)
	if(fhitperlakuan > ftab5):
		print("dengan tingkat kepercayaan 95%, perlakuan ini berpengaruh nyata")
	if(fhitperlakuan > ftab1 ):
		print("dengan tingkat kepercayaan 99%, perlakuan ini berpengaruh nyata")
	if(fhitperlakuan < ftab5):
		print("dengan tingkat kepercayaan 95%, perlakuan ini tidak berpengaruh nyata")
	if(fhitperlakuan < ftab1):
		print("dengan tingkat kepercayaan 99%, perlakuan ini tidak berpengaruh nyata")


else:
	print("ouchhh model belum dibuat")



