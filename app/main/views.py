from . import main_bp
from flask import render_template

@main_bp.route('/')
def show_index():
    return render_template('main/index.html')