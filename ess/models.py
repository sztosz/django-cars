from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Chassis(models.Model):
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}/{}".format(self.brand.name, self.name)


class Engine(models.Model):
    chassis = models.ForeignKey(Chassis)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}/{}/{}".format(self.chassis.brand.name, self.chassis.name, self.name)


class ECU(models.Model):
    car_model = models.ForeignKey(Engine)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}/{}/{}/{}".format(self.car_model.chassis.brand.name, self.car_model.chassis.name, self.car_model.name,
                                    self.name)


class Modification(models.Model):
    ecu = models.ManyToManyField(ECU)
    name = models.CharField(max_length=50)
    script = models.TextField()

    def __str__(self):
        return self.name
