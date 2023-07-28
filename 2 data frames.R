
#df1<-data.frame(c('ID','Name','Per'))
#df1<-edit(df1)
#df1<-data.frame(cbind('ID','Name','Per'))
#df1<-edit(df1)
#View(df2)
#names(df1)=c('ID','Name','perecent')
#View(df1)
#df2=data.frame(cbind('ID'=5))
#View(df2)
#df2=data.frame(cbind('ID'=2,'Status'='Enrolled','Year'=4))
#df2=edit(df2)


ID =c(1:3)
Name =c('Ali','Saif','Badar')
perce =c(65,56,88)
df1=data.frame('ID'=ID,'Name'=Name,'perce'=perce)
View(df1)


df2=data.frame(
  'ID'=c(2:5),
  'Status'=c('Enr','Graduate','Enr','Graduate'),
  'Year'=c(3,6,7,3))
View(df2)
#marge Data frames:
total<- merge(df1,df2,by='ID')
total
