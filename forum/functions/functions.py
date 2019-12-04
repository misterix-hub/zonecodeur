def handle_uploaded_file(file):  
    with open('forum/avatars/'+file.name, 'wb+') as destination:  
        for chunk in file.chunks():  
            destination.write(chunk)