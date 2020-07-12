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
import datetime, os, uuid

from flask import Flask, render_template, redirect, url_for, request, abort, Response, jsonify
from db_operations import *
from forms import AdoptionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/')
def root():
    return render_template('main.html')


@app.route('/adopt/<listing_id>', methods=['GET', 'POST'])
def adopt(listing_id):
    form = AdoptionForm()
        
    listing = get_listing(listing_id)
    if not listing:
        app.logger.error(f"Failed to get listing: {listing_id}")
        abort(404, description=f"Failed to get listing: {listing_id}")

    if form.validate_on_submit():
        adopter_name = form.name.data
        adopter_email = form.email.data
        email_message = form.message.data
        #TODO get owner's email
        #TODO send email
        app.logger.info("Send email to pet owner with content")
        return redirect(url_for('root'))

    return render_template('adopt.html', listing=listing, form=form)


@app.route('/users/<email>', methods=['GET', 'POST', 'DELETE'])
def handle_user(email):
    if request.method == 'POST':
        # TODO populate user details    
        new_user = User("test@example.com_" + str(uuid.uuid4()), "name", "+6598765432", [])
        created = create_user(new_user)
       
        if not created:
            app.logger.error("Failed to create user")
            abort(500, "Failed to create user")
        return Response("", status=201, mimetype='application/json')
    if request.method == 'GET':
        user = get_user(email)
        if not user:
            app.logger.error(f"Failed to get user: {email}")
            abort(404, description=f"Failed to get user: {email}")
        return user.to_json()
    if request.method == 'DELETE':
        deleted = delete_user(email)
        if not deleted:
            app.logger.error(f"Failed to delete user: {email}")
            abort(500, f"Failed to delete user: {email}")
        return ('', 204)

@app.route('/listings', methods=['GET', 'POST'])
def handle_listings():
    if request.method == 'POST':
        # TODO implement
        pass
    if request.method == 'GET':
        listings = get_listings()
        if not listings:
            app.logger.error("Failed to get listings")
            abort(500, "Failed to get listings")
        return jsonify(listings)

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
