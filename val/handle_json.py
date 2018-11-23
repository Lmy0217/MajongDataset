# coding=UTF-8
import copy
import json
import os
import hashlib

if __name__ == '__main__':
    f = open("via_region_data.json",encoding="utf-8")
    data = json.load(f)
    file_name = []
    single_pic = []
    pic_md5=[]
    print(len(data["_via_img_metadata"]))
    for image in data["_via_img_metadata"]:
       file_name.append(data["_via_img_metadata"][image]["filename"])
        #print(data["_via_img_metadata"][image]["filename"])
    for filename in os.listdir(r"./"):
        if(filename.endswith("jpg") or filename.endswith("png")
        or filename.endswith("PNG") or filename.endswith("JPG")):
            p = open("./" + filename, "rb")
            content = p.read()
            p_md5 = hashlib.md5(content).hexdigest()
            # 如果该图片的md5码已经出现过则此图片不再添加
            if (p_md5 not in pic_md5):
                pic_md5.append(p_md5)
                single_pic.append(filename)
            # 删除图片中有但是json中却没有的图片
            if filename not in file_name:
                os.remove("./"+filename)
    newjson = copy.deepcopy(data)
    newjson["_via_img_metadata"]={}
    # 删除json中有　图片却没有的json键值
    for image in data["_via_img_metadata"]:
        name = (data["_via_img_metadata"][image]["filename"])
        if name in single_pic:
            newjson["_via_img_metadata"][image] = data["_via_img_metadata"][image]
    json.dump(newjson,open('via_region_data1.json','w'))




    for filename in os.listdir(r"./"):
        if(filename.endswith("png" or "jpg" or "PNG" or "JPG")):
            if filename not in single_pic:
                os.remove("./"+filename)

    pass
