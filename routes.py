from flask import Blueprint, render_template
from controlers import index, persons


urls = Blueprint('urls', __name__)


urls.add_url_rule('/', 'index', index)
urls.add_url_rule('/persons', 'persons', persons)