from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.models import LoanApplication

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (Frontend)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.post("/api/submit")
async def submit_application(application: LoanApplication):
    # In a real app, we would save this to a DB.
    # For now, we validate and echo it back.
    return {
        "message": "Application submitted successfully",
        "data": application
    }

@app.get("/")
async def read_index():
    from fastapi.responses import FileResponse
    return FileResponse('frontend/index.html')
