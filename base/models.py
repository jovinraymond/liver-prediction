from django.db import models

class LiverCirrhosisPrediction(models.Model):
    n_days = models.FloatField()
    hepatomegaly = models.FloatField()
    albumin = models.FloatField()
    platelets = models.FloatField()
    prothrombin = models.FloatField()
    status = models.FloatField()
    prediction = models.IntegerField()

    def __str__(self):
        return f"Prediction: {self.prediction}"
