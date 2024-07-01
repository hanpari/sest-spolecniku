import os
from ftplib import FTP_TLS, error_perm

with open("secrets/ftp.secret","r") as f:
    try:
        HOST, LOGIN, PASSWORD = f.readline().split(";")
    except Exception as e:
        print(e)
        exit()

WWW_FOLDER = 'www/sest_spolecniku/'

def remove_ftp_dir(ftps, path):
    for item in ftps.nlst(path):
        item_path = f"{path}/{item}"
        try:
            ftps.delete(item_path)
            print(f"Deleted file: {item_path}")
        except:
            remove_ftp_dir(ftps, item_path)
    ftps.rmd(path)
    print(f"Deleted directory: {path}")

def upload_folder(ftps, path):
    for name in os.listdir(path):
        local_path = os.path.join(path, name)
        if os.path.isfile(local_path):
            print(f"Uploading {name}")
            with open(local_path, 'rb') as file:
                ftps.storbinary(f'STOR {name}', file)
        elif os.path.isdir(local_path):
            print(f"Creating directory {name}")
            try:
                ftps.mkd(name)
            except error_perm as e:
                if not e.args[0].startswith('550'):
                    raise
            print(f"Changing to directory {name}")
            ftps.cwd(name)
            upload_folder(ftps, local_path)
            print(f"Changing to parent directory")
            ftps.cwd("..")



# Connect to the FTP server
ftp = FTP_TLS(HOST)
ftp.login(LOGIN, PASSWORD)
ftp.prot_p()

print("Connected...")

remove_ftp_dir(ftp, WWW_FOLDER)

ftp.mkd(WWW_FOLDER)
ftp.cwd(WWW_FOLDER)

# Upload the folder
upload_folder(ftp, WWW_FOLDER)

# Quit the FTP session
ftp.quit()
