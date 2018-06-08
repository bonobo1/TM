
import re

from robobrowser import RoboBrowser

br = RoboBrowser()
br.open("https://github.com/login")

form = br.get_form() #in case there are multiple forms there are ways to isolate them
form["login_field"] = 'bonobo1'
form["password"] = 'Ta9Choo2416256?!'
br.submit_form(form)

src = str (RoboBrowser().parsed())

start = '<li class="dropdown-header header-nav-current-user css-truncate">' 
end = '</li>'

result = re.search('%s(.*)%s' % (start, end), src).group(1) # a regular expression that is used to get the content between the start and the end

print (result)


# print(str(browser.select))

# browser = mechanicalsoup.Browser()
# login_page = browser.get('http://www.tufast.de/webmail2/')
# login_form = login_page.soup.select(".form-signin")[1]

# login_form.find(attrs={"name": "username"})['value'] = 'username'
# login_form.find(attrs={"name": "password"})['value'] = 'password'

# page2 = browser.submit(login_form, login_page)
# print (str(page2.text))

