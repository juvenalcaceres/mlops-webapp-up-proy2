from app import predict_api 

input_data = {
    "incorrect_values":[[0,"x3",58,11,179,39.19207553,0.160829008,45]],
    "correct_values_nd": [
        [0,148,58,11,179,39.19207553,0.160829008,45] #not-diabetic
    ],
    "correct_values_d": [
        [2,180,74,24,21,23.9091702,1.488172308,22] #diabetic
    ]
}

def test_form_response_correct_values_not_diabetic(data=input_data["correct_values_nd"]):
    res=predict_api(data) 
    print(res)
    assert res == "not-diabetic"

def test_form_response_correct_values_diabetic(data=input_data["correct_values_d"]):
    res=predict_api(data)
    print(res)
    assert res == "diabetic"

def test_form_response_incorrect_values(data=input_data["incorrect_values"]):
    res=predict_api(data)
    print(res)
    assert res == "Values entered are not Numerical"
