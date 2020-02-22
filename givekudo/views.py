from django.shortcuts import render
from django.http import HttpResponse
from .forms import KudoForm
from django.contrib.auth.models import User
from users.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'givekudo/home.html')

@csrf_exempt
def givekudo(request):
	form=KudoForm()
	if request.user.is_authenticated:
		print(request.user.id)
		print(type(request.user.id))
		form = KudoForm()
		user_details=UserProfile.objects.get(user_id=request.user.id)
		org_members=UserProfile.objects.filter(organization_name=user_details.organization_name)
		form.fields["collegue_name"].choices = [(member.user_id, User.objects.get(id=member.user_id).get_username()) for member in org_members]
		print(form.fields["collegue_name"].choices)
		if request.method == "POST":
			form=KudoForm(data=request.POST)
			print(form)
			form.fields["collegue_name"].choices = [(member.user_id, User.objects.get(id=member.user_id).get_username()) for member in org_members]
			if form.is_valid():
			    print("yayyyyyyy")

		context = {'form': form}
		return render(request, 'givekudo/kudo.html', context)
	return render(request, 'givekudo/home.html')
