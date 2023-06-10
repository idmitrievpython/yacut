from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if  not form.validate_on_submit():
        return render_template('main.html', form=form)
    short = form.custom_id.data or get_unique_short_id()
    url_map = URLMap(
            original=form.original_link.data,
            short=short
        )
    flash(url_for('opinion_view', short=short, _external=True))
    db.session.add(url_map)
    db.session.commit()
    return render_template('main.html', form=form)


@app.route('/<string:short>')
def opinion_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)