import pandas as pd
import os, glob, shutil
from utils import generate_unqiue_id, fileter_dataset,generate_label

# reference : https://github.com/kakaobrain/coyo-dataset

# 1. 이미지 열어서
#    - 5 kb 미만
#    - 비율 3.0 이상
#    - Min(width,height)<200
# 2. 1번 기준에 해당 안되는 것에 대해서 각 이미지 이름을 int 식별자(Id)로 이미지 이름 바꾸고
# 3. 하나의 폴더안에 있는 모든 이미지들에 대해 지정할 label(brand, name, color, low/high) 입력
# 4. dataframe에 id column, label column에 저장.
# 5. 1~4 반복.

if __name__=='__main__':

    PATH_DATASET = 'dataset'
    paths_image_folder = []

    for folder_name in os.listdir(PATH_DATASET):
        paths_image_folder.append(os.path.join(PATH_DATASET,folder_name))

    PATH_TRASH = 'trash'
    if not os.path.exists(PATH_TRASH):
        os.mkdir(PATH_TRASH)

    folder_file_dict = {}
    item_list = []

    for path in paths_image_folder:
        if path not in folder_file_dict:
            folder_file_dict[path]=[]

        label = generate_label(path)
        for filename in glob.glob(os.path.join(path,'*.jpg')):
            # filter the image
            if fileter_dataset(filename=filename) :
                src = filename
                dst = PATH_TRASH
                shutil.move(src, dst)
            else:
                # generate uid
                new_filename,uid = generate_unqiue_id(path)
                os.rename(filename,new_filename)
                folder_file_dict[path].append(uid)
                item_list.append((uid,label))

    for k,items in folder_file_dict.items():
        print(f'There {len(items)} {k} items.')

    dataframe = pd.DataFrame(item_list, columns=['uid','label'])
    print(dataframe.head())


