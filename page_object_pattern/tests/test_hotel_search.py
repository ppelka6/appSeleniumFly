import pytest
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage



class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        # self.driver = webdriver.Chrome(ChromeDriverManager(driver_version='117.0.5938.89').install())
        # self.driver.implicitly_wait(10)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("22/09/2023", "25/09/2023")
        search_hotel_page.set_travellers("2", "2")
        search_hotel_page.perform_search()
        results_page = SearchResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()

        assert hotel_names[0] == 'Jumeirah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert price_values[0] == '$22'
        assert price_values[1] == '$50'
        assert price_values[2] == '$80'
        assert price_values[3] == '$150'



