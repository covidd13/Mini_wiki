file_name=str(input(">"))
if ".gif" in file_name:
    print('image/gif')
elif ".jpg" or ".jpeg" in file_name:
    print('image/jpeg')
elif ".png" in file_name:
    print('image/png')
elif ".pdf" in file_name:
    print('PDF')
elif ".txt" in file_name:
    print('text')
elif ".zip" in file_name:
    print('ZIP')