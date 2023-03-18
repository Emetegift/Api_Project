from db import db

class GPAModel(db.Model):
    __tablename__ = "grade"
    id = db.Column(db.Integer, primary_key=True)
    credit = db.Column(db.Integer, nullable=False)
    # grade = db.Column(db.String(3), nullable=False)
    course_code = db.Column(db.String(20), unique=True, nullable=False)
    
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    register_id = db.Column(db.Integer, db.ForeignKey('register.id')) 
       
    # course = db.relationship("CourseRegistrationModel", back_populates="grade", lazy="dynamic")
    register = db.relationship("EnrollmentModel", back_populates="grade", uselist=False)
    # student = db.relationship("StudentModel", back_populates="grade", uselist=False)
    