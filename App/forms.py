from django import forms
from django.contrib.auth.models import User
from .models import ImagePost, Profile

COUNTY = [
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma', ('Bungoma')),
    ('Busia', ('Busia')),
    ('Elgeyo-Marakwet', ('Elgeyo-Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Marsabit', ('Marsabit')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Mombasa', ('Mombasa')),
    ("Murang'a", ("Murang'a")),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita–Taveta', ('Taita–Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka-Nithi', ('Tharaka-Nithi')),
    ('Trans-Nzoia', ('Trans-Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

CATEGORIES = [
    ('Business', ('Business')),
    ('Beach', ('Beach')),
    ('Wallpaper', ('Wallpaper')),
    ('Love', ('Love')),
    ('Flower', ('Flower')),
    ('Nature', ('Nature')),
    ('People', ('People')),
    ('Girl', ('Girl')),
    ('Food', ('Food')),
    ('Sad', ('Sad')),
    ('Computer', ('Computer')),
    ('Office', ('Office')),
    ('City', ('City')),
    ('Cars', ('Cars')),
    ('Black And White', ('Black And White')),
    ('Travel', ('Travel')),
    ('Fashion', ('Fashion')),
    ('Music', ('Music')),
    ('House', ('House')),
    ('Work', ('Work')),
    ('Flowers', ('Flowers')),
    ('Health', ('Health')),
    ('Laptop', ('Laptop')),
    ('Art', ('Art')),
    ('Technology', ('Technology')),
    ('Abstract', ('Abstract')),
    ('Sport', ('Sport')),
    ('Space', ('Space')),
    ('Landscape', ('Landscape')),
    ('Architecture', ('Architecture')),
]

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']

class AddPostForm(forms.ModelForm):
    post_image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    caption = forms.CharField(max_length=50, required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Caption'}))
    category = forms.ChoiceField(required=True, choices=CATEGORIES, widget=forms.Select(attrs={'class': 'form-control choice', 'placeholder': 'Choose Category'}))
    location = forms.ChoiceField(required=True, choices=COUNTY, widget=forms.Select(attrs={'class': 'form-control choice', 'placeholder': 'Choose Location'}))

    class Meta:
        model = ImagePost
        fields = ['post_image', 'caption', 'category', 'location']