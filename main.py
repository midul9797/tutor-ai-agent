import uvicorn, os
from dotenv import load_dotenv
load_dotenv()
if __name__ == "__main__":
    if os.getenv("ENVIORNMENT") == "development":
        uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
    if os.getenv("ENVIORNMENT")=="production":
        uvicorn.run("api:app",host="0.0.0.0",port=10000, reload=True)