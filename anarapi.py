import pandas as pd
from decimal import Decimal as D
import numpy as np
import scipy.stats
import math

print("halo selamat datang di ANOVA")
print("silahkan masukkan rancangan acakmu, RAL, RAKL,RALFAKTORIAL, RAKLFAKTORIAL")
model = input("model rancanganmu?:[ral],[rakl],[ralfak],[raklfak]: ")
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
	print()
	print("======+")
	print("ANOVA |")
	print("================================================================================")
	print("sv		db		kt		fhit		ftab 0.05")
	print("================================================================================")
	print("prlkn		",bperlakuan,"		",round(ktperlakuan,3),"	",round(fhitperlakuan,3),"	",ftab5)
	print("ulngn		",bulangan,"		",round(ktulangan,3),"		",round(fhitperlakuan,3),"	")
	print("error		",berror,"		",round(kterror,3))
	print("total		",btotal,"		")
	print("================================================================================")




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
	print()
	print("======+")
	print("ANOVA |")
	print("================================================================================")
	print("sv		db		kt		fhit		ftab 0.05")
	print("================================================================================")
	print("prlkn		",bperlakuan,"	",round(ktperlakuan,3),"	",round(fhitperlakuan,3),"	",ftab5)
	print("error		",berror,"	",round(kterror,3))
	print("total		",btotal,"	")
	print("================================================================================")

elif(model=='raklfak'):
	b_anggota = len(data.values)
	b_perlakuan = len(pd.unique(data.perlakuan.values))
	b_ulangan = len(pd.unique(data.ulangan.values))

	fk=((data['hasil'].sum())**2)/(b_perlakuan*b_ulangan)
	print("fk: ",fk)
	yktotal=(data['hasil'].values**2).sum() - fk
	print("yk total: ",yktotal)
	ykperlakuan =((((data.groupby(['perlakuan']).sum()).values**2).sum())/b_ulangan)-fk
	print("ykperlakuan :",ykperlakuan)
	ykulangan=((((data.groupby(['ulangan']).sum()).values**2).sum())/b_perlakuan)-fk
	print("ykulangan: ", ykulangan)
	ykerror=yktotal-ykperlakuan-ykulangan
	print("yk error: ",ykerror)
	ykfaktor1 = (((data.groupby(['faktor1']).sum()).values**2).sum()/(len(data.groupby(['faktor2']).sum())*b_ulangan))-fk
	print("ykfaktor1: ", ykfaktor1)
	ykfaktor2 = (((data.groupby(['faktor2']).sum()).values**2).sum()/(len(data.groupby(['faktor1']).sum())*b_ulangan))-fk
	print("ykfaktor2: ",ykfaktor2)
	ykfaktor1xfaktor2 = ykperlakuan-ykfaktor1-ykfaktor2
	print("ykfaktor1xfaktor2: ",ykfaktor1xfaktor2)
	dbperl=b_perlakuan-1
	dbul=b_ulangan-1
	dbfak1 = len(data.groupby(['faktor1']).sum())-1
	dbfak2 = len(data.groupby(['faktor2']).sum())-1
	dbfak1xfak2=dbfak1*dbfak2
	dberr=dbperl*dbul
	dbtot=(b_perlakuan*b_ulangan)-1
	ktperl=ykperlakuan/dbperl
	ktul=ykulangan/dbul
	ktfak1=ykfaktor1/dbfak1
	ktfak2=ykfaktor2/dbfak2
	ktfak1x2=ykfaktor1xfaktor2/dbfak1xfak2
	kterr=ykerror/dberr
	fperl=ktperl/kterr
	ful=ktul/kterr
	ffak1=ktfak1/kterr
	ffak2=ktfak2/kterr
	ffak1x2=ktfak1x2/kterr
	ftab5 = scipy.stats.f.ppf(q=1-0.05, dfn=dbperl, dfd=dberr)
	ftab1 = scipy.stats.f.ppf(q=1-0.01, dfn=dbperl, dfd=dberr)
	ftabulangan = scipy.stats.f.ppf(q=1-0.05, dfn=dbul, dfd=dberr)
	ftabfak1=scipy.stats.f.ppf(q=1-0.05, dfn=dbfak1, dfd=dberr)
	ftabfak2=scipy.stats.f.ppf(q=1-0.05, dfn=dbfak2, dfd=dberr)

	k12 = scipy.stats.f.ppf(q=1-0.05,dfn=dbfak1xfak2, dfd=dberr)

	print()
	print("======+")
	print("ANOVA |")
	print("================================================================================")
	print("sv		db		kt		fhit		ftab 0.05")
	print("================================================================================")
	print("prlkn		",dbperl,"		",round(ktperl,3),"		",round(fperl,3),"	",ftab5)
	print("ulangan		",dbul,"		",round(ktul,3),"		",round(ful,3),"		",ftabulangan)
	print("faktor1		",dbfak1,"		",round(ktfak1,3),"		",round(ffak1,3),"	",ftabfak1)
	print("faktor2		",dbfak2,"		",round(ktfak2,3),"		",round(ffak2,3),"	",ftabfak2)
	print("fak1:2		",dbfak1xfak2,"		",round(ktfak1x2,3),"		",round(ffak1x2,3),"		",k12)
	print("error		",dberr,"		",round(kterr,3))
	print("total		",dbtot,"	")
	print("================================================================================")
	sd = math.sqrt(kterr/b_ulangan)
	if(fperl>ftab5):
		if(ffak1x2>k12):
			print("fhit interaksi faktor1 : faktor2 lebih besar dari f tab maka disimpulkan perlakuan berpengaruh nyata dan ada interaksi")
			print("SD: ",sd)
		elif(ffak1x2<k12):
			print("TIDAK ada interaksi, namun perlakuan berpengaruh nyata")
	else:
		print("tidak ada pengaruh antar perlakuan")
###
elif(model=='ralfak'):
	fk=((data['hasil'].sum())**2)/(b_perlakuan*b_ulangan)
	yktotal=(data['hasil'].values**2).sum() - fk
	ykperlakuan =((((data.groupby(['perlakuan']).sum()).values**2).sum())/b_ulangan)-fk
	ykerror=yktotal-ykperlakuan
	ykfaktor1 = (((data.groupby(['faktor1']).sum()).values**2).sum()/(len(data.groupby(['faktor1']).sum())*b_ulangan))-fk
	ykfaktor2 = (((data.groupby(['faktor2']).sum()).values**2).sum()/(len(data.groupby(['faktor2']).sum())*b_ulangan))-fk
	ykfaktor1xfaktor2 = ykperlakuan-ykfaktor1-ykfaktor2
	print('FK: ',fk)
	print('YK TOTAL: ',yktotal)
	print('YK PERLKUAN: ',ykperlakuan)
	print('YK ERROR :',ykerror)
	print('YK FAKTOR1: ',ykfaktor1)
	print('YK FAKTOR2: ',ykfaktor2)
	print('YK FAKOR1XFAKTOR2: ',ykfaktor1xfaktor2)

	dbperl=b_perlakuan-1
	dbul=b_ulangan-1
	dbfak1 = len(data.groupby(['faktor1']).sum())-1
	dbfak2 = len(data.groupby(['faktor2']).sum())-1
	dbfak1xfak2=dbfak1*dbfak2
	dberr=dbperl*dbul
	dbtot=(b_perlakuan*b_ulangan)-1
	ktperl=ykperlakuan/dbperl
	ktfak1=ykfaktor1/dbfak1
	ktfak2=ykfaktor2/dbfak2
	ktfak1x2=ykfaktor1xfaktor2/dbfak1xfak2
	kterr=ykerror/dberr
	fperl=ktperl/kterr
	ffak1=ktfak1/kterr
	ffak2=ktfak2/kterr
	ffak1x2=ktfak1x2/kterr
	ftab5 = scipy.stats.f.ppf(q=1-0.05, dfn=dbperl, dfd=dberr)
	ftab1 = scipy.stats.f.ppf(q=1-0.01, dfn=dbperl, dfd=dberr)
	k12 = scipy.stats.f.ppf(q=1-0.05,dfn=dbfak1xfak2, dfd=dberr)
	print()
	print("======+")
	print("ANOVA |")
	print("================================================================================")
	print("sv		db		kt		fhit		ftab 0.05")
	print("================================================================================")
	print("prlkn		",dbperl,"		",round(ktperl,3),"		",round(fperl,3),"	",ftab5)
	print("faktor1		",dbfak1,"		",round(ktfak1,3),"		",round(ffak1,3))
	print("faktor2		",dbfak2,"		",round(ktfak2,3),"		",round(ffak2,3))
	print("fak1:2		",dbfak1xfak2,"		",round(ktfak1x2,3),"		",round(ffak1x2,3),"	",k12)
	print("error		",dberr,"		",round(kterr,3))
	print("total		",dbtot,"	")
	print("================================================================================")
	sd = math.sqrt(kterr/b_ulangan)
	if(fperl>ftab5):
		if(ffak1x2>k12):
			print("fhit interaksi faktor1 : faktor2 lebih besar dari f tab maka disimpulkan perlakuan berpengaruh nyata")
			print("SD: ",sd)
	else:
		print("TIDAK ada interaksi")
else:
	print("ouchhh model belum dibuat")



