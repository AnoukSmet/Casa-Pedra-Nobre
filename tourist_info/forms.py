from django import forms
from .models import Recommendation, RecommendationCategory
from .widgets import CustomClearableFileInput


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ('category', 'name', 'image',
                  'intro', 'description', 'link_to_website',
                  'link_to_google_maps', 'distance'
                  )

    image = forms.ImageField(label="Image", required=True,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        categories = RecommendationCategory.objects.all()
        friendly_names = [(c.id, c.friendly_name) for c in categories]

        self.fields['category'].choices = friendly_names
        placeholders = {
            'category': 'Category',
            'name': 'Name',
            'image': 'Image',
            'intro': 'Intro',
            'description': 'Description',
            'link_to_website': 'Link to website',
            'link_to_google_maps': 'Link to Google Maps',
            'distance': 'Distance',
        }
        self.fields['category'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields['intro'].widget.attrs['rows'] = 2
            self.fields['description'].widget.attrs['rows'] = 5
            self.fields[field].widget.attrs['class'] = 'recommendation-form-fields'
            self.fields[field].label = False
