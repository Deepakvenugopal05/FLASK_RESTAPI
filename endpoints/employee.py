from flask import Blueprint,jsonify,request
from db.employee import Employee

from db.database import db
employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('',methods=['GET'])
def get_all_employess():
    try:
        data = Employee.query.all()
        if data:
            return jsonify([members.to_dict() for members in data])
        else:
            return jsonify({"Message": "No Employees Found"}),404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@employee_bp.route('',methods=['POST'])
def add_employee():
    try:
        json_data = request.json
        existing_employee = Employee.query.get(json_data.get('EmpId'))
        if existing_employee :
            return jsonify({"message": "Employee with this ID already exists"}), 400
        new_employee = Employee(**json_data)
        db.session.add(new_employee)
        db.session.commit()
        return jsonify(new_employee.to_dict(),{"Message":"New member added"}),201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@employee_bp.route('<int:emp_id>',methods=['GET'])
def get_specific_employee(emp_id):
    try:
        data = Employee.query.get(emp_id)
        if data:
            return jsonify(data.to_dict())
        else:
            return jsonify({"Message":"No User in this id"}),404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@employee_bp.route('<int:emp_id>',methods=['PUT'])
def update_specific_employee(emp_id):
    try:
        data = Employee.query.get(emp_id)
        if data:
            json_data = request.json
            if 'EmpName' in json_data:
                data.EmpName = json_data['EmpName']
            if 'Designation' in json_data:
                data.Designation = json_data['Designation']
            if 'Manager' in json_data:
                data.Manager = json_data['Manager']
            if 'deptid' in json_data:
                data.deptid = json_data['deptid']
            db.session.commit()
            return jsonify(data.to_dict()),201
        else:
            return jsonify({'Message':'No Employee is found in this id'}),404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@employee_bp.route('<int:emp_id>',methods=['DELETE'])
def delete_specific_employee(emp_id):
    try:
        data = Employee.query.get(emp_id)
        if data:
            db.session.delete(data)
            db.session.commit()
            return jsonify({'Message':"This user is deleted!!" })
        else:
            return jsonify({"Message":"No User Found in this ID!!"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    