# Generated by Django 3.0.8 on 2020-07-06 18:01
import uuid

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import magic_link.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MagicLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "token",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique login token",
                        unique=True,
                    ),
                ),
                (
                    "redirect_to",
                    models.CharField(
                        default="/",
                        help_text="URL to which user will be redirected after logging in. ('/')",
                        max_length=255,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="When the link was originally created",
                    ),
                ),
                (
                    "expires_at",
                    models.DateTimeField(
                        default=magic_link.models.link_expires_at,
                        help_text="When the link is due to expire (uses DEFAULT_EXPIRY)",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Set to False to deactivate the token"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="magic_links",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MagicLinkUse",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="When the token page was requested",
                    ),
                ),
                ("http_method", models.CharField(max_length=10)),
                (
                    "session_key",
                    models.CharField(
                        blank=True,
                        help_text="The request session identifier",
                        max_length=40,
                    ),
                ),
                (
                    "remote_addr",
                    models.CharField(
                        blank=True,
                        help_text="The client IP address, extracted from HttpRequest",
                        max_length=100,
                    ),
                ),
                (
                    "ua_string",
                    models.TextField(
                        blank=True,
                        help_text="The client User-Agent, extracted from HttpRequest headers",
                    ),
                ),
                (
                    "link_is_valid",
                    models.BooleanField(
                        default=True,
                        help_text="Snapshot of parent link is_valid property at the time of use",
                    ),
                ),
                (
                    "error",
                    models.CharField(
                        blank=True,
                        help_text="If the link use failed the error will be recorded here",
                        max_length=100,
                    ),
                ),
                (
                    "link",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="magic_link.MagicLink",
                    ),
                ),
            ],
            options={
                "get_latest_by": ("timestamp",),
            },
        ),
    ]
