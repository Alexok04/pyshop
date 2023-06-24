from django.forms import ModelForm, Textarea

from home.models import Category


class CategoryForm(ModelForm):
    # CamelCase moment тут ще

    class Meta:
        model = Category
        fields = (
            "name",
            "image",
        )
        widgets={
            "name": Textarea

        }