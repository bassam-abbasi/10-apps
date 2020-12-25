import os
import cat_service
import subprocess
import platform

def print_header():
    print('-----------------------')
    print('     LOL Cats App')
    print('-----------------------')


def create_folder(folder_name: str):
    current_folder_path = os.path.dirname(__file__)
    print(current_folder_path)
    full_path = os.path.join(current_folder_path, folder_name)

    print ('Full path {}'.format(full_path))
    if os.path.exists(full_path) and os.path.isdir(full_path):
        return full_path
    else:
        os.mkdir(full_path)
        return full_path


def download_cats(folder, cat_num):
    print("Downloading cats from server...")
    for i in range(1, cat_num+1):
        cat_name = 'lolcat_{}'.format(i)
        print("Downloading cat {}".format(cat_name))
        cat_service.get_cats(folder, cat_name)
    print("Done")
    

def display_images(folder_path):
    cmd_dict = {'Darwin':'open', 'Linux':'xdg-open','Windows':'explorer'}
    if cmd_dict.get(platform.system()):
        subprocess.run([cmd_dict.get(platform.system()),folder_path])
    else:
        print("We doen't support your OS: {}".format(platform.system()))

def main():
    folder_name = "cats_factory"
    print_header()
    folder_path = create_folder(folder_name)
    download_cats(folder_path,3)
    display_images(folder_path)

if __name__ == '__main__':
    main()