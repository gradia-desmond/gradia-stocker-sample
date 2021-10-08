import os
import re


def test_user_can_upload_gia_if_valid_csv_file(browser, data_entry_clerk, tanly, gary, kary, initial_stones):
    browser.login(username=data_entry_clerk.username, password=data_entry_clerk.raw_password)

    browser.find_element_by_link_text("Splits").click()
    browser.find_element_by_link_text("UPLOAD STONE DATA").click()

    browser.find_element_by_link_text("Goldway Adjust Stone Data").click()

    os.chdir("../django_backend")
    gw_csv_file_path = os.path.join(os.getcwd(), "grading/tests/fixtures/gw_adjust.csv")
    upload_file_input = browser.find_element_by_name("file")
    upload_file_input.send_keys(gw_csv_file_path)

    browser.find_element_by_name("_upload").click()

    assert re.match(r"^http://localhost:\d+/admin/grading/split/\d+/change/", browser.current_url) is not None


def test_user_can_upload_gia_if_invalid_csv_file(browser, data_entry_clerk, tanly, gary, kary, initial_stones):
    browser.login(username=data_entry_clerk.username, password=data_entry_clerk.raw_password)

    browser.find_element_by_link_text("Splits").click()
    browser.find_element_by_link_text("UPLOAD STONE DATA").click()

    browser.find_element_by_link_text("Goldway Adjust Stone Data").click()

    os.chdir("../django_backend")
    gia_csv_file_path = os.path.join(os.getcwd(), "grading/tests/fixtures/gw_adjust_invalid.csv")
    upload_file_input = browser.find_element_by_name("file")
    upload_file_input.send_keys(gia_csv_file_path)

    browser.find_element_by_name("_upload").click()

    assert re.match(r"^http://localhost:\d+/grading/gw_grading_data_upload_url/", browser.current_url) is not None
    browser.assert_body_contains_text("Data Upload Failed")
    # import pdb; pdb.set_trace()

    browser.assert_body_contains_text("Grader user `foo` account does not exist")  # Some error message