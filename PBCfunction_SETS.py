def PeriodicBound3DE_SETS(mdb,NameModel,NameSet,LV,Lc):
    from part import THREE_D, DEFORMABLE_BODY
    #Create reference parts and assemble
    NameRef1='RP-1'; NameRef2='RP-2';NameRef3='RP-3';NameRef4='RP-4';NameRef5='RP-5'; NameRef6='RP-6'; Tol=10000000;MF=10000000;
    Lx=LV[1][0]; Ly=LV[1][1]; Lz=LV[1][2]
    L1=int(round(MF*Lx));L2=int(round(MF*Ly));L3=int(round(MF*Lz))
	#Get all nodes
    nodesAll=mdb.models[NameModel].parts['RVE'].sets[NameSet].nodes
    nodesAllCoor=[]
    for nod in mdb.models[NameModel].parts['RVE'].sets[NameSet].nodes:
		##if nod<=len(nodesAll):
        nodesAllCoor.append(nod.coordinates)
		#else:
		#break
    f = open('Coor_List.txt', 'wb')
    for i in range(len(nodesAllCoor)):
        Coor1=nodesAllCoor[i]
		#print('Coordinates',Coor1[0])
		#f.write("%i %5.3f %5.3f %5.3f\n" % (i, Coor1[0], Coor1[1]),Coor1[2])
    f.close()
	#print(len(nodesAllCoor))
	#print(len(nodesAll))
    ranNodes=range(0,len(nodesAll))
	#np.savetxt('Coor', nodesAllCoor, delimiter=',')
    #K=0
    repConst=0
    #For virtices
    Origin=[];X_limit=[];Y_limit=[];Z_limit=[];XYZ_limit=[]
	#For Faces
    X=[];Y=[];Z=[];XB=[];YB=[];ZB=[]
    VX=[];VY=[];VZ=[];VXB=[];VYB=[];VZB=[]	
	#For edges and Virtual edges
    OY=[];YXY=[];XYX=[];OX=[];ZYZ=[];YZXYZ=[];XYZXZ=[];XZZ=[];YYZ=[];OZ=[];XZX=[];XYXYZ=[]
    VOY=[];VYXY=[];VXYX=[];VOX=[];VZYZ=[];VYZXYZ=[];VXYZXZ=[];VXZZ=[];VYYZ=[];VOZ=[];VXZX=[];VXYXYZ=[]
    NOY=0;NYXY=0;NXYX=0;NOX=0;NZYZ=0;NYZXYZ=0;NXYZXZ=0;NXZZ=0;NYYZ=0;NOZ=0;NXZX=0;NXYXYZ=0
    i=0;ii=0;j=0;jj=0;k=0;kk=0
	#repnod1=0
    #Find periodically located nodes and apply equation constraints
    for repnod1 in range(0,len(nodesAll)):
        if repnod1<=(len(nodesAll)):
            Coor1=nodesAllCoor[repnod1]		
			#print("Node_Number",repnod1)
			#print(Coor1)
            Xc=int(round(MF*Coor1[0]));Yc=int(round(MF*Coor1[1]));Zc=int(round(MF*Coor1[2]))
            Xn=Coor1[0];Yn=Coor1[1];Zn=Coor1[2]
            GET_BY_BOX=mdb.models[NameModel].parts['RVE'].nodes.getByBoundingBox(Xn-(Lc/Tol),Yn-(Lc/Tol),Zn-Lc/Tol,Xn+(Lc/Tol),Yn+(Lc/Tol),Zn+Lc/Tol)
			#print(Xc,Yc)
            if Xc==0 and Yc==0 and Zc==0:
                Origin=Coor1
                mdb.models[NameModel].parts['RVE'].Set(name='C7', nodes=GET_BY_BOX)
				#repnod1=repnod1+1
            elif Xc==L1 and Yc==0 and Zc==0:
                X_limit=Coor1
                mdb.models[NameModel].parts['RVE'].Set(name='C8', nodes=GET_BY_BOX)
				#repnod1=repnod1+1
            elif Xc==L1 and Yc==L2 and Zc==0:
                XY_limit=Coor1
                mdb.models[NameModel].parts['RVE'].Set(name='C4', nodes=GET_BY_BOX)
				#repnod1=repnod1+1
            elif Xc==0 and Yc==L2 and Zc==0:
                Y_limit=Coor1
                mdb.models[NameModel].parts['RVE'].Set(name='C3', nodes=GET_BY_BOX)
				#repnod1=repnod1+1			
            elif Xc==L1 and Yc==L2 and Zc==L3:
                XYZ_limit=Coor1
                mdb.models[NameModel].parts['RVE'].Set(name='C1', nodes=GET_BY_BOX)
				#repnod1=repnod1+1
            elif Xc==L1 and Yc==0 and Zc==L3:
                XZ_limit=Coor1
                mdb.models[NameModel].parts['RVE'].Set(name='C5', nodes=GET_BY_BOX)
				#repnod1=repnod1+1
            elif Xc==0 and Yc==0 and Zc==L3:
                Z_limit=Coor1
                mdb.models[NameModel].parts['RVE'].Set(name='C6', nodes=GET_BY_BOX)
				#repnod1=repnod1+1
            elif Xc==0 and Yc==L2 and Zc==L3:
                YZ_limit=Coor1
                mdb.models[NameModel].parts['RVE'].Set(name='C2', nodes=GET_BY_BOX)
				#repnod1=repnod1+1
            elif Xc==0 and Zc==0 and Yc!=0 and Yc!=L2:
                OY.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='bredge'+str(NOY), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NOY=NOY+1
				#print("OY")
            elif Yc==L2 and Zc==0 and Xc!=0 and Xc!= L1:
                YXY.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='rtedge'+str(NYXY), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NYXY=NYXY+1
				#print("YXY")
            elif Xc==L1 and Zc==0 and Yc!=0 and Yc!=L2:
                XYX.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='fredge'+str(NXYX), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NXYX=NXYX+1
				#print("XYX")
            elif Yc==0 and Zc==0 and Xc!=0 and Xc!=L1:
                OX.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='rbedge'+str(NOX), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NOX=NOX+1
				#print("OX")

            elif Xc==0 and Zc==L3 and Yc!=0 and Yc!= L2:
                ZYZ.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='bledge'+str(NZYZ), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NZYZ=NZYZ+1
				#print("ZYZ")
            elif Yc==L2 and Zc==L3 and Xc!=0 and Xc!= L1:
                YZXYZ.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='ltedge'+str(NYZXYZ), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NYZXYZ=NYZXYZ+1
				#print("ZXYZ")
            elif Xc==L1 and Zc==L3 and Yc!=0 and Yc!= L2:
                XYZXZ.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='fledge'+str(NXYZXZ), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NXYZXZ=NXYZXZ+1
				#print("XYZXZ")
            elif Yc==0 and Zc==L3 and Xc!=0 and Xc!= L1 :
                XZZ.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='lbedge'+str(NXZZ), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NXZZ=NXZZ+1
				#print("XZZ")
			
            elif Yc==0 and Xc==0 and Zc!=0 and Zc!=L3:
                OZ.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='bbedge'+str(NOZ), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NOZ=NOZ+1	
				#print("OZ")				
            elif Xc==0 and Yc==L2 and Zc!=0 and Zc!=L3:
                YYZ.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='btedge'+str(NYYZ), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NYYZ=NYYZ+1
				#print("YYZ")				
            elif Yc==0 and Xc==L1 and Zc!=0 and Zc!=L3:
                XZX.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='fbedge'+str(NXZX), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NXZX=NXZX+1
				#print("XZX")				
            elif Xc==L1 and Yc==L2 and Zc!=0 and Zc!=L3:
                XYXYZ.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='ftedge'+str(NXYXYZ), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                NXYXYZ=NXYXYZ+1
				#print("XYXYZ")				
            elif Xc==0 and Yc!=0 and Yc!=L2 and Zc!=0 and Zc!=L3:
                X.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='back'+str(i), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                i=i+1
            elif Xc==L1 and Yc!=0 and Yc!=L2 and Zc!=0 and Zc!=L3:
                XB.append(Coor1) 
                mdb.models[NameModel].parts['RVE'].Set(name='front'+str(ii), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                ii=ii+1
            elif Yc==0 and Xc!=0 and Xc!=L1 and Zc!=0 and Zc!=L3:
                Y.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='bot'+str(j), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                j=j+1
            elif Yc==L2 and Xc!=0 and Xc!=L1 and Zc!=0 and Zc!=L3:
                YB.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='top'+str(jj), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                jj=jj+1
            elif Zc==0 and Yc!=0 and Yc!=L2 and Xc!=0 and Xc!=L1:
                Z.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='right'+str(k), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                k=k+1
            elif Zc==L3 and Yc!=0 and Yc!=L2 and Xc!=0 and Xc!=L1:
                ZB.append(Coor1)
                mdb.models[NameModel].parts['RVE'].Set(name='left'+str(kk), nodes=GET_BY_BOX)
				#repnod1=repnod1+1
                kk=kk+1				
            else:
                continue
				#repnod1=repnod1+1
        else:
            break
    print("All sets made")
    print("NOY=", NOY,";","NYXY=",NYXY,";","NXYX=",NXYX,";","NOX=",NOX,";","NZYZ=",NZYZ,";","NYZXYZ=",NYZXYZ,";","NXYZXZ=",NXYZXZ)
    print("NXZZ=",NXZZ,";","NYYZ=",NYYZ,";","NOZ=",NOZ,";","NXZX=",NXZX,";","NXYXYZ=",NXYXYZ)
    print("i=",i,";","j=",j,";","k=",k,"ii=",ii,";","jj=",jj,";","kk=",kk)
    print("Dimesnions of RVE in  micrometers [Lx,Ly,Lz]",Lx,";",Ly,";",Lz)
    return(OY,YXY,XYX,OX,ZYZ,YZXYZ,XYZXZ,XZZ,OZ,YYZ,XZX,XYXYZ,X,XB,Y,YB,Z,ZB)