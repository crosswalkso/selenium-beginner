# This file is going to include method that will parse
# The specific data that we need from each one of the deal boxes.
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.XPATH,
            '//div[@data-testid="property-card"]',
        )

    # no element error -> try except -> slow
    def pull_deal_box_attributes(self):
        collection = []
        for idx, deal_box in enumerate(self.deal_boxes):
            # Pulling the hotel name
            hotel_name = (
                deal_box.find_element(
                    By.XPATH,
                    f'//div[@data-testid="property-card"][{idx+1}]//div[@data-testid="title"]',
                )
                .get_attribute("innerHTML")
                .strip()
            )
            try:
                hotel_price = (
                    deal_box.find_element(
                        By.XPATH,
                        f'//div[@data-testid="property-card"][{idx+1}]//span[@data-testid="price-and-discounted-price"]',
                    )
                    .get_attribute("innerHTML")
                    .strip()
                )
            except Exception as e:
                hotel_price = "''"
            try:
                hotel_score = (
                    deal_box.find_element(
                        By.XPATH,
                        f'//div[@data-testid="property-card"][{idx+1}]//div[@data-testid="review-score"]/div[@aria-label]',
                    )
                    .get_attribute("aria-label")
                    .strip()
                )
            except Exception as e:
                hotel_score = "''"
            hotel_name = f"'{hotel_name}'"
            hotel_price = f"'{hotel_price}'"
            hotel_score = f"'{hotel_score}'"
            collection.append([hotel_name, hotel_price, hotel_score])
        return collection
