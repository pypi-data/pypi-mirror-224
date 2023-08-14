# -*- coding: utf-8 -*-
import os;
import json;
import shutil;

# 添加文本
def appendText(file,content):
    with open(file,"a",encoding="utf-8") as f:
        f.write(content);

# 写入文本
def writeText(file,content,mode="w"):
    with open(file,mode,encoding="utf-8") as f:
        f.write(content);
# 读取文本
def readText(file,mode="r"):
    with open(file,mode,encoding='utf-8') as f :
        return f.read();

# 写入json
def writeJson(filePath,dictObj):
    writeText(filePath,json.dumps(dictObj,indent=2));

# 读取json
def readJson(filePath):
    strContent = readText(filePath);
    return json.loads(strContent);

# 文件后缀
def fileSuffix(fileDir):
    return os.path.splitext(fileDir)[-1];

# 创建目录
def createDirectoryIfAbsence(filepath):
    if not os.path.exists(filepath):
        os.mkdir(filepath);

# 创建文件
def createFileIfAbsence(filePath,content=""):
    if(os.path.exists(filePath)==False):
        f= open(filePath,"w+");
        f.write(content);
        f.close();

# 打开网站
def openWeb(url):
    os.system('"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" %s'%url); 

# 测试用
def main():
    print("i am main func");

if __name__ == '__main__':
    main();