from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from scipy.stats import norm

app = FastAPI()


# Pydantic model for request data
class PopulationIncome(BaseModel):
    """ Takes mean and standard deviation to calculate probability"""
    income_mean = 1000
    income_standarddev = 500
    probability_of = 1500

class ProbabilityResponse(BaseModel):
    """Responds to the user with calculated probability of an income over $1500"""
    probability: float

@app.post("/income_probability/", response_model = ProbabilityResponse)
def income_probability(population_income: PopulationIncome):
    z = (population_income.probability_of - population_income.income_mean) / population_income.income_standarddev
    probability = 1 - norm.cdf(z)
    return {"probability": probability}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host= "0.0.0.0", port = 8000)