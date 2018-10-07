from django import forms

from leaflet.forms.widgets import LeafletWidget
# from djgeojson.fields import MultiLineStringField

from paths.models import GeoWalk

class NewWalkForm(forms.ModelForm):
    # geom = MultiLineStringField()

    class Meta:
        model = GeoWalk
        fields = ('name', 'description', 'geom')
        widgets = {'geom': LeafletWidget()}

