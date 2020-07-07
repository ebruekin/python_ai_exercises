from numpy import exp,random,array,dot,mean,abs,transpose
import numpy as np

girdi =np.array([[0,0,1],[1,1,1],[1,0,1]])
tGirdi = np.transpose(girdi)

gercekS = np.array([[0,1,1]])
tGercekS = np.transpose(gercekS)
agirlik = np.array([[1.0,1.0,1.0]])
tAgirlik = np.transpose(agirlik)

print(girdi, "girdiler \n")
print(tGercekS ,"cıktılar \n")
print(tAgirlik , "agirlik \n")


for tekrarn in range(100):
    hücreDegeri = np.dot(girdi,tAgirlik)
    print(hücreDegeri,"hücre değeri \n")
    
    tahmin = 1 / (1+np.exp(-hücreDegeri))
    print(tahmin , "tahmin \n")
    
    tAgirlik +=np.dot(tGirdi,((tGercekS-tahmin)*tahmin*(1-tahmin))) 
    
    print(tAgirlik , "agırlık \n")
    
    hata = np.mean(np.abs(tGercekS-tahmin))
    
    print(hata ,"hata \n")
    
a = np.array([1,0,0])
b = np.dot(a,tAgirlik)

c = 1 /(1+np.exp(-b)) # tahmin ettirttik
print(c)