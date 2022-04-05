#FUNCTION TO APPLY PERIODIC BOUNDARY CONDITIONS IN 3D
#LatticeVec:	An array with the lattice vectors, for example [(1.0, 0.0), (1.0, 1.0)] for a square lattice
def Tie_constrains(mdb,NameModel):	
    #Create TIE (BREDGE)
	Master_set='RVE-1.SET_Virtual_Node_(fr-br)edge'; Slave_set='RVE-1.SET_Edge-bredge'; Set_Name='VC_(fr-br)edge'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (BLEDGE)
	Master_set='RVE-1.SET_Virtual_Node_(fl-bl)edge'; Slave_set='RVE-1.SET_Edge-bledge'; Set_Name='VC_(fl-bl)edge'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (LBEDGE)
	Master_set='RVE-1.SET_Virtual_Node_(lt-lb)edge'; Slave_set='RVE-1.SET_Edge-lbedge'; Set_Name='VC_(lt-lb)edge'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (RBEDGE)
	Master_set='RVE-1.SET_Virtual_Node_(rt-rb)edge'; Slave_set='RVE-1.SET_Edge-rbedge'; Set_Name='VC_(rt-rb)edge'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (BTEDGE)
	Master_set='RVE-1.SET_Virtual_Node_(ft-bt)edge'; Slave_set='RVE-1.SET_Edge-btedge'; Set_Name='VC_(ft-bt)edge'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (BBEDGE)
	Master_set='RVE-1.SET_Virtual_Node_(fb-bb)edge'; Slave_set='RVE-1.SET_Edge-bbedge'; Set_Name='VC_(fb-bb)edge'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (FBEDGE)
	Master_set='RVE-1.SET_Virtual_Node_(ft-fb)edge'; Slave_set='RVE-1.SET_Edge-fbedge'; Set_Name='VC_(ft-fb)edge'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (BACK)
	#Virtual Nodes for back & the nodes of the front surface are copied
	Master_set='RVE-1.SET_Virtual_Node_back'; Slave_set='RVE-1.SET-Back'; Set_Name='VC-back'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (BOTTOM)
	Master_set='RVE-1.SET_Virtual_Node_bot'; Slave_set='RVE-1.SET-Bottom'; Set_Name='VC_bot'
	createTie(NameModel, Master_set, Slave_set, Set_Name)
	
	#Create TIE (RIGHT)
	Master_set='RVE-1.SET_Virtual_Node_right'; Slave_set='RVE-1.SET-Right'; Set_Name='VC_right'
	createTie(NameModel, Master_set, Slave_set, Set_Name)

def createTie(NameModel, Master_set, Slave_set, Set_Name):
	TIE=mdb.models[NameModel].Tie(adjust=ON, master=
			mdb.models[NameModel].rootAssembly.sets[Master_set], name=Set_Name, 
			positionToleranceMethod=COMPUTED, slave=
			mdb.models[NameModel].rootAssembly.sets[Slave_set], thickness=ON, 
			tieRotations=ON)
	mdb.models[NameModel].constraints[Set_Name].setValues(constraintEnforcement=
		NODE_TO_SURFACE)
	return(TIE)


def convertTuple(tup): 
    str =  ''.join(tup) 
    return str