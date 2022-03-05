To get the depth map of the object, please run the modules as the same order as the following steps:

1- "shadow_mask.py": this module creates and saves masks for each image. The created masks will be stored in
the folder "masks"

2- "photometric_stereo.py": this module calculates gradients of the normals (p and q) and albedo.

3- "depth_from_gradient.py": this module calculates depth using the function "frankotchellappa" of the module
"frankoChapello" which is given calculated p and q from step 2 as input, and finally plots the depth map and saves
the image as depth_map.png