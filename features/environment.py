import os
from appium import webdriver
from sauceclient import SauceClient

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
url = 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key)

def before_scenario(context, scenario):
  context.name = scenario.name

  desired_caps = {
    "name": context.name,
    "app": "https://s3.amazonaws.com/appium/TestApp8.4.app.zip",
    "platformName": "iOS",
    "deviceName": os.environ.get('deviceName'),
    "browserName": "",
    "platformVersion": "8.4",
    "appiumVersion": "1.4.11",
    "deviceOrientation": "portrait"
  }
  
  context.driver = webdriver.Remote(url, desired_caps)

def after_scenario(context, scenario):
  if hasattr(context, 'driver'):
    context.driver.quit()
    sauce_client = SauceClient(username, access_key)
    test_status = scenario.status == 'passed'
    sauce_client.jobs.update_job(context.driver.session_id, passed = test_status)
    