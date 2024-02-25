from flask import Blueprint, current_app, render_template
import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from memegen import generate_meme


bp = Blueprint("pages", __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)

            # generate meme
            meme_filename = generate_meme(upload_path)
            meme_path = os.path.join(current_app.config['MEME_FOLDER'], meme_filename)
            # return redirect(url_for('pages.download_file', name=filename))
            return send_from_directory(current_app.config['MEME_FOLDER'], meme_filename)
        # return 'File not uploaded', 400
    
    return render_template("pages/upload.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], name)

# bp.add_url_rule(
#     "/uploads/<name>", endpoint="download_file", build_only=True
# )

