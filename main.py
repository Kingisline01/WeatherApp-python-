import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import requests
from geopy.geocoders import Nominatim

class WeatherApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.location_label = Label(text='Enter Location:')
        self.layout.add_widget(self.location_label)
        
        self.location_input = TextInput(hint_text='City, Country', multiline=False)
        self.layout.add_widget(self.location_input)
        
        self.get_weather_button = Button(text='Get Weather')
        self.get_weather_button.bind(on_press=self.get_weather)
        self.layout.add_widget(self.get_weather_button)
        
        self.weather_info = Label(text='')
        self.layout.add_widget(self.weather_info)
        
        return self.layout

    def get_weather(self, instance):
        location = self.location_input.text
        if location:
            try:
                geolocator = Nominatim(user_agent="weather_app")
                location = geolocator.geocode(location)
                
                if location:
                    lat, lon = location.latitude, location.longitude
                    api_key = '428824a4797c407f93e123408242406'  # Replace with your actual WeatherAPI key
                    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}'
                    
                    response = requests.get(url)
                    print(f"Response Status Code: {response.status_code}")  # Debugging info
                    print(f"Response Data: {response.json()}")  # Debugging info
                    
                    if response.status_code == 200:
                        weather_data = response.json()
                        temp = weather_data['current']['temp_c']
                        description = weather_data['current']['condition']['text']
                        self.weather_info.text = f"Temperature: {temp}°C\nDescription: {description.capitalize()}"
                    elif response.status_code == 401:
                        self.weather_info.text = "Invalid API key."
                    else:
                        self.weather_info.text = f"Could not retrieve weather data. Status code: {response.status_code}"
                else:
                    self.weather_info.text = "Location not found."
            except Exception as e:
                self.weather_info.text = f"An error occurred: {e}"
        else:
            self.weather_info.text = "Please enter a location."

if __name__ == '__main__':
    WeatherApp().run()
