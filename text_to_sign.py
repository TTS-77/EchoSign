import cv2
import os
import numpy as np

SIGN_FOLDER = "signs"

def load_image(filename):
    """
    Try loading .jpg or .jpeg
    """
    jpg_path = os.path.join(SIGN_FOLDER, filename + ".jpg")
    jpeg_path = os.path.join(SIGN_FOLDER, filename + ".jpeg")

    if os.path.exists(jpg_path):
        return cv2.imread(jpg_path)
    elif os.path.exists(jpeg_path):
        return cv2.imread(jpeg_path)
    else:
        return None


# Get input
user_text = input("Enter text: ").lower()
words = user_text.split()

window_name = "Sign Language Display"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

for word in words:

    # Try full word first
    img = load_image(word)

    if img is not None:
        img = cv2.resize(img, (600, 600))
        cv2.imshow(window_name, img)
        cv2.waitKey(1200)

    else:
        # Word not found → break into letters
        for letter in word:
            if letter.isalpha():
                letter_img = load_image(letter)

                if letter_img is not None:
                    letter_img = cv2.resize(letter_img, (600, 600))
                    cv2.imshow(window_name, letter_img)
                    cv2.waitKey(800)
                else:
                    blank = np.zeros((600, 600, 3), dtype=np.uint8)
                    cv2.putText(blank,
                                f"{letter.upper()} NOT FOUND",
                                (150, 300),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (0, 0, 255),
                                3)
                    cv2.imshow(window_name, blank)
                    cv2.waitKey(800)

cv2.destroyAllWindows()