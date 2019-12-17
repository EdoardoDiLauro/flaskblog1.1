from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class TravelForm (FlaskForm) :
    destination= StringField('Destination',
                        validators=[DataRequired()])
    budget = StringField('Budget',
                        validators=[DataRequired()])
    duration = StringField('Duration in days',
                        validators=[DataRequired()])
    participants = StringField('Participants',
                        validators=[DataRequired()])
    description = TextAreaField('Description',
                        validators=[DataRequired()])
    submit = SubmitField('Create Travel')
