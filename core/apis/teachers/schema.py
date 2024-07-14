from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from core.models.teachers import Teacher
from marshmallow import EXCLUDE, fields

class TeachersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unkonwn = EXCLUDE

    id = fields.Integer(required = True, allow_none = False)
    user_id = fields.Integer(required = True, allow_non = False)
    created_at = fields.DateTime(dump_only = True)
    update_at = fields.DateTime(dump_only = True)