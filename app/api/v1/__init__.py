from flask import Blueprint
from app.api.v1 import task, case, image

__author__ = 'kai.cao'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    task.api.register(bp_v1)
    case.api.register(bp_v1)
    image.api.register(bp_v1)

    return bp_v1
