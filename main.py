from fastapi import FastAPI

from app.api.v1 import router as v1_router
from app.repositories.joint_model_repository import KerasJointModelRepository

app = FastAPI()
app.include_router(v1_router, prefix="/v1")
app.state.joint_model_repository = KerasJointModelRepository()
