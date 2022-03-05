import numpy as np
import shadow_mask as sm

# read light coordinate from refined_light.txt file and convert to an array (12, 3)
lights = np.genfromtxt('refined_light.txt', delimiter=',', unpack=True)

'''photometric stereo function to get p and q
I is an 3D array of all images (h, w, no. of images)
mask is the corresponding shadow mask with the same shape as I
L is an array of the corresponding light sources (no. of images, 3)'''
def ps(I, mask, L):
    h, w, num_img = I.shape
    albedo = np.zeros((h, w))
    p = np.zeros((h, w))
    f = np.zeros((h, w))
    q = np.zeros((h, w))
    g = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            pix = np.reshape(mask[i, j, :], (-1, 1))  # take a pixel of all masks
            active_pixel = [i for i in range(len(pix)) if pix[i] == 1]  # check if that pixel is out of shadow
            if len(active_pixel) > 2:  # check if there are at least 3 values for that pixel
                irrad = np.reshape(I[i, j, active_pixel], (len(active_pixel), 1))  # take that pixel from active images
                corr_light = L[active_pixel, :]  # take the corresponding lighting coordinate
                n = np.matmul(np.linalg.pinv(corr_light), irrad)  # calculate normal vector
                albedo[i, j] = n_length = np.linalg.norm(n)
                p[i, j] = -n[0] / n_length
                q[i, j] = -n[1] / n_length
                f[i, j] = 2 * p[i, j] / (np.sqrt(p[i, j]**2 + q[i, j]**2 + 1) + 1)
                g[i, j] = 2 * q[i, j] / (np.sqrt(p[i, j]**2 + q[i, j]**2 + 1) + 1)

    return p, q, albedo, f, g


p, q, albedo, f, g = ps(sm.I, sm.shadow_mask, lights)




