from django.contrib import admin

from .models import (Point,
                     Detail,
                     Feature,
                     Item,
                     Category,
                     SubGroup,
                     Group,
                     SubProperty,
                     Property,
                     Organization
                     )


admin.site.register(Point)
admin.site.register(Detail)
admin.site.register(Feature)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(SubGroup)
admin.site.register(Group)
admin.site.register(SubProperty)
admin.site.register(Property)
admin.site.register(Organization)