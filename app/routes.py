from flask import render_template, request
from form import ContactForm
from app import app

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
   
    return render_template('contact.html', form=form)
