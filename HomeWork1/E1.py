import os
import copy
import re
import string
import math
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import weight

stoplist=stopwords.words('english')
stoplist.append("'s")
PS=PorterStemmer()
diffwords=dict()
def dir_list(path):
    dirlist=[]
    for root,dirname,filename in os.walk(path):
       for name in dirname:
           dirlist.append(os.path.join(root,name))
    return dirlist

def file_list(dirlist):
    filelist=[]
    for dirname in dirlist:
        for root,dirs,filename in os.walk(dirname):
            for file in filename:
                filelist.append(os.path.join(root,file))
    return filelist
    
#将所有的标点符号转化为空格在进行计算
def splitword(filelist):
    matrix=dict()
    wlist=dict()
    for filename in filelist:
        f=open(filename,'r',errors='ignore')
        alltext=re.sub('\W+','\n',f.read()).replace('_',' ').split()
        alltext=[PS.stem(words.lower()) for words in alltext if not any(ch.isnumeric() for ch in words)  and len(words)>1]
        f.close()
        alltext=[word for word in alltext if word not in stoplist]
        for wordz in alltext:
           if wordz not in diffwords.keys():
               diffwords[wordz]=set([filename])
           else :
               diffwords.get(wordz).add(filename)
           if wordz not in wlist.keys():
               wlist[wordz]=1
           else :
               wlist[wordz]=wlist.get(wordz)+1
        matrix[filename]=wlist
        wlist={}
    print('done')
    return matrix

def main():
    dirlist=dir_list('C:\\Users\wangl\\Downloads\\20news-18828\\')
    filelist=file_list(dirlist)
    matrix=splitword(filelist)
    mmatrix=weight.tfidf(len(filelist),diffwords,matrix)
    #mmatrix=weight.wfidf(len(filelist),diffwords,matrix)

if __name__=="__main__":
    main()
