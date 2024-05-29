from django.db import models
import os

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class LensOption(models.Model):
    colour = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.colour


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='product_images/')

    def __str__(self):
        return self.name
    

def product_image_upload_path(instance, filename):
    return os.path.join('product_images', f'product_{instance.product.sku}', filename)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"Image for {self.product.name}"

class FrameSize(models.Model):
    product = models.OneToOneField(Product, related_name='frame_size', on_delete=models.CASCADE)
    a_measurement = models.DecimalField(max_digits=5, decimal_places=2, help_text="Size of frame per lens horizontally (in mm)")
    b_measurement = models.DecimalField(max_digits=5, decimal_places=2, help_text="Size of frame per lens vertically (in mm)")
    bridge_measurement = models.DecimalField(max_digits=5, decimal_places=2, help_text="Bridge measurement (in mm)")
    temple_length = models.PositiveIntegerField(choices=[(i, f'{i} mm') for i in range(125, 255, 5)], help_text="Temple length (in mm)")

    def __str__(self):
        return f"{self.product.name} Frame Size"

    class Meta:
        verbose_name = "Frame Size"
        verbose_name_plural = "Frame Sizes"
        
