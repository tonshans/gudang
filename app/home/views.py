from flask import render_template
from flask_login import login_required, current_user

from .forms import InventorySearchForm
from . import home


@home.route('/', methods=['GET'])
def homepage():
    form = InventorySearchForm()
    return render_template('home/index.html', form=form, title="Selamat Datang.!")


@home.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('home/dashboard.html', title="Dashboard")


@home.route('/admin/dashboard', methods=['GET'])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    return render_template('home/admin_dashboard.html')
