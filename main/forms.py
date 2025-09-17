from django.forms import ModelForm
from main.models import Product

class ProducForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description","rarity","stocks", "thumbnail", "is_featured"]