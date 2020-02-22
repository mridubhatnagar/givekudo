from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile

class KudoForm(forms.Form):
	collegue_name=forms.ChoiceField(choices=(), help_text="Select colleague to whom you want to give kudo.")
	kudo_count = forms.ChoiceField(choices=[(x, x) for x in range(1, 4)])
	message = forms.CharField(max_length=100, help_text="Write a message for your team member.")


	def clean_collegue_name(self):
		import ipdb; ipdb.set_trace();
		self.collegue_name = int(self.cleaned_data.get('collegue_name'))
		return self.collegue_name


	def clean_kudo_count(self):
		self.kudo_count = int(self.cleaned_data.get('kudo_count'))