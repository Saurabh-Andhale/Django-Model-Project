from django.shortcuts import render
from testapp.forms import studentForm

def student_view(request):
    if request.method=='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            print('form valisation success')
            print('Name:',form.cleaned_data['name'])
            print('Mark:',form.cleaned_data['mark'])
            form.save(commit=True)
            print('record inserted in to')
    form=studentForm()
    my_dict = {'form': form}
    return render(request,'testapp/studentform.html',my_dict)





