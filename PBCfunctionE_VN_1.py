#FUNCTION TO APPLY PERIODIC BOUNDARY CONDITIONS IN 3D
def PeriodicBound3DE(mdb,NameModel,OY,YXY,XYX,OX,ZYZ,YZXYZ,XYZXZ,XZZ,OZ,YYZ,XZX,XYXYZ,X,XB,Y,YB,Z,ZB,VXYX,VXYZXZ,VYZXYZ,VYXY,VXYXYZ,VXZX,VXB,VYB,VZB):
    MF=1E15
    #C6-C2  
    mdb.models[NameModel].Equation(name='EC1-C6-C2',
    terms=((1.0,'RVE-1.C6', 1),(-1.0, 'RVE-1.C2', 1),(1,'RP-1', 2)))
    mdb.models[NameModel].Equation(name='EC2-C6-C2-RP2',
    terms=((1.0,'RVE-1.C6', 2),(-1.0, 'RVE-1.C2', 2),(1,'RP-2', 2)))
    mdb.models[NameModel].Equation(name='EC3-C6-C2',
    terms=((1.0,'RVE-1.C6', 3),(-1.0, 'RVE-1.C2', 3),(1,'RP-3', 2)))
		
		#C2-C3
    mdb.models[NameModel].Equation(name='EC1-C2-C3',
    terms=((1.0,'RVE-1.C2', 1),(-1.0, 'RVE-1.C3', 1),(-1,'RP-1',3)))
    mdb.models[NameModel].Equation(name='EC2-C2-C3',
    terms=((1.0,'RVE-1.C2', 2),(-1.0, 'RVE-1.C3', 2),(-1,'RP-2', 3)))
    mdb.models[NameModel].Equation(name='EC3-C2-C3-RP3',
    terms=((1.0,'RVE-1.C2', 3),(-1.0, 'RVE-1.C3', 3),(-1,'RP-3', 3)))
		
		#C3-C4
    mdb.models[NameModel].Equation(name='EC1-C3-C4-RP1',
    terms=((1.0,'RVE-1.C3', 1),(-1.0, 'RVE-1.C4', 1),(1,'RP-1', 1)))
    mdb.models[NameModel].Equation(name='EC2-C3-C4',
    terms=((1.0,'RVE-1.C3', 2),(-1.0, 'RVE-1.C4', 2),(1,'RP-2', 1)))
    mdb.models[NameModel].Equation(name='EC3-C3-C4',
    terms=((1.0,'RVE-1.C3', 3),(-1.0, 'RVE-1.C4', 3),(1,'RP-3', 1)))
		
		#C4-C8
    mdb.models[NameModel].Equation(name='EC1-C4-C8',
    terms=((1.0,'RVE-1.C4', 1),(-1.0, 'RVE-1.C8', 1),(-1,'RP-1', 2)))
    mdb.models[NameModel].Equation(name='EC2-C4-C8-RP2',
    terms=((1.0,'RVE-1.C4', 2),(-1.0, 'RVE-1.C8', 2),(-1,'RP-2', 2)))
    mdb.models[NameModel].Equation(name='EC3-C4-C8',
    terms=((1.0,'RVE-1.C4', 3),(-1.0, 'RVE-1.C8', 3),(-1,'RP-3', 2)))
		
		#C8-C5
    mdb.models[NameModel].Equation(name='EC1-C8-C5',
    terms=((1.0,'RVE-1.C8', 1),(-1.0, 'RVE-1.C5', 1),(1,'RP-1', 3)))
    mdb.models[NameModel].Equation(name='EC2-C8-C5',
    terms=((1.0,'RVE-1.C8', 2),(-1.0, 'RVE-1.C5', 2),(1,'RP-2', 3)))
    mdb.models[NameModel].Equation(name='EC3-C8-C5-RP3',
    terms=((1.0,'RVE-1.C8', 3),(-1.0, 'RVE-1.C5', 3),(1,'RP-3', 3)))
		
		#C5-C1
    mdb.models[NameModel].Equation(name='EC1-C5-C1',
    terms=((1.0,'RVE-1.C5', 1),(-1.0, 'RVE-1.C1', 1),(1,'RP-1', 2)))
    mdb.models[NameModel].Equation(name='EC2-C5-C1-RP2',
    terms=((1.0,'RVE-1.C5', 2),(-1.0, 'RVE-1.C1', 2),(1,'RP-2', 2)))
    mdb.models[NameModel].Equation(name='EC3-C5-C1',
    terms=((1.0,'RVE-1.C5', 3),(-1.0, 'RVE-1.C1', 3),(1,'RP-3', 2)))
		
		#C1-C7
    mdb.models[NameModel].Equation(name='EC1-C1-C7-RP1',
    terms=((1.0,'RVE-1.C1', 1),(-1.0, 'RVE-1.C7', 1),(-1,'RP-1', 1),(-1,'RP-2', 1),(-1,'RP-3', 1)))
		
    mdb.models[NameModel].Equation(name='EC2-C1-C7-RP2',
    terms=((1.0,'RVE-1.C1', 2),(-1.0, 'RVE-1.C7', 2),(-1,'RP-2', 2),(-1,'RP-1', 2),(-1,'RP-3', 2)))
		
    mdb.models[NameModel].Equation(name='EC3-C1-C7-RP3',
    terms=((1.0,'RVE-1.C1', 3),(-1.0, 'RVE-1.C7', 3),(-1,'RP-3', 3),(-1,'RP-2', 3),(-1,'RP-1', 3)))
		#Create constrain for edges
		
		#OZ-XZX (bbedge-fbedge)
    for EG1 in range(0,len(VXZX)):
        dz=0
        C1=VXZX[EG1]
        Z1=int(round(MF*C1[2]))
        for EG2 in range(0,len(VXYXYZ)):
            C2=VXYXYZ[EG2]
            Z2=int(round(MF*C2[2]))
            dz=Z1-Z2
            if dz==0:
                mdb.models[NameModel].Equation(name='C-bbedge'+str(EG1)+'-fbedge'+str(EG2)+'-RP1',
                terms=((1.0,'RVE-1.V_bbedge'+str(EG1), 1),(-1.0, 'RVE-1.V_fbedge'+str(EG2), 1),(1,'RP-1', 1)))
                mdb.models[NameModel].Equation(name='C-bbedge'+str(EG1)+'-fbedge'+str(EG2)+'-RP2',
                terms=((1.0,'RVE-1.V_bbedge'+str(EG1), 2),(-1.0, 'RVE-1.V_fbedge'+str(EG2), 2),(1,'RP-2', 1)))
                mdb.models[NameModel].Equation(name='C-bbedge'+str(EG1)+'-fbedge'+str(EG2)+'-RP-3',
                terms=((1.0,'RVE-1.V_bbedge'+str(EG1), 3),(-1.0, 'RVE-1.V_fbedge'+str(EG2), 3),(1,'RP-3', 1)))
            else:
                continue
		
		#ZYZ-OY (bledge-bredge) (bredge is repalced by the virtual edge(V-bredge))
    for EA1 in range(0,len(VXYZXZ)):
        dy=0
        C1=VXYZXZ[EA1]
        Y1=int(round(MF*C1[1]))
        for EA2 in range(0,len(VXYX)):
            C2=VXYX[EA2]
            Y2=int(round(MF*C2[1]))
            dy=Y2-Y1
            if dy==0:
                mdb.models[NameModel].Equation(name='C-bledge'+str(EA1)+'-bredge'+str(EA2)+'-RP1',
                terms=((-1.0,'RVE-1.V_bledge'+str(EA1), 1),(1.0, 'RVE-1.V_bredge'+str(EA2), 1),(1,'RP-1', 3)))
                mdb.models[NameModel].Equation(name='C-bledge'+str(EA1)+'-bredge'+str(EA2)+'-RP2',
                terms=((-1.0,'RVE-1.V_bledge'+str(EA1), 2),(1.0, 'RVE-1.V_bredge'+str(EA2), 2),(1,'RP-2', 3)))
                mdb.models[NameModel].Equation(name='C-bledge'+str(EA1)+'-bredge'+str(EA2)+'-RP3',
                terms=((-1.0,'RVE-1.V_bledge'+str(EA1), 3),(1.0, 'RVE-1.V_bredge'+str(EA2), 3),(1,'RP-3', 3)))				
            else:
                continue		
		
		#OY-XYX (bredge-fredge)
    for EA1 in range(0,len(VXYX)):
        dy=0
        C1=VXYX[EA1]
        Y1=int(round(MF*C1[1]))
        for EA2 in range(0,len(XYX)):
            C2=XYX[EA2]
            Y2=int(round(MF*C2[1]))
            dy=Y1-Y2
            if dy==0:
                mdb.models[NameModel].Equation(name='C-bredge'+str(EA1)+'-fredge'+str(EA2)+'-RP1',
                terms=((1.0,'RVE-1.V_bredge'+str(EA1), 1),(-1.0, 'RVE-1.fredge'+str(EA2), 1),(1,'RP-1', 1)))
                mdb.models[NameModel].Equation(name='C-bredge'+str(EA1)+'-fredge'+str(EA2)+'-RP2',
                terms=((1.0,'RVE-1.V_bredge'+str(EA1), 2),(-1.0, 'RVE-1.fredge'+str(EA2), 2),(1,'RP-2', 1)))
                mdb.models[NameModel].Equation(name='C-bredge'+str(EA1)+'-fredge'+str(EA2)+'-RP3',
                terms=((1.0,'RVE-1.V_bredge'+str(EA1), 3),(-1.0, 'RVE-1.fredge'+str(EA2), 3),(1,'RP-3', 1)))
            else:
                continue
			
		#YYZ-OZ (btedge-bbedge)
    for EI1 in range(0,len(VXYXYZ)):
        dz=0
        C1=VXYXYZ[EI1]
        Z1=int(round(MF*C1[2]))
        for EI2 in range(0,len(VXZX)):
            C2=VXZX[EI2]
            Z2=int(round(MF*C2[2]))
            dz=Z1-Z2
            if dz==0:
                mdb.models[NameModel].Equation(name='C-btedge'+str(EI1)+'-bbedge'+str(EI2)+'-RP1',
                terms=((-1.0,'RVE-1.V_btedge'+str(EI1), 1),(1.0, 'RVE-1.V_bbedge'+str(EI2), 1),(1,'RP-1', 2)))
                mdb.models[NameModel].Equation(name='C-btedge'+str(EI1)+'-bbedge'+str(EI2)+'-RP2',
                terms=((-1.0,'RVE-1.V_btedge'+str(EI1), 2),(1.0, 'RVE-1.V_bbedge'+str(EI2), 2),(1,'RP-2', 2)))
                mdb.models[NameModel].Equation(name='C-btedge'+str(EI1)+'-bbedge'+str(EI2)+'-RP3',
                terms=((-1.0,'RVE-1.V_btedge'+str(EI1), 3),(1.0, 'RVE-1.V_bbedge'+str(EI2), 3),(1,'RP-3', 2)))
            else:
                continue

		#XYZXZ-ZYZ (fledge-bledge)
    for EF1 in range(0,len(XYZXZ)):
        dy1=0;
        C1=XYZXZ[EF1]
        Y1=int(round(MF*C1[1]))
        for EF2 in range(0,len(VXYZXZ)):
            C2=VXYZXZ[EF2] 
            Y2=int(round(MF*C2[1]))
            dy=Y1-Y2
            if dy==0:
                mdb.models[NameModel].Equation(name='C-fledge'+str(EF1)+'-bledge'+str(EF2)+'-RP1',
                terms=((-1.0,'RVE-1.fledge'+str(EF1), 1),(1.0, 'RVE-1.V_bledge'+str(EF2), 1),(1.0,'RP-1', 1)))
                mdb.models[NameModel].Equation(name='C-fledge'+str(EF1)+'-bledge'+str(EF2)+'-RP2',
                terms=((-1.0,'RVE-1.fledge'+str(EF1), 2),(1.0, 'RVE-1.V_bledge'+str(EF2), 2),(1.0,'RP-2', 1)))
                mdb.models[NameModel].Equation(name='C-fledge'+str(EF1)+'-bledge'+str(EF2)+'-RP3',
                terms=((-1.0,'RVE-1.fledge'+str(EF1), 3),(1.0, 'RVE-1.V_bledge'+str(EF2), 3),(1.0,'RP-3', 1)))
            else:
                continue

		#XYXYZ-YYZ (ftedge-btedge)
    for EE1 in range(0,len(XYXYZ)):
        dz=0
        C1=XYXYZ[EE1]
        Z1=int(round(MF*C1[2]))
        for EE2 in range(0,len(VXYXYZ)):
            C2=VXYXYZ[EE2]
            Z2=int(round(MF*C2[2]))
            dz=Z2-Z1
            if dz==0:
                mdb.models[NameModel].Equation(name='C-ftedge'+str(EE1)+'-btedge'+str(EE2)+'-RP1',
                terms=((-1.0,'RVE-1.ftedge'+str(EE1), 1),(1.0, 'RVE-1.V_btedge'+str(EE2), 1),(1.0,'RP-1', 1)))
                mdb.models[NameModel].Equation(name='C-ftedge'+str(EE1)+'-btedge'+str(EE2)+'-RP2',
                terms=((-1.0,'RVE-1.ftedge'+str(EE1), 2),(1.0, 'RVE-1.V_btedge'+str(EE2), 2),(1.0,'RP-2', 1)))
                mdb.models[NameModel].Equation(name='C-ftedge'+str(EE1)+'-btedge'+str(EE2)+'-RP3',
                terms=((-1.0,'RVE-1.ftedge'+str(EE1), 3),(1.0, 'RVE-1.V_btedge'+str(EE2), 3),(1.0,'RP-3', 1)))
            else:
                continue

		#XZZ-OX (lbedge-rbedge)	
    for ED1 in range(0,len(VYZXYZ)):
        dx=0
        C1=VYZXYZ[ED1]
        X1=int(round(MF*C1[0]))
        for ED2 in range(0,len(VYXY)):
            C2=VYXY[ED2]
            X2=int(round(MF*C2[0]))
            dx=X1-X2
            if dx==0:
                mdb.models[NameModel].Equation(name='C-lbedge'+str(ED1)+'-rbedge'+str(ED2)+'-RP1',
                terms=((-1.0,'RVE-1.V_lbedge'+str(ED1), 1),(1.0, 'RVE-1.V_rbedge'+str(ED2), 1),(1.0,'RP-1', 3)))
                mdb.models[NameModel].Equation(name='C-lbedge'+str(ED1)+'-rbedge'+str(ED2)+'-RP2',
                terms=((-1.0,'RVE-1.V_lbedge'+str(ED1), 2),(1.0, 'RVE-1.V_rbedge'+str(ED2), 2),(1.0,'RP-2', 3)))
                mdb.models[NameModel].Equation(name='C-lbedge'+str(ED1)+'-rbedge'+str(ED2)+'-RP3',
                terms=((-1.0,'RVE-1.V_lbedge'+str(ED1), 3),(1.0, 'RVE-1.V_rbedge'+str(ED2), 3),(1.0,'RP-3', 3)))
            else:
                continue


		#YZXYZ-XZZ (ltedge-lbedge)
    for EH1 in range(0,len(YZXYZ)):
        dx=0
        C1=YZXYZ[EH1]
        X1=int(round(MF*C1[0]))	
        for EH2 in range(0,len(VYZXYZ)):
            C2=VYZXYZ[EH2]
            X2=int(round(MF*C2[0]))
            dx=X2-X1
            if dx==0:
                mdb.models[NameModel].Equation(name='C-ltedge'+str(EH1)+'-lbedge'+str(EH2)+'-RP1',
                terms=((-1.0,'RVE-1.ltedge'+str(EH1), 1),(1.0, 'RVE-1.V_lbedge'+str(EH2), 1),(1.0,'RP-1', 2)))
                mdb.models[NameModel].Equation(name='C-ltedge'+str(EH1)+'-lbedge'+str(EH2)+'-RP2',
                terms=((-1.0,'RVE-1.ltedge'+str(EH1), 2),(1.0, 'RVE-1.V_lbedge'+str(EH2), 2),(1.0,'RP-2', 2)))
                mdb.models[NameModel].Equation(name='C-ltedge'+str(EH1)+'-lbedge'+str(EH2)+'-RP3',
                terms=((-1.0,'RVE-1.ltedge'+str(EH1), 3),(1.0, 'RVE-1.V_lbedge'+str(EH2), 3),(1.0,'RP-3', 2)))
            else:
                continue
		
		#OX-YXY (rbedge-rtedge)
    for EB1 in range(0,len(VYXY)):
        dx=0
        C1=VYXY[EB1]
        X1=int(round(MF*C1[0]))
        for EB2 in range(0,len(YXY)):
            C2=YXY[EB2]
            X2=int(round(MF*C2[0]))
            dx=X1-X2
            if dx==0:
                mdb.models[NameModel].Equation(name='C-rbedge'+str(EB1)+'-rtedge'+str(EB2)+'-RP1',
                terms=((1.0,'RVE-1.V_rbedge'+str(EB1), 1),(-1.0, 'RVE-1.rtedge'+str(EB2), 1),(1.0,'RP-1', 2)))
                mdb.models[NameModel].Equation(name='C-rbedge'+str(EB1)+'-rtedge'+str(EB2)+'-RP2',
                terms=((1.0,'RVE-1.V_rbedge'+str(EB1), 2),(-1.0, 'RVE-1.rtedge'+str(EB2), 2),(1.0,'RP-2', 2)))
                mdb.models[NameModel].Equation(name='C-rbedge'+str(EB1)+'-rtedge'+str(EB2)+'-RP3',
                terms=((1.0,'RVE-1.V_rbedge'+str(EB1), 3),(-1.0, 'RVE-1.rtedge'+str(EB2), 3),(1.0,'RP-3', 2)))
            else:
                continue		
		
		#X-Planes (Back-Front)
		#Create dispalcement constrain for Virtual Nodes and X-plane
    for A1 in range(0,len(XB)):
        dy=0; dz=0;
        C1=XB[A1]
        Y1=int(round(MF*C1[1]))
        Z1=int(round(MF*C1[2]))
        for A2 in range(0,len(VXB)):
            C2=VXB[A2]
            Y2=int(round(MF*C2[1]))
            Z2=int(round(MF*C2[2]))
            dy=Y2-Y1
            dz=Z2-Z1
				#print(dy)
            if dy==0 and dz==0:
                mdb.models[NameModel].Equation(name='C-front'+str(A1)+'-back'+str(A2)+'RP1',
                terms=((-1.0,'RVE-1.front'+str(A1), 1),(1.0, 'RVE-1.V_back'+str(A2), 1),(1.0,'RP-1', 1)))
                mdb.models[NameModel].Equation(name='C-front'+str(A1)+'-back'+str(A2)+'RP2',
                terms=((-1.0,'RVE-1.front'+str(A1), 2),(1.0, 'RVE-1.V_back'+str(A2), 2),(1.0,'RP-2', 1)))
                mdb.models[NameModel].Equation(name='C-front'+str(A1)+'-back'+str(A2)+'RP3',
                terms=((-1.0,'RVE-1.front'+str(A1), 3),(1.0, 'RVE-1.V_back'+str(A2), 3),(1.0,'RP-3', 1)))
            else:
                continue				

		#Y-Planes (bot-top)
    for B1 in range(0,len(YB)):
        dx=0; dz=0;
        C1=YB[B1]
        X1=int(round(MF*C1[0]))
        Z1=int(round(MF*C1[2]))
        for B2 in range(0,len(VYB)):
            C2=VYB[B2]
            X2=int(round(MF*C2[0]))
            Z2=int(round(MF*C2[2]))
            dx=X2-X1
            dz=Z2-Z1
				#print(dy)
            if dx==0 and dz==0:
                mdb.models[NameModel].Equation(name='C-top'+str(B1)+'-bot'+str(B2)+'RP1',
                terms=((-1.0,'RVE-1.top'+str(B1), 1),(1.0, 'RVE-1.V_bot'+str(B2), 1),(1.0, 'RP-1', 2)))
                mdb.models[NameModel].Equation(name='C-top'+str(B1)+'-bot'+str(B2)+'RP2',
                terms=((-1.0,'RVE-1.top'+str(B1), 2),(1.0, 'RVE-1.V_bot'+str(B2), 2),(1.0, 'RP-2', 2)))
                mdb.models[NameModel].Equation(name='C-top'+str(B1)+'-bot'+str(B2)+'RP3',
                terms=((-1.0,'RVE-1.top'+str(B1), 3),(1.0, 'RVE-1.V_bot'+str(B2), 3),(1.0, 'RP-3', 2)))
            else:
                continue					
				
		# #Z-Planes
    for D1 in range(0,len(ZB)):
        dx=0; dy=0;
        C1=ZB[D1]
        X1=int(round(MF*C1[0]))
        Y1=int(round(MF*C1[1]))
        for D2 in range(0,len(VZB)):
            C2=VZB[D2]
            X2=int(round(MF*C2[0]))
            Y2=int(round(MF*C2[1]))
            dx=X2-X1
            dy=Y2-Y1
				#print(dy)
            if dy==0 and dx==0:
                mdb.models[NameModel].Equation(name='C-left'+str(D1)+'-right'+str(D2)+'RP1',
                terms=((-1.0,'RVE-1.left'+str(D1), 1),(1.0, 'RVE-1.V_right'+str(D2), 1),(1.0, 'RP-1', 3)))
                mdb.models[NameModel].Equation(name='C-left'+str(D1)+'-right'+str(D2)+'RP2',
                terms=((-1.0,'RVE-1.left'+str(D1), 2),(1.0, 'RVE-1.V_right'+str(D2), 2),(1.0, 'RP-2', 3)))
                mdb.models[NameModel].Equation(name='C-left'+str(D1)+'-right'+str(D2)+'RP3',
                terms=((-1.0,'RVE-1.left'+str(D1), 3),(1.0, 'RVE-1.V_right'+str(D2), 3),(1.0, 'RP-3', 3)))
            else:
                continue