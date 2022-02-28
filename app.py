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
    age = request.form.get('age')
    duration = request.form.get('duration')
    month = request.form.get('month')
    date = request.form.get('date')
    balance = request.form.get('balance')
    pout = request.form.get('poutcome')
    job = request.form.get('job_type')
    camp = request.form.get('campaign')
    contact = request.form.get('contact')
    house = request.form.get('housing')

    jb = {'blue-collar': 1, 'entrepreneur': 2, 'housemaid': 3, 'services': 4, 'technician': 5, 'self-employed': 6, 'admin': 7, 'unknown': 8, 'management': 9, 'unemployed': 10, 'retired': 11, 'student': 12}
    mnth = {'may': 1, 'jan': 2, 'jul': 3, 'nov': 4, 'jun': 5, 'aug': 6, 'feb': 7, 'apr': 8, 'oct': 9, 'sep': 10, 'mar': 11, 'dec': 12}
    pou = {'unknown': 1, 'failure': 2, 'other': 3, 'success': 4}
    con = {'unknown': 1, 'telephone': 2, 'cellular': 3}
    hl = {'yes':1,'no':0}

    job = jb.get(job)
    month = mnth.get(month)
    pout = pou.get(pout)
    contact = con.get(contact)
    house = hl.get(house)
    
   
    #*************************************************************
    data_json = {"age":age,"duration":duration,"month":month,"date":date,"balance":balance,
                 "pout":pout,"job":job,"camp":camp,"contact":contact,"house":house}

    op1 = predict_api(data_json)
    
    #*************************************************************
    return render_template('index.html', prediction_text='The person may: {}'.format(op1))

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict_api(data_json):
    config = read_params(params_path)
    api_url = config["api_webapp_url"]
    api_url = str(api_url)
    r = requests.post(api_url, json = data_json)
    #{"duration":1,"month":1,"date":1,"age":13,"balance":0,"pout":1,"job":1,"camp":1,"contact":1,"house":1,"predict":"not deposit"}

    try:
        prediction = json.loads(r.text)
        prediction= prediction["predict"]
    except Exception as e:
        print(e)
    print("LLAMADA DESDE EL API")
    print('PREDICTION:{}'.format(prediction), file=sys.stderr)
    return prediction 


if __name__ =='__main__':
    app.run(host ='0.0.0.0', port = port ,debug = True)
#########################################################################
