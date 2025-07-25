from django.db import models
from PIL import Image

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    # nested class to specify the product variety

    class Variety(models.TextChoices):
        France = "FR", "France"
        Maroc = "MAR", "Maroc"
        Espagne = "ESP", "Espagne"
        Italie = "IT", "Italie"
        Tunisie = "TUN", "Tunisie"
        Turquie = "TUR", "Turquie"
        Egypte = "EGY", "Egypte"

    variety = models.fields.CharField(choices=Variety.choices, max_length=3)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)
            img = img.convert("RGB")  # pour éviter les bugs avec PNG/transparence
            img = img.resize((200, 200), Image.LANCZOS)  # redimensionne proprement
            img.save(img_path)

    def __str__(self):
        return f'{self.name}'
    
class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # date de création de la facture
    products = models.ManyToManyField('Product', through='InvoiceItem')  # les produits liés
    customer_name = models.CharField(max_length=100)  # optionnel, au cas où
    notes = models.TextField(blank=True, null=True)    # champ libre


    def total_price(self):
        return sum(item.total_price() for item in self.invoiceitem_set.all())

    def __str__(self):
        return f"Facture #{self.pk} -{self.customer_name}- {self.created_at.strftime('%Y-%m-%d')}"
    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"