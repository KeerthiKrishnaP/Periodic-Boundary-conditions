#Sub funtions
def BC_JOB(step_name,mdb,model_name,Ref_point1,Ref_point2,Ref_point3,C1,C2,job_name):
	Type=job_name.split('-', 1 )
	job=Type[1]
	num_CPUS=1
	if job=='G12':
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-1', region=mdb.models[model_name].rootAssembly.sets[Ref_point1], u1=C1, 
			u2=C2, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)

		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-2', region=mdb.models[model_name].rootAssembly.sets[Ref_point2], u1=0.0,
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)

		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-3', region=mdb.models[model_name].rootAssembly.sets[Ref_point3], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
	#JOB_Submission for G12
		mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
			explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
			memory=90, memoryUnits=PERCENTAGE, model=model_name, modelPrint=OFF, 
			multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
			numCpus=num_CPUS, numDomains=4, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
			'', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
		mdb.jobs[job_name].submit(consistencyChecking=OFF)
		mdb.jobs[job_name].waitForCompletion()
	
	elif job=='G13':
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-1', region=mdb.models[model_name].rootAssembly.sets[Ref_point1], u1=C1, 
			u2=0.0, u3=C2, ur1=UNSET, ur2=UNSET, ur3=UNSET)

		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-2', region=mdb.models[model_name].rootAssembly.sets[Ref_point2], u1=0.0,
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)

		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-3', region=mdb.models[model_name].rootAssembly.sets[Ref_point3], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
	#JOB_Submission for G13
		mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
			explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
			memory=90, memoryUnits=PERCENTAGE, model=model_name, modelPrint=OFF, 
			multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
			numCpus=num_CPUS, numDomains=4, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
			'', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
		mdb.jobs[job_name].submit(consistencyChecking=OFF)
		mdb.jobs[job_name].waitForCompletion()
	
	elif job=='G23':
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-1', region=mdb.models[model_name].rootAssembly.sets[Ref_point1], u1=0.0, 
			u2=C1, u3=C2, ur1=UNSET, ur2=UNSET, ur3=UNSET)

		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-2', region=mdb.models[model_name].rootAssembly.sets[Ref_point2], u1=0.0,
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)

		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-3', region=mdb.models[model_name].rootAssembly.sets[Ref_point3], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
	#JOB_Submission for G13
		mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
			explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
			memory=90, memoryUnits=PERCENTAGE, model=model_name, modelPrint=OFF, 
			multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
			numCpus=num_CPUS, numDomains=4, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
			'', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
		mdb.jobs[job_name].submit(consistencyChecking=OFF)
		mdb.jobs[job_name].waitForCompletion()
	
	elif job=='E11':
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-1', region=mdb.models[model_name].rootAssembly.sets[Ref_point1], u1=C1, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-2', region=mdb.models[model_name].rootAssembly.sets[Ref_point2], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-3', region=mdb.models[model_name].rootAssembly.sets[Ref_point3], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)

	#JOB_Submission for E11
		mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
			explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
			memory=90, memoryUnits=PERCENTAGE, model=model_name, modelPrint=OFF, 
			multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
			numCpus=num_CPUS, numDomains=4, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
			'', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
		mdb.jobs[job_name].submit(consistencyChecking=OFF)
		mdb.jobs[job_name].waitForCompletion()
	
	elif job=='E22':
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-1', region=mdb.models[model_name].rootAssembly.sets[Ref_point1], u1=0.0, 
			u2=C1, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-2', region=mdb.models[model_name].rootAssembly.sets[Ref_point2], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-3', region=mdb.models[model_name].rootAssembly.sets[Ref_point3], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
			
	#JOB_Submission for E22
		mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
			explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
			memory=90, memoryUnits=PERCENTAGE, model=model_name, modelPrint=OFF, 
			multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
			numCpus=num_CPUS, numDomains=4, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
			'', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
		mdb.jobs[job_name].submit(consistencyChecking=OFF)
		mdb.jobs[job_name].waitForCompletion()

	elif job=='E33':
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-1', region=mdb.models[model_name].rootAssembly.sets[Ref_point1], u1=0.0, 
			u2=0.0, u3=C1, ur1=UNSET, ur2=UNSET, ur3=UNSET)
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-2', region=mdb.models[model_name].rootAssembly.sets[Ref_point2], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)
		mdb.models[model_name].DisplacementBC(amplitude=UNSET, createStepName=step_name, 
			distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
			'BC-3', region=mdb.models[model_name].rootAssembly.sets[Ref_point3], u1=0.0, 
			u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET)

	#JOB_Submission for E33
		mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
			explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
			memory=90, memoryUnits=PERCENTAGE, model=model_name, modelPrint=OFF, 
			multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
			numCpus=num_CPUS, numDomains=4, numGPUs=0, queue=None, resultsFormat=ODB, scratch=
			'', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
		mdb.jobs[job_name].submit(consistencyChecking=OFF)
		mdb.jobs[job_name].waitForCompletion()