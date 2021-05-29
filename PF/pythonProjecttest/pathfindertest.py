# 英文部分

pfEngorigin=open("C:\\Users\\jiang\\Downloads\\pfEngafter.txt",encoding="utf-8")  #用UTF-8读取英文txt

dicEng={} #英文字典
key_id="" #法术id


#定义区域

def addtwodimdict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

#建立一个二维字典

def seltitle(str):
    exceptions = ["and", "or", "the", "a", "of", "in", "on"]
    lowercase_words = str.lower().split(" ")
    final_words = ""
    for i in lowercase_words:
        if i in exceptions:
            final_words += " " + i
        else:
            final_words += " " + i.capitalize()
    final_words = final_words.strip()
    return (final_words)

#部分大写


for line in pfEngorigin:
    snippet=line.strip().split(":")
    if len(snippet)==2:
        snippet[1] = snippet[1].strip().strip(",").strip('"')
        snippet[0] = snippet[0].strip().strip(",").strip('"')

    if snippet[0]=='id':
        key_id=snippet[1]

    if len(snippet)==2:
        addtwodimdict(dicEng,key_id,snippet[0],snippet[1])

#分三步 1. 格式化条目和内容 2. 将ID变换为当前法术ID 3. 在当前法术ID下填充二维字典

# print(dicEng["CAVE FANGS".lower().title()])

pfEngorigin.close()


# 中文部分

pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseUW.txt",encoding="utf-8")  #用UTF-8读取中文txt
dicChiese={} #中文字典
key_id="" #法术id
description = "" #法术描述

newspell = 2#开始检查一个新法术（中文） ACG的汉化字典制作方法中使用


# 定义


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

# 判断字符串中是否含有中文

def is_contain_English(check_str):
    for ch in check_str:
        if ch in set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"):
            return (True)

    return False



# 判断字符串中是否有英文



# 将英文字典替换为中文字典 ACG


pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseACG.txt",encoding="utf-8")  #用UTF-8读取中文txt

for line in pfChineseorigin:

    if line == "\n" and newspell > 0:
        newspell = newspell-1

    if newspell == 0:
        snippet=line.split("（")
        if len(snippet) == 2:
            snippet[1] = seltitle(snippet[1].split('）')[0].strip().strip(",").strip('"').strip("）").lower().title())
            key_id=snippet[1]
            newspell = 2
            addtwodimdict(dicChiese,key_id,'name',line.strip())
            description = ""


    elif len(line)>3 :
        snippet=line.strip().split("：",1)

        if snippet[0].strip() == "学派":
            if "（" in snippet[1]:
                subschool = snippet[1].split("（")[-1].split("）")[0].strip()
                addtwodimdict(dicChiese,key_id,"subschool",subschool)
            else:
                subschool=""
                addtwodimdict(dicChiese,key_id,"subschool",subschool)
            if "[" in snippet[1]:
                type= snippet[1].split("[")[-1].split("]")[0].strip()
                addtwodimdict(dicChiese,key_id,"types",type)
            else:
                type=""
                addtwodimdict(dicChiese,key_id,"types",type)

            newspell=2
        elif snippet[0].strip() == "环位":
            spellclass ={}
            for i in snippet[1].strip().strip(",").strip("，").split("，"):
                occupation = i.strip().split()[0]
                classnumber= i.strip().split()[-1]
                spellclass.update({occupation:classnumber})
            class_sort = ""
            for i in spellclass:
                class_sort = class_sort + '["'+ i + '",' + str(spellclass[i]) + '],'
            class_sort = "[" + class_sort.strip(",") +"]"
            addtwodimdict(dicChiese,key_id,"class",class_sort)
            newspell=2

        elif len(snippet) >= 2 and snippet[0] in ["施放时间","施法时间","成分","范围","目标","持续时间","豁免","抗力","法术抗力","区域","专注"]:
            snippet[1] = snippet[1].strip().strip(",")
            snippet[0] = snippet[0].strip().strip(",")
            addtwodimdict(dicChiese,key_id,snippet[0],snippet[1])
            newspell=2

        else:
            newspell=2
            description = description + '<p>&emsp;&emsp;'+str(line.strip())+"</p>"
            addtwodimdict(dicChiese,key_id,"shortDescription",description)

print(dicChiese["Nauseating Dart".lower().title()])


# ACG所用方法，使用空行区别法术







def method1():
    newspell=1
    description = ""
    key_id=""

    for line in pfChineseorigin:

        if is_contain_chinese(line)==False and newspell > 0:
            newspell = newspell-1

        if newspell == 0:
            snippet=line.split("（")
            if len(snippet) == 2:
                snippet[1] = seltitle(snippet[1].split('）')[0].strip().strip(",").strip('"').strip("）").lower().title())
                key_id=snippet[1]
                newspell = 1
                addtwodimdict(dicChiese,key_id,'name',line.strip())
                description = ""


        elif len(line)>3 :
            snippet=line.strip().split("：",1)

            if snippet[0].strip() == "学派":
                if "（" in snippet[1]:
                    subschool = snippet[1].split("（")[-1].split("）")[0].strip()
                    addtwodimdict(dicChiese,key_id,"subschool",subschool)
                else:
                    subschool=""
                    addtwodimdict(dicChiese,key_id,"subschool",subschool)
                if "[" in snippet[1]:
                    type= snippet[1].split("[")[-1].split("]")[0].strip()
                    addtwodimdict(dicChiese,key_id,"types",type)
                else:
                    type=""
                    addtwodimdict(dicChiese,key_id,"types",type)
                newspell=1
            elif snippet[0].strip() == "等级":
                spellclass ={}
                for i in snippet[1].strip().strip(",").strip("，").split("，"):
                    occupation = i.strip()[:-1]
                    classnumber= i.strip()[-1]
                    spellclass.update({occupation:classnumber})
                class_sort = ""
                for i in spellclass:
                    class_sort = class_sort + '["'+ i + '",' + str(spellclass[i]) + '],'
                class_sort = "[" + class_sort.strip(",") +"]"
                addtwodimdict(dicChiese,key_id,"class",class_sort)
                newspell=1
            elif len(snippet) >= 2 and snippet[0].strip() in ["施放时间","施法时间","效果","成分","范围","目标","持续","持续时间","豁免","抗力","法术抗力","区域","专注"]:
                snippet[1] = snippet[1].strip().strip(",")
                snippet[0] = snippet[0].strip().strip(",")
                addtwodimdict(dicChiese,key_id,snippet[0],snippet[1])
                newspell=1
            else:
                newspell=1
                description = description + '<p>&emsp;&emsp;'+str(line.strip())+"</p>"
                addtwodimdict(dicChiese,key_id,"shortDescription",description)

pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseUI.txt",encoding="utf-8")  #用UTF-8读取中文txt

method1()

pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseMA.txt",encoding="utf-8")  #用UTF-8读取中文txt

method1()


pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseOA.txt",encoding="utf-8")  #用UTF-8读取中文txt

method1()

# print(dicChiese["Bleed Glory".lower().title()])

# UI/MA/OA 所用方法，类似于ACG





pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseUW.txt",encoding="utf-8")  #用UTF-8读取中文txt
newspell=1


for line in pfChineseorigin:

    if is_contain_chinese(line)==False and newspell > 0:
        newspell = newspell-1

    if newspell == 0:
        snippet=line.split("（")
        if len(snippet) == 2:
            snippet[1] = seltitle(snippet[1].split('）')[0].strip().strip(",").strip('"').strip("）").lower().title())
            key_id=snippet[1]
            newspell = 1
            addtwodimdict(dicChiese,key_id,'name',line.strip())
            description = ""


    elif len(line)>3 :
        snippet=line.strip().split("：",1)

        if snippet[0].strip() == "学派":
            if "（" in snippet[1]:
                subschool = snippet[1].split("（")[-1].split("）")[0].strip()
                addtwodimdict(dicChiese,key_id,"subschool",subschool)
            if "【" in snippet[1]:
                type= snippet[1].split("【")[-1].split("】")[0].strip()
                addtwodimdict(dicChiese,key_id,"types",type)

            newspell=1
        elif snippet[0].strip() == "等级":
            spellclass ={}
            for i in snippet[1].strip().strip(",").strip("，").split("，"):
                occupation = i.strip()[:-1]
                classnumber= i.strip()[-1]
                spellclass.update({occupation:classnumber})
            class_sort = ""
            for i in spellclass:
                class_sort = class_sort + '["'+ i + '",' + str(spellclass[i]) + '],'
            class_sort = "[" + class_sort.strip(",") +"]"
            addtwodimdict(dicChiese,key_id,"class",class_sort)
            newspell=1
        elif len(snippet) >= 2 and snippet[0] in ["施法时间","成分","范围","目标","持续时间","豁免","抗力","距离","法术抗力","区域","专注","效果"]:
            snippet[1] = snippet[1].strip().strip(",")
            snippet[0] = snippet[0].strip().strip(",")
            addtwodimdict(dicChiese,key_id,snippet[0],snippet[1])
            newspell=1

        else:
            newspell=1
            description = description + '<p>&emsp;&emsp;'+str(line.strip())+"</p>"
            addtwodimdict(dicChiese,key_id,"shortDescription",description)

# print(dicChiese["Bleed Glory".lower().title()])

# UW 所用方法，类似于ACG




pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseUC&UM&ARG&APG.txt",encoding="utf-8")  #用UTF-8读取中文txt
newspell=1


for line in pfChineseorigin:

    if is_contain_chinese(line)==False and newspell > 0:
        newspell = newspell-1

    if newspell == 0 and "(" in line and line.strip()[-1] in [")","）","]","】"]:
        snippet=line.split("(")
        if len(snippet) == 2:
            snippet[1] = seltitle(snippet[1].split(')')[0].strip().strip(",").strip('"').strip(")").lower().title())
            key_id=snippet[1]
            newspell = 2
            addtwodimdict(dicChiese,key_id,'name',line.strip())
            description = ""

    elif len(line)>3:
        snippet=line.strip().split("  ",1)
        if snippet[0].strip() == "学派":
            if "(" in snippet[1]:
                subschool = snippet[1].split("(")[-1].split(")")[0].strip()
                addtwodimdict(dicChiese,key_id,"subschool",subschool)
            if "[" in snippet[1]:
                type= snippet[1].split("[")[-1].split("]")[0].strip()
                addtwodimdict(dicChiese,key_id,"types",type)
            newspell=2
        elif snippet[0].strip() == "环位":
            spellclass ={}
            for i in snippet[1].strip().strip(",").strip("，").split(","):
                occupation = i.strip()[:-1]
                classnumber= i.strip()[-1]
                spellclass.update({occupation:classnumber})
            class_sort = ""
            for i in spellclass:
                class_sort = class_sort + '["'+ i + '",' + str(spellclass[i]) + '],'
            class_sort = "[" + class_sort.strip(",") +"]"
            addtwodimdict(dicChiese,key_id,"class",class_sort)
            newspell=2
        elif len(snippet) >= 2 and snippet[0].strip() in ["施法时间","释放时间","持续时间","成分","目标","持续","豁免","抗力","法术抗力","区域",'范围',"专注"]:
            snippet[-1] = snippet[-1].strip().strip(",")
            snippet[0] = snippet[0].strip().strip(",")
            addtwodimdict(dicChiese,key_id,snippet[0],snippet[1])
            newspell=2

        elif is_contain_chinese(line) == True:
            newspell=2
            description = description + '<p>&emsp;&emsp;'+str(line.strip())+"</p>"
            addtwodimdict(dicChiese,key_id,"shortDescription",description)


print(dicChiese["Youthful Appearance".lower().title()])

# UC\UM 所用方法










def method2():
    description = ""
    key_id=""

    for line in pfChineseorigin:
        if "【" in line:
            snippet=line.split("(")
            snippet[-1] = seltitle(snippet[-1].split(')')[0].strip().strip(",").strip('"').strip("）").lower().title())
            key_id= snippet[-1]


            addtwodimdict(dicChiese,key_id,'name',line.strip())
            description = ""


        elif len(line)>3 and is_contain_chinese(line)==True:
            snippet=line.strip().split("：",1)
            if snippet[0].strip() == "等级":
                spellclass ={}
                if "、" in snippet[1]:
                    class_list = snippet[1].strip().strip(",").strip("，").strip("、").split("、")
                else:
                    class_list = [snippet[1].strip().strip(",").strip("、").strip("，")]
                for i in class_list:
                    occupation = i.strip().split()[0]
                    classnumber= i.strip().split()[1]
                    spellclass.update({occupation:classnumber})
                class_sort = ""
                for i in spellclass:
                    class_sort = class_sort + '["'+ i + '",' + str(spellclass[i]) + '],'
                class_sort = "[" + class_sort.strip(",") +"]"
                addtwodimdict(dicChiese,key_id,"class",class_sort)
            elif snippet[0] == "持续":
                snippet[1] = snippet[1].strip().strip(",")
                addtwodimdict(dicChiese,key_id,"持续时间",snippet[1])

            elif len(snippet) >= 2 and snippet[0] in ["施放时间","成分","范围","目标","豁免","抗力","法术抗力","区域","专注"]:
                snippet[1] = snippet[1].strip().strip(",")
                snippet[0] = snippet[0].strip().strip(",")
                addtwodimdict(dicChiese,key_id,snippet[0],snippet[1])
            else:
                description = description + '<p>&emsp;&emsp;'+str(line.strip())+"</p>"
                addtwodimdict(dicChiese,key_id,"shortDescription",description)

pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseVC.txt",encoding="utf-8")  #用UTF-8读取中文txt
method2()

pfChineseorigin=open("C:\\Users\\jiang\\Downloads\\pfChineseHA.txt",encoding="utf-8")  #用UTF-8读取中文txt
method2()

# print(dicChiese['Hide bruises'.lower().title()])

# HA\VC所用方法



dictrans={'name':'name',"effect":"效果","duration":"持续时间",'shortDescription':"shortDescription","types":"types","subschool":"subschool", 'class':'class','materials':"成分", 'area':"区域",'target':"目标",  'duration':"持续时间", 'savingThrow':"豁免"}



#中英文key 对照表



def trans(a):
    if a in dictrans:
        return(dictrans[a])
    else:
        return("")

dicafter = dicEng #汉化后的字典
spellname=list(dicEng.keys()) #法术名称（key1）

# 定义


for i in spellname:
    if i in dicChiese:
        spellexplain = list(dicEng[i].keys())
        for j in spellexplain:
            if trans(j) in dicChiese[i]:
                addtwodimdict(dicafter,i,j,dicChiese[i][trans(j)])


# 此时已经汉化完毕，需要将汉化完成的字典导入原本的spell 文件


def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:

    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

# 修改txt中单个Str的函数

def multialter(file_input,file_output,dict):
    file_data = ""
    spellid = "none"

    with open(file_input, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                if '"id"' in line:
                    spellid = line.split('"')[-2]
                    file_data += line
                else:
                    tag = line.split('"',2)[1]
                    if tag == 'description' and spellid in dict and "shortDescription" in dict[spellid] and len(dict[spellid]["shortDescription"])>6:
                        descriptionbefore = line.split("<h2>描述</h2>",1)
                        newline = str(descriptionbefore[0]) + "<h2>描述</h2>\\n  " + dicafter[spellid]["shortDescription"] + '\\n</div>\\n",\n'
                        file_data=file_data+newline
                    elif spellid in dict and tag in dict[spellid]:
                        linesplit = line.split(":",1)

                        if tag =="shortDescription":
                            newline = linesplit[0]+': "'+dicafter[spellid][tag]+'"\n'
                        elif linesplit[1][1]=='"':
                            newline = linesplit[0]+': "'+dicafter[spellid][tag]+'",\n'
                        elif linesplit[1][1]=='[' :
                            newline = linesplit[0]+': '+dicafter[spellid][tag]+',\n'
                        else:
                            newline= line
                        file_data = file_data + newline
                    else:
                        file_data += line
            else:
                file_data += line
    with open(file_output,"w",encoding="utf-8") as f:
        f.write(file_data)


multialter("C:\\Users\\jiang\\Downloads\\pfEng.txt","C:\\Users\\jiang\\Downloads\\pfEngafter.txt",dicafter)


