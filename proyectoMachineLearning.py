import joblib
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, flash
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generalciudad', methods=['GET','POST'])
def generalciudad():
    prediction = ''
    ciudad=''
    tipocuenta=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encodergeneralciudad.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modelogeneralciudad.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        ciudad=data['city_name']
        tipocuenta=data['shop_type']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('generalciudad.html',
    prediction=prediction, 
    ciudad=ciudad, 
    tipocuenta=tipocuenta, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )

@app.route('/generalestado', methods=['GET','POST'])
def generalestado():
    prediction = ''
    estado=''
    tipocuenta=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encodergeneralestado.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modelogeneralestado.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        estado=data['estado']
        tipocuenta=data['shop_type']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('generalestado.html',
    prediction=prediction, 
    estado=estado, 
    tipocuenta=tipocuenta, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )

@app.route('/generalregion', methods=['GET','POST'])
def generalregion():
    prediction = ''
    region=''
    tipocuenta=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encodergeneralregion.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modelogeneralregion.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        region=data['region']
        tipocuenta=data['shop_type']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('generalregion.html',
    prediction=prediction, 
    region=region, 
    tipocuenta=tipocuenta, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )


@app.route('/claveciudad', methods=['GET','POST'])
def claveciudad():
    prediction = ''
    ciudad=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encoderclaveciudad.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modeloclaveciudad.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        ciudad=data['city_name']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('claveciudad.html',
    prediction=prediction, 
    ciudad=ciudad, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )


@app.route('/claveestado', methods=['GET','POST'])
def claveestado():
    prediction = ''
    estado=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encoderclaveestado.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modeloclaveestado.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        estado=data['estado']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('claveestado.html',
    prediction=prediction, 
    estado=estado, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )

@app.route('/claveregion', methods=['GET','POST'])
def claveregion():
    prediction = ''
    region=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encoderclaveregion.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modeloclaveregion.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        region=data['region']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('claveregion.html',
    prediction=prediction, 
    region=region, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )

@app.route('/normalciudad', methods=['GET','POST'])
def normalciudad():
    prediction = ''
    ciudad=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encodernormalciudad.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modelonormalciudad.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        ciudad=data['city_name']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('normalciudad.html',
    prediction=prediction, 
    ciudad=ciudad, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )

@app.route('/normalestado', methods=['GET','POST'])
def normalestado():
    prediction = ''
    estado=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encodernormalestado.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modelonormalestado.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        estado=data['estado']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('normalestado.html',
    prediction=prediction, 
    estado=estado, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )

@app.route('/normalregion', methods=['GET','POST'])
def normalregion():
    prediction = ''
    region=''
    categoriaventas=''
    ordenessemana=''
    semanasonline=''

    if request.method == 'POST':
        forma = dict(request.form)
        print(forma)

        encoder = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\encodernormalregion.sav')
        model = joblib.load('C:\\Users\\Ivan\\Desktop\\Maestria\\Machine Learning I\\Proyecto Final\\Proyecto Despliegue AWS\\modelos\\modelonormalregion.sav')

        data = dict(request.form)
        data['complete_order_c'] = int(data['complete_order_c'])
        data['online_weeks'] = int(data['online_weeks'])

        X = pd.DataFrame([data])
        print(X)

        X_numeric = X.select_dtypes(include='number')
        X_categorical = X.select_dtypes(include='object')
        X_categorical = encoder.transform(X_categorical)
        X = np.concatenate((X_numeric,X_categorical), axis=1)
        prediction = model.predict(X)[0]
        print(prediction)

        region=data['region']
        categoriaventas=data['shop_category']
        ordenessemana=data['complete_order_c']
        semanasonline=data['online_weeks']
        

    return render_template('normalregion.html',
    prediction=prediction, 
    region=region, 
    categoriaventas=categoriaventas,
    ordenessemana=ordenessemana,
    semanasonline=semanasonline )

if __name__== '__main__':
    app.run(debug=True)
