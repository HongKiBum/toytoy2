from setuptools import setup, find_packages

setup(
    name="fun_tools",
    version="1.0.0",
    description="A collection of fun games and utilities",
    author="홍기범",
    author_email="hgb9720@hanyang.ac.kr",
    packages=find_packages(),
    install_requires=[
        "pygame",
        "opencv-python",
        "numpy",
        "mediapipe",
        "Pillow",
        "ultralytics",
        "pytesseract",
        "speechrecognition",
    ],
    python_requires=">=3.8",
)
