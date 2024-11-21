from django import forms

from b_d_p.main_app.models import Data


class InputForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"
