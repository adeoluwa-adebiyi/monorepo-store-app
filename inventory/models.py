from django.db import models


class ProductBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False)
    brand = models.ForeignKey('ProductBrand', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=24, decimal_places=8)
    category = models.ForeignKey('ProductCategory', on_delete=models.SET_NULL, null=True)
    image = models.TextField(null=True)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    # parent_category = models.ForeignKey('ParentCategory', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ParentCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class ParentCategoryProductListing(models.Model):
    id = models.AutoField(primary_key=True)
    parent_category = models.ForeignKey("ParentCategory",on_delete=models.CASCADE)
    product_listing = models.ForeignKey("ProductListing", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.parent_category}/{self.product_listing}"

    class Meta:
        unique_together = ["parent_category", "product_listing"]


class ProductListing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class ProductProductListing(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    pcp_listing = models.ForeignKey("ParentCategoryProductListing", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pcp_listing} - {self.product.name}"

    class Meta:
        unique_together = ["product", "pcp_listing"]





