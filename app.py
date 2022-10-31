from flask import Flask, render_template, request
import os
import yaml 
import sys
import requests
import json 

port = int(os.environ.get("PORT", 5000))

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
    #output = [x for x in request.form.values()]
    pregnancies = request.form.get('pregnancies')
    plasmaglucose = request.form.get('plasmaglucose')
    diastolicbloodpressure = request.form.get('diastolicbloodpressure')
    tricepsthickness = request.form.get('tricepsthickness')
    seruminsulin = request.form.get('seruminsulin')
    bmi = request.form.get('bmi')
    diabetespedigree = request.form.get('diabetespedigree')
    age = request.form.get('age')
    
    #*************************************************************
    data_json = {
        "pregnancies":pregnancies,
        "plasmaglucose":plasmaglucose,
        "diastolicbloodpressure":diastolicbloodpressure,
        "tricepsthickness":tricepsthickness,
        "seruminsulin":seruminsulin,
        "bmi":bmi,
        "diabetespedigree":diabetespedigree,
        "age":age
    }
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
    
    #*************************************************************
    return render_template('index.html', prediction_text='The person may: {}'.format(op1))

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

class  NotANumber(Exception):
    def __init__(self, message="Los valores no son numericos"):
        self.message = message
        super().__init__(self.message)

def validate_input(dict_request):
    for _, val in dict_request.items():
        try:
            val=int(val)
        except Exception as e:    
            #try:
            #    print(val)
            #    val=float(val)
            #except Exception as e:
            #    raise NotANumber
            return True
    return True

def predict_api(data_json):

    try:
        if validate_input(data_json):

            config = read_params(params_path)
            #api_url = config["api_webapp_url"]
            #api_url = config["api_webapp_url_azure"]
            #api_url = str(api_url)
            endpoint = config["api_webapp_url_azure"]
            
            x_new = [[2,180,74,24,21,23.9091702,1.488172308,22],
                   [0,148,58,11,179,39.19207553,0.160829008,45]]

            # Convert the array to a serializable list in a JSON document
            input_json = json.dumps({"data": x_new})

            # Set the content type
            try:
                headers = { 'Content-Type':'application/json' }
                predictions = requests.post(endpoint, input_json, headers = headers)
                predicted_classes = json.loads(predictions.json())
            except Exception as e:
                return "ESTO ES ERROR 2 {}".format(e) 
            
            #r = requests.post(api_url, json = data_json)
            try:
                #prediction = json.loads(r.text)
                #prediction= prediction["predict"]
                prediction = predicted_classes[0]
            except Exception as e:
                print('This is error output', file=sys.stderr)
                print('This is standard output', file=sys.stdout)
                print(e)
                return "ESTO ES ERROR {}".format(e)
            print("LLAMADA DESDE EL API")
            print('PREDICTION:{}'.format(prediction), file=sys.stderr)
            return prediction 
            

    except NotANumber as e:
        prediction =  str(e)
        return prediction 



if __name__ =='__main__':
    app.debug = True
    app.run()
    #app.run(host ='0.0.0.0', port = port ,debug = True)
#########################################################################
