from . import about_bp
from flask import render_template

@about_bp.route('/')
def show_index():
    title = 'About'
    return render_template('about/index.html', title=title)