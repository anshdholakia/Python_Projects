import os

def breakfunction(filen):
    sw=open(filen)
    d=sw.read()
    ds=d.split("\n")
    sw.close()
    return ds


def soldier(pathn,filen,ext):
    pathn=pathn
    filen=filen
    os.chdir(pathn)
    l=0
    ds=breakfunction(filen)
    if f in pathn:
        f_name,f_ext=os.path.splitext(f)
        if f_ext==f".{ext}":
            newName=f"{str(l)}{f_ext}"
            l+=1
            os.rename(filen,newName)
            pass
        if f_name not in ds:
            tn = f_name.title()
            new_name = f'{tn}{f_ext}'
        else:
            new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)

if __name__=='__main__':
    pathn=input("Enter path")
    filen=input("Enter file name")
    ext=input("Enter extension")
    soldier(pathn,filen,ext)

