from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired




class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='Title required')])
    description = TextAreaField('Description', validators=[DataRequired(message='Description required')])
    max_users = IntegerField('Max Users', validators=[DataRequired()])
    is_active = BooleanField('Is Active')
    submit = SubmitField('Create')

    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.begin_at.data = datetime.now()
    #     self.end_at.data = datetime.now()
    #
    # def validate_begin_at(self, begin_at):
    #     if begin_at.data < datetime.now():
    #         raise ValidationError('Begin at time must be in the future.')
    #
    # def validate_end_at(self, end_at):
    #     if end_at.data < self.begin_at.data:
    #         raise ValidationError('End at time must be after begin at time.')


class EventUpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='Title required')])
    description = TextAreaField('Description', validators=[DataRequired(message='Description required')])
    max_users = IntegerField('Max Users', validators=[DataRequired()])
    is_active = BooleanField('Is Active')
    submit = SubmitField('Update Event')