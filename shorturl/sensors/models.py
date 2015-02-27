from django.db import models


class SensorData(models.Model):
    sensor = models.CharField(max_length=250)
    value = models.FloatField()

    @classmethod
    def create_sensor(self, sensor, value):
        """
            Register and return new SensorData.
        """
        
        sensor_data = SensorData(sensor=sensor, value=value)
        sensor_data.save();
        return sensor_data;
