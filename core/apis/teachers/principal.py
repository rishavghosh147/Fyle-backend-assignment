from flask import Blueprint
from core.apis.decorators import authenticate_principal
from core.models.teachers import Teacher
from .schema import TeachersSchema
from core.apis.responses import APIResponse

principal_teachers_resources=Blueprint("principal_teachers_resources",__name__)

@principal_teachers_resources.route('/teachers', methods=['get'])
@authenticate_principal
def get_all_teachers(p):
    """Return list of all teachers"""
    teachers=Teacher.get_teachers()
    dump_teachers=TeachersSchema().dump(teachers)
    return APIResponse.respond(data=dump_teachers)