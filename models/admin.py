from db import db

class AdminModel(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # registered_students_in_each_course = db.Column(db.Integer, nullable=False)
    password = db.Column(db.Text, nullable=False)
    # score = db.Column(db.Float, nullable=True)
    
    course = db.relationship("CourseRegistrationModel", back_populates="admin", lazy="dynamic")
    register = db.relationship("EnrollmentModel", back_populates="admin", lazy="dynamic")
    grade = db.relationship("CourseRegistrationModel", back_populates="admin", lazy="dynamic", overlaps="course")
    
    
    
    