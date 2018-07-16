RESTful API for an address book, implemented in Python using Flask.

A list of dependencies can be found in the requirements.txt file.

DATA:

The contact data in the address book as three fields: name, address, and phone number. Of these three, name is used as a unique identifier (i.e. no two entries have the same name).
Currently, the contact data is sourced from the hard-coded 'contacts' list in adbook.py. In the full implementation, the contact data would be stored on an Elasticsearch data store instead, and all references to the list would be replaced with Elasticsearch calls. 

ENDPOINTS:

http://127.0.0.1:5000
This serves as a home page. In the current implementation, it does not have any significant functionality and merely provides a title page.

http://127.0.0.1:5000/contact?pageSize={}&page={}&query={}
This serves GET requests. It provides a listing of the contact data. THe user selects how many entries are to be shown with pageSize, and chooses the offset using page (starting at 0). If the pageSize/page selection is completely outside the list bounds, an error message is returned. However, if it is only partially outsie the list bounds, all entries until the end of the list are displayed without error. In the current implementation, it is assumed that both page and pageSize are non-negative integers. Unfortunately, due to Elasticsearch currently not being implemented, the third parameter 'query' has not been given functionality. 

http://127.0.0.1:5000/contact/{name}
This serves POST, GET, PUT and DELETE requests. The GET request handler returns the contact's data if {name} corresponds to a valid entry, otherwise returns an error message. The DELETE request handler likewise deletes the contact's data if {name} corresponds to a valid entry, otherwise returns an error message.

TESTING:
This API's functionality was tested with Insomnia (https://insomnia.rest/). A full list of requests used to test the API (copied as curl commands) can be found in the testing.txt file. 