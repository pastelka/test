"""Test cteni xml dat"""
import requests
import xml.etree.ElementTree as ET

response = requests.get("http://10.1.2.11/XMLstatus", timeout=30)
root = ET.fromstring(response.text)
print(root.find('.//WaterTankVolume').text)
print(root.find('.//TemperatureOut').text)
