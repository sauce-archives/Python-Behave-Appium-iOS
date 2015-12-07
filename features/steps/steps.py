import os
from appium import webdriver

@given('we input values 8 and 12 into the fields')
def step_impl(context):
  field_one = context.driver.find_element_by_accessibility_id("TextField1")
  field_one.send_keys("12")

  field_two = context.driver.find_elements_by_class_name("UIATextField")[1]
  field_two.send_keys("8")

@when('we click the submit button')
def step_impl(context):
  button = context.driver.find_element_by_accessibility_id("ComputeSumButton")
  button.click()

@then('the value should equal 20')
def step_impl(context):
  sum = context.driver.find_element_by_class_name("UIAStaticText").text
  assert int(sum) == 20, "ERROR MESSAGE"
