import sys
import pathlib
import os
import shutil


def copy_and_sort_folder(folder_for_parcing:pathlib.Path, to_move_folder:pathlib.Path):
    for item in folder_for_parcing.iterdir():
        if item.is_dir():
            copy_and_sort_folder(item, to_move_folder)
        else:
            to_move_subfolder = os.path.join(str(to_move_folder), item.suffix.replace('.',''))
            #print(to_move_subfolder)
            if not os.path.exists(to_move_subfolder):
                os.mkdir(to_move_subfolder)
            shutil.copy(item, to_move_subfolder)

if __name__ == '__main__':
    #print(sys.argv)
    if len(sys.argv) > 1:
        folder_for_parcing = pathlib.Path(sys.argv[1])
        #print(folder_for_parcing.is_dir())
        if not folder_for_parcing.is_dir():
            print('Error: folder name incorrect')
        else:
            try:
                to_move_folder = pathlib.Path(sys.argv[2])
            except IndexError:
                to_move_folder = pathlib.Path('dist')
            print(to_move_folder)
            if not os.path.exists(to_move_folder):
                os.mkdir(to_move_folder)
            copy_and_sort_folder(folder_for_parcing, to_move_folder)
    else:
        print('Error: folder name required')