import requests
import pandas as pd

schemes = {

    "HDFC_Top100":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for name,code in schemes.items():

    print(name)

    url=f"https://api.mfapi.in/mf/{code}"

    response=requests.get(url)

    data=response.json()

    df=pd.DataFrame(data["data"])

    file=f"data/raw/{name}.csv"

    df.to_csv(file,index=False)

    print("Saved",file)