# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

import math
import numpy as np

execfile('make_sets_2.py')
execfile('copy_nodes.py')
execfile('Create_Tie.py')
execfile('PBCfunction_SETS.py')
execfile('BC_ODB.py')
execfile('PBCfunctionE_VN_1.py')

step_name='elastic';
Vf=0.60;
R=0.008;
SR=math.sqrt
M_PI=math.pi
fraction=SR((2*M_PI)/(Vf))
IFD=fraction-2
print('Inter fiber distance calculated:  ', IFD)
Lx=2*R+IFD*R;
Ly=Lx;
Lz=0.003;
print('Dimensions of RVE:',Lx,Ly,Lz)
for mod in range (0,4):
    if mod==0:
        model_name='Model-1';Mod_Num='1'
        Lc=0.0008
    elif mod==1:
        model_name='Model-2';Mod_Num='2'
        Lc=0.0005
    elif mod==2:
        model_name='Model-3';Mod_Num='3'
        Lc=0.00025
    elif mod==3:
        model_name='Model-4';Mod_Num='4'
        Lc=0.0002
    #Create thnew model ///
    mdb.Model(modelType=STANDARD_EXPLICIT, name=model_name)
    mdb.models[model_name].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models[model_name].sketches['__profile__'].rectangle(point1=(0.0, 0.0), point2=(Lx, Ly))
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(Lx/2, Ly/2), point1=( (Lx/2)-R, Ly/2))
    mdb.models[model_name].Part(dimensionality=THREE_D, name='Matrix', type=DEFORMABLE_BODY)
    mdb.models[model_name].parts['Matrix'].BaseSolidExtrude(depth=Lz, sketch=
        mdb.models[model_name].sketches['__profile__'])
    del mdb.models[model_name].sketches['__profile__']
    
    # # Cut fibers from the matrix
	# # Cut the fibers space from matrix
    # # Create datums in matrix part for creation of the fiber space for fibers
    XY_plane=mdb.models[model_name].parts['Matrix'].DatumPlaneByPrincipalPlane(offset=0.0, principalPlane=XYPLANE)
    IDP=XY_plane.id
    Y_axis=mdb.models[model_name].parts['Matrix'].DatumAxisByPrincipalAxis(principalAxis=YAXIS)
    IDL1=Y_axis.id
    Z_axis=mdb.models[model_name].parts['Matrix'].DatumAxisByPrincipalAxis(principalAxis=ZAXIS)
    IDL2=Z_axis.id
    mdb.models[model_name].ConstrainedSketch(gridSpacing=0.02, name='__profile__', sheetSize=0.5, transform=
        mdb.models[model_name].parts['Matrix'].MakeSketchTransform(sketchPlane=mdb.models[model_name].parts['Matrix'].datums[IDP], 
        sketchPlaneSide=SIDE1,sketchUpEdge=mdb.models[model_name].parts['Matrix'].datums[IDL1], sketchOrientation=LEFT, origin=(0.0, 0.0, 0.0)))
    mdb.models[model_name].parts['Matrix'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models[model_name].sketches['__profile__'])
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(0.0,0.0), point1=(0.0,R))
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(Lx,0.0), point1=(Lx-R,0.0)) 
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(0.0,Ly), point1=(R,Ly))     
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(Lx,Ly), point1=(Lx,Ly-R)) 
    mdb.models[model_name].parts['Matrix'].CutExtrude(flipExtrudeDirection=ON, 
        sketch=mdb.models[model_name].sketches['__profile__'], sketchOrientation=
        LEFT, sketchPlane=mdb.models[model_name].parts['Matrix'].datums[IDP], 
        sketchPlaneSide=SIDE1, sketchUpEdge=
        mdb.models[model_name].parts['Matrix'].datums[3])
    del mdb.models[model_name].sketches['__profile__']
   
    #Create the fiber as a part
    mdb.models[model_name].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(Lx/2, Ly/2), point1=( (Lx/2)-R, Ly/2))
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(0.0,0.0), point1=(0.0,R))
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(Lx,0.0), point1=(Lx-R,0.0)) 
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(0.0,Ly), point1=(R,Ly))     
    mdb.models[model_name].sketches['__profile__'].CircleByCenterPerimeter(center=(Lx,Ly), point1=(Lx,Ly-R)) 
    mdb.models[model_name].Part(dimensionality=THREE_D, name='Fiber', type=DEFORMABLE_BODY)
    mdb.models[model_name].parts['Fiber'].BaseSolidExtrude(depth=Lz, sketch=mdb.models[model_name].sketches['__profile__'])
    del mdb.models[model_name].sketches['__profile__']
    
    XY_plane=mdb.models[model_name].parts['Fiber'].DatumPlaneByPrincipalPlane(offset=0.0, principalPlane=XYPLANE)
    IDP=XY_plane.id
    Y_axis=mdb.models[model_name].parts['Fiber'].DatumAxisByPrincipalAxis(principalAxis=YAXIS)
    IDL1=Y_axis.id
    Z_axis=mdb.models[model_name].parts['Fiber'].DatumAxisByPrincipalAxis(principalAxis=ZAXIS)
    IDL2=Z_axis.id
    mdb.models[model_name].ConstrainedSketch(gridSpacing=0.02, name='__profile__', sheetSize=0.5, transform=
        mdb.models[model_name].parts['Fiber'].MakeSketchTransform(sketchPlane=mdb.models[model_name].parts['Fiber'].datums[IDP], 
        sketchPlaneSide=SIDE1,sketchUpEdge=mdb.models[model_name].parts['Fiber'].datums[IDL1], sketchOrientation=LEFT, origin=(0.0, 0.0, 0.0)))
    mdb.models[model_name].parts['Fiber'].projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=mdb.models[model_name].sketches['__profile__'])
    mdb.models[model_name].sketches['__profile__'].rectangle(point1=(0.0, 0.0),point2=(Lx, Ly))
    mdb.models[model_name].sketches['__profile__'].rectangle(point1=(-R, -R),point2=(Lx+R, Ly+R))
    mdb.models[model_name].parts['Fiber'].CutExtrude(flipExtrudeDirection=ON, 
        sketch=mdb.models[model_name].sketches['__profile__'], sketchOrientation=
        LEFT, sketchPlane=mdb.models[model_name].parts['Fiber'].datums[IDP], 
        sketchPlaneSide=SIDE1, sketchUpEdge=
        mdb.models[model_name].parts['Fiber'].datums[3])
    del mdb.models[model_name].sketches['__profile__']

    #Create materials and assign section
    mdb.models[model_name].Material(name='Glass fiber')
    mdb.models[model_name].materials['Glass fiber'].Elastic(table=((72000.0, 0.22), ))
    mdb.models[model_name].Material(name='Epoxy')
    mdb.models[model_name].materials['Epoxy'].Elastic(table=((3300.0, 0.375),)) 

    #Creat section
    mdb.models[model_name].HomogeneousSolidSection(material='Glass fiber', name='Fibers', 
        thickness=1.0)
    mdb.models[model_name].HomogeneousSolidSection(material='Epoxy', name='Matrixs', 
        thickness=1.0)


    #Create and assign sections
    mdb.models[model_name].parts['Fiber'].Set(cells=(
        mdb.models[model_name].parts['Fiber'].cells,), name='Fiberface')
    mdb.models[model_name].parts['Fiber'].SectionAssignment(offset=0.0, offsetField='', 
        offsetType=MIDDLE_SURFACE, region=
        mdb.models[model_name].parts['Fiber'].sets['Fiberface'], sectionName=
        'Fibers', thicknessAssignment=FROM_SECTION)
    mdb.models[model_name].parts['Matrix'].Set(cells=(
        mdb.models[model_name].parts['Matrix'].cells,), name='Matrixface')
    mdb.models[model_name].parts['Matrix'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models[model_name].parts['Matrix'].sets['Matrixface'], 
        sectionName='Matrixs', thicknessAssignment=FROM_SECTION)

    # #create assebly and generate mesh
    mdb.models[model_name].rootAssembly.Instance(dependent=OFF, name='Fiber', part=
        mdb.models[model_name].parts['Fiber'])
    mdb.models[model_name].rootAssembly.Instance(dependent=OFF, name='Matrix', 
        part=mdb.models[model_name].parts['Matrix'])
    mdb.models[model_name].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
        instances=(mdb.models[model_name].rootAssembly.instances['Fiber'], 
        mdb.models[model_name].rootAssembly.instances['Matrix']),
        keepIntersections=ON, name='RVE', originalInstances=DELETE)
    mdb.models[model_name].rootAssembly.makeDependent(instances=(
        mdb.models[model_name].rootAssembly.instances['RVE-1'], ))

    # #RVE
    mdb.models[model_name].parts['RVE'].seedPart(deviationFactor=0.1, 
        minSizeFactor=0.1, size=Lc)
    mdb.models[model_name].parts['RVE'].setElementType(elemTypes=(ElemType(
        elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
        kinematicSplit=AVERAGE_STRAIN, hourglassControl=ENHANCED, 
        distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
        ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
        mdb.models[model_name].parts['RVE'].cells.getByBoundingBox(0.0,0.0,0.0,Lx,Ly,Lz), ))
    mdb.models[model_name].parts['RVE'].setMeshControls(algorithm=ADVANCING_FRONT, 
        regions=mdb.models[model_name].parts['RVE'].cells.getByBoundingBox(0.0,0.0,0.0,Lx,Ly,Lz), technique=SWEEP)
    mdb.models[model_name].parts['RVE'].generateMesh()

    #Create Step
    step_name='elastic'
    mdb.models[model_name].StaticStep(name='elastic', previous='Initial')
    mdb.models[model_name].fieldOutputRequests['F-Output-1'].setValues(
        variables=('E', 'S', 'IVOL','U','EVOL'))
    mdb.models[model_name].HistoryOutputRequest(createStepName=
        'elastic', name='H-Output-1', variables=('ALLAE', 'ALLIE', 'ALLSE', 
        'ETOTAL'))
    #Constrain for perodic PBC and solving job
    mdb.models[model_name].parts['RVE'].Set(faces=(mdb.models[model_name].parts['RVE'].faces,), name='PerBound')
    #Make sets of the part in RVE
    (NameRef1, NameRef2, NameRef3, NameRef4, NameRef5, NameRef6)=make_sets(mdb,model_name,'PerBound',[(0.0,0.0,0.0),(Lx,Ly,Lz)],Lc)
    #create sets of the RVE to make PBC and Reference points
    (OY,YXY,XYX,OX,ZYZ,YZXYZ,XYZXZ,XZZ,OZ,YYZ,XZX,XYXYZ,X,XB,Y,YB,Z,ZB)=PeriodicBound3DE_SETS(mdb,model_name,'PerBound',[(0.0,0.0,0.0),(Lx,Ly,Lz)],Lc)
    #Create the reference points in assembly 
    (VXYX,VXYZXZ,VYZXYZ,VYXY,VXYXYZ,VXZX,VXB,VYB,VZB)=create_Reference_nodes(mdb,model_name,'RVE',[(0.0,0.0,0.0),(Lx,Ly,Lz)],Lc,OY,YXY,XYX,OX,ZYZ,YZXYZ,XYZXZ,XZZ,OZ,YYZ,XZX,XYXYZ,X,XB,Y,YB,Z,ZB)
    #Regenerate assembly
    mdb.models[model_name].rootAssembly.regenerate()
    #Create TIE constrain between the RVE and virtual nodes
    Tie_constrains(mdb,model_name)
    PeriodicBound3DE(mdb,model_name,OY,YXY,XYX,OX,ZYZ,YZXYZ,XYZXZ,XZZ,OZ,YYZ,XZX,XYXYZ,X,XB,Y,YB,Z,ZB,VXYX,VXYZXZ,VYZXYZ,VYXY,VXYXYZ,VXZX,VXB,VYB,VZB)
    print(mod+1)
    for i in range(0,3):
        direction=1+i
        print(direction)
        if direction==1:
            job_type='-E11'
            job_name=Mod_Num+job_type
            Ref_point1='RP-1'; Ref_point2='RP-2'; Ref_point3='RP-3'; C1=Lx*0.01; C2=0.0; job=job_name
            # BC_JOB(step_name,mdb,model_name,Ref_point1,Ref_point2,Ref_point3,C1,C2,job)
        # elif direction==2:
            # job_type='-E22'
            # job_name=Mod_Num+job_type
            # Ref_point1='RP-2'; Ref_point2='RP-1'; Ref_point3='RP-3'; C1=Ly*0.01; C2=0.0; job=job_name
            # BC_JOB(step_name,mdb,model_name,Ref_point1,Ref_point2,Ref_point3,C1,C2,job)
        # elif direction==3:
            # job_type='-E33'
            # job_name=Mod_Num+job_type
            # Ref_point1='RP-3'; Ref_point2='RP-2'; Ref_point3='RP-1'; C1=Lz*0.01; C2=0.0; job=job_name
            # BC_JOB(step_name,mdb,model_name,Ref_point1,Ref_point2,Ref_point3,C1,C2,job)
        # else:
            # continue
    # print("New Model will be created")