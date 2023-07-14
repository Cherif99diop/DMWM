from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

# Charger les données et les fusionner
clics = pd.read_csv("clics.csv")
impressions = pd.read_csv("impressions.csv")
achats = pd.read_csv("achats.csv")

merged_data = pd.merge(clics, impressions, on="cookie_id", how="right")
merged_data = pd.merge(merged_data, achats, on="cookie_id",how="left")

merged_data=merged_data.fillna("-")


@app.get("/CHEIKH_DMWM/data")
async def get_data():
    return merged_data.to_dict(orient="records")



