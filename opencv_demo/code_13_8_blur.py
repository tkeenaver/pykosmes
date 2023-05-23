#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.9 OpenCV로 이미지 필터링하기, 352쪽
#
import numpy as np
import cv2

org = cv2.imread('data/mandrill.png', 1)

blurred33 = cv2.blur(org, (3, 3))
blurred99 = cv2.blur(org, (9, 9))

cv2.imshow('original', org)
cv2.imshow('blurred 3x3', blurred33)
cv2.imshow('blurred 9x9', blurred99)


# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()