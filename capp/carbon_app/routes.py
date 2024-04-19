from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm, TrainForm
import json

carbon_app=Blueprint('carbon_app',__name__)

#Emissions factor per transport in kg per passemger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D

efco2 = {
    'Bicycle': {'Non-electric': 0, 'Electric': 0.006},
    'Scooter': {'Electric': 0.015, 'Gasoline': 0.075},
    'Motorbike': {'Petrol': 0.129},
    'Bus': {'Diesel': 0.025, 'Biodiesel': 0.007},
    'Train': {'Diesel': 0.091, 'Electric (Nordic)': 0.007, 'Electric (Europe)': 0.024},
    'Car': {
        'Petrol': 0.167, 'Diesel': 0.137, 'Biodiesel': 0.037,
        'Electric (Nordic)': 0.014, 'Electric (Europe)': 0.045
    },
    'Ferry': {'Diesel': 0.226},
    'Plane': {
        'Scheduled flight (economy)': 0.133,
        'Charter flight (economy)': 0.118,
        'Scheduled flight (business)': 0.298
    }
}


#Carbon app, main page
@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='The Carbon APP')

#New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bus.html', title='New Entry Bus', form=form)

#New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()

        return redirect(url_for('carbon_app.your_data'))

    return render_template('carbon_app/new_entry_car.html', title='New Entry Car', form=form)

@carbon_app.route('/carbon_app/new_entry_train', methods=['GET', 'POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        try:
            kms = form.kms.data
            fuel = form.fuel_type.data
            transport = 'Train'

            co2 = float(kms) * efco2[transport][fuel]
            co2 = float("{:.2f}".format(co2))

            emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
            db.session.add(emissions)
            db.session.commit()
            return redirect(url_for('carbon_app.your_data'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error')
    return render_template('carbon_app/new_entry_train.html', title='New Entry Train', form=form)

#New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'

        # Calculating only CO2 emissions based on the distance and fuel type
        co2 = float(kms) * efco2[transport][fuel]
        total = co2  # Total emissions are equivalent to CO2 emissions as CH4 is no longer considered

        # Formatting the output to two decimal places for consistency
        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        # Creating and storing the emissions record in the database
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()

        # Redirecting the user to the data overview page
        return redirect(url_for('carbon_app.your_data'))

    # Render the form template for entering new plane emissions
    return render_template('carbon_app/new_entry_plane.html', title='New Entry Plane', form=form)


#New entry ferry
@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET', 'POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_ferry.html', title='New Entry Ferry', form=form)     
   

#New entry motorbike
@carbon_app.route('/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'

        # Calculating only CO2 emissions based on the distance and fuel type
        co2 = float(kms) * efco2[transport][fuel]
        total = co2  # Total emissions are equivalent to CO2 emissions as CH4 is no longer considered

        # Formatting the output to two decimal places for consistency
        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        # Creating and storing the emissions record in the database
        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()

        # Redirecting the user to the data overview page
        return redirect(url_for('carbon_app.your_data'))

    # Render the form template for entering new motorbike emissions
    return render_template('carbon_app/new_entry_motorbike.html', title='New Entry Motorbike', form=form)
#New entry bicycle
@carbon_app.route('/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry walk
@carbon_app.route('/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_walk.html', title='new entry walk', form=form)


#Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    # Table
    entries = Transport.query.filter_by(author=current_user) \
                             .filter(Transport.date > (datetime.now() - timedelta(days=5))) \
                             .order_by(Transport.date.desc(), Transport.transport.asc()).all()

    # Define transport types including 'Train'
    transport_types = ['Bicycle', 'Bus', 'Car', 'Ferry', 'Motorbike', 'Plane', 'Scooter', 'Walk', 'Train']

    # Initialize emissions and kilometers data for each transport type
    emission_transport = [0] * len(transport_types)
    kms_transport = [0] * len(transport_types)

    # Aggregate emissions and kilometers by transport type
    for entry in entries:
        if entry.transport in transport_types:
            index = transport_types.index(entry.transport)
            emission_transport[index] += entry.co2
            kms_transport[index] += entry.kms

    # Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(Transport.total), Transport.date) \
                                  .filter(Transport.date > (datetime.now() - timedelta(days=5))) \
                                  .filter_by(author=current_user) \
                                  .group_by(Transport.date) \
                                  .order_by(Transport.date.asc()).all()
    over_time_emissions = [entry[0] for entry in emissions_by_date]
    dates_label = [entry[1].strftime("%m-%d-%y") for entry in emissions_by_date]

    # Kilometers by date (individual)
    kms_by_date = db.session.query(db.func.sum(Transport.kms), Transport.date) \
                             .filter(Transport.date > (datetime.now() - timedelta(days=5))) \
                             .filter_by(author=current_user) \
                             .group_by(Transport.date) \
                             .order_by(Transport.date.asc()).all()
    over_time_kms = [entry[0] for entry in kms_by_date]

    return render_template('carbon_app/your_data.html', title='your_data', entries=entries,
                           emissions_by_transport=json.dumps(emission_transport),
                           kms_by_transport=json.dumps(kms_transport),
                           over_time_emissions=json.dumps(over_time_emissions),
                           over_time_kms=json.dumps(over_time_kms),
                           dates_label=json.dumps(dates_label))

@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted successfully", "success")
    return redirect(url_for('carbon_app.your_data'))
