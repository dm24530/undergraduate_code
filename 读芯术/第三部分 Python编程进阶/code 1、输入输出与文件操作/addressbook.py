#打开文件
with open('teleAddressBook.txt','rt') as ftele:
    with open('emailAddressBook.txt','rt') as femail:
        ftele.readline()        #跳过第一行
        femail.readline()
        lines1=ftele.readlines()   #将文件全部读出来，每一行作为一个元素形成一个列表
        lines2=femail.readlines()
        
        #建立空表用于存储姓名，电话，email
        list1_name=[]
        list1_tele=[]
        list2_name=[]
        list2_email=[]

        for line in lines1:         #获取第一个文本中的姓名和电话信息
            elements=line.split()    #将姓名电话分割
            #将他们分别放在定义的空列表中
            list1_name.append(elements[0])   #第一个元素是姓名
            list1_tele.append(elements[1])    #第二个元素是电话  将他们分别 放在

        for line in lines2:         #获取第二个文本中的姓名和邮件信息
            elements=line.split()
            list2_name.append(elements[0])
            list2_email.append(elements[1])
              
        #生成新的数据
        lines=[]
        #在新文件第一行写个表头
        lines.append('姓名\t电话\t\t邮箱\n')

        #遍历列表1
        for i in range(len(list1_name)):
            s=''
            if list1_name[i] in list2_name:         #查看列表1中的名字是否在列表2中
                j=list2_name.index(list1_name[i])   #如果它在里边我们找到它在第几个
                s='\t'.join([list1_name[i],list1_tele[i],list2_email[j]])    #join制表符
                s+='\n'
            else:
                s='\t'.join([list1_name[i],list1_tele[i],str('   ----   ')])    #如果列表1中的名字不在列表2中，Email用----填充
                s+='\n'
            lines.append(s)

        for i in range(len(list2_name)):
            s=''
            if list2_name[i] not in list1_name:       #列表2中的名字在列表一中没有出现
                s='\t'.join([list2_name[i],str('   ----   '),list2_email[i]])
                s+='\n'
                lines.append(s)

        #写入文件
        faddress=open('addressbook.txt','w')
        faddress.writelines(lines)

#关闭文件
faddress.close()
ftele.close()
femail.close()
print('新的通讯录已经合成')           
