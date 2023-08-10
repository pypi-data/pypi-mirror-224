
# please note this is done for academic research purposes and reimplementation to use this code for commercial purposes is not allowed#
import numpy as np
def shearlet1(list, angles, scales):
    def shearlet_kernel(x, y, scale, angle):

        sigma = 1.6
        xi = 3.2
        gamma = 0.1
        theta = angle * np.pi / 4
        psi = 0
        phi = 0
        omega = 0
        scale_factor = (2 ** scale) * np.sqrt(2)
        x_ = x * np.cos(theta) + y * np.sin(theta)
        y_ = -x * np.sin(theta) + y * np.cos(theta)
        gaussian = np.exp(-(x_ ** 2 + y_ ** 2) / (2 * (sigma * scale_factor) ** 2))
        sinusoid = np.sin((np.pi * xi * x_) / (scale_factor * gamma) + psi)
        modulator = np.exp(1j * (np.pi * omega * x_) / scale_factor + phi)
        return gaussian * sinusoid * modulator
    def shearlet_transform(img, scales, angles):

        rows, cols = img.shape
        # print (rows,cols)
        # Create the shearlet filters
        filters = create_shearlet_filters(rows, cols, scales, angles)
        num_filters = len(filters)
        # Initialize the output arrays
        coefficients = np.zeros((rows, cols, num_filters), dtype=np.float32)
        # Compute the shearlet transform coefficients
        for i, filter in enumerate(filters):
            # Apply the filter to the image
            filtered = np.real(np.fft.ifft2(np.fft.fft2(img) * np.fft.fft2(filter)))
            # Store the coefficient for this filter
            coefficients[:, :, i] = filtered
        return coefficients
    def create_shearlet_filters(rows, cols, scales, angles):

        filters = []
        for scale in range(scales):
            for angle in range(angles):
                filter = np.zeros((rows, cols))
                for x in range(rows):
                    for y in range(cols):
                        # Calculate the shearlet kernel value at this point
                        filter[x, y] = shearlet_kernel(x, y, scale, angle)
                # Normalize the filter to have unit L2 norm
                filter /= np.linalg.norm(filter)
                filters.append(filter)
        return filters
    if (list[0].shape == (100,100,3)):
      tt=[]  








      import matplotlib.pyplot as plt
      for i in range (len (list)):
        # print (i)
        img = list[i]


        gray_img = np.dot(img[:, :, :3], [0.2989, 0.5870, 0.1140])
        tt.append(gray_img)
  



        # print (gray_img.shape)
        coefficients = shearlet_transform(gray_img, scales, angles)
        # print (gray_img,coefficients)

        # fig, axs = plt.subplots(nrows=scales+1, ncols=angles, figsize=((scales+1)**2,angles))
        # axs[0, 0].imshow(gray_img, cmap='gray')
        # axs[0, 0].set_title('Original Image_gray')
        # axs[0, 1].imshow(img, cmap='gray')
        # axs[0, 1].set_title('Original Image')
        for scale in range(scales):

            for angle in range(angles):
                # print (scale,angle)
                idx = scale * angles + angle


                tt.append(coefficients[:, :, idx])



                print (coefficients[:, :, idx].shape)
                # axs[0].imshow(img, cmap='gray')
                # # axs[0].set_title('Original Image')
                # axs[scale+1, angle].imshow(coefficients[:, :, idx], cmap='gray')
                # axs[scale+1, angle].set_title(f'Scale {scale+1}, Angle {angle+1}')
        plt.tight_layout()

        plt.show()
      print ("Total coefficients calculated",len(tt))
      return tt
    else:
        print ("Adjust image size to 100x100x3")






