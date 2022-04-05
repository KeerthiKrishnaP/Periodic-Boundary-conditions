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

file=open('Output shear modulus.txt',"w+")
file.write('shear modulus in fiber dirrection G23 \n')
file.write('shear modulus in transverse dirrection G12 \n')
file.write('shear modulus in transverse dirrection G13 \n')
file.write('G12,	G13,	G23\n')
for i in range (0,3):
    if i==0:
        prefix='1'
    elif i==1:
        prefix='2'
    elif i==2:
        prefix='3'
    print('new run')
    job1=prefix+'-G12.odb'
    job2=prefix+'-G13.odb'
    job3=prefix+'-G23.odb'
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
    frameIVOL.insert(0,frameRepository[-1].fieldOutputs['IVOL']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
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
    C44=Avg_Stress[3]/Avg_Strain[3]
    G12=S12/E12
    print('Shear modulus G12: ',S12/E12)
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
    frameIVOL.insert(0,frameRepository[-1].fieldOutputs['IVOL']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
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
    C55=Avg_Stress[4]/Avg_Strain[4]
    G13=S13/E13
    print('Shear modulus G13: ',G13)

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
    frameIVOL.insert(0,frameRepository[-1].fieldOutputs['IVOL']
    .getSubset(region=RVE,position=INTEGRATION_POINT,elementType='C3D8R'));
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

    C66=Avg_Stress[5]/Avg_Strain[5]
    G23=S23/E23
    print('Shear modulus G23: ',G23)
    file.write("%s,%s,%s\n" %(G12,G13,G23))
file.close()