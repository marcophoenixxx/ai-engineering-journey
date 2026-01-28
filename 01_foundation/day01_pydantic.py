from pydantic import BaseModel, Field
import uuid
from datetime import datetime

class ModelConfig(BaseModel):
    model_name: str = Field(default="gemini-1.5-flash", description="Model name")
    max_tokens: int = Field(default=1024, description="Max tokens")
    temperature: float = Field(
        default=0.3,
        ge=0.0,
        le=1.0,
        description="Temperature"
    )

class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    email: str
    is_active: bool = Field(default=True)

class Project(BaseModel):
    project_name: str
    owner: User
    config: ModelConfig = Field(default_factory=ModelConfig)
    created_at: datetime = Field(default_factory=datetime.now)


if __name__ == "__main__":
    raw_data = {
        "project_name": "GenAI",
        "owner": {
            "username": "mugni",
            "email": "mugni@gmail.com",
        },
    }

    try:
        project = Project(**raw_data)
        print("Data Valid")
        print(project)
    except Exception as e:
        print("Data Invalid")
        print(e)