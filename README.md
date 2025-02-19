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

# install g unicorn 
    pip install gunicorn
    gunicorn -b 0.0.0.0:8000 app:app


Run Gunicorn WSGI server to serve the Flask Application
When you “run” flask, you are actually running Werkzeug’s development WSGI server, which forward requests from a web server.
Since Werkzeug is only for development, we have to use Gunicorn, which is a production-ready WSGI server, to serve our application.

Install Gunicorn using the below command:
```bash
pip install gunicorn
```
Run Gunicorn:
```bash
gunicorn -b 0.0.0.0:8000 app:app 
```
Gunicorn is running (Ctrl + C to exit gunicorn)!

Use systemd to manage Gunicorn
Systemd is a boot manager for Linux. We are using it to restart gunicorn if the EC2 restarts or reboots for some reason.
We create a <projectname>.service file in the /etc/systemd/system folder, and specify what would happen to gunicorn when the system reboots.
We will be adding 3 parts to systemd Unit file — Unit, Service, Install

Unit — This section is for description about the project and some dependencies
Service — To specify user/group we want to run this service after. Also some information about the executables and the commands.
Install — tells systemd at which moment during boot process this service should start.
With that said, create an unit file in the /etc/systemd/system directory
	
```bash
sudo vi /etc/systemd/system/steg.service
```
Then add this into the file.
```bash
[Unit]
Description=Flask Steganography App with Gunicorn
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/Project_Devops/Python_projects/flask-steganography-app
ExecStart=/home/ubuntu/Project_Devops/Python_projects/flask-steganography-app/venv/bin/gunicorn -b 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
```
Then enable the service:
```bash
sudo systemctl daemon-reload
sudo systemctl start steg
sudo systemctl enable steg
```
Check if the app is running with 
```bash
curl localhost:8000
```
Run Nginx Webserver to accept and route request to Gunicorn
Finally, we set up Nginx as a reverse-proxy to accept the requests from the user and route it to gunicorn.

Install Nginx 
```bash
sudo apt-get nginx
```
Start the Nginx service and go to the Public IP address of your EC2 on the browser to see the default nginx landing page
```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```
Edit the default file in the sites-available folder.
```bash
sudo nano /etc/nginx/sites-available/default
```
Add the following code at the top of the file (below the default comments)
```bash
upstream flasksteg {
    server 127.0.0.1:8000;
}
```
Add a proxy_pass to flaskhelloworld atlocation /
```bash
location / {
    proxy_pass http://flasksetg;
}
```
Restart Nginx 
```bash
sudo systemctl restart nginx
```
Tada! Our application is up!


# Run the app 
     cd Projects_devops/Python_projects/flask-steganography-app/
     python app.py 

