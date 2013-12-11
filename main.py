from mechanize import Browser

# create a new instance of Browser class
br = Browser()
br.set_handle_robots(False)

# fetch the stackoverflow.com url
br.open("http://www.stackoverflow.com")

# now we need to get the search form, so we get the first form
# in page, which is the search form, in position 0
br.select_form(nr=0)
# now we set value of the search field with name property as 'q'.
br.form['q'] = 'python'

# submit the request
response1 = br.submit()

# print the response, by calling the read() method
print response1.read()
