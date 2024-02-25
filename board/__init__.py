from flask import Flask, Request
from board import pages
import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename

# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = '/Users/aliasghar/hack24/uploads'
MEME_FOLDER = '/Users/aliasghar/hack24/memes'

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
    app.config['MEME_FOLDER'] = MEME_FOLDER 


    app.register_blueprint(pages.bp)
    return app

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS