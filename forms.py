from django import forms

class BenchmarkForm(forms.Form):
    dataset_size = forms.IntegerField(label='Static Dataset Size', min_value=1, initial=1000)
    num_attributes = forms.IntegerField(label='Number of Attributes', min_value=1, initial=10)
    abe_scheme_choices = [
        ('CP-ABE', 'CP-ABE (Ciphertext-Policy ABE)'),
        ('KP-ABE', 'KP-ABE (Key-Policy ABE)'),
    ]
    abe_scheme = forms.ChoiceField(label='ABE Scheme', choices=abe_scheme_choices)