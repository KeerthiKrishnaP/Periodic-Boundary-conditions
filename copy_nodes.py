def create_Reference_nodes(mdb,model_name,part_name,Lv,Lc,OY,YXY,XYX,OX,ZYZ,YZXYZ,XYZXZ,XZZ,OZ,YYZ,XZX,XYXYZ,X,XB,Y,YB,Z,ZB):
    #Parameters for the copied mesh 
    T=1000
    Tp=1000
    F=T*10
    Lx=Lv[1][0];Ly=Lv[1][1];Lz=Lv[1][2]
	#Virtual node for bredge & the node from fredge are copied
    Name_of_vector=XYX;Name_of_virtual_node='V_bredge' ;NameModel=model_name;Virtual_SET_Name='SET_Virtual_Node_(fr-br)edge'
    BB=[(-Lx/T-Lc/F,Lc/F,-Lc/F),(-Lx/T+Lc/F,Ly-Lc/F,Lc/F)]
    VXYX=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
	
	#Virtual node for bledge & the node from fledge are copied
    Name_of_vector=XYZXZ;Name_of_virtual_node='V_bledge' ;NameModel=model_name;Virtual_SET_Name='SET_Virtual_Node_(fl-bl)edge' 
    BB=[(-Lx/T-Lc/F,Lc/F,Lz-Lc/F),(-Lx/T+Lc/F,Ly-Lc/F,Lz+Lc/F)]
    VXYZXZ=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
	
	#Virtual node for lbedge & the nodes from ltedge are copied
    Name_of_vector=YZXYZ;Name_of_virtual_node='V_lbedge' ;NameModel=model_name;Virtual_SET_Name='SET_Virtual_Node_(lt-lb)edge'
    BB=[(Lc/F,-Ly/T-Lc/F,Lz-Lc/F),(Lx-Lc/F,-Ly/T+Lc/F,Lz+Lc/F)]
    VYZXYZ=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
	
	#Virtual node for rbedge & the nodes from rtedge are copied
    Name_of_vector=YXY;Name_of_virtual_node='V_rbedge' ;NameModel=model_name;Virtual_SET_Name='SET_Virtual_Node_(rt-rb)edge'
    BB=[(Lc/F,-Ly/T-Lc/F,-Lc/F),(Lx-Lc/F,-Ly/T+Lc/F,Lc/F)]
    VYXY=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
	
	#Virtual node for btedge & the nodes of ftedge are copied
    Name_of_vector=XYXYZ;Name_of_virtual_node='V_btedge' ;NameModel=model_name;Virtual_SET_Name='SET_Virtual_Node_(ft-bt)edge'
    BB=[(-Lx/T-Lc/F,Ly+Ly/T-Lc/F,Lc/F),(-Lx/T+Lc/F,Ly+Ly/T+Lc/F,Lz-Lc/F)]
    VXYXYZ=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
	
	#Virtual node for bbedge & the nodes of fbedge are copied
    Name_of_vector=XZX;Name_of_virtual_node='V_bbedge' ;NameModel=model_name;Virtual_SET_Name='SET_Virtual_Node_(fb-bb)edge'
    BB=[(-Lx/T-Lc/F,-Ly/T-Lc/F,Lc/F),(-Lx/T+Lc/F,-Ly/T+Lc/F,Lz-Lc/F)]
    VXZX=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
	
	#Virtual node for fbedge & the nodes of ftedge are copied
    Name_of_vector=XYXYZ;Name_of_virtual_node='V_fbedge' ;NameModel=model_name;Virtual_SET_Name='SET_Virtual_Node_(ft-fb)edge'
    BB=[(Lx+Lx/T-Lc/F,-Ly/T-Lc/F,Lc/F),(Lx+Lx/T+Lc/F,-Ly/T+Lc/F,Lz-Lc/F)]
    createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
	
	#Create virtial nodes for Surfaces
	#Virtual Nodes for back & the nodes of the front surface are copied
    Name_of_vector=XB; Name_of_virtual_node='V_back' ; NameModel=model_name; Virtual_SET_Name='SET_Virtual_Node_back'
    BB=[(-Lx/T-Lc/F,Lc/F,Lc/F),(-Lx/T+Lc/F,Ly-Lc/F,Lz-Lc/F)]
    VXB=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
	
	#Virtual Nodes for bot & the nodes from top surface are copieds
    Name_of_vector=YB; Name_of_virtual_node='V_bot' ; NameModel=model_name; Virtual_SET_Name='SET_Virtual_Node_bot'
    BB=[(Lc/F,-Ly/T-Lc/F,Lc/F),(Lx-Lc/F,-Ly/T+Lc/F,Lz-Lc/F)]
    VYB=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
    
    #Virtual Nodes for bot & the nodes from top surface are copieds
    Name_of_vector=ZB; Name_of_virtual_node='V_right' ; NameModel=model_name; Virtual_SET_Name='SET_Virtual_Node_right'
    BB=[(Lc/F,Lc/F,-Lz/T-Lc/F),(Lx-Lc/F,Ly-Lc/F,-Lz/T+Lc/F)]
    VZB=createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc)
    return(VXYX,VXYZXZ,VYZXYZ,VYXY,VXYXYZ,VXZX,VXB,VYB,VZB)
  
    
def createvirtualset(Name_of_vector,Name_of_virtual_node,NameModel,part_name,Virtual_SET_Name,T,Tp,Lx,Ly,Lz,BB,Lc):
    Virtual_Vector=[]
    Tv=T*10
	# print(Name_of_virtual_node)
	# print(len(Name_of_vector))
    for V in range(0,len(Name_of_vector)):
		#Virtual node for edges
        if Name_of_virtual_node=='V_bredge':
            C=Name_of_vector[V]; Vx=-Lx/T; Vy=C[1]; Vz=C[2]
            Virtual_Vector.append(C)
        elif Name_of_virtual_node=='V_bledge':
            C=Name_of_vector[V]; Vx=-Lx/T; Vy=C[1]; Vz=C[2]
            Virtual_Vector.append(C)
        elif Name_of_virtual_node=='V_lbedge':
            C=Name_of_vector[V]; Vx=C[0]; Vy=-Ly/T; Vz=C[2]
            Virtual_Vector.append(C)
        elif Name_of_virtual_node=='V_rbedge':
            C=Name_of_vector[V]; Vx=C[0]; Vy=-Ly/T; Vz=C[2]
            Virtual_Vector.append(C)
        elif Name_of_virtual_node=='V_btedge':
            C=Name_of_vector[V]; Vx=-Lx/T; Vy=Ly+Ly/T; Vz=C[2]
            Virtual_Vector.append(C)
        elif Name_of_virtual_node=='V_bbedge':
            C=Name_of_vector[V]; Vx=-Lx/T; Vy=-Ly/T; Vz=C[2]
            Virtual_Vector.append(C)
        elif Name_of_virtual_node=='V_fbedge':
            C=Name_of_vector[V]; Vx=Lx+Lx/T; Vy=-Ly/T; Vz=C[2]
            Virtual_Vector.append(C)
		#Virtual node for surfcae
        elif Name_of_virtual_node=='V_back':
            C=Name_of_vector[V]; Vx=-Lx/Tp; Vy=C[1]; Vz=C[2]
            Virtual_Vector.append(C)
        elif Name_of_virtual_node=='V_bot':
            C=Name_of_vector[V]; Vx=C[0]; Vy=-Ly/Tp; Vz=C[2]
            Virtual_Vector.append(C)
        elif Name_of_virtual_node=='V_right':
            C=Name_of_vector[V]; Vx=C[0]; Vy=C[1]; Vz=-Lz/Tp
            Virtual_Vector.append(C)
        mdb.models[NameModel].parts[part_name].Node(coordinates=(Vx, Vy, Vz))
        #create set for the virtual node
        mdb.models[NameModel].parts[part_name].Set(name=Name_of_virtual_node+str(V), nodes=mdb.models[NameModel].parts[part_name].nodes.getByBoundingBox(Vx-Lc/Tv,Vy-Lc/Tv,Vz-Lc/Tv,Vx+Lc/Tv,Vy+Lc/Tv,Vz+Lc/Tv))
    mdb.models[NameModel].parts[part_name].Set(name=Virtual_SET_Name, nodes=mdb.models[NameModel].parts[part_name].nodes.getByBoundingBox(BB[0][0],BB[0][1],BB[0][2],BB[1][0],BB[1][1],BB[1][2]))
    return(Virtual_Vector)