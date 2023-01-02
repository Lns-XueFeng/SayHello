from flask import flash, render_template, url_for, redirect, request

from sayhello import app, db
from sayhello.models import Message
from sayhello.forms import HelloForm


@app.route("/", methods=["GET", "POST"])
def index():
    hello_form = HelloForm()
    messages = Message.query.all()
    if hello_form.validate_on_submit():
        name = hello_form.name.data
        body = hello_form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash("Your message has been sent to the world!")
        return redirect(url_for("index"))
    return render_template("index.html", hello_form=hello_form, messages=messages)
