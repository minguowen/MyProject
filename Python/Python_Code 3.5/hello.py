import os
os.chdir('D:/testdata')   #将工作空间修改为文件所在的目录

#定义函数get_filedata从文件中取值
def get_filedata(filename):
    try:
        with open(filename)  as f:            #with语句打开和自动关闭文件
            data=f.readline()                 #从文件中逐行读取字符
            print(data.strip().split(','))
            return (data.strip().split(','))  #将字符间的空格清除后，用逗号分隔字符
    except IOError as ioerr:
        print ('File Error' + str(ioerr))     #异常处理，打印错误
        return (None)
    
#定义函数modify_time_format将所有文件中的时分表达方式统一为“分.秒”
def modify_time_format(time_string):
    if "-" in time_string:
        splitter="-"
    elif ":" in time_string:
        splitter=":"
    else:
        splitter="."
    (mins, secs)=time_string.split(splitter)  #用分隔符splitter分隔字符后分别存入mins和secs
    return (mins+ '.' +secs)

#定义函数get_prev_three返回文件中排名前三的不重复的时间成绩
def get_prev_three(filename):
    for each_t in get_filedata(filename):   #采用列表推导将统一时分表达方式后的记录生成新的列表
        print(each_t)
        new_list=modify_time_format(each_t)
        

    delete_repetition=set(new_list)                                              #采用集合set函数删除新列表中重复项，并生成新的集合
    in_order=sorted(delete_repetition)                                           #采用复制排序sorted函数对无重复性的新集合进行排序
    return (in_order[0:3])                                                       #返回列表前三项

# 分别输出对应文件中排名前三的不重复的时间成绩
print (get_prev_three("james.txt"))
print('\n')
print (get_prev_three("julie.txt"))
print('\n')
print (get_prev_three("mikey.txt"))
print('\n')
print (get_prev_three("sarah.txt"))
