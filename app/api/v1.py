from fastapi import APIRouter

from app.api.payload import JointGenerationRequest
from app.services.joint_generation_service import JointGenerationService

router = APIRouter()


@router.post("/joint")
def generate_joints(payload: JointGenerationRequest):
    joint_generation_service = JointGenerationService()
    generated_joints = joint_generation_service.generate(payload.depth_image_url)
    return generated_joints
