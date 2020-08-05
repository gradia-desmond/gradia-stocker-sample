from selenium.webdriver.support.ui import Select


def test_data_entry_can_split_parcel_to_stones(browser, data_entry_clerk, grader, receipt):
    # Yuki is a data entry clerk
    # there is a parcel that a grader has finished grading and has returned to
    # the vault
    parcel = receipt.parcel_set.first()

    # she logs in to the admin portal
    browser.login(data_entry_clerk.username, data_entry_clerk.raw_password)

    # she goes to add a split
    parcel_link = browser.find_element_by_link_text("Splits")
    browser.slowly_click(parcel_link)
    browser.click_add()

    # she selects the correct parcel to split on
    parcel_dropdown = Select(browser.find_element_by_id("id_original_parcel"))
    parcel_dropdown.select_by_visible_text(str(parcel))

    add_link = browser.find_element_by_link_text("Add another Stone")

    # she adds 50 stones
    for ii in range(50):
        add_link.click()
        grader_dropdown = Select(browser.find_element_by_name(f"stone_set-{ii}-grader_1"))
        grader_dropdown.select_by_visible_text(str(grader))
        browser.find_element_by_name(f"stone_set-{ii}-sequence_number").send_keys("23")
        browser.find_element_by_name(f"stone_set-{ii}-stone_id").send_keys("G12345")
        browser.find_element_by_name(f"stone_set-{ii}-carats").send_keys("2")
        browser.find_element_by_name(f"stone_set-{ii}-color").send_keys("D")
        browser.find_element_by_name(f"stone_set-{ii}-clarity").send_keys("VS2")
        browser.find_element_by_name(f"stone_set-{ii}-fluo").send_keys("a")
        browser.find_element_by_name(f"stone_set-{ii}-culet").send_keys("x")
        browser.find_element_by_name(f"stone_set-{ii}-table_pct").send_keys("10.1")
        browser.find_element_by_name(f"stone_set-{ii}-pavilion_depth_pct").send_keys("10.1")
        browser.find_element_by_name(f"stone_set-{ii}-total_depth_pct").send_keys("10.1")


    # the add link disappears because 50 stones is the limit
    assert not add_link.is_displayed()

    # she saves
    browser.click_save()

    # now the parcel does not show up by default
    browser.go_to_parcel_page()
    browser.assert_body_contains_text(f"0 parcels")

    # but shows up as having been split
    browser.slowly_click(browser.find_element_by_link_text("Including splits and exited"))
    browser.assert_body_contains_text(f"1 parcel")
    browser.assert_body_contains_text(f"split, unconfirmed")
    # it also shows that the parcel has been split into 50 stones
    browser.assert_body_contains_text(f"50 stones")

    # and we can see stones in the vault
    browser.go_to_stone_page()
    browser.assert_body_contains_text(f"vault, confirmed")
    browser.assert_body_contains_text(f"50 stones")
    # the stones show up as having been split from the correct parcel
    assert len(browser.find_elements_by_link_text(str(parcel))) == 50
