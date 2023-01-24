from fastapi import APIRouter, Depends

from app.api.dependencies import get_joint_model_repository
from app.api.payload import JointGenerationRequest
from app.repositories.joint_model_repository import JointModelRepository
from app.services.joint_generation_service import JointGenerationService

router = APIRouter()


@router.post("/joint")
def generate_joints(payload: JointGenerationRequest,
                    joint_model_repository: JointModelRepository = Depends(get_joint_model_repository)):
    joint_generation_service = JointGenerationService(joint_model_repository)
    generated_joints = joint_generation_service.generate(payload.depth_image_url)
    return generated_joints
