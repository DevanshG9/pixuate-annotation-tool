import os
import shutil
# Create the parser
#my_parser = argparse.ArgumentParser(description='Folder path on which the renaming process needs to be performed')

# Add the arguments
#my_parser.add_argument('Path', metavar='path', type=str, help='the path to list')

# Execute the parse_args() method
#args = my_parser.parse_args()

dir_cnt = 0
task_per_person = list()
file_per_person = 0
people = 5
ext = [".jpg",".png",".jpeg"] #Allowed file extensions that will undergo renaming
def check_size(path):
    print('Size of ', path,' is',len([files for root,dir, files in os.walk(path) for file in files if os.path.isfile(os.path.join(root,file))]))
    return len([files for root,dir, files in os.walk(path) for file in files if os.path.isfile(os.path.join(root,file))])

def split(path):
    print('File per person', file_per_person)
    global dir_cnt, task_per_person, people, ext, file_per_person
    print('Peoples:',[person for person in task_per_person])
 # path, people = input('Path to be split and people').split()

    for name in os.listdir(path):
        if name.endswith(tuple(ext)):
            try:
                if check_size(task_per_person[dir_cnt]) < file_per_person or dir_cnt == people-1:
                    shutil.move(os.path.join(path,name),task_per_person[dir_cnt])
                else:
                    dir_cnt += 1
                    shutil.move(os.path.join(path, name), task_per_person[dir_cnt])
            except:
                pass
        else:
            split(os.path.join(path,name))

    print('count:',check_size(path))

def create_Once():
    global task_per_person, people, file_per_person
    try:
        os.mkdir(os.path.join('/home/cocoslabs/Desktop','Segregated_tasks'))
        for i in range(people):
            try:
                os.mkdir(os.path.join('/home/cocoslabs/Desktop', 'Segregated_tasks/Person_' + str(i)))
                task_per_person.append(os.path.join('/home/cocoslabs/Desktop', 'Segregated_tasks/Person_' + str(i)))
            except:
                pass

    except:
        pass

path = '/home/cocoslabs/Desktop/code_pracs/'
create_Once()
file_per_person = int(check_size(path) / people)

split(path)