# -*- coding: utf-8 -*-
import cv2
import os
import sys
from logzero import logger

# Loading the cascades
# Cascades are a series of filters that are applied one after the other to detect the faces
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/haarcascade_smile.xml')


# Create a function that will do the detections
def detect(gray, frame, detect_smile=False):
    """create a function that takes as input the image in black and white
    (gray) and the original image (frame), and that will return the same
    image with the detector rectangles.

    Arguments:
        gray {object} -- [image in the gray scale]
        frame {object} -- [original image]

    Keyword Arguments:
        detect_smiles {bool} -- If True the function will also detect smiles (default: {False})

    Returns:
        object -- the image with the detector rectangles.
    """

    # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # For each detected face:
    for (x, y, w, h) in faces:

        # We paint a rectangle around the face.
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

        # We get the region of interest (zone with the face) in the black and white image.
        roi_gray = gray[y:y+h, x:x+w]

        # We get the region of interest in the colored image.
        roi_color = frame[y:y+h, x:x+w]

        # We apply the detectMultiScale method to locate one or several eyes in the image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)

        # For each detected eye:
        for (ex, ey, ew, eh) in eyes:
            # We paint a rectangle around the eyes, but inside the referential of the face.
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2)

        if detect_smile:
            # Detect smiles
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
            # Draw the rectangle around smile
            for (sx, sy, sw, sh) in smiles :
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0,0,255), 2)

    return frame


def read_img(path):
    """Given a path to an image file, returns a cv2 array

    str -> np.ndarray"""
    if os.path.isfile(path):
        return cv2.imread(path)
    else:
        logger.error('File not found')
        raise ValueError('Path provided is not a valid file: {}'.format(path))


def detect_from_img_file(input_file, detect_smile=False):

    img = read_img(input_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, img, detect_smile=detect_smile)

    output_file = ''.join(input_file.split('.')[:-1]) + '_output.' + input_file.split('.')[-1]
    logger.info(f'The output was saved at: {output_file}')
    cv2.imwrite(output_file, canvas)

    return output_file


def detect_from_video(detect_smile=False):
    # Turn the webcam on.
    video_capture = cv2.VideoCapture(0)

    while True:

        # Get the last frame.
        _, frame = video_capture.read()

        # colour transformations
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # We get the output of our detect function.
        canvas = detect(gray, frame, detect_smile=detect_smile)

        # We display the outputs.
        cv2.imshow('Video', canvas)

        # If we type 'q' on the keyboard:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # stop the loop.
            break

    # Turn the webcam off.
    video_capture.release()

    # Destroy all the windows inside which the images were displayed.
    cv2.destroyAllWindows()


if __name__ == '__main__':

    # Check if the -s argument was set
    smile = any('-s' in s for s in sys.argv)
    input_file = any('-f' in s for s in sys.argv)

	# Check input file
    if input_file:
        try:
            # Get the file name
            input_file = sys.argv[sys.argv.index('-f') + 1]
        except:
            input_file = None

    if input_file:
        logger.info(f"Performing detection from image: {input_file}")
        detect_from_img_file(input_file, detect_smile=smile)

    else:
        logger.info("Performing detection from webcam ...")
        logger.info('Press "q" to quit')
        detect_from_video(detect_smile=smile)

