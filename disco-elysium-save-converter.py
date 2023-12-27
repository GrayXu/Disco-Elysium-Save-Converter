import os
import sys
import shutil
import json
from datetime import datetime, timezone

current_time = datetime.now(timezone.utc)
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%SZ")

arguments = sys.argv

# a uniquename example
unique_name = "1aa3383628ec98183457aefd5ab00f6"

if len(arguments) < 3:
    print("example:")
    print("$ python3 disco-elysium-save-converter.py -s <pc_save_name> # pc save to switch")
    # print("$ python3 disco-elysium-save-converter.py -p <save file> # switch save to pc")  # TODO
    sys.exit(-1)


if arguments[1] == "-s":
    pc_savename = str(arguments[2])
    pc_savepath = os.path.join('pc_save',pc_savename)
    
    if os.path.exists(pc_savepath+'.ntwtf.zip') == False:
        print("PC save file not found")
        sys.exit(-1)

    # clean switch save dir
    if  os.path.exists(os.path.join('switch_save',unique_name)):
        shutil.rmtree(os.path.join('switch_save',unique_name))

    # mkdir
    os.makedirs(os.path.join('switch_save',unique_name))

    # cp jpg
    shutil.copy(pc_savepath + ".jpg", os.path.join('switch_save',unique_name,unique_name+".jpg"))

    # rename pc save zip
    shutil.copy(pc_savepath + ".ntwtf.zip", os.path.join('switch_save',unique_name,unique_name+".zip"))
    
    # generate json
    json_data = {
        "version": 1,
        "dateCreatedUTC": formatted_time,
        "uniqueName": "1aa3383628ec98183457aefd5ab00f6",
        "fileName": pc_savename,
        "title": "Transfered from PC",
        "subTitle": ""
    }
    json_string = json.dumps(json_data,ensure_ascii=False)
    with open(os.path.join("switch_save",unique_name,unique_name+'.json'), 'w') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

elif arguments[1] == "-p":
    # read json
    unique_name = str(arguments[2])
    with open(os.path.join("switch_save",unique_name,unique_name+'.json'), 'r', encoding='utf-8') as json_file:
        data_dict = json.load(json_file)
    pc_savename = data_dict['fileName']
    pc_savepath = os.path.join('pc_save',pc_savename)

    # cp jpg
    shutil.copy(os.path.join('switch_save',unique_name,unique_name+".jpg"), pc_savepath + ".jpg")
    # rename pc save zip
    shutil.copy(os.path.join('switch_save',unique_name,unique_name+".zip"), pc_savepath + ".ntwtf.zip")

    sys.exit(-1)

else:
    print("invalid argument")
    sys.exit(-1)
    