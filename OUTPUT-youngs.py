##############################################################################################################
##Output Homogenized properties##
##############################################################################################################
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
from visualization import *

file=open('Output youngs modulus_EVOL.txt',"w+")
file.write('youngs modulus in fiber dirrection E33 \n')
file.write('youngs modulus in transverse dirrection E22 \n')
file.write('poissions ratio in fiber dirrection nu23 \n')
file.write('poissions ratio in transverse dirrection nu12 \n')
file.write('E33,		E11,		E22,		n13,		n23,		n12 \n')
E33=[];E22=[];n23=[];n12=[]
for i in range(0,3):
    if i==0:
        prefix='1'
    elif i==1:
        prefix='2'
    elif i==2:
        prefix='3'   
    print('new run')
    Lc=0.05
    EcT=Lc;
    job1=prefix+'-E11.odb'
    job2=prefix+'-E22.odb'
    job3=prefix+'-E33.odb'

    # Open the Output Data Base for the current Job
    odb = openOdb(path=job1);
    myAssembly = odb.rootAssembly;
    #Take the elements sets only in the RVE but not in thet capsule
    RVE=odb.rootAssembly.instances['RVE-1']
    # Creating a temporary variable to hold the frame repository
    # provides the same functionality and speeds up the process
    frameRepository = odb.steps['elastic'].frames;
    frameS=[];
    frameE=[];
    frameIVOL=[];
    # Get only the last frame [-1]
    frameE.insert(0,frameRepository[-1].fieldOutputs['E']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
    frameS.insert(0,frameRepository[-1].fieldOutputs['S']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
    frameIVOL.insert(0,frameRepository[-1].fieldOutputs['EVOL']
    .getSubset(region=RVE,position=WHOLE_ELEMENT,elementType='C3D8R'));
    # Total Volume
    Tot_Vol=0;
    # Stress Sum
    Tot_Strain=0;
    #Total strain energy
    Tot_Stress=0;
    print(len(frameE[-1].values))
    print(len(frameS[-1].values))
    print(len(frameIVOL[-1].values))
    for El_Num in range(0,len(frameE[-1].values)):
        Tot_Vol=Tot_Vol+frameIVOL[0].values[El_Num].data;
        Tot_Strain=Tot_Strain+frameE[0].values[El_Num].data * frameIVOL[0].values[El_Num].data;
        Tot_Stress=Tot_Stress+frameS[0].values[El_Num].data * frameIVOL[0].values[El_Num].data;
    # Calculate Average
    Avg_Strain = Tot_Strain/Tot_Vol;
    Avg_Stress = Tot_Stress/Tot_Vol;
    # print('File number',i+1)
    print('E11')
    print ('Abaqus/Standard Stress Tensor Order:')
    print('Strain E11 E22 E33 E12 E13 E23',Avg_Strain)
    print('Stress S11 S22 S33 S12 S13 S23',Avg_Stress)
    print(Tot_Vol)
    S11=Avg_Stress[0];S22=Avg_Stress[1];S33=Avg_Stress[2]; S12=Avg_Stress[3]; S13=Avg_Stress[4]; S23=Avg_Stress[5]
    E11=Avg_Strain[0];E22=Avg_Strain[1];E33=Avg_Strain[2]; E12=Avg_Strain[3]; E13=Avg_Strain[4]; E23=Avg_Strain[5];

    C11=Avg_Stress[0]/Avg_Strain[0];
    C21=Avg_Stress[1]/Avg_Strain[0];
    C31=Avg_Stress[2]/Avg_Strain[0]

    # ##
    odb = openOdb(path=job2);
    myAssembly = odb.rootAssembly;
    #Take the elements sets only in the RVE but not in thet capsule
    RVE=odb.rootAssembly.instances['RVE-1']
    # Creating a temporary variable to hold the frame repository
    # provides the same functionality and speeds up the process
    frameRepository = odb.steps['elastic'].frames;
    frameS=[];
    frameE=[];
    frameIVOL=[];
    # Get only the last frame [-1]
    frameE.insert(0,frameRepository[-1].fieldOutputs['E']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
    frameS.insert(0,frameRepository[-1].fieldOutputs['S']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
    frameIVOL.insert(0,frameRepository[-1].fieldOutputs['EVOL']
    .getSubset(region=RVE,position=WHOLE_ELEMENT,elementType='C3D8R'));
    # Total Volume
    Tot_Vol=0;
    # Stress Sum
    Tot_Strain=0;
    #Total strain energy
    Tot_Stress=0;
    print(len(frameE[-1].values))
    print(len(frameS[-1].values))
    print(len(frameIVOL[-1].values))
    for El_Num in range(0,len(frameE[-1].values)):
        Tot_Vol=Tot_Vol+frameIVOL[0].values[El_Num].data;
        Tot_Strain=Tot_Strain+frameE[0].values[El_Num].data * frameIVOL[0].values[El_Num].data;
        Tot_Stress=Tot_Stress+frameS[0].values[El_Num].data * frameIVOL[0].values[El_Num].data;
    # Calculate Average
    Avg_Strain = Tot_Strain/Tot_Vol;
    Avg_Stress = Tot_Stress/Tot_Vol;
    print('E22')
    print ('Abaqus/Standard Stress Tensor Order:')
    print('Strain E11 E22 E33 E12 E13 E23',Avg_Strain)
    print('Stress S11 S22 S33 S12 S13 S23',Avg_Stress)
    print(Tot_Vol)
    S11=Avg_Stress[0];S22=Avg_Stress[1];S33=Avg_Stress[2]; S12=Avg_Stress[3]; S13=Avg_Stress[4]; S23=Avg_Stress[5]
    E11=Avg_Strain[0];E22=Avg_Strain[1];E33=Avg_Strain[2]; E12=Avg_Strain[3]; E13=Avg_Strain[4]; E23=Avg_Strain[5];

    C12=Avg_Stress[0]/Avg_Strain[1];
    C22=Avg_Stress[1]/Avg_Strain[1];
    C32=Avg_Stress[2]/Avg_Strain[1]

    # #######
    odb = openOdb(path=job3);
    myAssembly = odb.rootAssembly;
    #Take the elements sets only in the RVE but not in thet capsule
    RVE=odb.rootAssembly.instances['RVE-1']
    # Creating a temporary variable to hold the frame repository
    # provides the same functionality and speeds up the process
    frameRepository = odb.steps['elastic'].frames;
    frameS=[];
    frameE=[];
    frameIVOL=[];
    # Get only the last frame [-1]
    frameE.insert(0,frameRepository[-1].fieldOutputs['E']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
    frameS.insert(0,frameRepository[-1].fieldOutputs['S']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
    frameIVOL.insert(0,frameRepository[-1].fieldOutputs['EVOL']
    .getSubset(region=RVE,position=WHOLE_ELEMENT,elementType='C3D8R'));
    # Total Volume
    Tot_Vol=0;
    # Stress Sum
    Tot_Strain=0;
    #Total strain energy
    Tot_Stress=0;
    print('E33')
    print(len(frameE[-1].values))
    print(len(frameS[-1].values))
    print(len(frameIVOL[-1].values))
    for El_Num in range(0,len(frameE[-1].values)):
        Tot_Vol=Tot_Vol+frameIVOL[0].values[El_Num].data;
        Tot_Strain=Tot_Strain+frameE[0].values[El_Num].data * frameIVOL[0].values[El_Num].data;
        Tot_Stress=Tot_Stress+frameS[0].values[El_Num].data * frameIVOL[0].values[El_Num].data;
    # Calculate Average
    Avg_Strain = Tot_Strain/Tot_Vol;
    Avg_Stress = Tot_Stress/Tot_Vol;
    print ('Abaqus/Standard Stress Tensor Order:')
    print('Strain E11 E22 E33 E12 E13 E23',Avg_Strain)
    print('Stress S11 S22 S33 S12 S13 S23',Avg_Stress)
    print(Tot_Vol)
    S11=Avg_Stress[0];S22=Avg_Stress[1];S33=Avg_Stress[2]; S12=Avg_Stress[3]; S13=Avg_Stress[4]; S23=Avg_Stress[5]
    E11=Avg_Strain[0];E22=Avg_Strain[1];E33=Avg_Strain[2]; E12=Avg_Strain[3]; E13=Avg_Strain[4]; E23=Avg_Strain[5];

    C13=Avg_Stress[0]/Avg_Strain[2];
    C23=Avg_Stress[1]/Avg_Strain[2];
    C33=Avg_Stress[2]/Avg_Strain[2]

    # ####### evaluation of the properties##
    EL=C33-((2*C13*C13)/(C11+C12))
    # #E33.append(EL)
    print('Logitudnal Youngs Modulus direction 3: ', EL)
    ET=(C33*(C11+C12)-(2*C13*C13))*((C11-C12)/((C33*C11)-(C13*C13)))
    ET2=(C33*(C11+C12)-(2*C23*C23))*((C22-C12)/((C33*C11)-(C23*C23)))
    # #E22.append(ET)
    print('Transverse Youngs Modulus in direction 1: ', ET)
    print('Transverse Youngs Modulus in direction 2: ', ET2)
    nuT12=C13/(C11+C12)
    nuL23=C23/(C33+C12)
    # #n23.append(nuL)
    nuL13=(C33*C12-(C13*C13))/((C33*C11)-(C13*C13))
    nuL23=(C33*C12-(C23*C23))/((C33*C22)-(C23*C23))
    # #n12.append(nUT)
    print('Logitudnal poissons ratio nuL13: ',nuL13)
    print('Logitudnal poissons ratio nuL23: ',nuL23)
    print('Transverse poissons ratio: ',nuT12)
    file.write("%s,%s,%s,%s,%s,%s\n" %(EL, ET, ET2, nuL13, nuL23, nuT12))
file.close()