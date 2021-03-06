# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-22 09:46


from django.db import migrations

from ecommerce.extensions.catalogue.utils import create_subcategories

COUPON_CATEGORY_NAME = 'Coupons'

EDX_EMPLOYEE_COUPON_CATEGORY = 'edX Employee Request'


def create_edx_employee_category(apps, schema_editor):
    """Create edX employee coupon category."""
    Category = apps.get_model("catalogue", "Category")

    Category.skip_history_when_saving = True
    create_subcategories(Category, COUPON_CATEGORY_NAME, [EDX_EMPLOYEE_COUPON_CATEGORY, ])


def remove_edx_employee_category(apps, schema_editor):
    """Remove edX employee coupon category."""
    Category = apps.get_model("catalogue", "Category")

    Category.skip_history_when_saving = True
    Category.objects.get(
        name=COUPON_CATEGORY_NAME
    ).get_children().filter(
        name=EDX_EMPLOYEE_COUPON_CATEGORY
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('catalogue', '0044_add_enterprisecontractmetadata_product_attribute'),
    ]

    operations = [
        migrations.RunPython(create_edx_employee_category, remove_edx_employee_category)
    ]
