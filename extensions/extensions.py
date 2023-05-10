file_name=str(input(">"))
if ".gif" in file_name.casefold().strip():
    print('image/gif')
elif ".jpg" in file_name.casefold().strip():
    print('image/jpeg')
elif ".jpeg" in file_name.casefold().strip():
    print('image/jpeg')
elif ".png" in file_name.casefold().strip():
    print('image/png')
elif ".pdf" in file_name.casefold().strip():
    print('application/pdf')
elif ".txt" in file_name.casefold().strip():
    print('text/plain')
elif ".zip" in file_name.casefold().strip():
    print('application/zip')
else:
    print('application/octet-stream')