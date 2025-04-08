import uvicorn
import sys
from core.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8005)
