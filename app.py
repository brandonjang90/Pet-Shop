from flask import Flask, render_template, redirect, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from sqlalchemy import text
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'itsasecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species=form.species.data
        photo_url = form.photo.data
        age = form.age.data
        notes = form.notes.data
        
        pet = Pet (name = name, species=species, photo_url=photo_url, age=age, notes=notes)
       
        db.session.add(pet)
        db.session.commit()
        flash(f"{name} the {species} has been added!")
        return redirect('/')
    else:
        return render_template('form.html', form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo.data
        pet.available = form.available.data
        pet.notes = form.notes.data

        db.session.commit()
        flash(f"Information for {pet.name} has been updated.")
        return redirect('/')

    else:
        return render_template("edit.html", form=form, pet=pet)