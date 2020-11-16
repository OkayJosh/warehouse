import datetime
from django.utils.timezone import now
from rest_framework import serializers
from django.test import TestCase, override_settings

from .models import Inflow, Outflow
from .serializers import InflowSerializer, OutflowSerializer

from rest_framework.viewsets import ModelViewSet
from collections import OrderedDict
from functools import wraps




from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter
from rest_framework.test import APIRequestFactory

# from .views import LeadViewSet
factory = APIRequestFactory()

class InflowModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Inflow.objects.create( name ='beer', quantity='11', comment='First batch of delivery')

    def test_name_label(self):
        inflow = Inflow.objects.get(id=1)
        field_label = inflow._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_quantity_label(self):
        inflow=Inflow.objects.get(id=1)
        field_label = inflow._meta.get_field('quantity').verbose_name
        self.assertEqual(field_label, 'quantity')

    def test_name_max_length(self):
        inflow = Inflow.objects.get(id=1)
        max_length = inflow._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name_comma_qunatity(self):
        inflow = Inflow.objects.get(id=1)
        expected_object_name = f'{inflow.name}, {inflow.quantity}'
        self.assertEqual(expected_object_name, str(inflow))

class OutFlowModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Outflow.objects.create( name ='beer', quantity='11', comment='Eastern-Retail Limited')

    def test_name_label(self):
        outflow = Outflow.objects.get(id=1)
        field_label = outflow._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_quantity_label(self):
        outflow = Outflow.objects.get(id=1)
        field_label = outflow._meta.get_field('quantity').verbose_name
        self.assertEqual(field_label, 'quantity')

    def test_name_max_length(self):
        outflow = Outflow.objects.get(id=1)
        max_length = outflow._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name_comma_quantity(self):
        outflow = Outflow.objects.get(id=1)
        expected_object_name = f'{outflow.name}, {outflow.quantity}'
        self.assertEqual(expected_object_name, str(outflow))

# Serializer Tests
class InflowSerializerTests(TestCase):
    #Set up non-modified objects used by all test methods
    def setUp(self):
        self.inflow_attributes = {
            'name': 'beer',
            'quantity': int(511),
            'comment': 'Third Batch'
        }

        self.serializer_data = {
            'name': 'beer',
            'quantity': '511',
            'comment': 'Third Batch'
        }

        self.inflow = Inflow.objects.create(**self.inflow_attributes)
        self.serializer = InflowSerializer(instance=self.inflow)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'quantity', 'comment']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.inflow_attributes['name'])

    def test_quantity_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['quantity'], self.inflow_attributes['quantity'])

    def test_comment_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['comment'], self.inflow_attributes['comment'])


class OutflowSerializerTests(TestCase):
    #Set up non-modified objects used by all test methods
    def setUp(self):
        self.outflow_attributes = {
            'name': 'beer',
            'quantity': int(511),
            'comment': 'Third Batch'
        }

        self.serializer_data = {
            'name': 'beer',
            'quantity': '511',
            'comment': 'Third Batch'
        }

        self.outflow = Outflow.objects.create(**self.outflow_attributes)
        self.serializer = OutflowSerializer(instance=self.outflow)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'quantity', 'comment']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.outflow_attributes['name'])

    def test_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['quantity'], self.outflow_attributes['quantity'])

    def test_comment_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['comment'], self.outflow_attributes['comment'])
