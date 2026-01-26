from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Safe Roads API"
    debug: bool = False
    model_path: str = "model.pkl"
    cors_origins: list = ["http://127.0.0.1:8000", "http://localhost:8000", "http://127.0.0.1:5500", "http://localhost:5500"]

    class Config:
        env_file = ".env"


settings = Settings()

#########################################################################
# code to terminal to run the app:

   # cd C:\Users\Admin\Desktop\5_year\semester_A\final_project
   # .\venv\Scripts\activate 
   # python -m uvicorn backend.app:app --reload
   
#########################################################################