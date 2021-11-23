from app import app
from app import _Controller

from flask import (
    render_template,
    request,
    redirect,
    make_response,
    jsonify,
    send_from_directory,
    abort,
)
import os
import glob
import zipfile
import shutil

GCP_FILENAME = "gcp_list.txt"
GCP_INPUT_FILENAME = "gcp.txt"

def is_zip(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is a zip file
    if ext == "zip":
        return True
    else:
        return False


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/upload_images", methods=["GET", "POST"])
def upload_images():

    if request.method == "POST":

        file = request.files["file"]

        if file.filename == "":
            print("No filename.")
            return redirect(request.url)

        if not is_zip(file.filename):
            print("File its not a zip file.")
            return redirect(request.url)

        folder = glob.iglob(app.config["IMAGES_PATH"] + "*")
        for f in folder:
            shutil.rmtree(f)

        file_like_object = file.stream._file
        zip_file = zipfile.ZipFile(file_like_object)
        zip_file.extractall(app.config["IMAGES_PATH"])

        upload_images_path()

        res = make_response(jsonify({"message": "File uploaded"}), 200)

        return res

    return render_template("index.html")


def upload_images_path():
    max = 0
    size = 0
    path_name = ""
    for file in glob.iglob(app.config["IMAGES_PATH"] + "*"):
        size = os.stat(file).st_size
        if size > max:
            path_name = file + "/"
            app.config.update(IMAGES_FOLDER_PATH=path_name)
            max = size
    return path_name

@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":

        file = request.files["file"]

        if file.filename == "":
            print("No filename")
            return redirect("/")

        file.save(os.path.join(app.config["GCP_FILE_PATH"], GCP_INPUT_FILENAME))

        res = make_response(jsonify({"message": "File uploaded"}), 200)

        return res

    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():

    if request.method == "POST":
        
        if app.config["IMAGES_FOLDER_PATH"] == "":
            upload_images_path()

        
        border = request.form.get("border")
        border = border[:-1]

        check = request.form.get("check", -1)

        app.config["CHECK"] = check
        app.config["BORDER"] = border

        return render_template("results.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/download", methods=["GET"])
def download():
    try:
        return send_from_directory(
            app.config["GCP_FILE_PATH"], GCP_FILENAME, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route("/gcp_run", methods=["GET"])
def gcp_find():
    # por a retornar true quando acabar com sucesso, false quando contrario
    control = _Controller._Controller(app.config["BORDER"],app.config["CHECK"])
    control.run()

    res = make_response(jsonify({"message": "File generated"}), 200)

    return res

@app.route("/serverImages", methods=["GET"])
def serverWithImages():
    path = ""
    max = 0
    size = 0
    for file in glob.iglob(app.config["IMAGES_PATH"] + "*"):
            size = os.stat(file).st_size
            if size > max:
                path = os.path.basename(file)
                max = size

    res = make_response(jsonify({"path": path}), 200)

    return res