import flask
from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'SECRETKEY'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()


@app.route('/')
def root():
    """Homepage displays available pets."""

    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def addPetForm():
    """Shows form to add a pet"""

    
    form = AddPetForm()

    if form.validate_on_submit():
        pet = Pet(
        name = form.pet_name.data,
        species = form.species.data,
        photo_url = form.photo_url.data,
        age = form.age.data,
        notes = form.notes.data)

        db.session.add(pet)
        db.session.commit()
        
        return redirect("/")
        

    else:
        return render_template("addpet.html", form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def showpet(pet_id):
    """Page displays specific pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)


    if form.validate_on_submit():
        
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available=form.available.data

        db.session.add(pet)
        db.session.commit()
        
        return render_template('showpet.html', pet=pet, form=form)



    else:
        return render_template('showpet.html', pet=pet, form=form)