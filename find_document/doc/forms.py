from django import forms
from django.core.validators import FileExtensionValidator


class FileForm(forms.Form):
    file = forms.FileField(
        label="",
        required=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        widget=forms.FileInput(attrs={
            'class': 'file-input',
        }),
    )
