# 乘法口诀表
for i in range (1,10):
    for j in range (1,i+1):
        print('%s*%s=%2s'%(i,j,i*j),end='  ')
    print(' ')
# 冒泡排序
alist=[8,1,2,5,3,6,4,7,9,]
for i in range(len(alist)-1):
    for j in range(len(alist)-1-i):
        m=alist[j]
        n=alist[j+1]
        if m < n :
            continue
        num=alist[j]
        alist[j]=alist[j+1]
        alist[j+1]=num
print(alist)


# 排正序
alist.sort()
print(alist)
# 排倒序
alist.reverse()
print(alist)
#列表去重
al=[1,2,3,4,5,1,2,3]
al=list(set(al))

print(al)
# 列表去重方法(2),先元素循环再if判断
li=[1,2,3,4,5,1,2,3]
new_li=[]
for i in li:
    if i not in new_li:
       new_li.append(i)
print(new_li)