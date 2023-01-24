from pydantic import BaseModel


class Joint2D(BaseModel):
    x: float
    y: float


class GeneratedJoints(BaseModel):
    t1: Joint2D
    t2: Joint2D
    t3: Joint2D
    t4: Joint2D
    t5: Joint2D
    t6: Joint2D
    t7: Joint2D
    t8: Joint2D
    t9: Joint2D
    t10: Joint2D
    t11: Joint2D
    t12: Joint2D
    l1: Joint2D
    l2: Joint2D
    l3: Joint2D
    l4: Joint2D
    l5: Joint2D
    l6: Joint2D
