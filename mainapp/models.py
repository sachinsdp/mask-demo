from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    # ⭐ Ratings (1–5)
    accommodation = models.IntegerField(default=5,null=True, blank=True)
    travel = models.IntegerField(default=5,null=True, blank=True)
    food = models.IntegerField(default=5,null=True, blank=True)
    registration = models.IntegerField(default=5,null=True, blank=True)
    talks_and_discussions = models.IntegerField(default=5,null=True, blank=True)
    venue = models.IntegerField(default=5,null=True, blank=True)
    overall_experience = models.IntegerField(default=5,null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name