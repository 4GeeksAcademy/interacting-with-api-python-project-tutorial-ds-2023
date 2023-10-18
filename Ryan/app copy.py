from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

app = FastAPI()
#Write an API that computes the probability of an income be greater than $1500. Assume that the population follows a Normal Distribution: N(
=
1000
μ=1000,
=
500
σ=500 ).


#Store speed data in memory using a dictionary
average_speed = {}

# Pydantic model for request data
class SpeedInput(BaseModel):
    distance: float
    time: float

# Pydantic model for response data
class SpeedResponse(BaseModel):
    avg_speed: float

# Endpoint to compute the correlation between two vectors
@app.POST("/compute_avg_speed/", response_model= SpeedResponse)
async def calculate_speed(speed_input: SpeedInput):
    avg_speed = speed_input.distance / speed_input.time
    return {"avgerage speed": avg_speed}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)