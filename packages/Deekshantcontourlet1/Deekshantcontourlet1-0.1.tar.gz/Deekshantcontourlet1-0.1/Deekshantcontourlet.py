
# please note this is done for academic research purposes and reimplementation to use this code for commercial purposes is not allowed#
import numpy as np

def contourlet_transform(img, lp_levels, directions):
    import numpy as np
    from scipy.ndimage import gaussian_filter, zoom

    def downsample(image):
        return zoom(image, 0.5)

    def upsample(image):
        return zoom(image, 2)

    def lp_decomposition(img, levels):

        low_pass = img
        decompositions = []

        for _ in range(levels):
            filtered = gaussian_filter(low_pass, sigma=1)
            band_pass = low_pass - filtered
            decompositions.append(band_pass)
            low_pass = downsample(filtered)

        decompositions.append(low_pass)
        return decompositions

    def directional_filter(img, angle):


      dx = gaussian_filter(img, sigma=1, order=(0, 1))  
      dy = gaussian_filter(img, sigma=1, order=(1, 0))  
      return dx * np.cos(angle) + dy * np.sin(angle)

    def dfb_decomposition(band_pass_img, directions):

        step = np.pi / directions
        directional_subbands = []

        for i in range(directions):
            angle = i * step
            filtered = directional_filter(band_pass_img, angle)
            directional_subbands.append(filtered)

        return directional_subbands

    lp_imgs = lp_decomposition(img, lp_levels)
    contourlet_coeffs = []

    for band_pass_imges in lp_imgs[:-1]:
        coeffs = dfb_decomposition(band_pass_imges, directions)
        contourlet_coeffs.extend(coeffs)

    contourlet_coeffs.append(lp_imgs[-1])
    return contourlet_coeffs





