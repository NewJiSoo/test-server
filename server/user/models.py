from django.db import models
# from rest_framework_simplejwt.tokens import RefreshToken


class Users(models.Model):
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=17)

    # def get_token(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         "refresh": str(refresh),
    #         "access": str(refresh.access_token),
    #     }
