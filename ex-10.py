import requests
import pickle

url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
respons=requests.get(url)
respons_text=respons.text

readlines=respons_text.split("\n")
read=[[i] for i in readlines]
f=open("irisdata.pkl","wb")
pickle.dump(read,f)
f.close()



a=open("irisdata.pkl","rb")
z=pickle.load(a)
print(z)





