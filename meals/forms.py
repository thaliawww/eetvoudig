from django.forms import ModelForm, widgets
import django.forms as forms
from django.forms.utils import flatatt
from django.utils.html import format_html
from meals.models import Meal, Wbw_list, Bystander, Participation


class EuroWidget(widgets.TextInput):

    def render(self, name, value, attrs=None):
        return ('<div class="input-group">\
                    <span class="input-group-addon">€-cent</span>'+
                    super(EuroWidget, self).render(name, value, attrs)+
                '</div>')

    def value_from_datadict(self, data, files, name):
        return data[name]


class ParticipationForm(forms.Form):
    participations = forms.ModelChoiceField(label='Betalende',
                                            queryset=Participation.objects.all())

    def __init__(self, *args, **kwargs):
        wbw_list = kwargs.pop('wbw_list')
        forms.Form.__init__(self, *args, **kwargs)
        qs = Participation.objects.filter(wbw_list=wbw_list)
        self.fields['participations'].queryset = qs


class BystanderForm(ModelForm):
    class Meta:
        model = Bystander
        fields = ['name']
        labels = {'name': 'Naam mee-eter'}


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['description', 'price', 'payer']
        labels = {'description': 'Toelichting',
                  'price': 'Prijs',
                  'payer': 'Betaler'}
        widgets = {'price': EuroWidget()}


class WbwListsForm(forms.Form):
    wbw_lists = forms.ModelChoiceField(queryset=Wbw_list.objects.all().order_by('name'))
