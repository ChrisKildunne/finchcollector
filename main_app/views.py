from django.shortcuts import render

finches = [
    {'name': 'Finch 1', 'type': 'House Finch', 'color': 'red and white' , 'age': 2},
    {'name': 'Finch 2', 'type': 'Brown-Capped Rosy-Finch', 'color': 'brown', 'age': 4 },
    {'name': 'Finch 3', 'type': 'American Gold Finch', 'color': 'black and yellow', 'age': 5 }
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request,'about.html')
def finches_index(request):
    return render(request, 'finches/index.html',{
        'finches': finches
    })