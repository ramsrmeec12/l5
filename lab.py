import cv2
image = cv2.imread("sample.jpg")
if image is None:
    print("Error in Acquiring image")
    exit()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
edges = cv2.Canny(blur,300,500)
roi = image[100:300, 150:350]
cv2.imshow("edges",edges)
cv2.imshow("roi",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
