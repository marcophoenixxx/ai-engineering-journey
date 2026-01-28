from fastapi import FastAPI # import library FastAPI
from .schemas import Project # import class Project dari file schemas.py

# inisialisasi app
app = FastAPI()

# decorator (papan penunjuk jalan)
@app.post("/projects") # artinya kalau ada orang kirim data (POST) ke alamat /projects, panggil fungsi di bawah ini
def create_project(project: Project): # project: Project artinya parameter inputnya harus sesuai dengan class Project, dan FastAPI akan otomatis mengecek apakah data yang dikirim sudah benar atau belum
    return {
        "status": "success",
        "data": project,
        "message": f"Project {project.project_name} created successfully"
    }