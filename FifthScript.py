def test_05_AddItemsToCartWorks(self):
		"Test to make sure that the user can add items to the cart."
		self.browser.get("http://www.ebay.com")
		search_entry = self.browser.find_element_by_name("_nkw")
		search_entry.clear()
		search_entry.send_keys("iphone")
		search_entry.send_keys(Keys.RETURN)
		link = self.browser.find_element_by_link_text('iphone 7')
		link.click()
		self.browser.find_element_by_id("isCartBtn_btn").click()
		sleep(60)
		self.assertTrue("No results found." not in self.browser.page_source)