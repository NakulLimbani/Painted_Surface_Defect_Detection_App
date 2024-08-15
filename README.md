# Painted_Surface_Defect_Detection_App

A user-friendly web application for detecting defects on painted surfaces using live webcam input and image uploads.

## 📋 Table of Contents

- [📖 Introduction](#-introduction)
- [✨ Features](#-features)
- [💻 Tech Stack](#-tech-stack)
- [🚀 Setup](#-setup)
- [🔧 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## 📖 Introduction

The Painted Surface Defect Detection App offers real-time defect detection for painted surfaces using a webcam, as well as the ability to upload images for defect detection and severity classification. The application is hosted on [PythonAnywhere](https://surfacedefectdetection.pythonanywhere.com/) and utilizes both Django and Flask to provide a comprehensive solution.

## ✨ Features

- **Live Defect Detection**: Start and stop real-time defect detection using your webcam.
- **Image Upload Detection**: Upload an image to detect defects and classify their severity.
- **Real-Time Feedback**: Instant feedback on detected defects.
- **User-Friendly Interface**: Simple and intuitive controls for both live detection and image uploads.
- **Integration**: Combines Django for the main application with Flask for live detection functionality.

## 💻 Tech Stack

- **Frontend**: 
  - ![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
  - ![CSS](https://img.shields.io/badge/CSS-239120?style=for-the-badge&logo=css3&logoColor=white)
  - ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
- **Backend**: 
  - ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
  - ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- **Tools & Libraries**:
  - ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  - ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
  - ![Computer Vision](https://img.shields.io/badge/Computer_Vision-000000?style=for-the-badge&logo=opencv&logoColor=white)
  - ![Machine Learning](https://img.shields.io/badge/Machine_Learning-F7DF1E?style=for-the-badge&logo=python&logoColor=black)
  - ![Deep Learning](https://img.shields.io/badge/Deep_Learning-FF6F00?style=for-the-badge&logo=python&logoColor=white)
- **Database**: SQLite (default for Django applications).

## 🚀 Setup

### Prerequisites

- Python 3.x
- Django
- Flask
- Virtual environment tools (virtualenv, pipenv, etc.)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/NakulLimbani/Painted_Surface_Defect_Detection_App.git
    cd Painted_Surface_Defect_Detection_App
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

6. **Start the Flask server:**
    ```sh
    python app_flask.py  # Ensure this script starts the Flask server
    ```

## 🔧 Usage

- **Live Detection**:
  - Navigate to the [homepage](https://surfacedefectdetection.pythonanywhere.com/) to access live detection.
  - Click on the **Start Detection** button to begin real-time defect detection using your webcam.
  - Click on the **Stop Detection** button to halt the live defect detection.

- **Image Upload Detection**:
  - Use the **Upload Image** section on the homepage to select and upload an image.
  - The application will detect defects in the uploaded image and classify their severity.
  - Review the results displayed on the page after the analysis is complete.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
