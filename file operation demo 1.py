f=open('abc.txt','a')
print('file name:',f.name)
print('file mode:',f.mode)
print('is readable:',f.readable())
print('is writable:',f.writable())
print('is closed',f.closed)
f.close()
print('is closed:',f.closed)