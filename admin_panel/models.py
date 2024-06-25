import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class KazahstanCart1_2(models.Model):
    item1_2_message = models.TextField(verbose_name="Текст сообщения для пункта 1.2", blank=False, null=True)
    item1_2_reference = models.TextField(verbose_name="Ссылка для пунка 1.2", blank=True, null=True)
    item1_2_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 1.2",
                                        blank=True, null=True)
    item1_2_document_reserve = models.FileField(upload_to='documents', blank=True, null=True,
                                                verbose_name="Загрузка документа для пункта 1.2")

    class Meta:
        verbose_name = "Пункт 1.2 Карта Казахстана"
        verbose_name_plural = "Пункт 1.2 Карта Казахстана"

    def __str__(self):
        return f"{self.item1_2_message, self.item1_2_reference}"


@receiver(pre_delete, sender=KazahstanCart1_2)
def delete_document(sender, instance, **kwargs):
    if instance.item1_2_document or instance.item1_2_document_reserve:
        if os.path.isfile(instance.item1_2_document.path):
            os.remove(instance.item1_2_document.path)
        elif os.path.isfile(instance.item1_2_document_reserve.path):
            os.remove(instance.item1_2_document_reserve.path)


class KazahstanCart1_3(models.Model):
    item1_3_message = models.TextField(verbose_name="Текст сообщения для пункта 1.3", blank=False, null=True)
    item1_3_reference = models.TextField(verbose_name="Ссылка для пунка 1.3", blank=True, null=True)
    item1_3_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 1.3",
                                        blank=True, null=True)
    item1_3_document_reserve = models.FileField(upload_to='documents', blank=True, null=True,
                                                verbose_name="Загрузка документа для пункта 1.3")

    class Meta:
        verbose_name = "Пункт 1.3 Карта Казахстана"
        verbose_name_plural = "Пункт 1.3 Карта Казахстана"

    def __str__(self):
        return f"{self.item1_3_message, self.item1_3_reference}"


@receiver(pre_delete, sender=KazahstanCart1_3)
def delete_document(sender, instance, **kwargs):
    if instance.item1_3_document or instance.item1_3_document_reserve:
        if os.path.isfile(instance.item1_3_document.path):
            os.remove(instance.item1_3_document.path)
        elif os.path.isfile(instance.item1_3_document_reserve.path):
            os.remove(instance.item1_3_document_reserve.path)


class Deposited(models.Model):
    item2_1_message = models.TextField(verbose_name="Текст сообщения для пункта 2.1", blank=False, null=True)
    item2_1_reference = models.TextField(verbose_name="Ссылка для пункта 2.1", blank=True, null=True)
    item2_1_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 2.1",
                                        blank=True, null=True)
    item2_1_document_reserve = models.FileField(upload_to='documents', blank=True, null=True,
                                                verbose_name="Загрузка документа для пункта 2.1")

    class Meta:
        verbose_name = "Пункт 2.1 Депозит"
        verbose_name_plural = "Пункт 2.1 Депозит"

    def __str__(self):
        return f"{self.item2_1_message, self.item2_1_reference}"


@receiver(pre_delete, sender=Deposited)
def delete_document(sender, instance, **kwargs):
    if instance.item2_1_document or instance.item2_1_document_reserve:
        if os.path.isfile(instance.item2_1_document.path):
            os.remove(instance.item2_1_document.path)
        elif os.path.isfile(instance.item2_1_document_reserve.path):
            os.remove(instance.item2_1_document_reserve.path)


class OpenAccount3_1(models.Model):
    item3_1_message = models.TextField(verbose_name="Текст сообщения для пункта 3.1", blank=False, null=True)
    item3_1_reference = models.TextField(verbose_name="Ссылка для пункта 3.1", blank=True, null=True)
    item3_1_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 3.1",
                                        blank=True, null=True)
    item3_1_document_reserve = models.FileField(upload_to='documents', blank=True, null=True,
                                                verbose_name="Загрузка документа для пункта 3.1")

    class Meta:
        verbose_name = "Пункт 3.1 Открытие счетов"
        verbose_name_plural = "Пункт 3.1 Открытие счетов"

    def __str__(self):
        return f"{self.item3_1_message, self.item3_1_reference}"


@receiver(pre_delete, sender=OpenAccount3_1)
def delete_document(sender, instance, **kwargs):
    if instance.item3_1_document or instance.item3_1_document_reserve:
        if os.path.isfile(instance.item3_1_document.path):
            os.remove(instance.item3_1_document.path)
        elif os.path.isfile(instance.item3_1_document_reserve.path):
            os.remove(instance.item3_1_document_reserve.path)


class OpenAccount3_2(models.Model):
    item3_2_message = models.TextField(verbose_name="Текст сообщения для пункта 3.2", blank=False, null=True)
    item3_2_reference = models.TextField(verbose_name="Ссылка для пункта 3.2", blank=True, null=True)
    item3_2_document = models.FileField(upload_to='documents', verbose_name="Загрузка документа для пункта 3.2",
                                        blank=True, null=True)
    item3_2_document_reserve = models.FileField(upload_to='documents', blank=True, null=True,
                                                verbose_name="Загрузка документа для пункта 3.2")

    class Meta:
        verbose_name = "Пункт 3.2 Открытие счетов"
        verbose_name_plural = "Пункт 3.2 Открытие счетов"

    def __str__(self):
        return f"{self.item3_2_message, self.item3_2_reference}"


@receiver(pre_delete, sender=OpenAccount3_2)
def delete_document(sender, instance, **kwargs):
    if instance.item3_2_document or instance.item3_2_document_reserve:
        if os.path.isfile(instance.item3_2_document.path):
            os.remove(instance.item3_2_document.path)
        elif os.path.isfile(instance.item3_2_document_reserve.path):
            os.remove(instance.item3_2_document_reserve.path)


class GoToChat(models.Model):
    message = models.TextField(verbose_name="Текст сообщения для пункта 4", blank=False, null=True)
    reference = models.TextField(verbose_name="Ссылка для пункта 4", blank=True, null=True)

    class Meta:
        verbose_name = "Пункт Переход в чат"
        verbose_name_plural = "Пункт Переход в чат"

    def __str__(self):
        return f"{self.reference} - {self.message}"


class USDT(models.Model):
    message = models.TextField(verbose_name="Текст сообщения для пункта 5", blank=False, null=True)
    reference = models.TextField(verbose_name="Ссылка для пункта 5", blank=True, null=True)

    class Meta:
        verbose_name = "Пункт Перестановка USDT"
        verbose_name_plural = "Пункт Перестановка USDT"

    def __str__(self):
        return f"{self.reference} - {self.message}"
