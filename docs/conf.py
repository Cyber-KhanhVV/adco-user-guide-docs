project = 'ADCo ERP User Guide'
author = 'khanhvv'
release = '1.0'

extensions = ['myst_parser']
source_suffix = ['.rst', '.md']
master_doc = 'index'
html_theme = 'alabaster'
html_static_path = ['_static']  # Đảm bảo dòng này có

def setup(app):
    app.add_css_file('custom.css')
