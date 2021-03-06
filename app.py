from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///pet_adoption_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_pets():
    """Show available pets"""

    pets = Pet.query.all()

    return render_template('index.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding"""

    form = PetForm()

    # check if it's a post request AND validate the token
    if form.validate_on_submit():
        # Because of this validate_on_submit(), we can get the data directly from the form object
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # create the new pet
        new_pet = Pet(name=name, species=species,
                      photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added new pet: {name}")
        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Pet edit form; handle edits"""

    # get the pet instance
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    # check if it's a post request AND validate the token
    if form.validate_on_submit():
        # Because of this validate_on_submit(), we can get the data directly from the form object

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Updated information for pet: {pet.name}")
        return redirect("/")

    else:
        return render_template("edit_pet.html", form=form, pet=pet)
