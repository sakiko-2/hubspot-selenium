from selenium import webdriver
from selenium.webdriver.firefox.options import Options

login_url = 'https://app.hubspot.com/login'
your_email = 'your_email' # Please replace with your email
your_password = 'your_password' # Please replace with your Hubspot password

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path='geckodriver', firefox_options=options)
driver.get(login_url)
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
username.send_keys(your_email)
password.send_keys(your_password)

driver.find_element_by_id('loginBtn').click()
driver.implicitly_wait(10)
test_account_links = driver.find_elements_by_xpath("//td[@class='domain']//span[contains(text(), 'dev-')]")
if len(test_account_links) > 0:
  test_account_links[0].click()
else:
  print('No such element link with dev-')

def create_contact(email, firstname, lastname):
  driver.implicitly_wait(20)
  contact_nav = driver.find_elements_by_link_text('Contacts')
  if len(contact_nav) > 0:
    contact_nav[0].click()
    driver.implicitly_wait(10)
    driver.find_element_by_id('nav-secondary-contacts').click()
  else:
    print('No such element Contacts')

  driver.implicitly_wait(10)
  driver.find_element_by_xpath("//button//span[text()='Create contact']").click()

  driver.implicitly_wait(10)
  driver.find_element_by_xpath("//input[@data-field='email']").send_keys(email)
  driver.find_element_by_xpath("//input[@data-field='firstname']").send_keys(firstname)
  driver.find_element_by_xpath("//input[@data-field='lastname']").send_keys(lastname)
  driver.find_element_by_xpath("//button/span[text()='Create contact']").click()
  driver.implicitly_wait(12)
  print('Contact created:', email, firstname, lastname)

  contacts_list_link = driver.find_elements_by_xpath("//nav[@class='private-back-button']//span[text()='Contacts']")
  if len(contacts_list_link) > 0:
    contacts_list_link[0].click()

contacts = [
  { 'email': 'conact_test1@hubspot.com', 'firstname': 'Puppy', 'lastname': 'Smith' },
  { 'email': 'conact_test2@hubspot.com', 'firstname': 'Tom', 'lastname': 'Cat' },
  { 'email': 'conact_test3@hubspot.com', 'firstname': 'Talking', 'lastname': 'Bird' }
]

for contact_data in contacts:
  email = contact_data['email']
  firstname = contact_data['firstname']
  lastname = contact_data['lastname']
  create_contact(email, firstname, lastname)

print('Good bye')

driver.quit()
