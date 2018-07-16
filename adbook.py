from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

# creating flask instance
app = Flask(__name__)

# Hard-coded list which acts as dummy data for the contacts list.
# In the full application, data would be sent to and retrieved from
# an Elasticsearch data store. Here, the 'name' field is used as a
# unique identifier for each data entry.
contacts = [
    {'name': 'Anna', 'address': '15 Princeton Street', 'contact': '9852207700'}, 
    {'name': 'Barry', 'address': '6 Tower Road', 'contact': '2269004567'},
    {'name': 'Cheryl', 'address': 'Ashton House', 'contact': '8287590001'}, 
    {'name': 'David', 'address': '12 King Complex', 'contact': '3340901243'}
]

# Endpoint for the home page (i.e. http://127.0.0.1:5000).
# Not required, but it seems like good practice to have it.
@app.route('/', methods=['GET'])
def homepage():
    return "Coding challenge - Address Book"

# Endpoint for GET /contact?pageSize={}&page={}&query={} requests.
# Unfortunately, query={} is unused due to Elasticsearch not being
# integrated.
@app.route('/contact', methods=['GET'])
def contact_all():
    # Checks if query parameters are present.
    if 'pageSize' in request.args and 'page' in request.args:
        
        pageSize = int(request.args['pageSize'])
        page = int(request.args['page'])
        
        # The subsection of data to be shown for this particular 
        # pageSize and page begins at 'start' and stops at 'end'.
        # This implementation assumes that both pageSize and page
        # are non-negative integers and that page numbers start 
        # from 0. 
        
        start = pageSize * page
        # If 'start' is beyond the end of the list, returns
        # an error message.
        if(start >= len(contacts)):
            return 'Error: pageSize/page exceeds length of data'
        
        end = start + pageSize
        # If 'start' is within list, but 'end' is outside it,
        # 'end' is truncated to stop at the last entry.
        if(end > len(contacts)):
            end = len(contacts)
        
        # Returns the appropriate sublist from start to end.
        return jsonify(contacts[start:end])
    
    # Returns error if query parameters not present.    
    else:
        return 'Error: pageSize or page fields not provided'

# Endpoint for POST/GET/PUT/DELETE /contact/{name} requests.
@app.route('/contact/<name>', methods=['GET', 'DELETE'])
def contact_id(name):
    # Subsection for GET requests.
    if request.method == 'GET':
        # Searches the list of contacts using the unique 'name' 
        # identifier. If the desired entry is found, it is returned.
        # Else, an error message is displayed.  
        for contact in contacts:
            if(contact['name'] == name):
                return jsonify(contact['name'])
        return 'Error: Contact not found'        
    
    # Subsection for DELETE requests.
    if request.method == 'DELETE':
        # Searches the list of contacts using the unique 'name' 
        # identifier. If the desired entry is found, it is deleted
        # and a confirmation message is returned. Else, an error 
        # message is displayed.
        for contact in contacts:
            if(contact['name'] == name):
                contacts[:] = [c for c in contacts if c['name'] != name]
                return 'contact successfully deleted'
        return 'Error: Contact not found'
    
    # Returns error if an invalid method is used.
    else:
        return 'Error: Invalid request method'