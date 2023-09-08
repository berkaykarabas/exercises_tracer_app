import requests
import datetime as dt
MY_ID = "da25004a"
MY_API ="35bbe83a6cf77fd54e9c44360db1e0d4"
URL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_input=input("Tell me which exercises you did: ").title()
HEADERS={
    "x-app-id": MY_ID,
    "x-app-key":MY_API,
}
parameters={
    "query":user_input,
    "gender":"male",
    "weight_kg":80.5,
    "height_cm":176.5,
    "age":28
    }
response = requests.post(url=URL_ENDPOINT, json=parameters, headers=HEADERS)
result = response.json()
print(result["exercises"][0])
today=dt.datetime.now().strftime("%d/%m/%Y")
time=dt.datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response= requests.post(url="https://api.sheety.co/9835feb959dfccc4e836656d3088037e/myWorkouts/workouts",json=sheet_inputs)
    print(sheety_response.text)