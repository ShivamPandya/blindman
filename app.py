from flask import Flask, request, send_from_directory
from flask import  render_template as render
import cipher, decipher, os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
CIPHERED_FILE_PATH = os.path.join(APP_ROOT, "files", "ciphers")
DECIPHERED_FILE_PATH = os.path.join(APP_ROOT, "files", "deciphers")

@app.route('/')
def index():
    return render("index.html")

@app.route('/cipherFile')
def cipherFile():
    return render("cipherFile.html")

@app.route('/decipherFile')
def decipherFile():
    return render("decipherFile.html")

@app.route('/cipheredFile', methods=["POST"])
def cipheredFile():
    plaintext = request.form['plainText']
    cipher.cipher(plaintext)
    return send_from_directory(directory=CIPHERED_FILE_PATH, filename="ciphered.txt", as_attachment=True)

@app.route('/decipheredFile', methods=["POST"])
def decipheredFile():
    file = request.files['inputFile']
    filename = file.filename
    txtFile = os.path.join(APP_ROOT, "files", "ciphers", filename)
    file.save(txtFile)
    deciphered = decipher.decipher(txtFile)
    return send_from_directory(directory=DECIPHERED_FILE_PATH, filename="deciphered.txt", as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)
