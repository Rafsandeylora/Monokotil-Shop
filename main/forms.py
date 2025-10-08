from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, URLInput, Select
from main.models import Product

class ProducForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "thumbnail", "price", "stocks", "rarity", "is_featured"]
        
        # Mengubah label default dari model
        labels = {
            'name': 'Title',
            'description': 'Content',
            'thumbnail': 'Thumbnail URL',
            'is_featured': 'Featured Product'
        }
        
        # Menambahkan atribut seperti placeholder dan class CSS
        widgets = {
            'name': TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter product title'
            }),
            'description': Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 4,
                'placeholder': 'Enter product content'
            }),
            'category': Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'thumbnail': URLInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'https://example.com/image.jpg'
            }),
            'price': NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter price'
            }),
            'stocks': NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter stock quantity'
            }),
            'rarity': NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter rarity (1-5)'
            }),
            'is_featured': CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
            }),
        }