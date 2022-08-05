from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

from .models import File

# Create your views here.
# def index(request):
#     latest_name_list = File.objects.order_by('-pub_date')[:5]
#     output = ', '.join([f.name for f in latest_name_list])
#     return HttpResponse(output)
#     return HttpResponse("Hello, world. You're at the archive index.")

#Template view that can be used
def uploadPage(request):
    latest_name_list = File.objects.order_by('-pub_date')[:5]
    context = {'latest_name_list': latest_name_list}
    return render(request, 'archive/upload.html', context)

def archiveList(request):
    latest_name_list = File.objects.order_by('-pub_date')[:5]
    context = {'latest_name_list': latest_name_list}
    return render(request, 'archive/archivelist.html', context)

#Template view 2.0
# def index(request):
#     latest_name_list = File.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('archive/index.html')
#     context = {
#         'latest_name_list': latest_name_list,
#     }
#     return HttpResponse(template.render(context, request))

# def detail(request, name):
#     return HttpResponse("You're looking at name %s." % name)

# def user_directory_path(filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     #return 'user_{0}/{1}'.format(instance.user.id, filename)
#     return 'uploads'.format(filename)

# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form}))
