# Generated by Django 4.1 on 2022-08-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Product", "0001_initial"),
        ("Customer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("transaction_id", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField(max_length=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Customer.customer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Product.product",
                    ),
                ),
            ],
        ),
    ]
