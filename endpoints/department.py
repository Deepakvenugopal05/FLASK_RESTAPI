from flask import request, jsonify,Blueprint

from db.database import db
from db.department import Department

department_bp = Blueprint('department_bp',__name__)





@department_bp.route('',methods=['GET'])
def get_all_departments():
    try:
        data = Department.query.all()
        return jsonify([dept.to_dict() for dept in data])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@department_bp.route('',methods=['POST'])
def add_new_detail():
    try:
        json_data = request.json
        existing_detail = Department.query.get(json_data.get('DeptId'))
        if existing_detail :
            return jsonify({"message": "Department with this ID already exists"}), 400
        new_data = Department(**json_data)
        db.session.add(new_data)
        db.session.commit()
        return jsonify(new_data.to_dict(),{'Message':'New Department is added!!'}),201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@department_bp.route('<int:dept_id>',methods=['get'])
def get_specific_detail(dept_id):
    try:
        data = Department.query.get(dept_id)
        if data:
            return jsonify(data.to_dict())
        else:
            return jsonify({'Message':'No Department details in this id'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@department_bp.route('<int:dept_id>',methods=['PUT'])
def update_specific_department(dept_id):
    try:
        data = Department.query.get(dept_id)
        if data:
            json_data = request.json
            if 'DepartmentName' in json_data:
                data.DepartmentName = json_data['DepartmentName']
            db.session.commit()
            return jsonify({'Message':'Departments in this ID is Updated!!!'}),200
        else:
            return jsonify({'Message': 'No departments in this id'}),404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@department_bp.route('<int:dept_id>',methods = ['DELETE'])
def delete_specific_detail(dept_id):
    try:
        data = Department.query.get(dept_id)
        if data:
            db.session.delete(data)
            db.session.commit()
            return jsonify({'Message':'Departments in this ID is deleted'}),200
        else:
            return jsonify({'Message':'NO Departments in this ID'}),404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
    