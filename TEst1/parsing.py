import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://novus.zakaz.ua/uk'
driver.get(url)
driver.quit()


page_sours = driver.page_source

soup = BeautifulSoup(page_sours, 'html.parser')

for category in soup.find_all(class_='jsx-2341e7798cea6ab9 CategoriesMenuListItem')[3:6]:  # перебираємо категорії
    print(category.text)  # назва категорії
    print('https://novus.zakaz.ua' + category.find('a').get('href'))  # посилання на категорію

    driver = webdriver.Chrome()
    url = 'https://novus.zakaz.ua' + category.find('a').get('href')
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page_source, 'html.parser')

    for sub_category in soup.find_all(class_='jsx-897b0bbecd068e31 CategoriesBox__listItem')[
                        0:3]:  # перебираємо під-категорії
        print(
            '      ' + sub_category.find(class_='jsx-74f719c61c25da4f CategoryCard__title').text)  # назва під-категорії
        print('      ' + 'https://novus.zakaz.ua' + sub_category.find('a').get('href'))  # посилання на під-категорію

        driver = webdriver.Chrome()
        url = 'https://novus.zakaz.ua' + sub_category.find('a').get('href')
        driver.get(url)
        page_source = driver.page_source
        driver.quit()
        soup = BeautifulSoup(page_source, 'html.parser')

        for product in soup.find_all(class_='jsx-ebc81387b8a52f64 ProductsBox__listItem')[0:5]:
            print('            ' + product.find(class_='jsx-aa576fb7128a16a5 ProductTile__title').text)

            if product.find(class_='jsx-906554f8658dceda Price__value_caption Price__value_discount') is not None:
                print('            ' + product.find(
                    class_='jsx-906554f8658dceda Price__value_caption Price__value_discount').text)
            else:
                print('            ' + product.find(class_='jsx-906554f8658dceda Price__value_caption').text)

            print('            ' + 'https://novus.zakaz.ua' + product.find('a').get('href'))

    print('\n')