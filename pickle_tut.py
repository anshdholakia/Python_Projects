import pickle


# footballers=["messi","foden","lingard","debruyne"]
#
# file="Footballers.pkl"
# f=open(file,'wb')
# pickle.dump(footballers, f)  #dump footballers to Footballers.pkl
# f.close()


file="Footballers.pkl"
f=open(file,'rb')
picked=pickle.loads()
print(picked)

