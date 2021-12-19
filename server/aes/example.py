
import os
from datetime import datetime
from .aes import FileSystem

def encrypt(self, request):
    password = request.POST.get('password', None)
    file = request.FILES['file']
    filename = file.name
    result = FileSystem().upload(
        file, f'media/{directory.path}', password)
    result['path'] = result['url']
    result['url'] = "http://{}/{}".format(
        request.get_host(), result['url'])
    result['owner'] = request.user.id
    result['directory'] = directory.id
    result['name'] = filename

def decrypt(self, request, pk=None):
       
        filepath = os.path.join(os.getcwd(), doc.path)
        path = FileSystem().decode(filepath, form.data.get('password', ''))
        if os.path.exists(path):
            response = FileResponse(open(path, 'rb'))
            # if os.path.exists(filepath):
            #     os.remove(path)
            return response
        else:
            return Response({'detail': 'invalid password'}, 400)