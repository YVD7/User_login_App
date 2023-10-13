import shutil

# Define the directory you want to zip and the output zip file name
directory_to_zip = "Test1"
zip_filename = "PyQt5_User_login"

# Create a zip file from the directory
shutil.make_archive(zip_filename, 'zip', directory_to_zip)

print(f"Zip file '{zip_filename}' created successfully.")