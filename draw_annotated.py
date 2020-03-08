import cv2
import os



base_path = '/home/cocoslabs/Documents/Dev_Hitachi_Annotation/semantic-segmentation-editor/input-images/'
for file in os.listdir(base_path):
    if file.endswith('.txt'):
        try:
            img = cv2.imread(os.path.join(base_path, file.split('.')[0] + '.jpg'))
            print('file base name:', file.split('.')[0] + '.jpg')
            ori_h, ori_w = img.shape[:2]
        except:
            img = cv2.imread(os.path.join(base_path, file.split('.')[0] + '.jpeg'))
            print('file base name:', file.split('.')[0] + '.jpeg')
            ori_h, ori_w = img.shape[:2]
        with open(os.path.join(base_path,file), 'r') as f:
            for line in f:
                x_norm, y_norm, w_norm, h_norm = line.split(' ')[1:]
                print('x:',x_norm,' and y:',y_norm,' and w:',w_norm,' and h:',h_norm)
                # print('file base name:',file.split('.')[0]+'.jpg')
                h_lambda  = lambda h: float(h)*ori_h
                w_lambda  = lambda w: float(w)*ori_w
                x, w = w_lambda(x_norm), w_lambda(w_norm)
                y, h = h_lambda(y_norm), h_lambda(h_norm)
                print('Denomalised x:', x, ' and y:', y, ' and w:', w, ' and h:', h)
                print('obj 1 x:',x-(w/2),' and y:',y-(h/2))
                print('obj 2 x:',x+(w/2),' and y:',y-(h/2))
                print('obj 3 x:',x+(w/2),' and y:',y+(h/2))
                print('obj 4 x:',x-(w/2),' and y:',y+(h/2))
                cv2.rectangle(img, (int(x-(w/2)),int(y+(h/2))), (int(x+(w/2)), int(y-(h/2))), (255, 0, 0), 2)
            cv2.imshow('Annotated Image:',img)
            cv2.waitKey(0)
