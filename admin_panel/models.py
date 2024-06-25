from django.db import models


class KazahstanCart(models.Model):
    item1_2_message = models.TextField(verbose_name="Текст сообщения для пункта 1.2", blank=False, null=True)
    item1_2_reference = models.TextField(verbose_name="Ссылка для пунка 1.2", blank=False, null=True)
    item1_2_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 1.2", blank=False, null=True)

    item1_3_message = models.TextField(verbose_name="Текст сообщения для пункта 1.3", blank=False, null=True)
    item1_3_reference = models.TextField(verbose_name="Ссылка для пунка 1.3", blank=False, null=True)
    item1_3_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 1.3", blank=False, null=True)

    class Meta:
        verbose_name = "Пункт Карта Казахстана"
        verbose_name_plural = "ункт Карта Казахстана"

    def __str__(self):
        return f"{self.item1_2_message, self.item1_2_reference} - {self.item1_3_message, self.item1_3_reference}"


class Deposited(models.Model):
    item2_1_message = models.TextField(verbose_name="Текст сообщения для пункта 2.1", blank=False, null=True)
    item2_1_reference = models.TextField(verbose_name="Ссылка для пункта 2.1", blank=False, null=True)
    item2_1_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 2.1", blank=False, null=True)

    class Meta:
        verbose_name = "Пункт Депозит"
        verbose_name_plural = "Пункт Депозит"

    def __str__(self):
        return f"{self.item2_1_message, self.item2_1_reference}"


class OpenAccount(models.Model):
    item3_1_message = models.TextField(verbose_name="Текст сообщения для пункта 3.1", blank=False, null=True)
    item3_1_reference = models.TextField(verbose_name="Ссылка для пункта 3.1", blank=False, null=True)
    item3_1_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 3.1", blank=False, null=True)

    item3_2_message = models.TextField(verbose_name="Текст сообщения для пункта 3.2", blank=False, null=True)
    item3_2_reference = models.TextField(verbose_name="Ссылка для пункта 3.2", blank=False, null=True)
    item3_2_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 3.2", blank=False, null=True)

    class Meta:
        verbose_name = "Пункт Открытие счетов"
        verbose_name_plural = "Пункт Открытие счетов"

    def __str__(self):
        return f"{self.item3_1_message, self.item3_1_reference} - {self.item3_2_message, self.item3_2_reference}"


class GoToChat(models.Model):
    message = models.TextField(verbose_name="Текст сообщения для пункта 4", blank=False, null=True)
    reference = models.TextField(verbose_name="Ссылка для пункта 4", blank=False, null=True)

    class Meta:
        verbose_name = "Пункт Переход в чат"
        verbose_name_plural = "Пункт Переход в чат"

    def __str__(self):
        return f"{self.reference} - {self.message}"


class USDT(models.Model):
    message = models.TextField(verbose_name="Текст сообщения для пункта 5", blank=False, null=True)
    reference = models.TextField(verbose_name="Ссылка для пункта 5", blank=False, null=True)

    class Meta:
        verbose_name = "Пункт Перестановка USDT"
        verbose_name_plural = "Пункт Перестановка USDT"

    def __str__(self):
        return f"{self.reference} - {self.message}"
