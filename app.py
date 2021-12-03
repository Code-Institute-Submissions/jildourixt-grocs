#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, flash, render_template, redirect, request, \
    session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, \
    check_password_hash
from datetime import datetime
from copy import deepcopy
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/get_items')
def get_items():
    items = mongo.db.items.find().sort('category_name', 1)
    return render_template('items.html', items=items)


@app.route('/pick_item/<category_id>', methods=['GET', 'POST'])
def pick_item(category_id):
    items = mongo.db.items.find().sort('item_name', 1)
    category = \
        mongo.db.categories.find_one({'_id': ObjectId(category_id)})
    return render_template('pick_item.html', items=items,
                           category=category)


@app.route('/pick_plus_one/<category_id>/<item_id>', methods=['GET',
           'POST'])
def pick_plus_one(item_id, category_id):
    mongo.db.items.update_one({'_id': ObjectId(item_id)},
                          {'$inc': {'in_cupboard': 1}})
    category_id = category_id
    category = \
        mongo.db.categories.find_one({'_id': ObjectId(category_id)})
    return redirect(url_for('pick_item', category_id=category_id))


@app.route('/search_plus_one/<item_id>', methods=['GET', 'POST'])
def search_plus_one(item_id):
    mongo.db.items.update_one({'_id': ObjectId(item_id)},
                          {'$inc': {'in_cupboard': 1}})
    return redirect(url_for('categories'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # check if username already exists in db

        existing_user = \
            mongo.db.users.find_one({'username': request.form.get('username'
                                    ).lower()})

        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))

        register = {'username': request.form.get('username').lower(),
                    'password': generate_password_hash(request.form.get('password'
                    ))}
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie

        session['user'] = request.form.get('username').lower()
        return redirect(url_for('initialise', username=session['user']))

    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        # check if username exists in db

        existing_user = \
            mongo.db.users.find_one({'username': request.form.get('username'
                                    ).lower()})

        if existing_user:

            # ensure hashed password matches user input

            if check_password_hash(existing_user['password'],
                                   request.form.get('password')):
                session['user'] = request.form.get('username').lower()
                flash('Welcome, {}'.format(request.form.get('username'
                      )))
                items = mongo.db.items.find()
                return render_template('items.html', items=items)
            else:

                # invalid password match

                flash('Password/username incorrect')
                return redirect(url_for('login'))
        else:

            # username doesn't exist

            flash('Password/username incorrect')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):

    # get user's username from db

    username = mongo.db.users.find_one({'username': session['user'
            ]})['username']

    if session['user']:
        return render_template('profile.html', username=username)

    return redirect(url_for('login'))


@app.route('/initialise/<username>')
def initialise(username):
    admin_items = mongo.db.items.find({'created_by': 'admin'})
    for item in admin_items:

        # change user from "admin" to username

        item['created_by'] = username

        # check if item already exists in db

        if mongo.db.items.count_documents({'item_name': item['item_name'
                ], 'created_by': username}, limit=1) != 0:
            return redirect(url_for('initialise', username=username))
        else:

        # else insert copy with username

            new_item = deepcopy(item)
            del new_item['_id']
            mongo.db.items.insert_one(new_item)
    flash('Registration successful and initial items have been put into place.')
    return redirect(url_for('profile', username=username))


@app.route('/logout')
def logout():

    # remove user from session

    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('login'))


@app.route('/categories')
def categories():
    categories = mongo.db.categories.find().sort('category_name', 1)

    # get user from db

    username = mongo.db.users.find_one({'username': session['user'
            ]})['username']
    return render_template('categories.html', categories=categories)


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        last_used = datetime.now()
        item = {
            'category_name': request.form.get('category_name').lower(),
            'item_name': request.form.get('item_name').lower(),
            'in_cupboard': 1,
            'last_used': last_used,
            'created_by': session['user'],
            }

        # check if item already exists in db

        if mongo.db.items.count_documents({'item_name': request.form.get('item_name'
                ), 'created_by': session['user']}, limit=1) != 0:
            flash('Item already exists.')
            return render_template('add_item.html')
        else:
            mongo.db.items.insert_one(item)
            flash('Item added successfully')
            return redirect(url_for('get_items'))

    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template('add_item.html', categories=categories)


@app.route('/edit_item/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    last_used = datetime.now()
    if request.method == 'POST':
        submit = {
            'category_name': request.form.get('category_name').lower(),
            'item_name': request.form.get('item_name').lower(),
            'in_cupboard': 1,
            'last_used': last_used,
            'created_by': session['user'],
            }
        mongo.db.items.update_one({'_id': ObjectId(item_id)}, submit)
        flash('Item successfully updated')

    item = mongo.db.items.find_one({'_id': ObjectId(item_id)})
    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template('edit_item.html', item=item,
                           categories=categories)


@app.route('/plus_one/<item_id>', methods=['GET', 'POST'])
def plus_one(item_id):
    mongo.db.items.update_one({'_id': ObjectId(item_id)},
                          {'$inc': {'in_cupboard': 1}})
    items = mongo.db.items.find()
    return render_template('items.html', items=items)


@app.route('/minus_one/<item_id>', methods=['GET', 'POST'])
def minus_one(item_id):
    mongo.db.items.update_one({'_id': ObjectId(item_id)},
                          {'$inc': {'in_cupboard': -1}})
    items = mongo.db.items.find()
    return render_template('items.html', items=items)


@app.route('/set_zero/<item_id>')
def set_zero(item_id):
    mongo.db.items.update_one({'_id': ObjectId(item_id)},
                          {'$set': {'in_cupboard': 0}})
    flash('Item removed from list.')
    items = mongo.db.items.find()
    return render_template('items.html', items=items)


@app.route('/set_zero/<item_id>')
def set_all_zero(username):
    mongo.db.items.update_one({'_id': ObjectId(item_id)},
                          {'$set': {'in_cupboard': 0}})
    flash('Item removed from list.')
    items = mongo.db.items.find()
    return render_template('items.html', items=items)


@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    item = mongo.db.items.find({'_id': ObjectId(item_id)})
    mongo.db.items.remove({'_id': ObjectId(item_id)})
    flash('Item deleted.')
    return redirect(url_for('categories'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query').lower()
    items = list(mongo.db.items.find({'$text': {'$search': query}}))
    if len(items) == 0:
        flash('No results.')
    categories = mongo.db.categories.find().sort('category_name', 1)
    return render_template('categories.html', items=items,
                           categories=categories)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=False)
