import scipy
import numpy as np
from skimage import img_as_float
from skimage import filters
from pylab import *


def dual_gradient_energy(img):
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    hor_R = filters.sobel_h(R)
    hor_G = filters.sobel_h(G)
    hor_B = filters.sobel_h(B)

    ver_R = filters.sobel_v(R)
    ver_G = filters.sobel_v(G)
    ver_B = filters.sobel_v(B)

    sq_x = np.add(np.square(hor_R), np.add(np.square(hor_G), np.square(hor_B)))
    sq_y = np.add(np.square(ver_R), np.add(np.square(ver_G), np.square(ver_B)))

    energy = np.add(sq_x, sq_y)

    return energy


def find_seam(img, energy):
    minval = 1000
    seam = 0
    H = energy.shape[0]
    W = energy.shape[1]
    sPath = energy

    for i in range(1, H):
        for j in range(1, W - 1):
            if j == 1:
                sPath[i, j] += min(sPath[i - 1, j], sPath[i - 1, j + 1])
            elif j == W - 2:
                sPath[i, j] += min(sPath[i - 1, j - 1], sPath[i - 1, j])
            else:
                sPath[i, j] += min(sPath[i - 1, j - 1], sPath[i - 1, j], sPath[i - 1, j + 1])

    lastRow = sPath[H - 1, :]
    for each in range(1, W - 1):
        if lastRow[each] < minval:
            minval = lastRow[each]
            seam = each

    return minval, seam, sPath


def path(img, i, k, W, sPath):
    if i != 0:
        if k == 1:
            if sPath[i - 1, k + 1] < sPath[i - 1, k]:
                k += 1
        elif k == W - 2:
            if sPath[i - 1, k - 1] < sPath[i - 1, k]:
                k -= 1
        else:
            if (sPath[i - 1, k - 1] < sPath[i - 1, k]) and (sPath[i - 1, k - 1] < sPath[i - 1, k + 1]):
                k -= 1
            elif (sPath[i - 1, k + 1] < sPath[i - 1, k]) and (sPath[i - 1, k + 1] < sPath[i - 1, k - 1]):
                k += 1
    return k


def plot_seam(img, seam, sPath):
    H = img.shape[0]
    W = img.shape[1]
    k = seam
    sPath[H - 1, k] = 100
    for i in range(H - 1, -1, -1):
        img[i, k] = [255.0, 0, 0]
        k = path(img, i, k, W, sPath)
    return img


def show_seam(img, energy):
    H = img.shape[0]
    W = img.shape[1]
    maxEnergy = 0
    for i in range(0, H):
        for j in range(0, W):
            if energy[i][j] > maxEnergy:
                maxEnergy = energy[i][j]

    for i in range(0, H):
        for j in range(0, W):
            img[i][j] = math.floor(energy[i][j] / maxEnergy * 255)

    return img


def remove_seam(img, seam, sPath):
    H = img.shape[0]
    W = img.shape[1]
    new_img = np.zeros(shape=(H, W - 1, 3))
    k = seam

    for i in range(H - 1, -1, -1):
        t = img[i, :, :]
        new_img[i, :, :] = np.delete(t, k, axis=0)
        k = path(img, i, k, W, sPath)

    return new_img


def main():
    # print original image
    img = imread('ori.jpg')
    img = img_as_float(img)
    subplot(2, 2, 1)
    imshow(imread('ori.jpg'))
    title('Original')
    # figure()
    gray()
    # print seams
    for i in range(3): # No. of seams to be shown
        energy = dual_gradient_energy(img)
        min_val, seam, sPath = find_seam(img, energy)
        img = plot_seam(img, seam, sPath)
    subplot(2, 2, 2)
    imshow(img)
    title('Seam Plot')
    # print energy image
    img = imread('ori.jpg')
    img = img_as_float(img)
    energy = dual_gradient_energy(img)
    img = show_seam(img, energy)
    subplot(2, 2, 3)
    imshow(img)
    title('Energy Image')
    # print seam carved image
    img = imread('ori.jpg')
    img = img_as_float(img)
    for i in range(100): # No. of seams to be cut down
        energy = dual_gradient_energy(img)
        minval, seam, sPath = find_seam(img, energy)
        img = remove_seam(img, seam, sPath)
    subplot(2, 2, 4)
    imshow(img)
    title('New Image')

    show()


if __name__ == '__main__':
    main()
