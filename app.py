from flask import Flask,jsonify
import pikepdf

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pdfrotator/<path:file_path>/<int:angle_rotation>/<int:page_number>")
def pdf_rotator(file_path=None, angle_rotation=None,page_number=None):
    sample_pdf = pikepdf.Pdf.open(file_path)
    for i in range(1,(len(sample_pdf.pages)+1)):
        if i == page_number:
            res = sample_pdf.pages[i-1]
            res.rotate(angle_rotation, True)
    sample_pdf.save("newsample_pdf.pdf")
    result= {
        "file_path" : file_path,
        "angle_rotation" : angle_rotation,
        "page_number" : page_number
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

