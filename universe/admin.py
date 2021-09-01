from django.contrib import admin
from universe.models import (
    Galaxy,
    StarSystem,
    Star,
    Planet,

)
# Register your models here.
@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    pass


@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin):
    pass


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass


