import cv2 as cv

def findSimilarity(orjinal_img_path, referans_img_path, method):
    src_base = cv.imread('imageList\\'+orjinal_img_path)

    hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
    hsv_test1 = cv.cvtColor(referans_img_path, cv.COLOR_BGR2HSV)

    h_bins = 50
    s_bins = 60
    histSize = [h_bins, s_bins]

    h_ranges = [0, 180]
    s_ranges = [0, 256]
    ranges = h_ranges + s_ranges

    channels = [0, 1]
    hist_base = cv.calcHist([hsv_base], channels, None,
                            histSize, ranges, accumulate=False)
    cv.normalize(hist_base, hist_base, alpha=0,
                 beta=1, norm_type=cv.NORM_MINMAX)

    hist_test1 = cv.calcHist([hsv_test1], channels,
                             None, histSize, ranges, accumulate=False)
    cv.normalize(hist_test1, hist_test1, alpha=0,
                 beta=1, norm_type=cv.NORM_MINMAX)

    base_test1 = cv.compareHist(hist_base, hist_test1, method)
    return base_test1