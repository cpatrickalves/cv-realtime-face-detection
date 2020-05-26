# Real-time face detection
In this project, I use OpenCV and Viola-Jones Algorithm to build a simple face detection system that works in real-time.


## Getting Started

To detect the face the software uses the Haar-like features with the help of the *haarcascade_eye.xml* and *haarcascade_frontalface_default.xml* files.


### Prerequisites

To run this code, download Python 3 from [Python.org](https://www.python.org/). 

After installing Python, add the required package using pip installer:

```
pip install -r requirements.txt
```

### Usage

To run the detection on real-time using the webcam, run:
```
python face_recognition.py
```

To perform the face detection on an image, just add the file name as an argument:
```
python face_recognition.py -f image.jpg
```
The script will create an output with a similar name. It with add the *_output* in the file name (ex: image_output.jpg)

Add the `-s` flag to perform smile detection.

#### Example

<img src="https://user-images.githubusercontent.com/22003608/82897863-b27bef00-9f2e-11ea-983e-cec5fff8bc15.jpg" width=500>


### Web application

You can also run this script as an [Streamlit](https://www.streamlit.io/) application:
```
streamlit run app.py
```
It will automatically open the browser and show the app.

You can also test a demo on Heroku Plataform: [Face Detection Demo](https://face-detection-cpatrickalves.herokuapp.com/)

## Built With

* [OpenCV](https://opencv.org/) - Open Computer Vision Library.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
