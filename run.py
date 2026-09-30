from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. Define the origins (frontends) that are allowed to talk to this API
origins = [
    "https://smart-calculators.up.railway.app",# Replace with your actual Railway frontend URL
    "http://localhost:5173",                   # Keep this for local Vite development
    "http://localhost:3000",                   # Keep this if using Create React App locally
]

# 2. Add the CORS middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Allows specific domains
    allow_credentials=True,
    allow_methods=["*"],            # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Allows all headers (including your API keys if you use them)
)

@app.get("/")
def read_root():
    return {"message": "Hello World with CORS enabled!"}