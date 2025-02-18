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


pip install flask pillow stegano
Flask → For the web app
Pillow → Image processing
Stegano → Hiding and extracting text in images

to run the python application
python app.py

___________________________________________________________________________________


# update the apt repo on your machine
  sudo apt update
# Installation of  python3 and pip
  sudo apt install python3
  sudo apt install python3-pip
# check the packages installed properly or not
   python3 --version
   pip --version
# installation of  flask 
    cd ~
    mkdir myproject
    cd myproject
    sudo  apt install python3.12-venv
    . .venv/bin/activate
    pip install Flask
    cd ~
# installation of  stegano and libgl1

    pip install stegano
    sudo apt install libgl1
# clone the repository
     cd ~
     git clone https://github.com/Rathnakeerthi/Projects_devops.git

# Run the app 
     cd Projects_devops/Python_projects/flask-steganography-app/
     python app.py 

