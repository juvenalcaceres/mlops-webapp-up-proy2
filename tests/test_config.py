from app import predict_api 

class  NotANumber(Exception):
    def __init__(self, message="Values entered are not Numerical"):
        self.message = message
        super().__init__(self.message)

input_data = {
    "incorrect_values": 
    {
        "duration":1,
        "month":1,
        "date":1,
        "age":13,
        "balance":'0xxx',
        "pout":1,
        "job":1,
        "camp":1,
        "contact":1,
        "house":1,
    },

    "correct_values": 
    {
        "duration":1,
        "month":1,
        "date":1,
        "age":13,
        "balance":0,
        "pout":1,
        "job":1,
        "camp":1,
        "contact":1,
        "house":1, 
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
