from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for request data
class SpeedInput(BaseModel):
    distance: float
    time: float

# Pydantic model for response data
class SpeedResponse(BaseModel):
    avg_speed: float

# Endpoint to compute the average speed
@app.POST("/compute_avg_speed/", response_model=SpeedResponse)
async def calculate_speed(speed_input: SpeedInput):
    avg_speed = speed_input.distance / speed_input.time
    return {"avg_speed": avg_speed}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

