import os
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from steg import hide_text_in_image, extract_text_from_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if user wants to hide or extract text
        action = request.form.get("action")

        if action == "hide":
            # Hide text in an image
            image = request.files["image"]
            secret_text = request.form["secret_text"]

            if image and secret_text:
                image_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(image.filename))
                output_path = os.path.join(app.config["UPLOAD_FOLDER"], "encoded_" + image.filename)
                
                image.save(image_path)
                hide_text_in_image(image_path, secret_text, output_path)

                return send_file(output_path, as_attachment=True)

        elif action == "extract":
            # Extract hidden text from an image
            image = request.files["image"]

            if image:
                image_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(image.filename))
                image.save(image_path)
                hidden_text = extract_text_from_image(image_path)

                return f"Extracted Hidden Text: {hidden_text}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
