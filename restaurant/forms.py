from django.forms import ModelForm, Textarea, IntegerField
from .models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # set for each form field a class attribute to use a Bootstrap class.
        self.fields['note'].widget.attrs.update({'class': 'form-control'})
        # set for each form field a class attribute to use a Bootstrap class.
        self.fields['stars'].widget.attrs.update({'class': 'form-control'})
        self.fields['expenses'].widget.attrs.update({'class': 'form-control'})
        self.fields['visit_date'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['visit_date'].help_text = "YYYY-MM-DD"

    class Meta:
        """
        A class inside a class! 
        Specify which model the form is for and the fields we want in the form.

        More in documentation: 
        https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/
        """
        model = Review
        # the only fields that the user has to fill are these
        fields = ['note', 'expenses', 'visit_date', 'stars']
        labels = {
            'stars': ('Stars'),
            'note': ('Text'),
            'expenses': ('Expenses, $'),
            'visit_date': ('Date of visit')
        }
        widgets = {
            'note': Textarea(attrs={'rows': 5}),
            # 'stars': IntegerField(attrs={'rows': 1}),

        }
