from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_CONVERSION = 1.60934
class ConvertMilesToKilometersApp(App):

    message = StringProperty()

    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in the field and press enter"
        return self.root

    def handle_convert(self):
        miles = self.get_validated_miles()
        km = miles * MILE_CONVERSION
        self.root.ids.output_label.text = str(km)

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, change):
        new_km_value = self.get_validated_miles() + change
        self.root.ids.input_number.text = str(new_km_value)
        self.handle_convert()


ConvertMilesToKilometersApp().run()

