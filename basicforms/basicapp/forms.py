from django import forms
from django.core import validators
from .models import SignUp

# We create method "check_for_z" to check if the first character in the input
# is a letter 'z' or 'Z'
def check_for_z(value):
    if value[0].lower() != 'z':
        print("Need to start with z or Z ", value)
        raise forms.ValidationError("Need to start with z or Z")


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Re-enter email")
    text = forms.CharField(widget=forms.Textarea)
    # We create an input and pass to its validator the method "check_for_z"
    refree = forms.CharField(max_length=24, validators=[check_for_z])
    # We can also have a single validator for all fields at once

    # Each field has certain default validation check.
    # We can also add custom Validation
    # Eg. Lets demonstrate botcather

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
                                 validators.MaxLengthValidator(0)])
    # Hidden input widget hides the field from rendering.
    # But the field will be present in HTML element which a bot uses

    # Define a method starting with clean_<field_name>.
    # Django will automatically look for this method while Validation
    def clean_botcatcher(self):
        botcather = self.cleaned_data['botcatcher']
        if len(botcather):
            raise forms.ValidationError("Gotcha Bot!")
        return botcather

    def clean(self):
        # grab all clean data
        all_clean_data = super().clean()

        # Prints only clean data
        print("Clean data:", super().clean())

        if 'email' in all_clean_data and 'verify_email' in all_clean_data:
            if all_clean_data['email'] != all_clean_data['verify_email']:
                raise forms.ValidationError("Make sure emails are same")


class Form_SignUp(forms.ModelForm):
    # Can have validators/other modifications here. Not Compulsory.
    name = forms.CharField(label="Name", widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))
    # field names and form names should match
    class Meta:
        model = SignUp  # Assign model
        fields = "__all__"  # All fields in model
        # exclude = [exclude1,exclude2] #All model fields except
        # fields = (include1,include2) #Only these model fields
