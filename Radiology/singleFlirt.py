from nipype.interfaces import fsl
import os
flt = fsl.BET()
for i in range(1,33):
	os.mkdir('/root/Radiology/Bet/'+str(i))
	flt.inputs.in_file = '/root/Radiology/Flirt/'+str(i)+'/T1_flirt.nii.gz'
	flt.inputs.frac = 0.7
	flt.inputs.out_file = '/root/Radiology/Bet/'+str(i)+'/T1_bet.nii.gz' 
	res = flt.run()
	if os.path.exists('/root/Radiology/Flirt/'+str(i)+'/T2_flirt.nii.gz'):
		flt.inputs.in_file = '/root/Radiology/Flirt/'+str(i)+'/T2_flirt.nii.gz'
        	flt.inputs.frac = 0.7
        	flt.inputs.out_file = '/root/Radiology/Bet/'+str(i)+'/T2_bet.nii.gz'
        	res = flt.run()
	if os.path.exists('/root/Radiology/Flirt/'+str(i)+'/FLAIR_flirt.nii.gz'):
		flt.inputs.in_file = '/root/Radiology/Flirt/'+str(i)+'/FLAIR_flirt.nii.gz'
        	flt.inputs.frac = 0.7
        	flt.inputs.out_file = '/root/Radiology/Bet/'+str(i)+'/FLAIR_bet.nii.gz'
        	res = flt.run()
