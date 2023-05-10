file_name.casefold()=str(input(">"))
if ".gif" in file_name.casefold():
    print('image/gif')
elif ".jpg" or ".jpeg" in file_name.casefold():
    print('image/jpeg')
elif ".png" in file_name.casefold():
    print('image/png')
elif ".pdf" in file_name.casefold():
    print('PDF')
elif ".txt" in file_name.casefold():
    print('text')
elif ".zip" in file_name.casefold():
    print('ZIP')
else:
    print('application/octet-stream')