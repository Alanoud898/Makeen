data()
mydata= data.frame(Titanic)
View(mydata)
head(mydata)
#Select:
newdata1<- mydata[which(mydata$Class=='Crew'& mydata$Survived=='No'),]
newdata1
newdata2<- mydata[which(mydata$Class=='Crew'& mydata$Survived=='Yes'),]
newdata2
#subset:
newdata3<- subset(mydata,mydata$Class=='Crew'& mydata$Survived=='No', select=c(Class,Survived))
newdata3
newdata4<- subset(Age,gender=='M' & age > 25, select=gender:q4)
newdata4
#Random:
mysample1<- Age[sample(1:nrow(leadership),3,replace= FALSE),]
mysample1
mysample2<-mydata[sample(1:nrow(mydata), 50, replace=FALSE),]
mysample2
#Using SQL:
install.packages('sqldf')
library(sqldf)
newdf<- sqldf('select * from mtcars where carb=1 order by mpg', row.names=TRUE)
View(newdf)
