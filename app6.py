import os


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





def main():
    folder_name = "cats_factory"
    print_header()
    create_folder(folder_name)
    #get images
    #display images


if __name__ == '__main__':
    main()