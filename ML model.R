install.packages("caret")
library(caret)

getwd()
df=read.csv("ML.csv",sep=",")
head(df)
head(df,5)
colnames(df)
y=as.matrix(df[,5])
head(y)

lm1= train(Length.of.menstrual.cycle~.,data = data.frame(df), method="lm")
rf1=train(Length.of.menstrual.cycle~.,data=df,method="rf")
class(lm1)
attributes(lm1)
lm1$finalModel
rf1$finalModel


samp= createDataPartition(df$Length.of.menstrual.cycle,p=0.7,list = FALSE)
training= df[samp,]
testing=df[-samp,]

summary(lm1$finalModel)$r.squared
#Although a lower R-squared can be disappointing, it is a more defensible and realistic measure of your model's likely performance on new data.
lm1
lm1$results
rf1$results

#Cross- validation

tc=trainControl(method = "cv",number = 10)
lm1_cv=train(Length.of.menstrual.cycle~.,data = data.frame(df), method="lm",trControl=tc)
lm1_cv

compare_models(lm1,rf1)

model1=lm(Length.of.menstrual.cycle~Age+BMI+Height..in.cm.+Weight..in.kg.+Stress.level,data = df)
summary(model1)


anova(model1)

res=resid(model1)

plot(fitted(model1),res,main = "Residuals vs Fitted plot")
abline(0,0)
qqnorm(res)
qqline(res)
