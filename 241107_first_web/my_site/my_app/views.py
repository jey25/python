from django.shortcuts import render

# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def variable_view(request):
    
    my_var = {
        'first_name':"장",
        'last_name':"어영",
    }
    
    return render(request, 'my_app/variable.html', context=my_var)