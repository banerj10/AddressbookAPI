RESTful API for an address book, implemented in Python using Flask.
A list of dependencies can be found in the requirements.txt file.
The flask app can be run from the command line using 'set FLASK_APP=hello.py' and 'flask run'. 
(In Linux systems, 'export' should be used in place of 'set'.) 

DATA:

The contact data in the address book as three fields: name, address, and phone number. 
Of these three, name is used as a unique identifier (i.e. no two entries have the same name). 
When adding or updating entries, three checks are performed: that the name have no digits, 
that the phone number have not alphabets, and that the phone number consist of exactly nine 
characters. Currently, the contact data is sourced from the hard-coded 'contacts' list in 
adbook.py.

ENDPOINTS:

http://127.0.0.1:5000
This serves as a home page. In the current implementation, it does not have any significant 
functionality and merely provides a title page.

http://127.0.0.1:5000/contact?pageSize={}&page={}&query={}
This serves GET requests. It provides a listing of the contact data. The user selects how many 
entries are to be shown with pageSize, and chooses the offset using page (starting at 0). If the 
pageSize/page selection is completely outside the list bounds, an error message is returned. 
However, if it is only partially outsie the list bounds, all entries until the end of the list 
are displayed without error. In the current implementation, query={} has not been used and it is 
assumed that both page and pageSize are non-negative integers.

http://127.0.0.1:5000/contact
This serves POST requests. It requires three parameters in the request body: name, address and 
phone (the same as the fields in the contact data). If the paramters are valid (see the DATA 
section) and the name provided does not already exist in the contact data, the request data is 
added as a new contact.

http://127.0.0.1:5000/contact/{name}
This serves GET, PUT and DELETE requests. The GET request handler returns the contact's data if 
{name} corresponds to a valid entry, otherwise returns an error message. The PUT handler requires 
two parameters in the reuqest body: address and phone. (We do not require the name here as {name} 
is already present). If the paramters are valid (see the DATA section) and the name field 
corresponds to a valid entry in the contact data, the entry is updated with the new phone number 
and address. The DELETE request handler deletes the contact's data if {name} corresponds to a 
valid entry, otherwise returns an error message.

TESTING:

This API's functionality was tested with Insomnia (https://insomnia.rest/), an open-source 
software for sending HTTP requests. A list of requests used to test the API (copied as curl 
commands) can be found in the testing.txt file.

REFERENCES:
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://stackoverflow.com/questions/22947905/flask-example-with-post
https://stackoverflow.com/questions/4526273/what-does-enctype-multipart-form-data-mean
