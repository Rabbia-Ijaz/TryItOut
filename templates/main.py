from flask import Flask, render_template, request, url_for
import texturemod
import tailormod
import garmenttransfer
import cv2
from PIL import Image
app = Flask(__name__)
UPLOAD_FOLDER = 'static/inoutImgs'

@app.route('/')
def splash_html():
    return render_template('Splash.html')

@app.route('/Home.html')
def home_html():
    return render_template('Home.html')

@app.route('/texture.html')
def texture_html():
    return render_template('texture.html')

@app.route('/texture.html', methods = ['POST', 'GET'])
def upload_image_texture():
    if request.method == "POST":
        print("in the post now")
        image_file = request.files["ImageFile"]
        texture_file = request.files["TextureFile"]
        if (image_file):
            image_file.save("static/tempFolder/"+image_file.name+".jpg")
        if (texture_file):
            texture_file.save("static/tempFolder/"+texture_file.name+".jpg")

    result = texturemod.mainTextureFunc("static/tempFolder/ImageFile.jpg", "static/tempFolder/TextureFile.jpg")
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    print("A",result.shape)
    result = cv2.resize(result, (result.shape[0]*3,result.shape[1]*3))
    print("B", result.shape)
    img = Image.fromarray(result)
    img.save("static/tempFolder/result.jpg")
    return render_template('texture.html')

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/result.html')
def texture_result_html():    
    #imgPath = "static/tempFolder/result.png"
    return render_template("result.html",image= "static/tempFolder/result.jpg", module_flag = 'texture')

@app.route('/tailor.html')
def tailor_html():
    return render_template('tailor.html')

@app.route('/tailor.html', methods = ['POST', 'GET'])
def upload_image_tailor():
    if request.method == "POST":
        source_file = request.files["SourceFileTailor"]
        target_file = request.files["TargetFileTailor"]
        if (source_file):
            source_file.save("static/tempFolder/"+source_file.name+".jpg")
        if (target_file):
            target_file.save("static/tempFolder/"+target_file.name+".jpg")
    
    result = tailormod.main_tailor_function("static/tempFolder/SourceFileTailor.jpg", "static/tempFolder/TargetFileTailor.jpg")
    #result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(result)
    img.save("static/tempFolder/result.jpg")
    return render_template('tailor.html')

@app.route('/result.html')
def tailor_result_html():    
    #imgPath = "static/tempFolder/result.png"
    return render_template("result.html",image= "static/tempFolder/result.jpg", module_flag = 'tailor')

@app.route('/gtransfer.html')
def gtransfer_html():
    return render_template('gtransfer.html')

@app.route('/gtransfer.html', methods = ['POST', 'GET'])
def upload_image_gtransfer():
    print("aaa")
    if request.method == "POST":
        print("abc")
        source_file = request.files["SourceFileGtransfer"]
        print("def")
        target_file = request.files["TargetFileGtransfer"]
        print("ghi")
        if (source_file):
            source_file.save("static/tempFolder/"+source_file.filename)
        if (target_file):
            target_file.save("static/tempFolder/"+target_file.filename)
    
    result = garmenttransfer.GarmentTransfer(source_file.filename, target_file.filename)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(result)
    img.save("static/tempFolder/result.jpg")
    return render_template('gtransfer.html')
@app.route('/result.html')
def gtransfer_result_html():    
    #imgPath = "static/tempFolder/result.png"
    return render_template("result.html",image= "static/tempFolder/result.jpg", module_flag = 'gtransfer')


if __name__ == "__main__":
    app.run(debug=True)


