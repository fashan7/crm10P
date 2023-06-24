from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from lead.models import Lead
from manager.models import Manager
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)
    
class Privilege(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    assigned_users = models.ManyToManyField(
        'User',
        related_name='assigned_privileges',
        related_query_name='assigned_privileges'
    )


    def __str__(self):
        return self.code
    
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    USER_PROFILE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('administrator', 'Administrator'),
        ('manager', 'Manager'),
        ('advisor', 'Advisor'),
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    profile = models.CharField(max_length=20, choices=USER_PROFILE_CHOICES)
    manages_lead = models.ManyToManyField(Lead, related_name='managers')
    belongs_to_manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, default=None)
    privileges = models.ManyToManyField(
        'Privilege',
        related_name='users',
        related_query_name='users'
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


