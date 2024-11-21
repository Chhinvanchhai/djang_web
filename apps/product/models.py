from django.db import models
import uuid

def generate_unique_filename(instance, filename):
    # Generate a unique filename using uuid
    ext = filename.split('.')[-1]  # Get file extension
    filename = f'{uuid.uuid4()}.{ext}'  # Create a new filename
    return f'products/{filename}'  # Store the file in 'products/' directory

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    stock = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1)
    image = models.ImageField(upload_to=generate_unique_filename, null=True, blank=True)  # Add this line

    def __str__(self):
        return self.name


