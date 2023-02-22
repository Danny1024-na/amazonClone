from .models import Reviews
from django.forms import ModelForm


class ProductReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fileds = ['comment','rate']