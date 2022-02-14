#TODO
# Test Setup
test_value = 'it worked'

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_into_input(test_value)
# trng_page.click_button_1()
txt_from_input = trng_page.get_input_text()
assert txt_from_input == test_value, f"Test Failed: Input did not match expected {test_value}."
print("Test Passed.")
browser.quit()
