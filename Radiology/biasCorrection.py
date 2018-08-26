from nipype.interfaces import fsl
import os
fastr = fsl.FAST()
for i in range(1,2):
        infilestr='/root/Radiology/cbtc_train_'+str(i)+'/T1.nii'
	os.mkdir('/root/Radiology/'+str(i))
        outstr='/root/Radiology/'+str(i)+'/fast_'+str(i)+'_T1'
        fastr.inputs.in_files = infilestr
        fastr.inputs.bias_iters = 8
        fastr.inputs.number_classes = 4
        fastr.inputs.out_basename = outstr
        out = fastr.run()
        infilestr='/root/Radiology/cbtc_train_'+str(i)+'/T1C.nii'
        outstr='/root/Radiology/'+str(i)+'/fast_'+str(i)+'_T1C'
        fastr.inputs.in_files = infilestr
        fastr.inputs.bias_iters = 8
        fastr.inputs.number_classes = 4
        fastr.inputs.out_basename = outstr
        out = fastr.run()
        infilestr='/root/Radiology/cbtc_train_'+str(i)+'/T2.nii'
        outstr='/root/Radiology/'+str(i)+'/fast_'+str(i)+'_T2'
        fastr.inputs.in_files = infilestr
        fastr.inputs.bias_iters = 8
        fastr.inputs.number_classes = 4
        fastr.inputs.out_basename = outstr
        out = fastr.run()
        infilestr='/root/Radiology/cbtc_train_'+str(i)+'/FLAIR.nii'
        outstr='/root/Radiology/'+str(i)+'/fast_'+str(i)+'_FLAIR'
        if os.path.exists(infilestr):
                fastr.inputs.in_files = infilestr
                fastr.inputs.bias_iters = 8
                fastr.inputs.number_classes = 4
                fastr.inputs.out_basename = outstr
                out = fastr.run()
