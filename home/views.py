from django.shortcuts import HttpResponse,redirect,HttpResponseRedirect
from django.http import FileResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO


# Create your views here.

@csrf_exempt
def home(request):
    """
    This code defines a function called "home" that takes in a "request" object as a parameter. It extracts query parameters from the request object, creates a string that includes the parameter keys and values, and returns an HTTP response containing that string.
    
    This code defines a function that takes in a request from a user and looks for any extra information (like search terms or filters) that were included with it. It then creates a message that includes all of that extra information and sends it back to the user as a response.
    """
    # Exercise: If the method is GET, send the following "You are Getting it!"
    # otherwise if the method is POST, send the following "You are posting"
    # Use the HttpResponse
    # You may need to use Postman
    """
    if request.method == "GET":
        return HttpResponse("You are Getting it!")
    elif request.method == "POST":
        return HttpResponse("You are posting")
    else:
        return HttpResponse("Hello class!")
    """
    #location = request.GET.get('location')
    #return HttpResponse("Hello class! " + location)
    query_params = request.GET.dict()
    response_string = "Hello class! "
    for key, value in query_params.items():
        response_string += key + ": " + value + " "
    return HttpResponse(response_string)

def download_pdf(request):
    """
template = get_template('home/template.html') - loads the specified template file 'home/template.html'
context = {'data': 'example'} - creates a dictionary containing data that will be passed to the template
html = template.render(context) - renders the template with the given context, resulting in an html string
result = BytesIO() - creates an instance of BytesIO to store the generated PDF
pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result) - converts the rendered html to pdf and stores it in result
response = HttpResponse(result.getvalue(), content_type='application/pdf') - creates an HTTP response object with the contents of the PDF file and sets the content type to application/pdf
response['Content-Disposition'] = 'attachment; filename="invoice.pdf"' - sets the 'Content-Disposition' header to 'attachment; filename="example.pdf"' so that the browser prompts the user to download the file instead of displaying it.
if not pdf.err: - check if there's any error occurred during rendering pdf
return response - returns the HTTP response with the PDF file to the client
else: -if any error occurred
return HttpResponse("Error Rendering PDF", status=400) - returns an HTTP response with error message.
"""
    template = get_template('home/template.html')
    context = {'data': 'example'}
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        return response
    else:
        return HttpResponse("Error Rendering PDF", status=400)


    
def my_view(request):
    return redirect("/hello_world", status=302)

def hello_world(request):
    return HttpResponse("Hello, World!",status=302)