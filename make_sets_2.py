#FUNCTION TO APPLY PERIODIC BOUNDARY CONDITIONS IN 3D
#LatticeVec:	An array with the lattice vectors, for example [(1.0, 0.0), (1.0, 1.0)] for a square lattice
def make_sets(mdb,NameModel,NameSet,LV,Lc):
    from part import THREE_D, DEFORMABLE_BODY
    #Create reference parts and assemble
    NameRef1='RP-1'; NameRef2='RP-2';NameRef3='RP-3';NameRef4='RP-4';NameRef5='RP-5'; NameRef6='RP-6'; Tol=10000;MF=100000;
    global RP 
    RP=6
    global Lx; global Ly; global Lz;
    Lx=LV[1][0]; Ly=LV[1][1]; Lz=LV[1][2]
    L1=int(round(MF*Lx));L2=int(round(MF*Ly));L3=int(round(MF*Lz));T=1000;Tp=1000;F=1000;
    mdb.models[NameModel].Part(dimensionality=THREE_D, name=NameRef2, type=DEFORMABLE_BODY)
    mdb.models[NameModel].parts[NameRef2].ReferencePoint(point=(Lx/2, Ly/2, Lz+0.25*Lz))
    mdb.models[NameModel].Part(dimensionality=THREE_D, name=NameRef1, type=DEFORMABLE_BODY)
    mdb.models[NameModel].parts[NameRef1].ReferencePoint(point=(Lx/2, Ly+0.25*Ly, Lz/2))
    mdb.models[NameModel].Part(dimensionality=THREE_D, name=NameRef4, type=DEFORMABLE_BODY)
    mdb.models[NameModel].parts[NameRef4].ReferencePoint(point=(Lx+0.5*Lx, Ly/2, Lz/2))
    mdb.models[NameModel].Part(dimensionality=THREE_D, name=NameRef3, type=DEFORMABLE_BODY)
    mdb.models[NameModel].parts[NameRef3].ReferencePoint(point=(Lx+0.25*Lx, Ly/2, Lz/2))
    mdb.models[NameModel].Part(dimensionality=THREE_D, name=NameRef6, type=DEFORMABLE_BODY)
    mdb.models[NameModel].parts[NameRef6].ReferencePoint(point=(Lx+Lx, Ly/2, Lz/2))
    mdb.models[NameModel].Part(dimensionality=THREE_D, name=NameRef5, type=DEFORMABLE_BODY)
    mdb.models[NameModel].parts[NameRef5].ReferencePoint(point=(Lx+0.75*Lx, Ly/2, Lz/2))
    mdb.models[NameModel].rootAssembly.Instance(dependent=ON, name=NameRef1, 
        part=mdb.models[NameModel].parts[NameRef1])
    mdb.models[NameModel].rootAssembly.Instance(dependent=ON, name=NameRef2, 
        part=mdb.models[NameModel].parts[NameRef2])
    mdb.models[NameModel].rootAssembly.Instance(dependent=ON, name=NameRef3, 
        part=mdb.models[NameModel].parts[NameRef3])
    mdb.models[NameModel].rootAssembly.Instance(dependent=ON, name=NameRef4, 
        part=mdb.models[NameModel].parts[NameRef4])
    mdb.models[NameModel].rootAssembly.Instance(dependent=ON, name=NameRef5, 
        part=mdb.models[NameModel].parts[NameRef5])
    mdb.models[NameModel].rootAssembly.Instance(dependent=ON, name=NameRef6, 
        part=mdb.models[NameModel].parts[NameRef6])

    # #Create set of reference points
    mdb.models[NameModel].rootAssembly.Set(name=NameRef1, referencePoints=(
        mdb.models[NameModel].rootAssembly.instances[NameRef1].referencePoints[1],))
    mdb.models[NameModel].rootAssembly.Set(name=NameRef2, referencePoints=(
        mdb.models[NameModel].rootAssembly.instances[NameRef2].referencePoints[1],))
    mdb.models[NameModel].rootAssembly.Set(name=NameRef3, referencePoints=(
        mdb.models[NameModel].rootAssembly.instances[NameRef3].referencePoints[1],))
    mdb.models[NameModel].rootAssembly.Set(name=NameRef4, referencePoints=(
        mdb.models[NameModel].rootAssembly.instances[NameRef4].referencePoints[1],))
    mdb.models[NameModel].rootAssembly.Set(name=NameRef5, referencePoints=(
        mdb.models[NameModel].rootAssembly.instances[NameRef5].referencePoints[1],))
    mdb.models[NameModel].rootAssembly.Set(name=NameRef6, referencePoints=(
        mdb.models[NameModel].rootAssembly.instances[NameRef6].referencePoints[1],))		
		
	#Make the sets of nodes on surfaces for the RVE
	#SET-Y  For the nodes on the plane Y=0: "BOTTOM"
    #NODES
    Part_Name='RVE';Set_Name='SET-Bottom';BB=[(Lc/F,-Lc/F,Lc/F),(Lx-Lc/F,Lc/F,Lz-Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #SURFACE
    Part_Name='RVE';Set_Name='Surface_Bottom';BB=[(0.0,0.0,0.0),(Lx,0.0,Lz)];type='faces';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #Make Surface
    Part_Name='RVE';Surf_Name='BOTTOM-SURFACE';BB_S=[(0.0,0.0,0.0),(Lx,0.0,Lz)]
    make_surface(NameModel,Part_Name,Surf_Name,BB_S)
    
	# #SET-X for the nodes in the plane X=0: "BACK"
    #NODES
    Part_Name='RVE';Set_Name='SET-Back';BB=[(-Lc/F,Lc/F,Lc/F),(Lc/F,Ly-Lc/F,Lz-Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #SURFACE
    Part_Name='RVE';Set_Name='Surface_Back';BB=[(0.0,0.0,0.0),(0.0,Ly,Lz)];type='faces';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #Make Surface
    Part_Name='RVE';Surf_Name='BACK-SURFACE';BB_S=[(0.0,0.0,0.0),(0.0,Ly,Lz)]
    make_surface(NameModel,Part_Name,Surf_Name,BB_S)
    
	# #SET-Z for the nodes in the plane Z=0: "RIGHT"
    #NODES
    Part_Name='RVE';Set_Name='SET-Right';BB=[(Lc/F,Lc/F,-Lc/F),(Lx-Lc/F,Ly-Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #SURFACE
    Part_Name='RVE';Set_Name='Surface_Right';BB=[(0.0,0.0,0.0),(Lx,Ly,0.0)];type='faces';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #Make Surface
    Part_Name='RVE';Surf_Name='RIGHT-SURFACE';BB_S=[(0.0,0.0,0.0),(Lx,Ly,0.0)]
    make_surface(NameModel,Part_Name,Surf_Name,BB_S)
    
	# #SET-YB  For the nodes on the plane Y=Ly: "TOP"
    #NODES
    Part_Name='RVE';Set_Name='SET-Top';BB=[(Lc/F,Ly-Lc/F,Lc/F),(Lx-Lc/F,Ly+Lc/F,Lz-Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #SURFACE
    Part_Name='RVE';Set_Name='Surface_Top';BB=[(0.0,Ly,0.0),(Lx,Ly,Lz)];type='faces';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #Make Surface
    Part_Name='RVE';Surf_Name='TOP-SURFACE';BB_S=[(0.0,Ly,0.0),(Lx,Ly,Lz)]
    make_surface(NameModel,Part_Name,Surf_Name,BB_S)
    
    # #SET-XB for the nodes in the plane X=Lx: "Front"
    #NODES
    Part_Name='RVE';Set_Name='SET-Front';BB=[(Lx-Lc/F,Lc/F,Lc/F),(Lx+Lc/F,Ly-Lc/F,Lz-Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #SURFACE
    Part_Name='RVE';Set_Name='Surface_Front';BB=[(Lx,0.0,0.0),(Lx,Ly,Lz)];type='faces';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #Make Surface
    Part_Name='RVE';Surf_Name='FRONT-SURFACE';BB_S=[(Lx,0.0,0.0),(Lx,Ly,Lz)]
    make_surface(NameModel,Part_Name,Surf_Name,BB_S)
    
	# #SET-ZB for the nodes in the plane Z=Lz: "LEFT"
    #NODES
    Part_Name='RVE';Set_Name='SET-Left';BB=[(Lc/F,Lc/F,Lz-Lc/F),(Lx-Lc/F,Ly-Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #SURFACE
    Part_Name='RVE';Set_Name='Surface_Left';BB=[(0.0,0.0,Lz),(Lx,Ly,Lz)];type='faces';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #Make Surface
    Part_Name='RVE';Surf_Name='LEFT-SURFACE';BB_S=[(0.0,0.0,Lz),(Lx,Ly,Lz)]
    make_surface(NameModel,Part_Name,Surf_Name,BB_S)

	# # #Make sets for the edge elements for the RVE:
	# # #SET for Edge-OX (rbedge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-rbedge';BB=[(Lc/F,-Lc/F,-Lc/F),(Lx-Lc/F,Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-rbedge';BB=[(0.0,0.0,0.0),(Lx,0.0,0.0)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-OY (bredge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-bredge';BB=[(-Lc/F,Lc/F,-Lc/F),(Lc/F,Ly-Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-bredge';BB=[(0.0,0.0,0.0),(0.0,Ly,0.0)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-OZ (bbedge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-bbedge';BB=[(-Lc/F,-Lc/F,Lc/F),(Lc/F,Lc/F,Lz-Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-bbedge';BB=[(0.0,0.0,0.0),(0.0,0.0,Lz)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-YXY (rtedge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-rtedge';BB=[(Lc/F,Ly-Lc/F,-Lc/F),(Lx-Lc/F,Ly+Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-rtedge';BB=[(0.0,Ly,0.0),(Lx,Ly,0.0)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-XYXYZ (ftedge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-ftedge';BB=[(Lx-Lc/F,Ly-Lc/F,Lc/F),(Lx+Lc/F,Ly+Lc/F,Lz-Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-ftedge';BB=[(Lx,Ly,0.0),(Lx,Ly,Lz)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-YZXYZ (ltedge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-ltedge';BB=[(Lc/F,Ly-Lc/F,Lz-Lc/F),(Lx-Lc/F,Ly+Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-ltedge';BB=[(0.0,Ly,Lz),(Lx,Ly,Lz)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-ZYZ (bledge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-bledge';BB=[(-Lc/F,Lc/F,Lz-Lc/F),(Lc/F,Ly-Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-bledge';BB=[(0.0,0.0,Lz),(0.0,Ly,Lz)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edges-ZXZ (lbedge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-lbedge';BB=[(Lc/F,-Lc/F,Lz-Lc/F),(Lx-Lc/F,Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-lbedge';BB=[(0.0,0.0,Lz),(Lx,0.0,Lz)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-YYZ (btedge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-btedge';BB=[(-Lc/F,Ly-Lc/F,Lc/F),(Lc/F,Ly+Lc/F,Lz-Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-btedge';BB=[(0.0,Ly,0.0),(0.0,Ly,Lz)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-XYZXZ (fledge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-fledge';BB=[(Lx-Lc/F,Lc/F,Lz-Lc/F),(Lx+Lc/F,Ly-Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-fledge';BB=[(Lx,0.0,Lz),(Lx,Ly,Lz)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# #SET for Edge-XZX (fbedge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-fbedge';BB=[(Lx-Lc/F,-Lc/F,Lc/F),(Lx+Lc/F,Lc/F,Lz-Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-fbedge';BB=[(Lx,0.0,0.0),(Lx,0.0,Lz)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    # #SET for Edge-XYX (fredge)
    #NODES
    Part_Name='RVE';Set_Name='SET_Edge-fredge';BB=[(Lx-Lc/F,Lc/F,-Lc/F),(Lx+Lc/F,Ly-Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    #EDGE
    Part_Name='RVE';Set_Name='Edge-fredge';BB=[(Lx,0.0,0.0),(Lx,Ly,0.0)];type='edges';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)

    # #make nodes as sets
    # ##RVE
    # #Origin-C7
    Part_Name='RVE';Set_Name='C7';BB=[(-Lc/F,-Lc/F,-Lc/F),(Lc/F,Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    # # #X_limit-C8
    Part_Name='RVE';Set_Name='C8';BB=[(Lx-Lc/F,-Lc/F,-Lc/F),(Lx+Lc/F,Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    # # #Y_limit-C3
    Part_Name='RVE';Set_Name='C3';BB=[(-Lc/F,Ly-Lc/F,-Lc/F),(Lc/F,Ly+Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    # # #Z_limit-C6
    Part_Name='RVE';Set_Name='C6';BB=[(-Lc/F,-Lc/F,Lz-Lc/F),(Lc/F,Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    # # #XY_limit-C4
    Part_Name='RVE';Set_Name='C4';BB=[(Lx-Lc/F,Ly-Lc/F,-Lc/F),(Lx+Lc/F,Ly+Lc/F,Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
	# # #XZ_limit-C5
    Part_Name='RVE';Set_Name='C5';BB=[(Lx-Lc/F,-Lc/F,Lz-Lc/F),(Lx+Lc/F,Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    # # #YZ_limit-C2
    Part_Name='RVE';Set_Name='C2';BB=[(-Lc/F,Ly-Lc/F,Lz-Lc/F),(Lc/F,Ly+Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    # # #XYZ_limit-C1
    Part_Name='RVE';Set_Name='C1';BB=[(Lx-Lc/F,Ly-Lc/F,Lz-Lc/F),(Lx+Lc/F,Ly+Lc/F,Lz+Lc/F)];type='nodes';
    make_all_sets(NameModel,Part_Name,Set_Name,BB,type)
    return(NameRef1, NameRef2,NameRef3,NameRef4,NameRef5,NameRef6)

def make_surface(NameModel,Part_Name,Surf_Name,BB_S):
    mdb.models[NameModel].parts[Part_Name].Surface(name=Surf_Name, side1Faces=
        mdb.models[NameModel].parts[Part_Name].faces.getByBoundingBox(BB_S[0][0],BB_S[0][1],BB_S[0][2],BB_S[1][0],BB_S[1][1],BB_S[1][2]))

def make_all_sets(NameModel,Part_Name,Set_Name,BB,type):
    if type=='nodes': 
        mdb.models[NameModel].parts[Part_Name].Set(name=Set_Name, nodes=
            mdb.models[NameModel].parts[Part_Name].nodes.getByBoundingBox(BB[0][0],BB[0][1],BB[0][2],BB[1][0],BB[1][1],BB[1][2]))
    elif type=='faces':
        mdb.models[NameModel].parts[Part_Name].Set(name=Set_Name, faces=
            mdb.models[NameModel].parts[Part_Name].faces.getByBoundingBox(BB[0][0],BB[0][1],BB[0][2],BB[1][0],BB[1][1],BB[1][2]))
    elif type=='edges':
        mdb.models[NameModel].parts[Part_Name].Set(name=Set_Name, edges=
            mdb.models[NameModel].parts[Part_Name].edges.getByBoundingBox(BB[0][0],BB[0][1],BB[0][2],BB[1][0],BB[1][1],BB[1][2]))