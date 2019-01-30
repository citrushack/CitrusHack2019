from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import ( #to use emails as id instead of username, we have to extend the user model
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.core.validators import FileExtensionValidator
#from .validators import validate_file_extension
# Create your models here. 
# modified https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#specifying-custom-user-model
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None): #date_of_birth,
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            #date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password): #date_of_birth,
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            #date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    #Info that is NOT saved upon signup
    email_confirmed = models.BooleanField(default=False)
    app_status = models.CharField(max_length=30, default ="Pending")
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
        
    def email_user(self, subject, message, from_email=None, **kwargs):
      send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Profile(models.Model):
    # OneToOne Relationship between MyUser and Profile Model (basically linked)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    #School Information
    school = models.CharField(max_length=50)
    LEVEL_OF_STUDY_CHOICES = (
      ("Undergraduate", "Undergraduate"),
      ("Graduate", "Graduate"),
      ("High School","High School"),
      ("Prefer not to disclose", "Prefer not to disclose"),
    )
    level_of_study = models.CharField(max_length=30, choices=LEVEL_OF_STUDY_CHOICES)
    GRADUATION_YEAR_CHOICES = (
      ("2018", "2018"),
      ("2019", "2019"),
      ("2020", "2020"),
      ("2021", "2021"),
      ("2022", "2022"),
      ("2023 or later", "2023 or later"),
      ("Prefer not to disclose", "Prefer not to disclose"),
    )
    graduation_year = models.CharField(max_length=30, choices=GRADUATION_YEAR_CHOICES)
    major = models.CharField(max_length=30)

    #Additional Information
    GENDER_CHOICES = (
      ("Female", "Female"),
      ("Male", "Male"),  
      ("Other", "Other"), 
      ("Prefer not to disclose", "Prefer not to disclose"),
    )
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    RACE_CHOICES = (
      ('Asian/Pacific Islander', 'Asian/Pacific Islander'), 
      ('Black or African American','Black or African American'),
      ('Hispanic','Hispanic'),
      ('Native American', 'Native American'),   
      ('White/Caucasian', 'White/Caucasian'),
      ('Other','Other'),
      ('Prefer not to diclose', 'Prefer not to disclose'), 
    )
    race = models.CharField(max_length=30, choices=RACE_CHOICES)
    phone_number = models.CharField(max_length=12)
    SHIRT_SIZE_CHOICES = (
      ("XS", "XS"),
      ("S", "S"),
      ("M", "M"),
      ("L", "L"),
      ("XL", "XL"),
      ("XXL", "XXL"),
    )
    shirt_size = models.CharField(max_length=3, choices=SHIRT_SIZE_CHOICES)
    dietary_restrictions = models.CharField(max_length=100, default="", blank=True)

    #Profile Information
    linkedin = models.URLField(max_length=500, blank=True)
    github = models.URLField(max_length=500, blank=True)
    additional_link = models.URLField(max_length=500, blank=True)
    description = models.CharField(max_length=100, default="")
    learn_or_gain = models.CharField(max_length=250, default="")
    resume = models.URLField(max_length=500, blank=True)
    
    #Conduct and Policies
    conduct_box = models.BooleanField(default=False)
    share_box = models.BooleanField(default=False)


#might be better to have signal codes somewhere else 
@receiver(post_save, sender=MyUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
