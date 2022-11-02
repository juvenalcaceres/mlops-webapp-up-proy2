from flask import Flask, render_template, request
import os
import yaml 
import sys
import requests
import json 

static = os.path.join('web_apps', 'static')
template = os.path.join('web_apps', 'templates')

app = Flask(__name__,static_folder=static, template_folder=template)

params_path = "params.yaml"

#########################################################################

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def GetValues():

    pregnancies = request.form.get('pregnancies')
    plasmaglucose = request.form.get('plasmaglucose')
    diastolicbloodpressure = request.form.get('diastolicbloodpressure')
    tricepsthickness = request.form.get('tricepsthickness')
    seruminsulin = request.form.get('seruminsulin')
    bmi = request.form.get('bmi')
    diabetespedigree = request.form.get('diabetespedigree')
    age = request.form.get('age')
    
    data_json = []
    val = []
    val.append(pregnancies)
    val.append(plasmaglucose)
    val.append(diastolicbloodpressure)
    val.append(tricepsthickness)
    val.append(seruminsulin)
    val.append(bmi)
    val.append(diabetespedigree)
    val.append(age) 
    data_json.append(val)
        
    op1 = predict_api(data_json)

    return render_template('index.html', prediction_text='The person may: {}'.format(op1))

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def validate_input(dict_request):
    for val in dict_request:
        try:
            val=int(val)
        except Exception as e:
            try:
                val=float(val)
            except Exception as e:
                return False
    return True

def predict_api(data_json):
    try:
        if validate_input(data_json[0]):
            config = read_params(params_path)
            endpoint = config["api_webapp_url_azure"]
            x_new = data_json
            # Convert the array to a serializable list in a JSON document
            try:
                input_json = json.dumps({"data": x_new})
            except Exception as e:
                return "error {}".format(str(e)) 
            # Set the content type
            try:
                headers = { 'Content-Type':'application/json' }
                predictions = requests.post(endpoint, input_json, headers = headers)
                predicted_classes = json.loads(predictions.json())
                prediction = predicted_classes[0]
            except Exception as e:
                return "error {}".format(str(e)) 
            return prediction 
        else:
            return "Values entered are not Numerical"    
    except Exception as e:
        return "error {}".format(str(e))



if __name__ =='__main__':
    app.debug = True
    app.run()
#########################################################################
