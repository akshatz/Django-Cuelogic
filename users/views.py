from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			msg ='Account created for {}!'.format(username)
			messages.success(request, msg)
			return redirect('blog-home')
	else:
		form = UserRegisterForm() 
	return render(request, 'users/register.html', {'form': form})


# message.debug
# message.info
# message.success
# message.warning
# message.error