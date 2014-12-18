# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Country.name'
        db.alter_column('region_country', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))
        # Removing index on 'Country', fields ['name']
        db.delete_index('region_country', ['name'])

        # Adding unique constraint on 'Country', fields ['slug']
        db.create_unique('region_country', ['slug'])

        # Adding unique constraint on 'City', fields ['slug']
        db.create_unique('region_city', ['slug'])


        # Changing field 'City.name'
        db.alter_column('region_city', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))
        # Removing index on 'City', fields ['name']
        db.delete_index('region_city', ['name'])


    def backwards(self, orm):
        # Adding index on 'City', fields ['name']
        db.create_index('region_city', ['name'])

        # Removing unique constraint on 'City', fields ['slug']
        db.delete_unique('region_city', ['slug'])

        # Removing unique constraint on 'Country', fields ['slug']
        db.delete_unique('region_country', ['slug'])

        # Adding index on 'Country', fields ['name']
        db.create_index('region_country', ['name'])


        # Changing field 'Country.name'
        db.alter_column('region_country', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'City.name'
        db.alter_column('region_city', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        'region.city': {
            'Meta': {'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['region.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True', 'unique': 'True'})
        },
        'region.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True', 'unique': 'True'})
        }
    }

    complete_apps = ['region']