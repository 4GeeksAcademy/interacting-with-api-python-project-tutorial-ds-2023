from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


# Pydantic model for request data
class SpeedInputs(BaseModel):
    """ Takes miles and time inputs to calculate speed"""
    miles: float
    time: float

class SpeedResponse(BaseModel):
    """Responds to the user with calculated speed"""
    speed: float

@app.post("/average_speed/", response_model = SpeedResponse)
def average_speed(speed_inputs: SpeedInputs):
    speed = speed_inputs.miles / speed_inputs.time
    return {"speed": speed}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host= "0.0.0.0", port = 8000)
