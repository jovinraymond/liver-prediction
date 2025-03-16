from django.db import models

class LiverCirrhosisPrediction(models.Model):
<<<<<<< Updated upstream
    n_days = models.FloatField()
    hepatomegaly = models.FloatField()
    albumin = models.FloatField()
    platelets = models.FloatField()
    prothrombin = models.FloatField()
    status = models.FloatField()
=======
    n_days = models.FloatField(max_length=10)
    status = models.IntegerField(max_length=4)
    drug = models.IntegerField(max_length=4)
    age = models.IntegerField(max_length=6)
    sex = models.IntegerField(max_length=4)
    ascites = models.FloatField(max_length=4)
    hepatomegaly = models.FloatField(max_length=4)
    spiders = models.FloatField(max_length=4)
    edema = models.FloatField(max_length=4)
    bilirubin = models.FloatField(max_length=4)
    cholesterol = models.FloatField(default=0.0,max_length=10) 
    albumin = models.FloatField(max_length=10)
    copper = models.FloatField(max_length=10)
    alk_phos = models.FloatField(max_length=8)
    platelets = models.FloatField(max_length=10)
    prothrombin = models.FloatField(max_length=10)
    SGOT = models.FloatField(max_length=10)
    Tryglicerides = models.FloatField(max_length=10)
    platelets=models.FloatField(max_length=10)
    prothrombin = models.FloatField(default=0.0,max_length=10)
>>>>>>> Stashed changes
    prediction = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction: {self.prediction}"
