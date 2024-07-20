
from db.database import db
class Employee(db.Model):
    EmpId = db.Column(db.Integer, primary_key=True)
    EmpName = db.Column(db.String(50), nullable=False)
    Designation = db.Column(db.String(50), nullable=False)
    Manager = db.Column(db.Integer, nullable=True)
    deptid = db.Column(db.Integer, db.ForeignKey('department.DeptId'), nullable=False)
    
    def to_dict(self):
        return {
            'EmpId': self.EmpId,
            'EmpName': self.EmpName,
            'Designation': self.Designation,
            'Manager': self.Manager,
            'deptid': self.deptid
        }
