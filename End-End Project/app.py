import flask
from flask import request
app=flask.Flask(__name__)
app.config["DEBUG"]=True

from flask_cors import CORS
CORS(app)

@app.route('/')
def home():
    return '<h1>API Is working.. </h1>'

@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    model=joblib.load('marriage_age_predict_model.ml')
    age_predict=model.predict(
                       [[request.args['gender'],
                         request.args['religion'],
                         request.args['caste'],
                         request.args['mother_tongue'],
                         request.args['country'],
                         request.args['height_cms']]])
    return str(age_predict)



if __name__ == "__main__":
    app.run(debug=True)


#dynmaically link
#http://127.0.0.1:5000/predict?gender=0&caste=2&religion=2&mother_tongue=5&country=5&height_cms=176 