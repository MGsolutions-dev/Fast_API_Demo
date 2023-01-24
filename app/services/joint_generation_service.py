import asyncio

import aiohttp
import numpy as np

from app.repositories.joint_model_repository import JointModelRepository
from app.schema.joint import GeneratedJoints


class JointGenerationService:
    def __init__(self, joint_model_repository: JointModelRepository):
        self.joint_model_repository = joint_model_repository

    async def generate(self, image_url: str) -> GeneratedJoints:
        async with aiohttp.ClientSession() as session:
            result1, result2, result3 = await asyncio.gather(
                session.post(""),
                session.post(""),
                session.post(""),
            )
            generated_joint_1 = GeneratedJoints.parse_raw(**result1.json())
            print(generated_joint_1)
            print(result2.json())
            print(result3.json())
            # TODO download image and convert to numpy array
        image = np.array([0.0])
        return self.joint_model_repository.generate_joints(image)
