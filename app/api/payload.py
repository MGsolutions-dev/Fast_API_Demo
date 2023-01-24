from pydantic import BaseModel


class JointGenerationRequest(BaseModel):
    depth_image_url: str
