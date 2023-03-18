import re

def calculate_gpa(scores, units):
    total_grade_points = 0
    total_credits = 0

    for i in range(len(scores)):
        if scores[i] >= 80:
            grade_points = 4.0
        elif scores[i] >= 65:
            grade_points = 3.0
        elif scores[i] >= 55:
            grade_points = 2.0
        elif scores[i] >= 40:
            grade_points = 1.0
        else:
            grade_points = 0.0

        total_grade_points += grade_points * units[i]
        total_credits += units[i]

    gpa = round(total_grade_points / total_credits, 2)

    return gpa


def get_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 65:
        return 'B'
    elif score >= 55:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'










# from flask.views import MethodView
# from flask import Flask, jsonify, request
# from flask_smorest import Blueprint, abort
# from db import db
# from models import StudentModel, GPAModel, EnrollmentModel
# from schemas import GPARequestSchema
# from sqlalchemy.exc import SQLAlchemyError
# from flask_jwt_extended import jwt_required

# blp = Blueprint("GPA", __name__, description="Operations on GPA")

# @blp.route("/gpa/<int:gpa_id>")
# class GPACalculator(MethodView):
#     # @jwt_required()
#     @blp.response(200, GPARequestSchema)
#     def get(self, student_id):
#         gpa = EnrollmentModel.query.filter_by(student_id).all()
#         for student in StudentModel():
#             student.credit
            
            
        
#             return  gpa
    
# @blp.route("/calculate_gpa/student_id")
# class GPAList(MethodView):
#     # @jwt_required()
#     @blp.response(200, GPARequestSchema(many=True))
#     def get(self):
#         return  
    
# #     
#     # @jwt_required()
#     @blp.arguments(GPARequestSchema)
#     @blp.response(200, GPARequestSchema)
#     def post(self, course_data):
#         courses = GPAModel(**course_data)
#         total_credits = 0
#         total_grade_points = 0

#         if 'registered_courses' in course_data:
#             for course in course_data["registered_courses"]:
#                 if isinstance(course, str):
#                     course = jsonify.loads(courses)
#                 credits = course['credits']
#                 grade = course['grade']
#                 if grade == 'A':
#                     grade_points = 4.0
#                 elif grade == 'A-':
#                     grade_points = 3.7
#                 elif grade == 'B+':
#                     grade_points = 3.3
#                 elif grade == 'B':
#                     grade_points = 3.0
#                 elif grade == 'B-':
#                     grade_points = 2.7
#                 elif grade == 'C+':
#                     grade_points = 2.3
#                 elif grade == 'C':
#                     grade_points = 2.0
#                 elif grade == 'C-':
#                     grade_points = 1.7
#                 elif grade == 'D+':
#                     grade_points = 1.3
#                 elif grade == 'D':
#                     grade_points = 1.0
#                 else:
#                     grade_points = 0.0

#                 total_credits += credits
#                 total_grade_points += credits * grade_points

#             gpa = round(total_grade_points / total_credits, 2)
#             return {'gpa': gpa}
#         else:
#             return {'error': 'No registered courses found'}, 404


# blp.route(GPACalculator.as_view('gpa_calculator'))

