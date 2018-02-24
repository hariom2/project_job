# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# To make string auto slag
from autoslug import AutoSlugField
# Use for translation
from django.utils.translation import ugettext_lazy as _


class Battles(models.Model):
    name = models.CharField(
        max_length=52,
        help_text=_("Enter Battle Name"),
        null=True,
        blank=True
    )
    year = models.IntegerField(
        max_length=3,
        help_text=_("Enter Year"),
        null=True,
        blank=True
    )
    attacker_king = models.CharField(
        max_length=24,
        help_text=_("Enter attacker king"),
        null=True,
        blank=True
    )
    defender_king = models.CharField(
        max_length=24,
        help_text=_("Enter defender king"),
        null=True,
        blank=True
    )
    attacker_1 = models.CharField(
        max_length=27,
        help_text=_("Enter attacker 1"),
        null=True,
        blank=True
    )
    attacker_2 = models.CharField(
        max_length=9,
        help_text=_("Enter attacker 2"),
        null=True,
        blank=True
    )
    attacker_3 = models.CharField(
        max_length=7,
        help_text=_("Enter attacker 3"),
        null=True,
        blank=True
    )
    attacker_4 = models.CharField(
        max_length=6,
        help_text=_("Enter attacker 4"),
        null=True,
        blank=True
    )
    defender_1 = models.CharField(
        max_length=16,
        help_text=_("Enter defender_1"),
        null=True,
        blank=True
    )
    defender_2 = models.CharField(
        max_length=9,
        help_text=_("Enter defender_2"),
        null=True,
        blank=True
    )
    defender_3 = models.CharField(
        max_length=10,
        help_text=_("Enter defender 3"),
        null=True,
        blank=True
    )
    defender_4 = models.CharField(
        max_length=10,
        help_text=_("defender 4"),
        null=True,
        blank=True
    )
    attacker_outcome = models.CharField(
        max_length=4,
        help_text=_("Enter attacker outcome"),
        null=True,
        blank=True
    )
    battle_type = models.CharField(
        max_length=14,
        help_text=_("Enter battle type"),
        null=True,
        blank=True
    )
    major_death = models.IntegerField(
        max_length=1,
        help_text=_("Enter major death"),
        null=True,
        blank=True
    )
    major_capture = models.IntegerField(
        max_length=1,
        help_text=_("Enter major_capture"),
        null=True,
        blank=True
    )
    attacker_size = models.CharField(
        max_length=6,
        help_text=_("Enter attacker size"),
        null=True,
        blank=True
    )
    defender_size = models.CharField(
        max_length=5,
        help_text=_("Enter defender_size"),
        null=True,
        blank=True
    )
    attacker_commander = models.CharField(
        max_length=95,
        help_text=_("Enter attacker commander"),
        null=True,
        blank=True
    )
    defender_commander = models.CharField(
        max_length=109,
        help_text=_("Enter defender commander"),
        null=True,
        blank=True
    )
    summer = models.CharField(
        max_length=1,
        help_text=_("Enter summer"),
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=36,
        help_text=_("Enter location"),
        null=True,
        blank=True
    )
    region = models.CharField(
        max_length=15,
        help_text=_("Enter Battle Name"),
        null=True,
        blank=True
    )
    note = models.CharField(
        max_length=257,
        help_text=_("Enter note"),
        null=True,
        blank=True
    )


    def __str__(self):
        """Method to return object name in string."""
        return self.name

class King(models.Model):
    name = models.CharField(
        max_length=30,
        help_text=_("Enter King Name"),
        null=True,
        blank=True
    )
    slug = AutoSlugField(
        populate_from='name',
        unique=True,
        null=True
    )
    rating = models.FloatField(
        default=400,
    )

