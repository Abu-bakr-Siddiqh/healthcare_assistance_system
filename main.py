from flask import *
import pickle
import numpy as np
import pandas as pd
import sklearn
import re
import random
from random import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('front_page.html')

@app.route('/diabetes_pred')
def diabetes():
    return render_template('diabetes_prediction.html')

def ValuePredictor_diabetes(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,8)
    loaded_model = pickle.load(open("diabetes_model.pkl", "rb"))
    result_diabetes = loaded_model.predict(to_predict)
    return result_diabetes[0]


@app.route('/diabetes_result', methods=['GET','POST'])
def diabetes_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==8):
            result_diabetes = ValuePredictor_diabetes(to_predict_list)

    if (int(result_diabetes) == 1):
        prediction = 'You Have A Risk Of Diabetes'
    else:
        prediction = 'You Don"t Have Any Risk Of Diabetes'

    return(render_template('diabetes_prediction.html', prediction_diabetes = prediction))


@app.route('/heart_pred')
def heart():
    return render_template('heart_prediction.html')

def ValuePredictor_heart(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,13)
    loaded_model = pickle.load(open("heart_model.pkl", "rb"))
    result_heart = loaded_model.predict(to_predict)
    return result_heart[0]


@app.route('/heart_result', methods=['GET','POST'])
def heart_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==13):
            result_heart = ValuePredictor_heart(to_predict_list)

    if (int(result_heart) == 1):
        prediction = 'You Have A Risk Of Heart Attack'
    else:
        prediction = 'You Don"t Have Any Risk Of Heart Attack'

    return(render_template('heart_prediction.html', prediction_heart = prediction))


@app.route('/lung_cancer_pred')
def lung_cancer():
    return render_template('lung_cancer_prediction.html')

def ValuePredictor_lung_cancer(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,17)
    loaded_model = pickle.load(open("lung_cancer.pkl", "rb"))
    result_lung_cancer = loaded_model.predict(to_predict)
    return result_lung_cancer[0]


@app.route('/lung_cancer_result', methods=['GET','POST'])
def lung_cancer_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==17):
            result_lung_cancer = ValuePredictor_lung_cancer(to_predict_list)

    if (int(result_lung_cancer) == 1):
        prediction = 'You Have A Risk Of Lung Cancer'
    else:
        prediction = 'You Don"t Have Any Risk Of Lung Cancer'

    return(render_template('lung_cancer_prediction.html', prediction_lung_cancer = prediction))


@app.route('/breast_cancer_pred')
def breast_cancer():
    return render_template('breast_cancer_prediction.html')

def ValuePredictor_breast_cancer(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,15)
    loaded_model = pickle.load(open("breast_cancer.pkl", "rb"))
    result_breast_cancer = loaded_model.predict(to_predict)
    return result_breast_cancer[0]


@app.route('/breast_cancer_result', methods=['GET','POST'])
def breast_cancer_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==15):
            result_breast_cancer = ValuePredictor_breast_cancer(to_predict_list)

    if (int(result_breast_cancer) == 1):
        prediction = 'You Have A Risk Of Breast Cancer'
    else:
        prediction = 'You Don"t Have Any Risk Of Breast Cancer'

    return(render_template('breast_cancer_prediction.html', prediction_breast_cancer = prediction))


@app.route('/liver_pred')
def liver():
    return render_template('liver_prediction.html')

def ValuePredictor_liver(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,10)
    loaded_model = pickle.load(open("liver_model.pkl", "rb"))
    result_liver = loaded_model.predict(to_predict)
    return result_liver[0]


@app.route('/liver_result', methods=['GET','POST'])
def liver_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==10):
            result_liver = ValuePredictor_liver(to_predict_list)

    if (int(result_liver) == 1):
        prediction = 'You Have A Risk Of Liver Problem'
    else:
        prediction = 'You Don"t Have Any Risk Of Liver Problem'

    return(render_template('liver_prediction.html', prediction_liver = prediction))


@app.route('/fever')
def fever():
    return render_template('fever.html')

@app.route('/fever_result',methods=['GET','POST'])
def fever_result():
    age = request.form.get('Age')
    if int(age) <= int(1):
        return render_template("fever_1.html")
    elif int(age) >= int(2) and int(age) <= int(17):
        return render_template("fever_2.html")
    elif int(age) >= int(18):
        return render_template("fever_3.html")
    else:
        return "Enter the valid age...!";

@app.route('/cough')
def cough():
    return render_template('cough.html')

@app.route('/cough_result',methods=['GET','POST'])
def cough_result():
    age = request.form.get('Age')
    if int(age) <= int(2):
        return render_template("cough_1.html")
    elif int(age) >= int(2) and int(age) <= int(11):
        return render_template("cough_2.html")
    elif int(age) >= int(12) and int(age) <= int(17):
        return render_template("cough_3.html")
    elif int(age) >= int(18):
        return render_template("cough_4.html")
    else:
        return "Enter the valid age...!";


@app.route('/stomach_pain')
def stomach_pain():
    return render_template('stomach_pain.html')

@app.route('/stomach_pain_result',methods=['GET','POST'])
def stomach_pain_result():
    age = request.form.get('Age')
    if int(age) <= int(2):
        return render_template("stomach_pain_1.html")
    elif int(age) > int(2) and int(age) <= int(17):
        return render_template("stomach_pain_2.html")
    elif int(age) >= int(18):
        return render_template("stomach_pain_3.html")

@app.route('/allergy')
def allergy():
    return render_template('allergy.html')

@app.route('/allergy_result',methods=['GET','POST'])
def allergy_result():
    age = request.form.get('Age')
    if int(age) <= int(2):
        return render_template('allergy_1.html')
    elif int(age) > int(2) and int(age) <= int(12):
        return render_template('allergy_2.html')
    elif int(age) > int(12):
        return render_template('allergy_3.html')


@app.route('/head_ache')
def head_ache():
    return render_template('head_ache.html')

@app.route('/head_ache_result',methods=['GET','POST'])
def head_ache_result():
    age = request.form.get('Age')
    if int(age) <= int(12):
        return render_template("head_ache_1.html")
    elif int(age) > int(12) and int(age) <= int(17):
        return render_template("head_ache_2.html")
    elif int(age) > int(17) and int(age) <= int(65):
        return render_template("head_ache_3.html")
    elif int(age) > int(65):
        return render_template("head_ache_4.html")


@app.route('/heart_treatment')
def heart_treatment():
    return render_template('heart_treatment.html')

@app.route('/heart_doctors',methods=['GET','POST'])
def heart_doctors():
    location = request.form.get('location')
    if int(location) == int(0):
        return render_template("heart_chennai_doctors.html")
    elif int(location) == int(1):
        return render_template("heart_coimbature_doctors.html")
    elif int(location) == int(2):
        return render_template("heart_trivandrum_doctors.html")
    elif int(location) == int(3):
        return render_template("heart_kochi_doctors.html")
    elif int(location) == int(4):
        return render_template("heart_vijayawada_doctors.html")
    elif int(location) == int(5):
        return render_template("heart_vizag_doctors.html")
    elif int(location) == int(6):
        return render_template("heart_bangalore_doctors.html")


@app.route('/cancer_treatment')
def cancer_treatment():
    return render_template('cancer_treatment.html')

@app.route('/cancer_doctors',methods=['GET','POST'])
def cancer_doctors():
    location = request.form.get('location')
    if int(location) == int(0):
        return render_template("cancer_chennai_doctors.html")
    elif int(location) == int(1):
        return render_template("cancer_coimbature_doctors.html")
    elif int(location) == int(2):
        return render_template("cancer_trivandrum_doctors.html")
    elif int(location) == int(3):
        return render_template("cancer_kochi_doctors.html")
    elif int(location) == int(4):
        return render_template("cancer_vijayawada_doctors.html")
    elif int(location) == int(5):
        return render_template("cancer_vizag_doctors.html")
    elif int(location) == int(6):
        return render_template("cancer_bangalore_doctors.html")


@app.route('/diabetes_treatment')
def diabetes_treatment():
    return render_template('/diabetes_treatment.html')

@app.route('/diabetes_doctors',methods=['GET','POST'])
def diabetes_doctors():
    location = request.form.get('location')
    if int(location) == int(0):
        return render_template("diabetes_chennai_doctors.html")
    elif int(location) == int(1):
        return render_template("diabetes_coimbature_doctors.html")
    elif int(location) == int(2):
        return render_template("diabetes_trivandrum_doctors.html")
    elif int(location) == int(3):
        return render_template("diabetes_kochi_doctors.html")
    elif int(location) == int(4):
        return render_template("diabetes_vijayawada_doctors.html")
    elif int(location) == int(5):
        return render_template("diabetes_vizag_doctors.html")
    elif int(location) == int(6):
        return render_template("diabetes_bangalore_doctors.html")


if __name__ == "__main__":
    app.run(debug=True)