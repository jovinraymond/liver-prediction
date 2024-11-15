from django.db import models

class LiverCirrhosisPrediction(models.Model):
    n_days = models.FloatField(max_length=10)
    hepatomegaly = models.FloatField(max_length=4)
    albumin = models.FloatField(max_length=5)
    platelets = models.FloatField(max_length=10)
    prothrombin = models.FloatField(max_length=5)
    status = models.FloatField(max_length=4)
    prediction = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction: {self.prediction}"
