from wtforms import Form, BooleanField, PasswordField, StringField, validators, IntegerField, SelectField, DateField, FloatField
from datetime import date

class UserAccount(Form):
    userID   = IntegerField('UserID', [validators.NumberRange(min=0, max=100000)])
    name = StringField('Name', [validators.Length(min=4, max=35)])
    lastName = StringField('Last Name', [validators.Length(min=6, max=35)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.Length(min=4, max=35)])
    donor =  SelectField("Donor", choices=[("Yes", "No")], default="No")
    pickupID = IntegerField('PickupID', [validators.NumberRange(min=0, max=100000)])

class PickupStatus(Form):
    pickupID = IntegerField('PickupID', [validators.NumberRange(min=0, max=100000)])
    pickupDate = DateField('Pick up Date', default= date.today())
    restaurantID = IntegerField('RestaurantID', [validators.NumberRange(min=0, max=100000)])

class Restaurant(Form):
    restaurantID = IntegerField('RestaurantID', [validators.NumberRange(min=0, max=100000)])
    phone = StringField('Phone', [validators.Length(min=7, max=10)])
    foodID = IntegerField('FoodID', [validators.NumberRange(min=0, max=100000)])
    locationID = IntegerField('LocationID', [validators.NumberRange(min=0, max=100000)])

class FoodItem(Form):
    foodID = IntegerField('FoodID', [validators.NumberRange(min=0, max=100000)])
    foodName = StringField('Food Name', [validators.Length(min=4, max=35)])
    category = SelectField('Category', choices=[("None", "Vegetables", "Meat", "Drinks","Soup","Dairy")], default="None")
    quantity = IntegerField('Quantity', [validators.NumberRange(min=, max=100000)])
    pounds = FloatField('Pounds', default=0.00)
    expirationDate = DateField('Expiration Date', default= date.today())
    restaurantID = IntegerField('RestaurantID', [validators.NumberRange(min=0, max=100000)])

class Location(Form):
    locationID = IntegerField('LocationID', [validators.NumberRange(min=0, max=100000)])
    address = StringField('Address', [validators.Length(min=4, max=50)])
    ZipCode = IntegerField('ZipCode', [validators.NumberRange(min=0, max=5)])
    State = SelectField('State', choices=['None','AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
                                          'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI',
                                          'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY',
                                          'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 'VA',
                                          'VI', 'VT', 'WA', 'WI', 'WV', 'WY'], default="None")

class Cart(Form):
    cartID = IntegerField('CartID', [validators.NumberRange(min=0, max=100000)])
    userID   = IntegerField('UserID', [validators.NumberRange(min=0, max=100000)])
    foodID = IntegerField('FoodID', [validators.NumberRange(min=0, max=100000)])


