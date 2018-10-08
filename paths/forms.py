from django import forms

from leaflet.forms.widgets import LeafletWidget

from paths.models import GeoWalk

class NewWalkForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'Describe your walk'}
        ),
        max_length=150,
        help_text='The max length of the text is 150'
    )

    class Meta:
        model = GeoWalk
        fields = ('name', 'description', 'geom')
        widgets = {'geom': LeafletWidget()}

