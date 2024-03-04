# app.py

from flask import Flask, render_template, request, send_file
from weasyprint import HTML

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    content = file.read()
    pdf_file_path = 'generated_file.pdf'
    HTML(string=content).write_pdf(pdf_file_path)

    return send_file(pdf_file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
