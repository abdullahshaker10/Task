from django.db import models


MACHINE_CHOICES = (
    ('Large machine', 'Large machine'),
    ('Small machine', 'Small machine'),
    ('Espresso machine,', 'Espresso machine,')
)

PODS_CHOICES = (
    ('Large coffe pod', 'Large coffe pod'),
    ('Small coffe pod', 'Small coffe pod'),
    ('Espresso pod,', 'Espresso pod,')
)

COFFE_FLAVOR = (
    ('Vanilla', 'Vanilla'),
    ('Caramel', 'Caramel'),
    ('psl', 'psl'),
    ('Mocha', 'Mocha'),
    ('Hazelnut', 'Hazelnut')
)

PACK_SIZE = (
    ('1 dozen ', '1 dozen '),
    ('3 dozen ', '3 dozen '),
    ('5 dozen ', '5 dozen '),
    ('7 dozen ', '7 dozen ')
)

MODEL = (
    ('base model', 'base model'),
    ('premium model', 'premium model'),
    ('deluxe model', 'deluxe model,')
)


class CoffeMachine(models.Model):
    product_type = models.CharField(max_length=100, choices=MACHINE_CHOICES)
    model = models.CharField(max_length=100, choices=MODEL)
    water_line_compatible = models.BooleanField()


class CoffePods(models.Model):
    product_type = models.CharField(max_length=200, choices=PODS_CHOICES)
    coffe_flavor = models.CharField(max_length=100, choices=COFFE_FLAVOR)
    pack_size = models.CharField(max_length=100, choices=PACK_SIZE)
