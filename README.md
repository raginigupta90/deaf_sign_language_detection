# deaf_sign_language_detection

Overview
This project aims to detect and recognize American Sign Language (ASL) alphabet gestures (A to Z) using Python and OpenCV. The system captures hand gestures through a webcam and translates them into corresponding alphabet letters.

Features
Real-time Detection: Uses a webcam to capture and recognize ASL alphabet gestures in real-time.
OpenCV Integration: Utilizes OpenCV for image processing and gesture recognition.
Machine Learning: Implements machine learning algorithms to classify gestures accurately.
Installation

Clone the repository:
git clone https://github.com/your-username/deaf-sign-language-detection.git
cd deaf-sign-language-detection

Install the required dependencies:
pip install -r requirements.txt

Usage
Run the main script to start the application:


main.py
The application will activate your webcam and begin detecting ASL alphabet gestures.

Follow the on-screen instructions to perform gestures and see the detected output.

Project Structure

deaf-sign-language-detection/

├── README.md


├── requirements.txt


├── main.py


├── gesture_recognition.py

├── utils.py

├── models/

│   └── asl_model.h5

├── data/

│   ├── train/

│   └── test/

└── images/

    └── examples/
    
main.py: The main script to run the application.

gesture_recognition.py: Contains the gesture recognition logic using OpenCV.

utils.py: Utility functions for preprocessing and data handling.

models/: Directory for storing trained machine learning models.

data/: Directory for training and testing datasets.

images/: Contains example images used in the project.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any feature additions or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

