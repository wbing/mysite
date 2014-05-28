from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def home(request):
<<<<<<< HEAD
    return render_to_response('home/home.html')
=======
    if request.method=='GET':
        response=HttpResponse(checkSignature(request))
        return response
    else:
        return HttpResponse('welcom to my site')
>>>>>>> 46eaa418217d6e96f67936bd496c766803e3ebb4
# Create your views here.
