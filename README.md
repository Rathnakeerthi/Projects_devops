# Projects_devops

LSB Steganography (Least Significant Bit Steganography)
LSB (Least Significant Bit) Steganography is a technique used to hide secret data inside an image by modifying the least significant bits of pixel values. Since these bits cause very little visible change in the image, it is an effective and simple way to hide information.

Updated Folder Structure
Your project will now include:

php
Copy
Edit
flask-steganography-app/
│── app.py                # Main Flask application
│── uploads/              # Folder to store uploaded files
│── templates/            # HTML template files
│   ├── index.html        # Main UI for file upload
│── static/               # Static files (CSS, JS, images if needed)
│── steg.py               # Steganography functions (hiding/extracting text)
│── requirements.txt      # Dependencies (Flask, Pillow, Stegano)


Step 1: Install Required Libraries
Run the following command:

sh
Copy
Edit
pip install flask pillow stegano
Flask → For the web app
Pillow → Image processing
Stegano → Hiding and extracting text in images

to run the python application
python app.py

docker build -t steg-app:v1 .
docker run -p 5000:5000 steg-app:v1