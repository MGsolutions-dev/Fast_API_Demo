import numpy as np

from app.repositories.joint_model_repository import JointModelRepository
from app.schema.joint import GeneratedJoints


class JointGenerationService:
    def __init__(self, joint_model_repository: JointModelRepository):
        self.joint_model_repository = joint_model_repository

    def generate(self, image_url: str) -> GeneratedJoints:
        # TODO download image and convert to numpy array
        image = np.array([0.0])
        return self.joint_model_repository.generate_joints(image)
