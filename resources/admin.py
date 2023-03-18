# from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import StudentModel, AdminModel, CourseRegistrationModel, EnrollmentModel
from schemas import StudentSchema, UpdateStudentSchema, AdminSchema, EnrollmentSchema, ListCoursesWithStudentSchema, ScoreSchema,  GetStudentGradeSchema,CourseRegistrationSchema, UpdateCourseAdminSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import jwt_required

blp = Blueprint("Admin", __name__, description="Operations on Admin")

@blp.route("/student/<int:student_id>")
class Student(MethodView):
    # @jwt_required()
    @blp.response(200, StudentSchema)
    def get(self, student_id):
        student = StudentModel.query.get_or_404(student_id)
        return student
            
        
    def delete(self, student_id):
        student = StudentModel.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()

        return {"message": "Student deleted"}
    # @jwt_required()
    @blp.arguments(UpdateStudentSchema)
    @blp.response(200, StudentSchema)
    def put(self, student_data, student_id):
        student = StudentModel.query.get(student_id)
        if student:
            student.first_name = student_data["first_name"]
            student.last_name = student_data["last_name"]
            
        else:
            student = StudentModel(id=student_id, **student_data)
        
        db.session.add(student)
        db.session.commit()

        return student
    
    # @jwt_required()
    def delete(self, student_id):
        student_courses = CourseRegistrationModel.query.filter_by(student_id=student_id).all()
        for course in student_courses:
            db.session.delete(course)
            
        student = StudentModel.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()

        return {"message": "Student deleted"}

@blp.route("/students")
class StudentList(MethodView):
    # @jwt_required()
    @blp.response(200, StudentSchema(many=True))
    def get(self):
        return StudentModel.query.all()
      
    # @jwt_required()
    @blp.arguments(StudentSchema)
    @blp.response(200, StudentSchema)
    def post(self, student_data):
        student = StudentModel(**student_data)

        try:
            db.session.add(student)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Student with this email address already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while adding a student")

        return student, 201

@blp.route("/admins")
class AdminList(MethodView):
    # @jwt_required()
    @blp.response(200, AdminSchema(many=True))
    def get(self):
        return AdminModel.query.all()
    
    # @jwt_required()
    @blp.arguments(AdminSchema)
    @blp.response(200, AdminSchema)
    def post(self, admin_data):
        admin = AdminModel(**admin_data)

        try:
            db.session.add(admin)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Admin with this email address already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured while adding an admin")

        return admin, 201

    
    # @jwt_required()
    @blp.arguments(AdminSchema)
    @blp.response(200, AdminSchema)
    def post(self, admin_data):
        admin = AdminModel(**admin_data)

        try:
            db.session.add(admin)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while adding an admin")

        return admin, 201
     
    @blp.route("/courses-students")
    @blp.response(200, ListCoursesWithStudentSchema(many=True))
    @blp.doc(description='Get all courses and students registered for each course',
             summary='Get all courses and students registered for each course')
    # @jwt_required()
    def patch(self):
        all_course = CourseRegistrationModel.query.all()
        return all_course


# @blp.route("/student_course")
# class Student_Course(MethodView):
#     # @jwt_required()
#     @blp.response(200, StudentSchema(many=True)) 
#     @blp.response(200, EnrollmentSchema(many=True))
#     def patch(self):
#         student_course = StudentModel.query.all() + EnrollmentModel.query.all()
        
#         return student_course
    
@blp.route("/course/<int:course_id>")
class CourseRegistration(MethodView):
    # @jwt_required()
    @blp.response(200, CourseRegistrationSchema)
    def get(self, course_id):
        course = CourseRegistrationModel.query.get_or_404(course_id)
        return course
    
    @jwt_required()
    def delete(self, course_id):
        course = CourseRegistrationModel.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()

        return {"message": "Course deleted"}
    # @jwt_required()
    @blp.arguments(UpdateCourseAdminSchema)
    @blp.response(200, CourseRegistrationSchema)
    def put(self, course_data, course_id):
        course = CourseRegistrationModel.query.get(course_id)
        if course:
            course.name = course_data["course_name"]
            course.teacher_name = course_data["teacher_name"]
            course.registered_students = course_data["registered_students"]
        else:
            course = CourseRegistrationModel(id=course_id, **course_data)
        
        db.session.add(course)
        db.session.commit()

        return course


@blp.route("/Create course")
class CourseList(MethodView):
    # @jwt_required()
    @blp.response(200, CourseRegistrationSchema (many=True))
    def get(self):
        return CourseRegistrationModel.query.all()
    
    # @jwt_required()
    @blp.arguments(CourseRegistrationSchema)
    @blp.response(200, CourseRegistrationSchema)
    def post(self, course_data):
        courses = CourseRegistrationModel(**course_data)
            
        try:
            db.session.add(courses)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Course title already exist")
        except SQLAlchemyError:
            abort(500, message="An error occurred while adding this course ")
            
        return courses, 201
    
    
    
    
    
    
@blp.route("/get-grade/<string:stud_id>/<string:course_code>")
class GetGradeOfEachStudent(MethodView):
    @blp.response(200, GetStudentGradeSchema)
    @blp.doc(description='Get grade of a student',
             summary='Get grade of a student using stud_id (i.e matric number) and course_code')
    # @jwt_required()
    def get(self, stud_id: str, course_code: str):
        student = Student.query.filter_by(stud_id=stud_id).first()
        if not student:
            abort(404, message="Student not found/Invalid stud_id"), 404
        course = CourseRegistrationModel.query.filter_by(course_code=course_code.upper()).first()
        if not course:
            abort(404, message="Course not found/Invalid course_code"), HTTPStatus.NOT_FOUND
        course_registered = EnrollmentModel.query.filter_by(student_id=student.id, course_id=course.id).first()
        if not course_registered:
            abort(404, message="Student not registered for this course"), 404
        return course_registered


@blp.route("/upload-score/<string:stud_id>/<string:course_code>")
class UploadScore(MethodView):
    @blp.arguments(ScoreSchema)
    @blp.response(200, EnrollmentSchema)
    @blp.doc(description='Upload score for a student',
             summary='Upload score for a student using stud_id (i.e matric number) and course_code')
    # @jwt_required()
    def put(self, score_data, stud_id: str, course_code: str):
        student = Student.query.filter_by(stud_id=stud_id).first()
        if not student:
            abort(404, message="Student not found/Invalid stud_id"), 404
        course = CourseRegistrationModel.query.filter_by(course_code=course_code.upper()).first()
        if not course:
            abort(404, message="Course not found/Invalid course_code"),404
        course_registered = EnrollmentModel.query.filter_by(
            stud_id=stud_id, course_code=course_code.upper()
        ).first()
        # if course_registered and course_registered.score:
        #     abort(409, message="score already uploaded"), HTTPStatus.CONFLICT
        if not course_registered:
            abort(404, message="Student not registered for this course"), 404
        if score_data["score"] < 1 or score_data["score"] > 100:
            abort(400, message="score must be between 1 and 100"), 404
        # if not score_data["score"]:
        #     abort(400, message="score cannot be empty"), HTTPStatus.BAD_REQUEST
        course_registered.score = score_data["score"]
        course_registered.grade = get_grade(score_data["score"])
        db.session.commit()
        return course_registered


@blp.route("/calculate-gpa/<string:stud_id>")
class CalculateGPA(MethodView):
    @blp.doc(description='Calculate student GPA',
             summary='Calculate student GPA using stud_id (i.e matric number)')
    # @jwt_required()
    def patch(self, stud_id):
        student = Student.query.filter_by(stud_id=stud_id).first()
        if not student:
            abort(404, message="Student not found/Invalid stud_id"), 404

        course_registered_records = EnrollmentModel.query.filter_by(stud_id=stud_id).all()
        student_scores = [record.score for record in course_registered_records]

        course_registered_records = EnrollmentModel.query.filter_by(stud_id=stud_id).all()
        student_units = [record.course_unit for record in course_registered_records]

        if not student_scores:
            abort(404, message="Student has no score(s)"), HTTPStatus.NOT_FOUND
        gpa = calculate_gpa(student_scores, student_units)
        student.gpa = gpa
        db.session.commit()
        return {"message": f"Uploaded successfully, student GPA is : {gpa}"}, 201

# @blp.route("/courses-students")
# class GetCoursesStudents(MethodView):
#     @blp.response(200, ListCoursesWithStudentSchema(many=True))
#     @blp.doc(description='Get all courses and students registered for each course',
#              summary='Get all courses and students registered for each course')
#     # @jwt_required()
#     def get(self):
#         all_course = CourseRegistrationModel.query.all()
#         return all_course
