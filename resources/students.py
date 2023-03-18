from flask.views import MethodView
from flask import jsonify, request
from flask_smorest import Blueprint, abort
from db import db
from models import StudentModel, CourseRegistrationModel,EnrollmentModel
from schemas import StudentSchema, CourseRegistrationSchema, EnrollmentSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required

blp = Blueprint("Student", __name__, description="Operations on Students")
    
@blp.route("/Register_courses/<int:course_id>")
class Register(MethodView):
    @jwt_required()
    @blp.response(200, EnrollmentSchema)
    def get(self, course_id):
        register = EnrollmentModel.query.get_or_404(course_id)
        return register
    
    
@blp.route("/Register_courses")
class RegisterList(MethodView):
    # @jwt_required()
    @blp.response(200, EnrollmentSchema(many=True))
    def get(self):
        return EnrollmentModel.query.all()
        # return EnrollmentSchema.dump(register)

    # @jwt_required()
    @blp.arguments(EnrollmentSchema)
    @blp.response(200, EnrollmentSchema)
    def post(self, course_data):
        """Register a course"""
        course_code = course_data["course_code"]
        # check if the course exist in the course table
        course_exist = CourseRegistrationModel.query.filter_by(course_code=course_code).first()
        if  not course_exist:
            abort(404, message="Course does not exist")
        reg_course = EnrollmentModel(
             course_name = course_exist.course_name,
            course_code = course_exist.course_code,
            course_unit = course_exist.course_unit,
            semester = course_exist.semester,
            # first_name = course_exist.first_name,
            # last_name = course_exist.last_name,
            score = course_exist.score,
            grade = course_exist.grade,
            # student_id = course_exist.student_id,
            
            student_id = 2,
            course_id = course_exist.id,
            admin_id = 1
         )
        
        db.session.add(reg_course)
        db.session.commit()
        return {"message":f"Course <{course_code}> has been registered successfully"}, 201 
        # return f"Course <{course_code}> has been registered successfully"
        
@blp.route('/available_courses')
class available_courses(MethodView):
    # @jwt_required()
    @blp.response(200, CourseRegistrationSchema(many=True))
    def get(self):
        courses = CourseRegistrationModel.query.all()
        course_ids = [course.id for course in courses]
        student_id = request.args.get('student_id')
        if student_id:
            student = StudentModel.query.get_or_404(student_id)
            registered_courses = [course.id for course in student.courses]
            course_ids = list(set(course_ids) - set(registered_courses))
        return CourseRegistrationSchema().dump(CourseRegistrationModel.query.filter(CourseRegistrationModel.id.in_(course_ids)), many=True)

    