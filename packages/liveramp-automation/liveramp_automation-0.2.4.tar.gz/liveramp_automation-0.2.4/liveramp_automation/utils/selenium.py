import os
from urllib.parse import urlparse, urlunsplit
from liveramp_automation.helpers.file import FileHelper
from liveramp_automation.helpers.login import LoginHepler
from liveramp_automation.utils.log import Logger
from liveramp_automation.utils.time import MACROS, fixed_wait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, JavascriptException, NoSuchElementException


class SeleniumUtils:

    def __int__(self, driver):
        self.driver = driver

    def navigate_url(self, scheme=None, host_name=None, path=None, query=None):
        """ Navigate to the provided URL.

        :param scheme:
        :param host_name:
        :param path:
        :param query:
        :return:
        """
        parsed_uri = urlparse(self.driver.url)
        self.driver.get(urlunsplit((parsed_uri.scheme if scheme is None else scheme,
                                    parsed_uri.hostname if host_name is None else host_name,
                                    parsed_uri.path if path is None else path,
                                    parsed_uri.query if query is None else query,
                                    '')))

    def save_screenshot(self, name):
        """ Save a screenshot to the specified destination.

        :param name:
        :return:
        """
        data_dict = FileHelper.read_init_file(" /", "pytest.ini", "r")
        file_path = data_dict.get('screenshot', "reports/")
        name = file_path + "/{}_{}.png".format(MACROS["now"], name)
        self.driver.save_screenshot(os.path.join(path=name))

    def get_url(self, url):
        """ Open the page using the provided URL.

        :param url:
        :return:
        """
        self.driver.get(url)

    def find_element_by_dict(self, dictionary, timeout=5):
        """ Retrieve the first element that matches the criteria specified in the dictionary.

        :param dictionary:
        :param delay:
        :return:
        """
        by_type = (next(iter(dictionary)))
        locator = dictionary.get(by_type)
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by_type, locator)))
        except TimeoutException:
            Logger.info("element {} was not found".format(locator))
            return None

    def find_elements_by_dict(self, dictionary, timeout=3):
        """Search for all elements that match the criteria specified in the dictionary.

        :param dictionary:
        :param timeout:
        :return:
        """
        by_type = (next(iter(dictionary)))
        locator = dictionary.get(by_type)
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((by_type, locator)))
        except TimeoutException:
            Logger.info("element {} was not found".format(locator))

    def find_element(self, by_type, locator, timeout=3):
        """ Locate the first element and wait for it to load within the specified maximum timeout time.

        :param by_type:
        :param locator:
        :param timeout:
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by_type, locator)))
        except TimeoutException:
            Logger.info("element {} was not found".format(locator))
            return None

    def find_element_by_css(self, locator, by_type=By.CSS_SELECTOR, timeout=3):
        """ Search for the first element using the CSS_SELECTOR with the implementation of Explicit Waits.

        :param locator:
        :param by_type:
        :param timeout:
        :return:
        """
        return self.find_element(self.driver, by_type, locator, timeout)

    def find_elements(self, by_type, locator, timeout=3):
        """Find multiple elements and wait for them to load within the specified maximum timeout time.

        :param by_type:
        :param locator:
        :param timeout:
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((by_type, locator)))
        except TimeoutException:
            Logger.info("element {} was not found".format(locator))

    def find_elements_by_css(self, locator, by_type=By.CSS_SELECTOR, timeout=3):
        """Search all elements using the CSS_SELECTOR with the implementation of Explicit Waits.

        :param by_type:
        :param locator:
        :param timeout:
        :return:
        """
        return self.find_elements(self.driver, by_type, locator, timeout)

    def count_elements(self, by_type, locator, timeout=5):
        """Obtain the count of matching elements within the specified maximum timeout duration.

        :param by_type:
        :param locator:
        :param timeout:
        :return:
        """
        try:
            return len(
                WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by_type, locator))))
        except TimeoutException:
            TimeoutException('element was not found: {}'.format(locator))
        return 0

    def is_element_clickable(self, by_type, locator, timeout=3):
        """ Retrieve the clickable status of the element within the specified maximum timeout period.

        :param by_type:
        :param locator:
        :param timeout:
        :return:
        """
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by_type, locator)))

    def is_element_enabled(self, by_type, locator, timeout=3):
        """ Return the status of the element within the specified maximum timeout time.

        :param by_type:
        :param locator:
        :param timeout:
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by_type, locator))).is_enabled()
        except TimeoutException:
            raise Exception("element {} was not found".format(locator))

    def get_index_elements(self, by_type, locator, timeout):
        """ Retrieve the index and a list of elements based on the provided locator.

        :param by_type:
        :param locator:
        :param timeout:
        :return:  [(0, ele1), (1, ele2)]
        """
        elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by_type, locator)))
        if elements:
            return [(index, element) for index, element in enumerate(elements)]
        else:
            return []

    def get_text_index_elements(self, text, by_type, locator, timeout=3):
        """ Obtain a list of index_element based on the provided text that matches the text of the locator.

        :param text:
        :param by_type:
        :param locator:
        :param timeout:
        :return:  [(0, ele1), (1, ele2)]  element contains text
        """
        index_elements = self.get_index_elements(self.driver, by_type, locator, timeout)
        if index_elements:
            return [index_element for index_element in index_elements if text in index_element[1].text]
        else:
            Logger.info("No elements were found that match the provided text in the locator.")
            return []

    def is_text_found(self, text, by_type, locator, timeout=5):
        """ Return a boolean value based on the presence of the identified text.

        :param text:
        :param by_type:
        :param locator:
        :param timeout:
        :return:
        """
        if self.get_text_index_elements(self.driver, text, by_type, locator, timeout):
            return True
        else:
            return False

    def click(self, by_type, locator, delay=2, timeout=5):
        """ click method: if the page could be scrolldown, will scroll the page to the element
        This is done to ensure that the element is visible on the screen before attempting to click it.

        :param by_type:
        :param locator:
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by_type, locator)))
        except TimeoutException:
            Logger.info('Element was not clickable: {}'.format(locator))
        el = self.find_element(self.driver, by_type, locator)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", el)
            el.click()
            return
        except JavascriptException:
            fixed_wait(delay)
            Logger.info("Couldn't execute javascript: scrollIntoView() for element: {str(el)} locator: {locator}")
        el = self.find_element(self.driver, by_type, locator)
        el.click()
        Logger.info("Element found and clicked.")

    def click_text(self, text, by_type, locator, timeout=3, index=0):
        """Retrieve a list of index_element based on the provided text that matches the text of the locator,
        then click the element corresponding to the provided index.

        :param text:
        :param by_type:
        :param locator:
        :param timeout:
        :return:
        """
        for obj in self.get_text_index_elements(self.driver, text, by_type, locator, timeout):
            obj[index].click()

    def hover_element_and_click(self, element, by_type=None, locator=None, index=0):
        """Hover over the element at index+1 and then click it.

        :param element:
        :param by_type:
        :param locator:
        :param index:
        :return:
        """
        if by_type and locator:
            ActionChains(self.driver).move_to_element(element).perform()
            self.find_elements(self.driver, by_type, locator)[index].click()
        else:
            ActionChains(self.driver).move_to_element(element).click(element).perform()

    def hover_text_and_click(self, text, by_type, locator, click_type=None, click_locator=None, index=0,
                             timeout=7):
        """Retrieve a list of index_element based on the provided text that matches the text of the locator.
        Then, hover over and click the element at index+1.

        :param text:
        :param by_type:
        :param locator:
        :param click_type:
        :param click_locator:
        :param index:
        :param timeout:
        :return:
        """
        index_elements = self.get_text_index_elements(self.driver, text, by_type, locator, timeout)
        if index_elements:
            for index_ele in index_elements:
                self.hover_element_and_click(self.driver, index_ele[index], click_type, click_locator, index)
                break
        else:
            raise NoSuchElementException('locator: {}'.format(locator))

    def drag_and_drop(self, source_element, target_element):
        """Perform a drag-and-drop action from the source element to the target element.

        :param source_element:
        :param target_element:
        :return:
        """
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def click_by_dict(self, dictionary):
        """ Click the element using a dictionary of provided types.

        :param dictionary:
        :return:
        """
        by_type = (next(iter(dictionary)))
        locator = dictionary.get(by_type)
        self.click(self.driver, by_type, locator)

    def click_by_css(self, locator, by_type=By.CSS_SELECTOR):
        """Click the element using its CSS selector.

        :param locator:
        :param by_type:
        :return:
        """
        self.click(self.driver, by_type, locator)

    def click_no_scroll(self, locator, by_type=By.CSS_SELECTOR):
        """Click the element using its CSS selector without scrolling.

        :param locator:
        :param by_type:
        :return:
        """
        el = self.find_element(self.driver, by_type, locator)
        el.click()

    def select(self, option, by_type, locator):
        """

        :param option:
        :param by_type:
        :param locator:
        :return:
        """
        _select = Select(self.find_element(self.driver, by_type, locator))
        _select.select_by_visible_text(option)

    def select_by_dict(self, option, dictionary):
        by_type = (next(iter(dictionary)))
        locator = dictionary.get(by_type)
        _select = Select(self.find_element(self.driver, by_type, locator))
        _select.select_by_visible_text(option)

    def type_text(self, text, by_type, locator):
        el = self.find_element(self.driver, by_type, locator)
        el.click()
        el.send_keys(text)

    def type_text_dict(self, text, dictionary):
        by_type = (next(iter(dictionary)))
        locator = dictionary.get(by_type)
        self.type_without_click(self.driver, text, by_type, locator)

    def type_text_(self, text, locator, by_type=By.CSS_SELECTOR):
        return self.type_text(self.driver, text, by_type, locator)

    def type_without_click(self, text, by_type, locator):
        el = self.find_element(self.driver, by_type, locator)
        el.send_keys(text)

    def clear_text(self, by_type, locator, delay=3):
        el = self.find_element(self.driver, by_type, locator, delay)
        el.click()
        el.clear()

    def type_text_press_enter(self, text, by_type, locator):
        self.find_element(self.driver, by_type, locator).send_keys(text)
        self.find_element(self.driver, by_type, locator).send_keys(Keys.RETURN)

    def clear_input_box_press_enter(self, by_type, locator):
        # when clear() not working,should make sure double click can choose all characters in put box
        ele = self.find_element(self.driver, by_type, locator)
        ActionChains(self.driver).double_click(ele).perform()
        ele.send_keys(Keys.DELETE)
        ele.send_keys(Keys.ENTER)
        fixed_wait()

    def get_text(self, by_type, locator):
        el = self.find_element(self.driver, by_type, locator)
        return self.get_text_from_element(self.driver, el)

    def get_text_from_page(self):
        return self.get_text(self.driver, By.TAG_NAME, "body")

    def get_text_from_element(self, el):
        self.driver.execute_script("arguments[0].scrollIntoView();", el)
        return el.text

    def get_attribute(self, by_type, locator, attribute):
        el = self.find_element(self.driver, by_type, locator)
        return el.get_attribute(attribute)

    def get_child_elements_by_css_selector(self, by_type, parent_locator, child_css):
        el = self.find_element(self.driver, by_type, parent_locator)
        return el.find_elements_by_css_selector(child_css)

    def switch_window(self):
        fixed_wait(5)
        handles = self.driver.window_handles
        size = len(handles)
        for x in range(size):
            if handles[x] != self.driver.current_window_handle:
                self.driver.switch_to.window(handles[x])

    def wait_for_title(self, title, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_contains(title))
        except TimeoutException as e:
            return

    def wait_for_link(self, link_text, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException as e:
            return

    def find_n_click(self, button_text, css_selector):
        action_buttons = self.find_elements(self.driver, By.CSS_SELECTOR, css_selector)
        for button in action_buttons:
            if button_text == button.text:
                button.click()
                fixed_wait(1)
                break

    def find_n_directly_click_row(self, button_text, css_selector):
        """

        :param button_text:
        :param css_selector:
        :return:
        """
        action_buttons = self.find_elements(self.driver, By.CSS_SELECTOR, css_selector)
        for button in action_buttons:
            fixed_wait(1)
            if button_text in button.text:
                button.click()
                fixed_wait(1)
                break

    def select_motiff_radio_button(self, button_text, css_selector):
        """select the button when the text is as equal to the expected one

        :param button_text:
        :param css_selector:
        :return:
        """
        options = self.find_elements(self.driver, By.CSS_SELECTOR, css_selector)
        for option in options:
            if button_text == option.text:
                action_button = option.find_element(By.CSS_SELECTOR, 'input')
                action_button.click()
                fixed_wait(1)
                break

    def find_row_n_click_button(self, row_text, button_text, row_css, button_css):
        """Find table row and button in that row, click button

        :param row_text:
        :param button_text:
        :param row_css:
        :param button_css:
        :return:
        """
        action_rows = self.find_elements(self.driver, By.CSS_SELECTOR, row_css)
        for row in action_rows:
            if row_text in row.text:
                action_buttons = row.find_elements(By.CSS_SELECTOR, button_css)
                for button in action_buttons:
                    if button_text in button.text:
                        button.click()
                        fixed_wait(1)
                        return

    def find_row_n_return_cell_element(self, row_text, row_css, cell_css):
        """Find table row and button in that row, click button

        :param row_text:
        :param row_css:
        :param cell_css:
        :return:
        """
        action_rows = self.find_elements(self.driver, By.CSS_SELECTOR, row_css)
        if action_rows is None:
            return None
        for row in action_rows:
            if row_text in row.text:
                target_cell = row.find_element(By.CSS_SELECTOR, cell_css)
                return target_cell

    def find_row_n_return_cell_text(self, row_text, row_css, cell_css):
        """Find table row and button in that row, click button

        :param row_text:
        :param row_css:
        :param cell_css:
        :return:
        """
        action_rows = self.find_elements(self.driver, By.CSS_SELECTOR, row_css)
        if action_rows is None:
            return None
        for row in action_rows:
            if row_text in row.text:
                target_cell = row.find_element(By.CSS_SELECTOR, cell_css)
                return target_cell.text

    def find_row_n_click_element(self, row_text, row_css, element_css, n=None):
        """Find table row and button in that row, click button

        :param row_text:
        :param row_css:
        :param element_css:
        :param n:
        :return:
        """
        action_rows = self.find_elements(self.driver, By.CSS_SELECTOR, row_css)
        flag = 0
        for row in action_rows:
            if row_text in row.text:
                flag += 1
                action_element = row.find_element(By.CSS_SELECTOR, element_css)
                try:
                    WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_css)))
                except TimeoutException:
                    Logger.info(f"Element {row.text} never became clickable")
                self.driver.execute_script("arguments[0].scrollIntoView();", action_element)
                action_element.click()
                fixed_wait(1)
                if n is not None and n >= flag:
                    return
        return

    def find_row_n_click_element_by2(self, row_text, another_text, row_css, element_css, n=None):
        """Compare whether the two colomus values are as expected

        :param row_text:
        :param another_text:
        :param row_css:
        :param element_css:
        :param n:
        :return: int
        """
        """Find table row and button in that row, click button"""
        action_rows = self.find_elements(self.driver, By.CSS_SELECTOR, row_css)
        flag = 0
        for row in action_rows:
            if row_text.lower() in row.text.lower() and another_text.lower() in row.text.lower():
                flag += 1
                action_element = row.find_element(By.CSS_SELECTOR, element_css)
                action_element.click()
                fixed_wait(1)
                if n is not None and n >= flag:
                    return flag
        return flag

    def find_hower_n_click(self, text, css_selector, hover_css_selector):
        """find and hover the matched text row , then click the row

        :param text:
        :param css_selector:
        :param hover_css_selector:
        :return:
        """
        rows = self.find_elements(self.driver, By.CSS_SELECTOR, css_selector)
        for row in rows:
            if text in row.text:
                view_button = row.find_element(By.CSS_SELECTOR, hover_css_selector)
                hover = ActionChains(self.driver).move_to_element(view_button)
                hover.perform()
                view_button.click()
                fixed_wait(1)
                return True
        return False

    def find_hower_n_click_different(self, text, css_selector, hover_css_selector, click_css_selector):
        """ after finding and howering the elemetns according to the matched css_selector,
        finally appear the element we want then do a click

        :param text:
        :param css_selector:
        :param hover_css_selector:
        :param click_css_selector:
        :return:
        """
        rows = self.find_elements(self.driver, By.CSS_SELECTOR, css_selector)
        for row in rows:
            if text in row.text:
                view_button = row.find_element(By.CSS_SELECTOR, hover_css_selector)
                hover = ActionChains(self.driver).move_to_element(view_button)
                hover.perform()
                fixed_wait(1)
                row.find_element(By.CSS_SELECTOR, click_css_selector).click()
                fixed_wait()
                break

    def find_n_type_text(self, search_text, css_selector, type_text_css_selector, text_to_type):
        """ return the flag whethet the text is in the matched css_selector

        :param search_text:
        :param css_selector:
        :param type_text_css_selector:
        :param text_to_type:
        :return:
        """
        elems = self.find_elements(self.driver, By.CSS_SELECTOR, css_selector)
        for elem in elems:
            if search_text in elem.text:
                type_text_elem = elem.find_element(By.CSS_SELECTOR, type_text_css_selector)
                self.driver.execute_script("arguments[0].scrollIntoView();", type_text_elem)
                type_text_elem.click()
                type_text_elem.clear()
                type_text_elem.send_keys(text_to_type)
                fixed_wait()
                return True
        return False

    def click_motiff_item_presentation_list(self, ul_role, item):
        """Click the motiff presentation list according to the matched locator

        :param ul_role:
        :param item:
        :return:
        """
        rows = self.find_elements(self.driver, By.CSS_SELECTOR, f'div[role="presentation"] ul[role="{ul_role}"] li')
        for row in rows:
            if item in row.text:
                row.click()
                break
        fixed_wait()

    def refresh_page(self):
        """ Refresh the page.

        :return:
        """
        self.driver.refresh()


    def close_popup_banner(self):
        """ close the popup banner according to the matched locators

        :return:
        """
        dialog_button = self.find_element(self.driver, By.CSS_SELECTOR, 'button[id^="pendo-button"]')
        if dialog_button is None:
            dialog_button = self.find_element(self.driver, By.CSS_SELECTOR, 'button[id^="pendo-close"]')
        if dialog_button is not None:
            dialog_button.click()

    def close_pendo_banners(self):
        """close all the popup banners according to the matched locators

        :return:
        """
        dialog_button = self.find_element(self.driver, By.CSS_SELECTOR, 'button[id^="pendo-close-guide"]')
        if dialog_button is not None:
            dialog_button.click()
