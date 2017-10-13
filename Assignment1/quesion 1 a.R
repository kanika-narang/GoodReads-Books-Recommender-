#Question 1 a part


# salary is a table with two columns Id and TotalPay and 148654 rows
salary <- data.frame(Salaries[,c("Id","TotalPay")])

# calculating mean on the column TotalPay
meanTotalPay <- mean(salary$TotalPay)
meanTotalPay
p= 0.4
n= 148654
np= n * p


# To select 59462 random rows from the total 148654 rows
listofrows <- sample(1:148654, np, replace=FALSE)
listofrows

# select the TotalPay from the sampled rows
sampleTotalpay <- salary[listofrows,"TotalPay"]
sampleTotalpay

# calculating mean on sampled data
samplemean <- mean(sampleTotalpay)
samplemean
#sample mean = 74980.19

# we need to do this m times let m=100

x <- replicate(100, {
  listofrows <- sample(1:148654, 59462 , replace=FALSE)
  sampleTotalpay <- salary[listofrows,"TotalPay"]
  samplemean <- mean(sampleTotalpay)
})

# to compute the average of mean of m samples
avg <- mean(x)
avg

# we need to do the same for different values of p 
# generating 100 values of p at a gap of 0.01
pvector <- seq(0.01,1, by=0.01)
pvector


n= 148654
# y vector will store the 100 average mean generated for different p values
y= c()
for (p in pvector)
{
  np <- n*p
  x <- replicate(100, {
    listofrows <- sample(1:148654, np , replace=FALSE)
    sampleTotalpay <- salary[listofrows,"TotalPay"]
    samplemean <- mean(sampleTotalpay)
  })
  meanx <- mean(x)
  y <- c(y, meanx)
}
y


#ploting the the mean values of 
plot(pvector ,y, main="Average mean values for m samples Vs values of p ",ylim = c(min(y),max(y)),pch = 1, col = "blue" ,xlab="value of p", ylab="Average mean value")

#adding the line to show average value of entire data 
abline(h=74768.32, col="red", lwd=2)


# Doing Sampling for different values of m
p=0.4
m_vector=c(1,5,10,100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000)
y= c()
for (m in m_vector)
{
  np <- n*p
  x <- replicate(m, {
    listofrows <- sample(1:148654, np , replace=FALSE)
    sampleTotalpay <- salary[listofrows,"TotalPay"]
    samplemean <- mean(sampleTotalpay)
  })
  meanx <- mean(x)
  y <- c(y, meanx)
}
y

#ploting the the mean values 
plot(m_vector ,y, main="Average mean values for m samples Vs values of m ",pch = 1, col = "blue" ,xlab="value of m", ylab="Average mean value")

#adding the line to show average value of entire data 
abline(h=74768.32, col="red", lwd=2)



# Doing Sampling for different values of m (showing central limit theorem)
p=0.4
m_vector2=seq(1,1000,5)
length(m_vector2)
y2= c()
for (m in m_vector2)
{
  np <- n*p
  x <- replicate(m, {
    listofrows <- sample(1:148654, np , replace=FALSE)
    sampleTotalpay <- salary[listofrows,"TotalPay"]
    samplemean <- mean(sampleTotalpay)
  })
  meanx <- mean(x)
  y2 <- c(y2, meanx)
}
y2

#ploting the the mean values 
plot( y2,m_vector2, main="Average mean values for m samples Vs values of m ",pch = 1, col = "blue" ,ylab="value of m", xlab="Average mean value")

#adding the line to show average value of entire data 
abline(v=74768.32, col="red", lwd=2)