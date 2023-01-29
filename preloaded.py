import replicate
import random
import string
from utils import finalRoast, finalCompliment
from cv2 import imshow, imwrite,waitKey, destroyWindow
from cv2 import VideoCapture

type_string = input("'roast' or 'compliment'?")
specific_img = input("'dog', 'cat', or 'cpax'?")

if (type_string == 'roast'):
    finalRoast("demo/" + specific_img + ".jpeg")
elif (type_string == 'compliment'):
    finalCompliment("demo/" + specific_img + ".jpeg")
