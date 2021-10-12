from app import app
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
import zipfile

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

        file_like_object = file.stream._file
        zip_file = zipfile.ZipFile(file_like_object)
        zip_file.extractall(app.config["IMAGES_PATH"])

        app.config["IMAGES_FOLDER_FILENAME"] = os.path.splitext(file.filename)[0]

        res = make_response(jsonify({"message": "File uploaded"}), 200)

        return res

    return render_template("index.html")


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


@app.route("/results", methods=["GET", "POST"])
def results():

    if request.method == "POST":

        border = request.form.get("border")
        border = border[:-1]

        check = request.form.get("check", -1)

        print("border", border)
        print("check", check)

        gcp_finder(border, check)

        try:
            return send_from_directory(app.config["GCP_FILE_PATH"], GCP_FILENAME, as_attachment=True)
        except FileNotFoundError:
            abort(404)

    return render_template("results.html")


@app.route("/about")
def about():
    return render_template("about.html")


def gcp_finder(border, check):

    lista_de_GCP_fixos = {
        0: (41.399764282, -6.979935297, 745),
        1: (41.399996133, -6.979810771, 756),
        13: (89.393838443, -6.456447899, 745),
    }

    gcp_path = app.config["GCP_FILE_PATH"] + GCP_FILENAME

    with open(gcp_path,"x") as f:
        for i in range(0,6):
            f.write("coordenadas gcp teste escrita\n")
    return 0
