import os
import time
import random
import math
import peripherals
import copy
	
##---------------------------------------------------------------- INITIAL VALUES --------------------------------------------------------------------------------------------------

ingreso_valido=False
ListOfHoppers=[]
ListOfHoppers_ordered=[]
ListOfHoppers_ordered_bckp=[]
parametros_confirmed=False
qb=[]  #quantity of bill
qc=[]  #qtty of coin
vb=[]	#value of bill
vc=[]	#value of coin

flags=[]
flags_1=[]
flags_time=[]



recyclerEE=[]
recyclerFE=[]
print("PaymentSimulator v1.0")
print("Ingrese parametros. Para salir presione ctrl+c. Para afirmaciones ingrese 'y' o solo  presione Intro")
##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##----------------------------------------------------------------- SETTINGS PART --------------------------------------------------------------------------------------------------
##-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not parametros_confirmed:



##----------------------------------------------------------------- HOPPERS ---------------------------------------------------------------------------------------------------------


	no_hoppers=int(input("ingrese el numero de hoppers: "))
	if no_hoppers==0:
		hopper_available=False
	else:
		hopper_available=True
	if hopper_available:
		for counter in range (1,1+ no_hoppers):
			while not ingreso_valido:
				print("ingrese el valor de moneda para el hoper ",counter,": ")
				value_hoppers=float(input(""))
				if value_hoppers==0.1 or value_hoppers==0.2 or value_hoppers==0.5 or value_hoppers==1 or value_hoppers==2 or value_hoppers==5:
					ingreso_valido=True
				else:
					print("ingreso no valido, intente nuevamente")
					ingreso_valido=False
			if ingreso_valido: 
				ingreso_valido=False
				print("ingrese capacidad maxima de monedas para este hopper",counter,": ")
				max_capacity_hopper=int(input(""))
				while not ingreso_valido:
					print("ingrese un valor entre 0 y 1 que indique el porcentaje de la capacidad maxima para que el hoper se considere vacio: ")
					reserve_hopper=float(input(""))
					if reserve_hopper>=0 and reserve_hopper<=1:
						ingreso_valido=True
					else:
						print("ingreso no valido, intente nuevamente")
						ingreso_valido=False
				ingreso_valido=False
			
				ListOfHoppers.append(peripherals.hoppers(value_hoppers,max_capacity_hopper,reserve_hopper))
		
		
		ListOfHoppers_ordered=copy.deepcopy(ListOfHoppers)
		ListOfHoppers_ordered.sort(key=lambda hoppers:hoppers.get_voc(), reverse=True)
		ListOfHoppers_ordered_bckp=copy.deepcopy(ListOfHoppers_ordered)
			
		'''
		for h in ListOfHoppers_ordered:
			print(h)
		for h in ListOfHoppers_ordered_bckp:
			print(h)
		'''
		
		
	else:
		pass

##----------------------------------------------------------------- STACKER ---------------------------------------------------------------------------------------------------------


	temporal_str=(input("desea habilitar el stacker? y/n: "))
	if temporal_str=="n":	
		stacker_available=False
	else:
		stacker_available=True


	if stacker_available:
		ingreso_valido=False
		while not ingreso_valido:
			print("ingrese la cantidad maxima del stacker: ")
			max_capacity_stacker=int(input(""))
			if max_capacity_stacker<15000:
				ingreso_valido=True
			else:
				print("ingreso no valido o numero muy elevado, intente nuevamente")
				ingreso_valido=False
		if ingreso_valido: 
			ingreso_valido=False
			while not ingreso_valido:
				print("ingrese un valor entre 0 y 1 que indique el porcentaje de la capacidad maxima para que el hoper se considere lleno [margin]: ")
				margin_stacker=float(input(""))
				if margin_stacker>=0 and margin_stacker<=1:
					ingreso_valido=True
				else:
					print("ingreso no valido, intente nuevamente")
					ingreso_valido=False
			ingreso_valido=False
			
			
			stacker=peripherals.storage(max_capacity_stacker, margin_stacker)
			stacker_bckp=copy.deepcopy(stacker)

		
	else:
		pass


##-----------------------------------------------------------------CUSTODIAN BAG---------------------------------------------------------------------------------------------------------


	temporal_str=(input("desea habilitar el custodian bag? y/n: "))
	if temporal_str=="n":	
		custodian_bag_available=False
	else:
		custodian_bag_available=True


	if custodian_bag_available:
		ingreso_valido=False
		while not ingreso_valido:
			print("ingrese la cantidad maxima  de monedas del custodian bag: ")
			max_capacity_custodian_bag=int(input(""))
			if max_capacity_custodian_bag<15000:
				ingreso_valido=True
			else:
				print("ingreso no valido o numero muy elevado, intente nuevamente")
				ingreso_valido=False
		if ingreso_valido: 
			ingreso_valido=False
			while not ingreso_valido:
				print("ingrese un valor entre 0 y 1 que indique el porcentaje de la capacidad maxima para que el custodian bag se considere lleno [margin]: ")
				margin_custodian_bag=float(input(""))
				if margin_custodian_bag>=0 and margin_custodian_bag<=1:
					ingreso_valido=True
				else:
					print("ingreso no valido, intente nuevamente")
					ingreso_valido=False
			ingreso_valido=False
			
			
			custodian_bag=peripherals.storage(max_capacity_custodian_bag, margin_custodian_bag)
			custodian_bag_bckp=copy.deepcopy(custodian_bag)
		
	else:
		pass


##-----------------------------------------------------------------RECICLADOR --------------------------------------------------------------------------------------------------------


	temporal_str=(input("desea habilitar el reciclador? y/n: "))
	if temporal_str=="n":	
		recycler_available=False
	else:
		recycler_available=True



	if recycler_available:
		ingreso_valido=False
		while not ingreso_valido:
			print("ingrese la capacidad maxima del reciclador: ")
			max_capacity_recycler=int(input(""))
			if max_capacity_recycler<250:
				ingreso_valido=True
			else:
				print("ingreso no valido o numero muy elevado, intente nuevamente")
				ingreso_valido=False
		if ingreso_valido: 
			ingreso_valido=False
			while not ingreso_valido:
				print("ingrese un valor entre 0 y 1 que indique el porcentaje de la capacidad maxima para que el stacker se considere lleno [pfull]: ")
				pfull=float(input(""))
				if pfull>=0 and pfull<=1:
					ingreso_valido=True
				else:
					print("ingreso no valido, intente nuevamente")
					ingreso_valido=False
	
		if ingreso_valido: 
			ingreso_valido=False
			while not ingreso_valido:
				print("ingrese un valor entre 0 y 1 que indique el porcentaje de la capacidad minima para que el stacker se considere vacio [pemty]: ")
				pempty=float(input(""))
				if pempty>=0 and pempty<=1:
					ingreso_valido=True
				else:
					print("ingreso no valido, intente nuevamente")
					ingreso_valido=False
			ingreso_valido=False

		
			
		temporal_str=(input("desea especificar cantidades normales de billetes de cada valor? y/n. Las cantidades normales son la cantidad de billetes que regulan la cantidad de billletes presentes en el reciclador al que se debe alcanzar para asegurar el vuelto: "))
		if temporal_str=="y":	
			modnormal_available=True
		else:
			modnormal_available=False	

		
		if modnormal_available:
			ingreso_valido=False
			while not ingreso_valido:
				print("ingrese la cantidad de billetes de 100 normales en el stacker : ")
				qob100_normal=float(input(""))
				print("ingrese la cantidad de billetes de 50 normales en el stacker : ")
				qob50_normal=float(input(""))
				print("ingrese la cantidad de billetes de 10 normales en el stacker : ")
				qob20_normal=float(input(""))
				print("ingrese la cantidad de billetes de 10 normales en el stacker : ")
				qob10_normal=float(input(""))
				

			
				if qob100_normal+qob100_normal+qob50_normal+qob20_normal+qob10_normal>=max_capacity_recycler:
					ingreso_valido=False
					print("ingreso no valido. Se excedio la capacidad maxima, intente nuevamente")
				else:
					
					ingreso_valido=True	

		
		else:
			qob100_normal=0	
			qob50_normal=20
			qob20_normal=20
			qob10_normal=10


		
		recycler=peripherals.billsrecycler(max_capacity_recycler,qob100_normal,qob50_normal,qob20_normal,qob10_normal,pfull,pempty)
		recycler_bckp=copy.deepcopy(recycler)

		
	else:
		pass





##----------------------------------------------------------------- SPECIFIC PARAMETERS ---------------------------------------------------------------------------------------------------------

	temporal_str=(input("desea aceptar monedas de 5 sol?: y/n"))
	if temporal_str=="n":	
		pass
	else:
		qc.append(0)
		vc.append(5)
	

	
	temporal_str=(input("desea aceptar monedas de 2 sol?: y/n"))
	if temporal_str=="n":	
		pass
	else:
		qc.append(0)
		vc.append(2)

	temporal_str=(input("desea aceptar monedas de 1 sol?: y/n"))
	if temporal_str=="n":	
		pass
	else:
		qc.append(0)
		vc.append(1)


	temporal_str=(input("desea aceptar billetes de 200 soles?: y/n"))
	if temporal_str=="n":	
		pass
	else:
		qb.append(0)
		vb.append(200)

	temporal_str=(input("desea aceptar billetes de 100 soles?: y/n"))
	if temporal_str=="n":	
		pass
	else:
		qb.append(0)
		vb.append(100)



	temporal_str=(input("desea aceptar billetes de 50 soles?: y/n"))
	if temporal_str=="n":	
		pass
	else:
		qb.append(0)
		vb.append(50)





	
	temporal_str=(input("desea aceptar billetes de 20 soles?: y/n"))
	if temporal_str=="n":	
		pass
	else:
		qb.append(0)
		vb.append(20)	
	

	temporal_str=(input("desea aceptar billetes de 10 soles?: y/n"))
	if temporal_str=="n":	
		pass
	else:
		qb.append(0)
		vb.append(10)


	

	
	
	
		
	Ii=int(input("(1): ingrese el monto minimo que se ingresara por transaccion: "))
	Is=int(input("(2): ingrese el monto maximo que se ingresara por transaccion: "))  
	TransacPerDay=int(input("ingrese el cantidad de transacciones por dia: "))  
	ingreso_valido=False
	while not ingreso_valido:	
		DutyCycle=float(input("ingrese el cantidad de horas por dia: "))
		if DutyCycle>0 and DutyCycle<=24:
			ingreso_valido=True
		else:
			print("ingreso no valido, intente nuevamente")
			ingreso_valido=False
	



##----------------------------------------------------------------- DETAILED PARAMETERS ---------------------------------------------------------------------------------------------------------



	print("-------------------------------RESUMEN DE PARAMETROS------------------------")
	print("hoppers definidos:")
	if hopper_available:
		for hoppers in ListOfHoppers_ordered:
			print(hoppers)
		
	else:
		print("none")

	print("stacker definido:")
	if stacker_available:
		print(stacker) 
	else:
		print("none")

	print("custodian bag definido:")
	if custodian_bag_available:
		print(custodian_bag)
	else:
		print("none")

	print("recycler definido:")
	if 	recycler_available:
		print(recycler)
	else:
		print("none")

	print("acepted coins:")
	print(vc)
	
	print("acepted bills:")
	print(vb)

	print("monto minimo: ", Ii)
	print("monto maximo: ", Is)
	print("Transacciones por dia: ",TransacPerDay)
	print("Tiempo promedio de funcionamiento:", DutyCycle)



##----------------------------------------------------------------- CONFIRM PARAMETERS---------------------------------------------------------------------------------------------------------
	
	temporal_str=(input("parametros ok? y/n: "))
	if temporal_str=="n":	
		parametros_confirmed=False
		del ListOfHoppers_ordered[:]
		del qb[:]
		del vb[:]
		del qc[:]
		del vc[:]
	else:
		parametros_confirmed=True


if hopper_available:
	for e in range(len(ListOfHoppers_ordered)+2): ##solo hay un custodian bag + un stacker , ademas de los hoppers
		flags.append(False)
		flags_1.append(False)
		flags_time.append(0)
else:
	for e in range(2): ##solo hay un custodian bag + un stacker , ademas de los hoppers
		flags.append(False)
		flags_1.append(False)
		flags_time.append(0)
	
##-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##-------------------------------------------------------------------------SIMULATION-----------------------------------------------------------------------------------------------------
##-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
UEOS=False

while not UEOS:

	EOS=False
	m=0
	while not EOS:


		##--------------------------------------------------------------------- Generacion de billetera ------------------------------------------------------
		m+=1
		incorrecto=True
		suficiente=False
		
		C=Ii+random.randint(0,Is-Ii)


		print("---------------------------------- iteracion ",m,": -------------------------------------")
		print("El monto a cobrar es: ",C)
	

		while incorrecto:
			I=C+random.randrange(0,vb[0],1)	
			##print("billetera es ",I)
			incorrecto=False
	

	
			MT=0
		
			for n in range(len(vb)):
					##print(n, "-------")
					A=math.ceil(I/vb[n])
					qb[n]=random.randrange(0,A,1)
					temp=qb[n]*vb[n]
					I=I-temp
					MT=MT+temp
					'''
					print("vb[n]",vb[n])
					print("A ",A)
					print("qb[n] ",qb[n])
					print("temp ",temp)
					print("MT",MT)
					'''
					if MT>=C:
					
						MT=MT-temp
						I=I+temp
						qb[n]=math.ceil((C-MT)/vb[n])
						temp=qb[n]*vb[n]
						I=I-temp
						MT=MT+temp
						suficiente=True
						break
					else:
						pass
				
		
				
				
			##print("I queda--------------------------------------------- :",I)		
			if suficiente is False:
			
				for n in range(len(vc)):

					A=math.ceil(I/vc[n])
					qc[n]=random.randrange(0,A,1)
					temp=qc[n]*vc[n]
					MT=MT+temp
					I=I-temp
					'''
					print("vc[n]",vc[n])
					print("A ",A)
					print("qc[n] ",qc[n])
					print("temp ",temp)
					print("MT",MT)
					'''
					if MT>=C:
						MT=MT-temp
						I=I+temp
						qc[n]=math.ceil((C-MT)/vc[n])
						temp=qc[n]*vc[n]
						MT=MT+temp
						I=I-temp
						suficiente=True
						break
					else:
						pass
				
			
			
			else:
				pass
	#verificador para estabilidad
			NT=0
			for n in range(len(vb)):
				NT=NT+qb[n]*vb[n]
			for n in range(len(vc)):
				NT=NT+qc[n]*vc[n]

			if NT==MT:
				verificador=True	
			else: 	
				verificador=False	


			verificador=True



		

			if (I==0 or suficiente) and verificador:
				incorrecto=False	
				print("Monto ingresado es", MT)



	#------------------------------------------------------------------------generacion de vuelto-------------------------------------------------------

				q2p=MT-C #quantity to pay
				print(" vuelto [q2pay] :",q2p)
		


	#------------------------------------------------------------------------vizualizacion------------------------------------------------------


			
				print("value of bills: ",vb,". Quantity bills: ",qb)
				print("value of coins: ",vc,". Quantity coin: ",qc)
			
		
	
		
		

				if custodian_bag_available:
				#-----------------------------  	agregar monedas a custodian bag   ------------------------------
					print("CUSTODIAN BAG:  actualmente hay", custodian_bag.get_qoc(), "monedas, En total es [voc] ", custodian_bag.get_voc(),". Hay espacio para: ", custodian_bag.capacity2fill() )
	
					for n in range(len(qc)):		
						custodian_bag.add_money(qc[n],vc[n])

					print("CUSTODIAN BAG: hay ", custodian_bag.get_qoc(), "monedas, En total es [voc] ", custodian_bag.get_voc(),".")
					print("CUSTODIAN BAG is filled? :", custodian_bag.get_isFilled())
					flags[1]=custodian_bag.get_isFilled()
					if flags[1]==True and flags_1[1]==False:
						flags_time[1]=m	
					else:
						pass				
					flags_1[1]=flags[1]
				else:
					flags[1]=True





				#-----------------------------               envio al reciclador   ----------------------------------------
				if recycler_available:

					print("RECYCLER: inicial. actualmente hay", recycler.get_q100(),recycler.get_q50(),recycler.get_q20(),recycler.get_q10())
					#agregar billetes a reciclador 
					for n in range(len(vb)):			
						recycler.add_bills(qb[n],vb[n])
				
					if recycler.get_isFilled():
						recyclerFE.append(m)
						print("RECYCLER: warning of OVERFILLED")
					else:
						pass

					print("RECYCLER: temporal: actualmente hay", recycler.get_q100(),recycler.get_q50(),recycler.get_q20(),recycler.get_q10())
					[lob,q2p]=recycler.pay(q2p)
					print("RECYCLER: final - vuelto: actualmente quedan", recycler.get_q100(),recycler.get_q50(),recycler.get_q20(),recycler.get_q10())


				#------------------------luego del vuelto, se envia el exceso respecto a la cantidad normal al STACKER Aqu'i se incluye los billetes de 200 en caso hubiera -----
			
					for n in range(len(qb)):
						if vb[n]==200:	
							stacker.add_money(qb[n],vb[n])
						else:
							pass


					h=recycler.get_q100()-recycler.get_p100()
					if h>0:
						stacker.add_money(h,100)
						recycler.subs_100(h)
					else:
						pass

					h=recycler.get_q50()-recycler.get_p50()
					if h>0:
						stacker.add_money(h,50)
						recycler.subs_50(h)
					else:
						pass
			
					h=recycler.get_q20()-recycler.get_p20()
					if h>0:
						stacker.add_money(h,20)
						recycler.subs_20(h)
					else:
						pass

					h=recycler.get_q10()-recycler.get_p10()
					if h>0:
						stacker.add_money(h,10)
						recycler.subs_10(h)
					else:
						pass
			
					if recycler.get_isEmpty():
						recyclerEE.append(m)
						print("RECYCLER: warning to be LACKING")
					else:
						pass

					print("RECYCLER: final - envio al stacker : actualmente quedan: [100,50,20,10]", recycler.get_q100(),recycler.get_q50(),recycler.get_q20(),recycler.get_q10())
		
			
				else:
					if stacker_available:				
						for n in range(len(vb)):
							stacker.add_money(qb[n],vb[n])
					else:
						pass
			
				if stacker_available:

					print("STACKER: hay ", stacker.get_qoc(), "billetes, En total es [voc] ", stacker.get_voc(),".")
					print("STACKER is filled? :", stacker.get_isFilled())
					flags[0]=stacker.get_isFilled()
					if flags[0]==True and flags_1[0]==False:
						flags_time[0]=m	
					else:
						pass				
					flags_1[0]=flags[0]
				else: 
					pass
			
				'''	
				for n in range(len(qb)):
					qb[n]=0
				for n in range(len(qc)):
					qc[n]=0
		
				if m==10:
					EOS=True

		'''		
	
		##-------------------------------zona de trabajo
		##--------- continuacion vuelto monedas----------
			
		
				if hopper_available:
					i=1
					for hopper in ListOfHoppers_ordered:
						print("HOPPER",i," inicialmente hubo", hopper.get_qoc(), "de monedas [voc] = ", hopper.get_voc(),". qom: ", hopper.get_qom())
						if hopper.get_qoc()>0:	
							[qoc2pay,q2p]=hopper.pay(q2p)
						else:
							pass
						i+=1
				
					if q2p>0:				
						print("no se entregu'o el vuelto completo de monedas")
					else:
						pass
					i=1
					for hopper in ListOfHoppers_ordered:
						print("HOPPER ",i,": actualmente hay", hopper.get_qoc(), "de monedas [voc] = ", hopper.get_voc(),". qom: ", hopper.get_qom())
						print ("qoc 2 pay: ", hopper.get_qoc())
						print("is empty? :", hopper.get_isEmpty())
						i+=1
	
						flags[i]=hopper.get_isEmpty()
						if flags[i]==True and flags_1[i]==False:
							flags_time[i]=m	
						else:
							pass			
						flags_1[i]=flags[i]

				else: 	
					pass	
			
			
		
				for n in range(len(qb)):
					qb[n]=0
				for n in range(len(qc)):
					qc[n]=0

				temp_bool=True
				for value_bool in flags:
					temp_bool=value_bool and temp_bool
				EOS=temp_bool		
			

		
				#if m==10:
				#	EOS=True

			else:
				m-=1
				print("iteracion no concretada. Monto ingresado insuficiente")



	#------------------------------------------------------------------------Conclusion-----------------------------------------------------------------------------


	#-----------------------------------------------------------------------------------------------------------------------------------------------------------------



	print("----------------------------------CONCLUSION: -------------------------------------")

	STACKER_days=flags_time[0]/TransacPerDay
	STACKER_hours=STACKER_days*DutyCycle
	print("STACKER filled: ",STACKER_days,"days or ", STACKER_hours, "hours.", "QoT =", flags_time[0])

	if custodian_bag_available:
		CUSTODIAN_BAG_days=flags_time[1]/TransacPerDay
		CUSTODIAN_BAG_hours=CUSTODIAN_BAG_days*DutyCycle
		print("CUSTODIAN_BAG filled: ", CUSTODIAN_BAG_days,"days or ", CUSTODIAN_BAG_hours, "hours.","QoT =", flags_time[1])

	if hopper_available:
		i=1
		for hopper in ListOfHoppers_ordered:
			i+=1
			HOPPER_days=flags_time[i]/TransacPerDay
			HOPPER_hours=flags_time[i]*DutyCycle/TransacPerDay
			print("HOPPER",i-1,"(",hopper.get_voc(),")"," empty in: ",HOPPER_days,"days or ", HOPPER_hours, "hours.","QoT =", flags_time[i])
	else: 
		pass

	
	if recycler_available:

		print("EVENTOS: Recycler filled event: ", len(recyclerFE),". Recycler empty event: ",len(recyclerEE))
	else:
		pass

	print( "EOS = ",m,"transacciones. ",m/TransacPerDay ," days, " ,m*DutyCycle/TransacPerDay ,"hours.")
	
	
	print("--------------------------------------------------------------------------------")
	UEOS_char=(input("desea volver a simular con los mismos parametros?? y/n: "))
	if UEOS_char=="n":
		UEOS=True
	else:
		if hopper_available:
			for e in range(len(ListOfHoppers_ordered)+2): ##solo hay un custodian bag + un stacker , ademas de los hoppers
				flags[e]=False
				flags_1[e]=False
				flags_time[e]=0
			
			ListOfHoppers_ordered=copy.deepcopy(ListOfHoppers_ordered_bckp)
		else:
			for e in range(2): ##solo hay un custodian bag + un stacker , ademas de los hoppers
				flags[e]=False
				flags_1[e]=False
				flags_time[e]=0


		if stacker_available:
			stacker=copy.deepcopy(stacker_bckp)
		else:
			pass
		if custodian_bag_available:
			custodian_bag=copy.deepcopy(custodian_bag_bckp)
		else:
			pass
		if recycler_available:
			recycler=copy.deepcopy(recycler_bckp)
		else:
			pass






