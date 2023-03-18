from db import db

class StudentModel(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email_address = db.Column(db.String(80), unique=True, nullable=False)
    gpa = db.Column(db.Float, nullable=False, default=0.00)
    # password = db.Column(db.Text, nullable=False,)
    
    
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    # grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'))
    
    course = db.relationship("CourseRegistrationModel", back_populates="student", lazy="dynamic")
    # admin = db.relationship("AdminModel", back_populates="Student", uselist=False)