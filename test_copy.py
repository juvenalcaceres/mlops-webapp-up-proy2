from app import predict_api 

class  NotANumber(Exception):
    def __init__(self, message="Values entered are not Numerical"):
        self.message = message
        super().__init__(self.message)
#0,148,58,11,179,39.19207553,0.160829008,45
input_data = {
    "incorrect_values": 
    { 
        "pregnancies":0,
        "plasmaglucose":'0xxx',
        "diastolicbloodpressure":58,
        "tricepsthickness":11,
        "seruminsulin":179,
        "bmi":39.19207553,
        "diabetespedigree":0.160829008,
        "age":45,
    },

    "correct_values": 
    { 
        "pregnancies":0,
        "plasmaglucose":148,
        "diastolicbloodpressure":58,
        "tricepsthickness":11,
        "seruminsulin":179,
        "bmi":39.19207553,
        "diabetespedigree":0.160829008,
        "age":45, 
    }
}

def test_form_response_correct_values(data=input_data["correct_values"]):
    res=predict_api(data)
    print(res)
    assert res in ["deposit","not deposit"]


def test_form_response_incorrect_values(data=input_data["incorrect_values"]):
    res=predict_api(data)
    print(res)
    assert res == "Values entered are not Numerical"
