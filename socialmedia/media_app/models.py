from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Users(models.Model):
    username = models.CharField(max_length=100 ,unique = True)
    first_name =models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    bio = models.TextField()
    website = models.URLField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Post(models.Model):
    caption = models.TextField()
    image_or_video_content = models.FileField(upload_to='static/posts/')
    publication_date = models.DateTimeField( auto_now_add=True)
    location_post = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Like(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user.username} on Post {self.post}"

class Comment(models.Model):
    publication_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment  {self.user.username} on Post {self.post}"

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Follow(models.Model):
    follower = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"

class Message(models.Model):
    sender = models.ForeignKey(Users, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Users, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    time  = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    group_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name


