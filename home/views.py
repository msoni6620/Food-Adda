from django.shortcuts import render
from django.http import HttpResponse
# def home(request):

#     return HttpResponse("""Hey I am new in this
#                         <a href="https://www.google.com">Google</a>""")

def starttemp(request):
    peoples=[
        {"Name":"rahul","Age":"100"},
        {"Name":"Aditya","Age":"94"},
        {"Name":"Venita","Age":"17"},
        {"Name":"Vanshika","Age":"64"}
    ]
    text="""  Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut consectetur cupiditate, laboriosam, sunt quaerat quasi nam dolorem quidem necessitatibus possimus maiores et laborum at incidunt optio adipisci qui pariatur ipsam dolore eveniet sed dolores. Possimus sunt recusandae odio explicabo, perspiciatis tempore ullam, distinctio beatae reiciendis voluptatibus placeat, commodi sit enim. Quaerat dolore hic porro ipsum aut sapiente saepe repudiandae velit consequatur eaque aliquid amet magnam, quisquam a enim fugit beatae sed accusantium libero nam id mollitia quo tempore alias. Inventore saepe voluptatibus laborum, nesciunt in quisquam quo. Libero aliquid, quasi cupiditate autem dolor quas, non unde possimus pariatur, ut temporibus!
    """
    v=["Vegetable","Potato","mango"]
    return render(request,"index.html",context={"page":"Django Tut","peoples":peoples,"text":text,"v":v})

def about(request):
    context={"page":"about"}
    return render(request,"contact.html",context)


def contact(request):
    context={"page":"contact"}
    return render(request,"about.html",context)

def suceses_page(request):
    print('*'*15)
    return HttpResponse("<h1> Hey there will be some issue </h1> <hr> <b> <h2> what is your name</h2>")

# Create your views here.
