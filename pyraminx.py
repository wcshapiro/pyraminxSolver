import main

class Pyraminx:
    def __init__(self):
      self.masterPyraminx = [
        [
            ['R00'],
            ['R10', 'R11', 'R12'],
            ['R20', 'R21', 'R22', 'R23', 'R24'],
            ['R30', 'R31', 'R32', 'R33', 'R34', 'R35', 'R36'], ],  # front

        [
            ['Y00'],
            ['Y10', 'Y11', 'Y12'],
            ['Y20', 'Y21', 'Y22', 'Y23', 'Y24'],
            ['Y30', 'Y31', 'Y32', 'Y33', 'Y34', 'Y35', 'Y36'], ],  # right front corner

        [
            ['G00'],
            ['G10', 'G11', 'G12'],
            ['G20', 'G21', 'G22', 'G23', 'G24'],
            ['G30', 'G31', 'G32', 'G33', 'G34', 'G35', 'G36'], ],  # left front corner


        [['B00', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06'],  # bottom front row
         ['B10', 'B11', 'B12', 'B13', 'B14'],
         ['B20', 'B21', 'B22'],
         ['B30']]]