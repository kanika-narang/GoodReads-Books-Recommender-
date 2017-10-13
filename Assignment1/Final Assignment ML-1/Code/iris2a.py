import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Read in the data.
#IrisTraining_corrupted1,IrisTraining.csv
iris_training = pd.read_csv("/home/chetna/Desktop/Masters/Master-Sem3/ML/irisdataset/IrisTraining_corrupted1.csv")
iris_testing = pd.read_csv("/home/chetna/Desktop/Masters/Master-Sem3/ML/irisdataset/IrisTesting.csv")

y = pd.factorize(iris_training['Species'])[0]

# print(iris_training.head(10))
# print (y)
features = iris_training.columns[:4]
print(features)
target_names=["Iris-setosa","Iris-versicolor","Iris-virginica"];
clf = RandomForestClassifier()
clf.fit(iris_training[features], y)
clf.predict(iris_testing[features])
#print(clf.predict_proba(iris_testing[features])[0:20])
output_array = clf.predict(iris_testing[features])
print("Corrupted data by adding noise...output is:")
count0=0;
count1=0;
count2=0;
count3=0;
for i in output_array:
 	if(i == 0):
 		count0+=1
 	elif(i == 1):
 		count1+=1
 	else(i == 2):
 		count2+=1
 	

col1=[count0 , 0 , 0 , 0]
col2=[0, count1 , 0 , 0]
col3=[0, 0 , count2 , 0]
col4=[0, 0, 0,count3]		
df=pd.DataFrame({'Iris-setosa':col1, 'Iris-versicolor':col2, 'Iris-virginica': col3 }, index=target_names)
print(df)