from flask import Flask, request, jsonify

# creating flask instance
app = Flask(__name__)

# Hard-coded list which acts as dummy data for the contacts list.
# The 'name' field is used as a unique identifier for each data entry.
contacts = [
    {'name': 'Anna', 'address': '15 Princeton Street', 'phone': '9852207700'}, 
    {'name': 'Barry', 'address': '6 Tower Road', 'phone': '2269004567'},
    {'name': 'Cheryl', 'address': 'Ashton House', 'phone': '8287590001'}, 
    {'name': 'David', 'address': '12 King Complex', 'phone': '3340901243'}
]

# Endpoint for the home page (i.e. http://127.0.0.1:5000).
# Not required, but it seems like good practice to have it.
@app.route('/', methods=['GET'])
def homepage():
    return "Coding challenge - Address Book"

# Endpoint for GET /contact?pageSize={}&page={}&query={} and
# POST /contact requests. The GET request has all its parameters 
# present in the URL and the POST request has parameters name,
# address and contact present in the body in x-www-form-urlencoded
# format. query={} is unused as of this current implementation. 
@app.route('/contact', methods=['GET', 'POST'])
def contact_all():
    # Subsection for GET requests.
    if request.method == 'GET':
        # Checks if query parameters are present in URL.
        if ('pageSize' in request.args and 'page' in request.args):        
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
            return 'Error: parameters not provided in request URL'

    # Subsection for POST requests.
    if request.method == 'POST':
        # Checks if query parameters are present in request body.
        if ('name' in request.form and 'address' in request.form and
            'phone' in request.form):        
            name = str(request.form['name'])
            address = str(request.form['address'])
            phone = str(request.form['phone'])
            # Returns error message if name has digits or if
            # phone number has letters or if phone number does
            # not have 10 digits.
            if(not name.isalpha() or not phone.isdigit() or
                len(phone) != 10):
                return 'Error: invalid values in parameters'
            # Returns error if contact already exists.    
            for contact in contacts:
                if(contact['name'] == name):
                    return 'Error: contact already present'
            # If parameters are valid and contact does not already
            # exist, appends contact and returns a success message. 
            contacts.append({'name': name, 'address': address, 
                'phone':phone})
            return 'Contact successfully added' 
        # Returns error if query parameters not present.    
        else:
            return 'Error: parameters not provided in request body'

# Endpoint for GET/PUT/DELETE /contact/{name} requests.
# These requests can be used respectively to display, update or 
# delete a particular contact denoted by <name>, and return an
# error mesage if <name> is not found.
@app.route('/contact/<name>', methods=['GET', 'PUT', 'DELETE'])
def contact_id(name):
    # Subsection for GET requests.
    if request.method == 'GET':
        # Searches the list of contacts using the unique 'name' 
        # identifier. If the desired entry is found, it is returned.
        # Else, an error message is displayed.  
        for contact in contacts:
            if(contact['name'] == name):
                return jsonify(contact)
        return 'Error: Contact not found'

    # Subsection for PUT requests.
    if request.method == 'PUT':
        # Checks if query parameters are present in request body.
        if ('address' in request.form and 'phone' in request.form):
            address = str(request.form['address'])
            phone = str(request.form['phone'])
            # Returns error message if phone number has letters or
            # if phone number does not have 10 digits.
            if(not phone.isdigit() or len(phone) != 10):
                return 'Error: invalid values in parameters'
            # Checks if a contact with <name> exists. If yes, updates 
            # data and returns a success message.
            for contact in contacts:
                if(contact['name'] == name):
                    contact['address'] = address
                    contact['phone'] = phone
                    return 'Contact successfully updated'
            # Returns error message if <name> is not found. 
            return 'Error: Contact not found' 
        # Returns error if query parameters not present.    
        else:
            return 'Error: parameters not provided in request body'        
    
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