import pymongo
import os
import cv2

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["labeltool-local"]
mycol = mydb["SseSamples"]

myquery = { "objects"}

mydoc = mycol.find()

for x in mydoc:
  if 'sample' not in x['file']:  # Remove later
    dir_name = os.path.join(os.getcwd(),'/home/cocoslabs/Documents/Dev_Hitachi_Annotation/semantic-segmentation-editor/input-images'+x['folder'])
    file_name = os.path.join(dir_name,x['file'])
    print('Name of file:',file_name)
    # print(x['objects'], end="\n\n")
    with open(file_name.split('.')[0] + '.' + 'txt', 'w') as f:
      for cnt,annotated_obj in enumerate(x['objects']):
        polygon = annotated_obj['polygon']
        x_list = [x['x'] for x in polygon]
        y_list = [y['y'] for y in polygon]
        x = min(x_list) + (max(x_list)-min(x_list))/2
        y = min(y_list)+(max(y_list)-min(y_list))/2
        w = max(x_list)-min(x_list)
        h = max(y_list)-min(y_list)
        img = cv2.imread(file_name)
        ori_h, ori_w = img.shape[:2]
        print('Originl height:',ori_h,' and width:',ori_w)
        f.write(str(annotated_obj['classIndex'])+' '+str(x/ori_w)+' '+str(y/ori_h)+' '+str(w/ori_w)+' '+str(h/ori_h)+'\n')
          # f.write(str(annotated_obj['classIndex']) + ' ' + str((x / ori_w) * 10) + ' ' + str((y / ori_h) * 10) + ' ' + str((w / ori_w) * 10) + ' ' + str((h / ori_h) * 10) + '\n')
        print('Center points--------x:',int((max(x_list)-min(x_list))/2),' and y:',int((max(y_list)-min(y_list))/2))
        print('h:',int(max(y_list)-min(y_list)),' and w:',int(max(x_list)-min(x_list)))
        print('whole obj:',annotated_obj)

      #x y w h
