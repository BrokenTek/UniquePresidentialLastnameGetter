from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def queryPresident():

    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://duckduckgo.com')

    try:
        input_field = driver.find_element(By.ID, "searchbox_input")
        print("Primary Page Result for DuckDuckGo.com")
    except NoSuchElementException:
        print("Secondary Page Result for DuckDuckGo.com")
        input_field = driver.find_element(By.ID, "search_form_input_homepage")

    input_field.click()
    input_field.send_keys("presidents of the united states")
    input_field.send_keys(Keys.RETURN)

    results_list = driver.find_elements(By.CLASS_NAME, "nrn-react-div")
    results_list[1].click()

    president_lastname_list = list()
    presidents_box_list = driver.find_elements(By.CLASS_NAME, 'col-sm-6')
    for box in presidents_box_list:
        fullname = box.find_element(By.CLASS_NAME, 'acctext--con').text
        fullname_split = fullname.split(" ")
        if fullname_split[-1] == "Jr.":
            lastname = fullname_split[-2] + " " + fullname_split[-1]
        else:
            lastname = fullname_split[-1]
        president_lastname_list.append(lastname)

    return set(president_lastname_list)

def main():
    print(queryPresident())

if __name__ == "__main__":
    main()
