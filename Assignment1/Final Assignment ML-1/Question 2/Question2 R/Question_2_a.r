
library(party)
library(randomForest)
library(caret)
library(e1071)

trainData <- read.csv(file='./IrisTraining.csv')
testData <- read.csv(file='./IrisTesting.csv')

print(head(trainData))
print(head(testData))

#Training random forest on actual uncorrupted data
iris_rf <- randomForest(Species~.,data=trainData)

#Testing the dataset after training it on uncorrupted
irisPred<-predict(iris_rf,newdata=testData)
print(irisPred)

print ("WITHOUT CORRUPTION:")
confusionMatrix(testData$Species, irisPred)

#Solving now on corrupted data
trainDataCorrupted <- read.csv(file='./IrisTraining_corrupted1.csv')
print(head(trainDataCorrupted))


#training on corrupted data
iris_rf_corrupted1 <- randomForest(Species~.,data=trainDataCorrupted)

#testing dataset after training on corrupted
irisPred_corrupted1<-predict(iris_rf_corrupted1,newdata=testData)
print(irisPred_corrupted1)

print ("WITH CORRUPTION PART 1:")
confusionMatrix(testData$Species, irisPred_corrupted1)
