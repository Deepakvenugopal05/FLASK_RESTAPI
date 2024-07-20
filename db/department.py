from db.database import db
class Department(db.Model):
    DeptId = db.Column(db.Integer, primary_key=True)
    DepartmentName = db.Column(db.String(50), nullable=False)
    employees = db.relationship('Employee', backref='department', lazy=True)
    
    def to_dict(self):
        return {
            'DeptId': self.DeptId,
            'DepartmentName': self.DepartmentName
        }