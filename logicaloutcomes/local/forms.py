from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from bootstrap3_datetime.widgets import DateTimePicker

from aristotle_mdr import models as MDR
from aristotle_mdr.contrib.autocomplete import widgets

class CompareIndicatorsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        from comet.models import Indicator
        self.user = kwargs.pop('user')
        self.qs = Indicator.objects.visible(self.user)
        super(CompareIndicatorsForm, self).__init__(*args, **kwargs)

        self.fields['indicator_1'] = forms.ModelChoiceField(
            queryset=self.qs,
            empty_label="None",
            label=_("First item"),
            required=True,
            widget=widgets.ConceptAutocompleteSelect(model=Indicator)
        )

        self.fields['indicator_2'] = forms.ModelChoiceField(
            queryset=self.qs,
            empty_label="None",
            label=_("Second item"),
            required=True,
            widget=widgets.ConceptAutocompleteSelect(model=Indicator)
        )

        self.fields['indicator_3'] = forms.ModelChoiceField(
            queryset=self.qs,
            empty_label="None",
            label=_("Third item"),
            required=True,
            widget=widgets.ConceptAutocompleteSelect(model=Indicator)
        )
