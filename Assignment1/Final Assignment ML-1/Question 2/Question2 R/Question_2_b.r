
library(party)
library(randomForest)
library(caret)
library(e1071)

trainDataCorrupted2 <- read.csv(file='./IrisTraining_corrupted2.csv')
testData <- read.csv(file='./IrisTesting.csv')

print(head(trainDataCorrupted2))
print(head(testData))

#training on corrupted data
iris_rf_corrupted2 <- randomForest(Species~.,data=trainDataCorrupted2)

#testing dataset after training on corrupted
irisPred_corrupted2<-predict(iris_rf_corrupted2,newdata=testData)
print(irisPred_corrupted2)

print ("WITH CORRUPTION PART 2:")
confusionMatrix(testData$Species, irisPred_corrupted2)


