# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sousdirection(models.Model):

    #__Sousdirection_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    iddir = models.TextField(max_length=255, null=True, blank=True)
    nom = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Sousdirection_FIELDS__END

    class Meta:
        verbose_name        = _("Sousdirection")
        verbose_name_plural = _("Sousdirection")


class Direction(models.Model):

    #__Direction_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    nom = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Direction_FIELDS__END

    class Meta:
        verbose_name        = _("Direction")
        verbose_name_plural = _("Direction")


class Service(models.Model):

    #__Service_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    nom = models.TextField(max_length=255, null=True, blank=True)
    descrption = models.TextField(max_length=255, null=True, blank=True)

    #__Service_FIELDS__END

    class Meta:
        verbose_name        = _("Service")
        verbose_name_plural = _("Service")


class Bureau(models.Model):

    #__Bureau_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    nom = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Bureau_FIELDS__END

    class Meta:
        verbose_name        = _("Bureau")
        verbose_name_plural = _("Bureau")


class Utilisateurs(models.Model):

    #__Utilisateurs_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    nom = models.TextField(max_length=255, null=True, blank=True)
    postnom = models.TextField(max_length=255, null=True, blank=True)
    prenom = models.TextField(max_length=255, null=True, blank=True)
    pwd = models.TextField(max_length=255, null=True, blank=True)
    role = models.TextField(max_length=255, null=True, blank=True)
    idafectation = models.CharField(max_length=255, null=True, blank=True)

    #__Utilisateurs_FIELDS__END

    class Meta:
        verbose_name        = _("Utilisateurs")
        verbose_name_plural = _("Utilisateurs")


class Ticket(models.Model):

    #__Ticket_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    titre = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    priorite = models.TextField(max_length=255, null=True, blank=True)
    statut = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    iddemandeur = models.CharField(max_length=255, null=True, blank=True)
    idintervenant = models.CharField(max_length=255, null=True, blank=True)
    typeticket = models.CharField(max_length=255, null=True, blank=True)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")


class Fichemateriel(models.Model):

    #__Fichemateriel_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    nom = models.TextField(max_length=255, null=True, blank=True)
    typemateriel = models.TextField(max_length=255, null=True, blank=True)
    marque = models.TextField(max_length=255, null=True, blank=True)
    model = models.TextField(max_length=255, null=True, blank=True)
    numserie = models.TextField(max_length=255, null=True, blank=True)
    autresinfo = models.TextField(max_length=255, null=True, blank=True)
    idaffectation = models.TextField(max_length=255, null=True, blank=True)
    etat = models.TextField(max_length=255, null=True, blank=True)

    #__Fichemateriel_FIELDS__END

    class Meta:
        verbose_name        = _("Fichemateriel")
        verbose_name_plural = _("Fichemateriel")



#__MODELS__END
