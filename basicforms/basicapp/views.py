from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "basicapp/index.html")


from .forms import FormName, Form_SignUp
def form_name_view(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name", form.cleaned_data['name'])
            print("Email", form.cleaned_data['email'])
            print("Text", form.cleaned_data['text'])
            print("Refree", form.cleaned_data['refree'])
        else:
            print("ERROR!!", form.cleaned_data['name'])
    else:
        print("REQUEST METHOD: ", request.method)

    form_dict = {"form": form}
    return render(request, "basicapp/form_page.html", context=form_dict)


def form_signUp_view(request):
    form = Form_SignUp()

    if request.method == 'POST':
        form = Form_SignUp(request.POST)

        if form.is_valid():
            form.save(commit=True)  # Save form to database
            return index(request)
        else:
            print("Invalid")

    form_dict = {"form": form}
    return render(request, 'basicapp/form_signUp.html', context=form_dict)
