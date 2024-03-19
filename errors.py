import codecs

def lire(file_path):
    List=[]
    with codecs.open(file_path, encoding='utf-8') as f:
        for line in f:
            List.append(line.strip())
    return(List)

errors=lire('data/errors.txt')

def RESET():
    file=open('data/errors.txt','w')
    file.write('0')
    file.close()
    
def COUNT():
    file=open('data/errors.txt','r')
    txt=file.read()
    file.close()
    return(txt)

def ADD(i):
    file=open('data/errors.txt','r')
    txt=file.read()
    file.close()
    file=open('data/errors.txt','w')
    file.write(str(int(txt)+i))
    file.close()