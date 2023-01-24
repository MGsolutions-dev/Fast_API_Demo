from starlette.requests import Request


def get_joint_model_repository(request: Request):
    return request.app.state.joint_model_repository
