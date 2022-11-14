class Converter:
    def __init__(self, distance, measurement):
        self.distance = distance
        self.measurement = measurement

    def get_factorial(self, measurement):
        # metric based of centimeters
        meter_measures = {
            'millimeters': 1000,
            'centimeters': 100,
            'meters': 1,
            'kilometers': 0.001,
            'inches': 39.37007871,
            'feet': 3.28083991,
            'yards': 1.09361331,
            'miles': 0.0006213711921
        }

        return meter_measures.get(measurement)

    def millimeters(self):
        factorial = self.get_factorial('millimeters')
        return (self.distance / self.get_factorial(self.measurement)) * factorial

    def centimeters(self):
        factorial = self.get_factorial('centimeters')
        return (self.distance / self.get_factorial(self.measurement)) * factorial

    def meters(self):
        # the measurement object is necessary for converting
        factorial = self.get_factorial('meters')
        return (self.distance / self.get_factorial(self.measurement)) * factorial

    def kilometers(self):
        factorial = self.get_factorial('kilometers')
        return (self.distance / self.get_factorial(self.measurement)) * factorial

    def inches(self):
        factorial = self.get_factorial('inches')
        return (self.distance / self.get_factorial(self.measurement)) * factorial

    def feet(self):
        factorial = self.get_factorial('feet')
        return (self.distance / self.get_factorial(self.measurement)) * factorial

    def yards(self):
        factorial = self.get_factorial('yards')
        return (self.distance / self.get_factorial(self.measurement)) * factorial

    def miles(self):
        factorial = self.get_factorial('miles')
        return (self.distance / self.get_factorial(self.measurement)) * factorial
