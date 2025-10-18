import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.ensemble import RandomForestRegressor

d=pd.read_csv(r"C:\Users\DELL\Desktop\ml project\house price pridiction\Housing.csv")
df=d.copy()
df.drop(columns=["furnishingstatus"],inplace=True)
le=LabelEncoder()

df["mainroad1"]=le.fit_transform(df["mainroad"])
df.drop(columns=["mainroad"],inplace=True)
df["guestroom1"]=le.fit_transform(df["guestroom"])
df.drop(columns=["guestroom"],inplace=True)
df["basement1"]=le.fit_transform(df["basement"])
df.drop(columns=["basement"],inplace=True)
df["hotwaterheating1"]=le.fit_transform(df["hotwaterheating"])
df.drop(columns=["hotwaterheating"],inplace=True)
df["airconditioning1"]=le.fit_transform(df["airconditioning"])
df.drop(columns=["airconditioning"],inplace=True)
df["prefarea1"]=le.fit_transform(df["prefarea"])
df.drop(columns=["prefarea"],inplace=True)

x0=df[["area","bedrooms","bathrooms","stories","parking","mainroad1","guestroom1","basement1", "hotwaterheating1","airconditioning1","prefarea1"]]
y0=df["price"]
xscaler=StandardScaler()

xsscaled=xscaler.fit_transform(x0)


lr=RandomForestRegressor(n_estimators=200,random_state=42)
lr.fit(xsscaled,y0)

new1=pd.DataFrame(columns=["area","bedrooms","bathrooms","stories","parking","mainroad1","guestroom1","basement1", "hotwaterheating1","airconditioning1","prefarea1"])


area=int(input("Enter area you want: "))
bedrooms=int(input("Enter how many bedrooms you want: "))
bathrooms=int(input("Enter how many bathrooms you want: "))
stories=int(input("Enter how many stories/flour you want: "))
parking=int(input("Enter how many parking you want: "))

mainroad=input("Enter you want house in mainroad say yes/no: ")
if mainroad=="yes":
    mainroad=1
elif mainroad=="no":
    mainroad=0
    
guestroom=input("Enter you want guestrooms say yes/no: ")
if guestroom=="yes":
    guestroom=1
elif guestroom=="no":
    guestroom=0
    
basement=input("Enter you want basements say yes/no: ")
if basement=="yes":
    basement=1
elif basement=="no":
    basement=0
    
hotwaterheating=input("Enter you want hotwaterheating say yes/no: ")
if hotwaterheating=="yes":
    hotwaterheating=1
elif hotwaterheating=="no":
    hotwaterheating=0
    
airconditioning=input("Enter you want airconditioning say yes/no: ")
if airconditioning=="yes":
    airconditioning=1
elif airconditioning=="no":
    airconditioning=0
    
prefarea=input("Enter you want prefarea say yes/no: ")
if prefarea=="yes":
    prefarea=1
elif prefarea=="no":
    prefarea=0


new1.loc[0]=[area,bedrooms,bathrooms,stories,parking,mainroad,guestroom,basement,hotwaterheating,airconditioning,prefarea]

sscaled2=xscaler.transform(new1)

new2=pd.DataFrame(sscaled2)
#print(new2)

new2.rename(columns={0:"area",1:"bedrooms",2:"bathrooms",3:"stories",4:"parking",5:"mainroad1",6:"guestroom1",7:"basement1",8: "hotwaterheating1",9:"airconditioning1",10:"prefarea1"},inplace=True)


x1=(new2[["area","bedrooms","bathrooms","stories","parking","mainroad1","guestroom1","basement1", "hotwaterheating1","airconditioning1","prefarea1"]])
y_pred_scaled=lr.predict(x1)
value=int(y_pred_scaled.item())

print(f"the cost of house is approximately: {value}")

# mae=mean_absolute_error(y0,y_pred_scaled)
# r2=r2_score(y0,y_pred_scaled)

# print(f"MAE: {mae}")
# print(f"r2: {r2}")