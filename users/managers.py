from django.contrib.auth.base_user import BaseUserManager


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, email, password=None, **extra_fields):
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
