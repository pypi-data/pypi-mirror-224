from django.db import models

class UserIP(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
