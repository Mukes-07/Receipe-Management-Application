from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples = [ 
        {'name' : 'abhijeet swain','age':21},
        {'name' : 'siba prasadh','age':29},
        {'name' : 'syam parida','age':28},
        {'name' : 'abishek rana','age':23},
        {'name' : 'sumesh kumar','age':20},
        {'name' : 'tanmaya sekar','age':26},
        {'name' : 'ankit samal','age':22}
    ]
    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis labore dolorem nihil expedita
      fugit odit cumque optio quisquam soluta accusantium obcaecati assumenda eligendi, minima quasi consequatur 
      autem culpa possimus! Laboriosam.Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis labore
        dolorem nihil expedita fugit odit cumque optio quisquam soluta accusantium obcaecati assumenda eligendi,
          minima quasi consequatur autem culpa possimus! Laboriosam.Lorem ipsum dolor sit amet consectetur adipisicing elit. 
          Perferendis labore dolorem nihil expedita fugit odit cumque optio quisquam soluta accusantium obcaecati assumenda
            eligendi, minima quasi consequatur autem culpa possimus! Laboriosam.Lorem ipsum dolor sit amet consectetur 
            adipisicing elit. Perferendis labore dolorem nihil expedita fugit odit cumque optio quisquam soluta accusantium
              obcaecati assumenda eligendi, minima quasi consequatur autem culpa possimus! Laboriosam."""
    
    vegetables = ["pumpkin","Tomato","potato"]

    return render(request,"home/index.html",context={'peoples': peoples,'text':text,'vegetables':vegetables})

# def home(request):
#     return HttpResponse("""<h1>Hey i am a django server</h1> 
#                         <p> Hey this is  coming from django server</p> 
#                          <hr>   
#                         <h3>Hope you are doing good :)</h3>
#                         """)

def about(request):
    return render(request, "home/about.html")

def base(request):
    return HttpResponse("hello")

def contact(request):
    return render(request, "home/contact.html")
    
def success_page(request):
    return HttpResponse("<h1>Hey this is success page</h1>")