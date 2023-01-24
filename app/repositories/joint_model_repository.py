from abc import ABC, abstractmethod

import numpy as np

from app.schema.joint import GeneratedJoints, Joint2D


class JointModelRepository(ABC):
    @abstractmethod
    def generate_joints(self, image: np.ndarray) -> GeneratedJoints:
        raise NotImplementedError


class KerasJointModelRepository(JointModelRepository):
    def __init__(self):
        # Load keras model
        print("Keras Model Loaded!")
        pass

    def generate_joints(self, image: np.ndarray) -> GeneratedJoints:
        # TODO call keras model and return result
        return GeneratedJoints(
            t1=Joint2D(x=0.0, y=0.0),
            t2=Joint2D(x=0.0, y=0.0),
            t3=Joint2D(x=0.0, y=0.0),
            t4=Joint2D(x=0.0, y=0.0),
            t5=Joint2D(x=0.0, y=0.0),
            t6=Joint2D(x=0.0, y=0.0),
            t7=Joint2D(x=0.0, y=0.0),
            t8=Joint2D(x=0.0, y=0.0),
            t9=Joint2D(x=0.0, y=0.0),
            t10=Joint2D(x=0.0, y=0.0),
            t11=Joint2D(x=0.0, y=0.0),
            t12=Joint2D(x=0.0, y=0.0),
            l1=Joint2D(x=0.0, y=0.0),
            l2=Joint2D(x=0.0, y=0.0),
            l3=Joint2D(x=0.0, y=0.0),
            l4=Joint2D(x=0.0, y=0.0),
            l5=Joint2D(x=0.0, y=0.0),
        )
