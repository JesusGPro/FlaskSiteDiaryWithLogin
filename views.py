from flask import render_template, abort, request, redirect, url_for, flash, session
from datetime import date
import database
from datetime import datetime
from record import Record
from forms import RecordEditForm, LoginForm, SearchForm
from flask_login import login_user, logout_user, login_required, current_user
from user import get_user
from passlib.hash import pbkdf2_sha256 as hasher

x = datetime.now()
fecha = x.strftime("%c")

def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        user = get_user(username)
        session['username'] = request.form['username']
        if user is not None:
            password = form.data["password"]
            if hasher.verify(password, user.password):
                login_user(user)
                flash("You have logged in.")
                next_page = request.args.get("next", url_for("home_page"))
                return redirect(next_page)
                
        flash("Invalid credentials.")
    return render_template("login.html", form=form)


def logout_page():
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("home_page"))

def home_page():
    today = date.today()
    day_name = today.strftime("%A") + " " + str(today)
    return render_template("home.html", day=day_name)
    
def records_page():
    if request.method == 'GET':
        records = database.get_records()
        return render_template("records.html", records=sorted(records, reverse=True))
    else:
        if not current_user.is_admin:
            abort(401)
        form_record_keys = request.form.getlist("record_keys")
        for form_record_key in form_record_keys:
            database.delete_record(int(form_record_key))
        return redirect(url_for("records_page"))
            

def record_page(record_key):
    record, id = database.get_record(record_key)
    # If the record with the given id doesn't exist app will generate and HTTP
    if record is None:
        abort(404)
    return render_template("record.html", record=record, id=id)

@login_required
def record_add_page():
    if not current_user.is_admin:
        abort(401)
    form = RecordEditForm()
    if request.method == 'POST':
    # if form.validate_on_submit():
        title = form.data["title"]
        content = form.data["content"]
        record = Record(title, content, fecha)
        record_key = database.add_record(record)
        return redirect(url_for("record_page", record_key=record_key))
    return render_template("record_edit.html", form=form)


@login_required    
def record_edit_page(record_key):
    record = database.get_record(record_key)[0]
    form = RecordEditForm()
    if request.method == 'POST':
    # if form.validate_on_submit():
        title = form.data["title"]
        content = form.data["content"]
        record = Record(title, content, fecha)
        database.update_record(record_key, record)
        return redirect(url_for("record_page", record_key=record_key))
    form.title.data = record.title
    form.content.data = record.content if record.content else ""
    return render_template("record_edit.html", form=form)

    
def validate_record_form(form):
    form.data = {}
    form.errors = {}

    form_title = form.get("title", "").strip()
    if len(form_title) == 0:
        form.errors["title"] = "Title can not be blank."
    else:
        form.data["title"] = form_title

    form_content = form.get("content")
    if not form_content:
        form.data["content"] = None
    elif not form_content.isdigit():
        form.errors["content"] = "Content must consist of digits only."
    else:
        content = int(form_content)
        form.data["content"] = content

    return len(form.errors) == 0

@login_required 
def sql_search():
    if not current_user.is_admin:
        abort(401)
    form = RecordEditForm()
    if request.method == 'POST':
    # if form.validate_on_submit():
        key_word = form.data["search"]
        if key_word=="":
            return render_template('home.html')
        else:
            return redirect(url_for('search_result', word_h=key_word))
    return render_template("data_for_search.html", form=form)


@login_required 
def basic_search():
    if not current_user.is_admin:
        abort(401)
    form = SearchForm()
    if request.method == 'POST':
        key_word = form.searched.data
        return redirect(url_for('basic_search_result', word_s=key_word))
    return render_template("home.html")


def search_result(word_h):
    records = database.get_sql_search(word_h)
    flash("Query send without errors")
    return render_template("search_result_sql.html", len = len(records), records=records)

def basic_search_result(word_s):
    records = word_s
    records = database.get_basic_search(word_s)
    flash("Query send without errors")
    return render_template("search_result_sql.html", len = len(records), records=records)

@login_required    
def export_to_excel():
    import pandas as pd
    from tkinter import filedialog
    import sqlite3
    
    table_name = str(session['username'])
    connection = sqlite3.connect("site_diary.db")
    data_frame = pd.read_sql(f'SELECT ID, TITLE, CONTENT FROM {table_name}', connection)
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Spreadsheet files", "*.xlsx"), ("All files", "*.*")])
        data_frame.to_excel(file_path, index=False)  
        flash("Excel file record successfully")
    except:
        return render_template('home.html')
       
    return render_template('home.html')



    