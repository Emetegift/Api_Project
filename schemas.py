from marshmallow import Schema, fields, validate


# class GPARequestSchema(Schema):
#     id = fields.Int(dump_only=True)
#     grade = fields.List(fields.Str(), required=True)
#     # credit = fields.Int(required=True)
#     grade = fields. Str(required=True)
#     student_id = fields.Integer(required=True)
#     course_code = fields.Str(required=True)
#     registered_courses = fields.List(fields.Dict(required=True))

class PlainAdminSchema(Schema):
    id = fields.Int(dump_only=True)
    password = fields.Str(required=True, load_only=True)
    # grade = fields.List(fields.Nested(GPARequestSchema()), dump_only=True)


class PlainStudentSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email_address = fields.Str(required=True)
    # password = fields.Text(required=True, load_only=True)
    gpa = fields.Float(required=True)
    # credit = fields.Int(required=True)
    
class UpdateStudentSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    gpa = fields.Float()
    # credit= fields.Int()
    student_id = fields.Int()

class UpdateCourseAdminSchema(Schema):
    course_name = fields.Str()
    course_code = fields.Str()
    teacher_name = fields.Str()
    # credit = fields.Int()
    
class PlainCourseRegistrationSchema(Schema):
    id = fields.Int(dump_only=True)
    course_name = fields.Str(required=True)
    course_code = fields.Str(required=True)
    semester = fields.Str(required=True)
    teacher = fields.Str(load_only=True)
    # first_name = fields.Str(required=True)
    course_unit = fields.Str(required=True)
    # last_name = fields.Str(required=True)
    score= fields.Float(required=True)
    grade= fields.Str(required=True)
    
    
class CourseRegistrationSchema(PlainCourseRegistrationSchema):
    id = fields.Int(dump_only=True)
    course_name = fields.Str(required=True)
    course_code = fields.Str(required=True)
    semester = fields.Str(required=True)
    teacher = fields.Str(load_only=True)
    score= fields.Float(required=True)
    course_unit = fields.Str(required=True)
    grade= fields.Str(required=True)
    # grade = fields.Str(required=True)
    # registered_students_in_each_course = fields.Int(dump_only=True)
    # course_unit = fields.Str(required=True)
    # credit = fields.Int(required=True)
    
class StudentSchema(PlainStudentSchema):
    id = fields.Int(dump_only=True)
    # password = fields.Str(required=True, load_only=True)
    
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email_address = fields.Str(required=True)
    # password = fields.Str(required=True)
    
class AdminSchema(PlainAdminSchema):
    id = fields.Int(dump_only=True)   
    name = fields.Str(required=True)
    # registered_students_in_each_course = fields.Int(required=True)
    password = fields.Int(required=True, load_only=True)
    
class PlainEnrollmentSchema(Schema):
    id = fields.Int(dump_only=True)
    course_name = fields.Str(required=True)
    course_code = fields.Int(required=True)
    course_unit = fields.Str(required=True)
    semester = fields.Str(required=True)
    # first_name = fields.Str(required=True)
    # last_name = fields.Str(required=True)
    score = fields.Float(required=True)
    student_id = fields.Int(required=True)
    grade = fields.Str(required=True)
    
class EnrollmentSchema(Schema):
    id = fields.Int(dump_only=True)
    course_code = fields.Str(required=True)
    
       
class StudentWhoRegisteredACourseSchema(Schema):
    stud_id = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    grade = fields.Str(dump_only=True)
    score = fields.Float(dump_only=True)
    
    
class ListCoursesWithStudentSchema(Schema):
    id = fields.Int(dump_only=True)
    course_title = fields.Str(required=True)
    course_code = fields.Str(required=True)
    # year = fields.Int(dump_only=True)
    course_unit = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    teacher = fields.Str(required=True)
    student_registered = fields.Nested(StudentWhoRegisteredACourseSchema(), many=True)
    
    
class GetStudentGradeSchema(Schema):
    grade = fields.Str(dump_only=True)
    score = fields.Float(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    
class RegisterACourseSchema(Schema):
    course_code = fields.Str(required=True)
    
class ScoreSchema(Schema):
    score = fields.Float(required=True)