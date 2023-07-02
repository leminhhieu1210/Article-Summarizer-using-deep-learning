import process
from flask import Flask, request, render_template

# Khởi tạo flask app
app = Flask(__name__)


# Khai báo các route cho API
@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')


@app.route("/predict", methods=["POST"])
def predict():
    s = request.form['textOrg']
    sumText = process.decode_summary(s).replace("_", " ") if len(s.split()) > 10 else s
    return render_template('home.html', original_text='{}'.format(s), prediction_text='Predict: {}'.format(sumText))


if __name__ == "__main__":
    print("App run!")
    app.run(debug=True)
