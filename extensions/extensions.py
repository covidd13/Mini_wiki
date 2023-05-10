file_name=str(input(">"))
if ".gif" in file_name.casefold():
    print('image/gif')
elif ".jpg" or ".jpeg" in file_name.casefold():
    print('image/jpeg')
elif ".png" in file_name.casefold():
    print('image/png')
elif ".pdf" in file_name.casefold():
    print('application/pdf')
elif ".txt" in file_name.casefold():
    print('text/plain')
elif ".zip" in file_name.casefold():
    print('application/zip')
else:
    print('application/octet-stream')