from django.db import models

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'defect_detection_app'


class DefectClassification(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    classification = models.CharField(max_length=255)
    maximum_width = models.DecimalField(max_digits=10, decimal_places=3, default=0.000)
    severity = models.CharField(max_length=50, default='No Defect')


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
