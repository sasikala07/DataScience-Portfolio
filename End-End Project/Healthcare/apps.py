import flask
from flask import request
apps=flask.Flask(__name__)
apps.config['DEBUG']=True

from flask_cors import CORS
CORS(apps)


@apps.route('/')
def home():
    return '<h1>API is working.....</h1>'


@apps.route('/Predict',methods=['GET'])

def Predict():
    import joblib
    rf_model=joblib.load('heart_stroke_prediction.ml')
    stroke_pred=rf_model.predict(
        
                              [[request.args['gender'],
                                request.args['age'],
                                request.args['hypertension'],
                                request.args['heart_disease'],
                                request.args['ever_married'],
                                request.args['work_type'],
                                request.args['avg_glucose_level'],
                                request.args['bmi'],
                                request.args['smoking_status']]])
        
                           
    return str(stroke_pred)





if __name__ == "__main__":
    
    apps.run(debug=True)
    
    
    
    
#http://127.0.0.1:5000/predict?gender=1&age=80&hypertension=1&heart_disease=1&ever_married=1&work_type=0&avg_glucose_level=85&bmi=35&smoking_status=1