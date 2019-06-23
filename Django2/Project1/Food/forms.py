from django import forms
from .models import FoodStore


class FoodForm(forms.Form):
    """FoodForm definition."""
    name = forms.CharField(
        label='Enter food name you want to search.', max_length=50, required=True)


class AddFoodForm(forms.ModelForm):
    """Form definition for AddFood."""

    class Meta:
        """Meta definition for AddFoodform."""

        model = FoodStore
        fields = "__all__"


class AddFoodMForm(forms.ModelForm):
    """Form definition for AddFood."""

    class Meta:
        """Meta definition for AddFoodform."""

        model = FoodStore
        fields = ('code', 'product_name', 'energy_100g', 'fat_100g', 'cholesterol_100g', 'carbohydrates_100g',
                  'sugars_100g', 'starch_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'sodium_100g',
                  'alcohol_100g', 'vitamina_100g', 'vitamind_100g', 'vitamine_100g', 'vitamink_100g',
                  'vitaminc_100g', 'vitaminb1_100g', 'vitaminb2_100g', 'vitaminpp_100g', 'vitaminb6_100g',
                  'vitaminb9_100g', 'vitaminb12_100g', 'potassium_100g', 'chloride_100g', 'calcium_100g',
                  'phosphorus_100g', 'iron_100g', 'magnesium_100g', 'zinc_100g', 'copper_100g', 'manganese_100g',
                  'caffeine_100g')
