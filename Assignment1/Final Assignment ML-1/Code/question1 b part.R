# salary is a table with two columns Id and TotalPay and 148654 rows
salary <- data.frame(Salaries[,c("Id","TotalPay")])

# calculating mean on the column TotalPay
meanTotalPay <- mean(salary$TotalPay)
meanTotalPay


# getting sample size from a gaussian with mean= 1000 and standard devia
S=rnorm(n = 1, mean = 1000, sd = 100)
S = ceiling(S)
S


# To select S random rows from the total 148654 rows
listofrows <- sample(1:148654, S, replace=FALSE)
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
  listofrows <- sample(1:148654, S, replace=FALSE)
  sampleTotalpay <- salary[listofrows,"TotalPay"]
  samplemean <- mean(sampleTotalpay)
})
x

# to compute the average of mean of m samples
avg <- mean(x)
avg

# Generating different mean values from 101 to 148554 
# with a gap of 1485 so that we get 100 differnt values

mean_vector <- seq(101,148554, by=1485)
mean_vector 

length(mean_vector)


n= 148654
# y vector will store the 100 average mean generated for different mu values
y= c()
for (mu in mean_vector)
{
  S= (rnorm(n = 1, mean = mu, sd = 100))
  S = ceiling(S) 
  if(S> n)
  {
    S=n
  }
  else if(S<0)
  {
    S=0
  }
  x <- replicate(100, {
    listofrows <- sample(1:148654, S , replace=FALSE)
    sampleTotalpay <- salary[listofrows,"TotalPay"]
    samplemean <- mean(sampleTotalpay)
  })
  meanx <- mean(x)
  y <- c(y, meanx)
}
y

length(y)

#ploting the the mean values of 100 different mu values
plot( mean_vector,y , main="Average mean value for m samples Vs mu values " , ylim = c(74700,max(y)) ,
      pch = 1, col = "blue" ,xlab="mu value", ylab="mean value")

#adding the line to show average value of entire data 
abline(h=74768.32, col="red", lwd=2)




# ...........For different values of sigma
# Generating different sigma values
sd_vector <- seq(0, 100000, by =1000)
sd_vector

length(sd_vector)


n= 148654
# mean is fixed at n/2
# y vector will store the 101 average mean generated for different sigma values
y= c()

for (sd in sd_vector)
{
  S= (rnorm(n = 1, mean = (n/2), sd = sd))
  S = ceiling(S) 
  if(S> n)
  {
    S=n
  }
  else if(S<0)
  {
    S=1
  }
  x <- replicate(100, {
    listofrows <- sample(1:148654, S , replace=FALSE)
    sampleTotalpay <- salary[listofrows,"TotalPay"]
    samplemean <- mean(sampleTotalpay)
  })
  meanx <- mean(x)
  y <- c(y, meanx)
}
y

length(y)

#ploting the the mean values for different sigma values.
par(yaxp  = c(min(y), max(y), 20))
plot( sd_vector,y , main="Average mean value for m samples Vs sigma values " , ylim = c(min(y),max(y)) ,
      pch = 1, col = "blue" ,xlab="sigma value", ylab="Average mean value")

#adding the line to show average value of entire data 
abline(h=74768.32, col="red", lwd=2)


#.....For different values of m
# Generating different values of m
m_vector <- seq(1, 1000, by =10)
m_vector

length(m_vector)


n= 148654
# in this case mean is fixed at n/2 and sigma is fixed at 100
# y vector will store the 100 average mean generated for different m values with mean=n/2 and sigma=100
y= c()

for (m in m_vector)
{
  S= (rnorm(n = 1, mean = (n/2), sd = 100))
  S = ceiling(S) 
  if(S> n)
  {
    S=n
  }
  else if(S<0)
  {
    S=1
  }
  x <- replicate(m, {
    listofrows <- sample(1:148654, S , replace=FALSE)
    sampleTotalpay <- salary[listofrows,"TotalPay"]
    samplemean <- mean(sampleTotalpay)
  })
  meanx <- mean(x)
  y <- c(y, meanx)
}
y

length(y)

#ploting the the mean values of 100 different values of m
plot( m_vector,y , main="Average mean value Vs value of m" , ylim = c(min(y),max(y)) ,
      pch = 1, col = "blue" ,xlab="m value", ylab="Average mean value")

#adding the line to show average value of entire data 
abline(h=74768.32, col="red", lwd=2)


#.....For different values of m (bigger values of m)
# Generating different values of m
m_vector =c(1,10,50,100,500,1000,1500,2000,3000,4000,5000,6000,7000)

n= 148654
# y vector will store the 100 average mean generated for different m values with mean=n/2 and sigma=100
y= c()

for (m in m_vector)
{
  S= (rnorm(n = 1, mean = (n/2), sd = 100))
  S = ceiling(S) 
  if(S> n)
  {
    S=n
  }
  else if(S<0)
  {
    S=1
  }
  x <- replicate(m, {
    listofrows <- sample(1:148654, S , replace=FALSE)
    sampleTotalpay <- salary[listofrows,"TotalPay"]
    samplemean <- mean(sampleTotalpay)
  })
  meanx <- mean(x)
  y <- c(y, meanx)
}
y

length(y)

#ploting 
plot( m_vector,y , main="Average mean value for different values of m " , ylim = c(min(y),max(y)) ,
      pch = 1, col = "blue" ,xlab="m value", ylab="Average mean value")

#adding the line to show average value of entire data 
abline(h=74768.32, col="red", lwd=2)
