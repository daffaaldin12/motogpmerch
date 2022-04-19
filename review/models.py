from django.db import models

class ReviewProduk(models.Model):
    nama = models.CharField(max_length=100)
    kondisi = models.CharField(max_length=100)
    rating = models.FloatField()
    tanggal_penjualan = models.DateField()
    review = models.TextField()
    gambar = models.ImageField(upload_to='motogpmerch-images')