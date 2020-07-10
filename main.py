# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
import datetime
import os

from flask import Flask, render_template, redirect, url_for
from db_operations import *
from forms import AdoptionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/')
def root():
    return render_template('main.html')


@app.route('/adopt', methods=['GET', 'POST'])
def adopt(pet=None):
    # Pet set to none for testing the route
    # Pet object expected to be passed when redirected from browsing
    form = AdoptionForm()
    if form.validate_on_submit():
        #TODO send message with data from form
        return redirect(url_for('root'))
    return render_template('adopt.html', pet=pet, form=form)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python38_render_template]
