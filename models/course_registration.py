from db import db

class CourseRegistrationModel(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(80), nullable=False)
    course_code = db.Column(db.String(20), unique=True, nullable=False)
    semester = db.Column(db.String(50), nullable=False)
    teacher = db.Column(db.String(50), nullable=False)
    # first_name = db.Column(db.String(50), nullable=False)
    # last_name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Float, nullable=False, default=0.0)
    grade = db.Column(db.String(10), default='N/A')
    # grade = db.Column(db.String(10), nullable=False)
    # credit = db.Column(db.Integer, nullable=False)
    course_unit = db.Column(db.String(5), nullable=False)
    registered_courses = db.relationship('EnrollmentModel', backref='register', lazy=True, cascade="all, delete")
    student_registered = db.relationship('EnrollmentModel', viewonly=True, overlaps="course,register", backref='student_')
    # registered_students_in_each_course = db.Column(db.Integer, nullable=False)
    
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    
    student = db.relationship("StudentModel", back_populates="course", uselist=False)
    admin = db.relationship('AdminModel', back_populates="course", uselist=False)
