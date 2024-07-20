from endpoints.employee import employee_bp
from endpoints.department import department_bp

def register_blueprints(app):
    app.register_blueprint(employee_bp, url_prefix='/employees')
    app.register_blueprint(department_bp, url_prefix='/departments')
