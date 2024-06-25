from django.contrib import admin
from .models import GoToChat, KazahstanCart1_2, KazahstanCart1_3, USDT, OpenAccount3_1, OpenAccount3_2, Deposited


@admin.register(KazahstanCart1_3)
class KazahstanCardAdmin(admin.ModelAdmin):
    pass


@admin.register(KazahstanCart1_2)
class KazahstanCardAdmin(admin.ModelAdmin):
    pass


@admin.register(USDT)
class USDTAdmin(admin.ModelAdmin):
    pass


@admin.register(OpenAccount3_1)
class OpenAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(OpenAccount3_2)
class OpenAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Deposited)
class DepositedAdmin(admin.ModelAdmin):
    pass


@admin.register(GoToChat)
class GoToChatAdmin(admin.ModelAdmin):
    pass
