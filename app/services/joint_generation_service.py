from app.schema.joint import GeneratedJoints, Joint2D


class JointGenerationService:
    def generate(self, image_url: str) -> GeneratedJoints:
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
