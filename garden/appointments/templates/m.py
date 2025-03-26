from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название услуги')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

class Master(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    contact_info = models.TextField(verbose_name='Контактная информация')
    photo = models.ImageField(upload_to='masters/', verbose_name='Фото')
    services = models.ManyToManyField(Service, related_name='masters', verbose_name='Услуги')

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Visit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f"Запись: {self.name} к {self.master}"
