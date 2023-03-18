from django.db import models
from sklearn.tree import DecisionTreeClassifier
import joblib
# Create your models here.

class Data(models.Model):
    pregnancies = models.PositiveIntegerField(null=True)
    glucose = models.PositiveIntegerField(null=True)
    bloodpressure = models.PositiveIntegerField(null=True)
    skinthickness = models.PositiveIntegerField(null=True)
    insulin = models.PositiveIntegerField(null=True)
    bmi = models.PositiveIntegerField(null=True)
    diabetespedigreefunction = models.PositiveIntegerField(null=True)
    age = models.PositiveIntegerField(null=True)
    outcome = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('diabetes_DTS_algorithm.joblib')
        self.outcome = ml_model.predict([[ self.pregnancies, self.glucose, self.bloodpressure, self.skinthickness, self.insulin, self.bmi, self.diabetespedigreefunction, self.age]])
        return super().save(*args, **kwargs)    

    def __str__(self):
        return f'prediction of id: {self.id}'  
        