from db import db
from flask_jwt_extended import get_jwt_identity

class EnrollmentModel(db.Model):
    __tablename__ = "register"
    id  = db.Column(db.Integer(), primary_key=True)
    course_name = db.Column(db.String(80), nullable=False)
    course_code = db.Column(db.String(20),unique=True, nullable=False)
    semester = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Float, nullable=False, default=0.0)
    course_unit = db.Column(db.Integer, nullable=False)
    # first_name = db.Column(db.String(50), nullable=False)
    # last_name = db.Column(db.String(50), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    grade = db.Column(db.String(10), default='N/A')
    student_id = db.Column(db.String(80), nullable=False)

    
    # student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    # course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    
    admin_id= db.Column(db.Integer, db.ForeignKey('admin.id'))
    
    admin = db.relationship("AdminModel", back_populates="register", uselist=False)
    grade = db.relationship("GPAModel", back_populates="register",  uselist=False)
    # student = db.relationship("StudentModel", back_populates="register", lazy="dynamic")
    
    
    
    
#     def __repr__(self):
#             return '<CourseRegistered %r>' % self.id


# def check_if_registered(course_code):
#     course = EnrollmentModel.query.filter_by(
#         course_code=course_code, student_id =get_jwt_identity()
#     ).first()
#     if course:
#         return True
#     return False
   
    

    