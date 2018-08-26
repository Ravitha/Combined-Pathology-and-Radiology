import nipype.interfaces.fsl as fsl
applyxfm = fsl.preprocess.ApplyXFM()
applyxfm.inputs.in_file = '/root/Radiology/cbtc_train_1/T2.nii'
applyxfm.inputs.in_matrix_file = '/root/Radiology/Flirt/T1_flirt.mat'
applyxfm.inputs.reference = '/root/Radiology/cbtc_train_1/T1C.nii'
applyxfm.inputs.apply_xfm = True
result = applyxfm.run()
