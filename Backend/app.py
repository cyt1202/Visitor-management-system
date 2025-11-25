import os
from flask import Flask, render_template
from auth_routes import auth_bp
from visitor_routes import visitor_bp
from admin_routes import admin_bp
from db import close_db

'''
Application Entry

Initializes Flask application

Registers all Blueprints

Loads database configuration

Serves as the starting point of the server
'''

base_dir = os.path.abspath(os.path.dirname(__file__))

template_dir = os.path.join(base_dir, '../Frontend')
static_dir = os.path.join(base_dir, '../Frontend')

# Initialize Flask
app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)
app.teardown_appcontext(close_db)

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(visitor_bp, url_prefix="/api")
app.register_blueprint(admin_bp, url_prefix="/api/admin")

# Adding Page Routes
@app.route('/')
def index():
    try:
        return render_template('login.html')
    except Exception as e:
        return f"Error: Cannot find login.html. Please check if the file exists in the Frontend folder.<br>Detailed error: {e}"

@app.route('/<page_name>.html')
def render_pages(page_name):
    try:
        return render_template(f'{page_name}.html')
    except Exception as e:
        return f"Error: Cannot find {page_name}.html.<br>Detailed error: {e}", 404

if __name__ == "__main__":
    print(f"--> Frontend template path set to: {template_dir}") 
    app.run(debug=True)