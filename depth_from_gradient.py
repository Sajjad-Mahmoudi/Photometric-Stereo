import numpy as np
from frankoChapello import frankotchellappa
import photometric_stereo as ps
from matplotlib import pyplot as plt

# get the depth map using frankotchellappa function
depth = frankotchellappa(ps.p, ps.q)

# get the real part of the numbers as suggested in "frankoChapello" module
depth_real = depth.real

# plot the depth map
plt.imshow(depth_real, cmap='gray')
plt.savefig('depth_map.png')
