from flask import Blueprint
from core.apis.decorators import authenticate_principal,accept_payload
from core.models.assignments import Assignment
from .schema import AssignmentSchema, AssignmentGradeSchema
from core.apis.responses import APIResponse
from core import db

principal_assignments_resources=Blueprint("principal_assignments_resources",__name__)

@principal_assignments_resources.route('/assignments', methods=['get'])
@authenticate_principal
def get_assignments(p):
    student_assignments=Assignment.get_submitted_or_graded_assignments()
    student_assignments_dump=AssignmentSchema().dump(student_assignments, many=True)
    return APIResponse.respond(data=student_assignments_dump)

@principal_assignments_resources.route('/assignments/grade', methods=['post'])
@accept_payload
@authenticate_principal
def grade_assignment(p, incoming_data):
    assignment = AssignmentGradeSchema().load(incoming_data)
    graded_assignment = Assignment.mark_grade(
        _id = assignment.id,
        grade = assignment.grade,
        auth_principal = p
    )
    db.session.commit()
    dump_graded_assignment = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data = dump_graded_assignment)
