# Use any combination of search parameters.
# Each parameter may be used only once.
# A search request has to contain at least one valid name,
# email address, phone, username, user id, URL, or a full US address (including a house number). //

# Python Code:

# imports
from piplapis.search import SearchAPIRequest, Person, Address, Name, Phone, Email, Job, DOB

# run search (request/response)
SearchAPIRequest.set_default_settings(api_key=u'Your API Key', minimum_probability=None,
    show_sources=None, minimum_match=None, hide_sponsored=None, live_feeds=None, use_https=True)

fields = [Phone(raw=19785550145), Email("clark.kent@example.com"), Name(first=u'Clark', last=u'Kent')]
request = SearchAPIRequest(person=Person(fields=fields))
response = request.send()

# print portion of response
if response.person:   # Has data so single Full Person response
    currentPerson = response.person
    print("Number of Names:", len(currentPerson.names))
    print("Name(s):" + "\n" .join(map(str, currentPerson.names)))
    print("Username(s):" + "\n" .join(map(str, currentPerson.usernames)))
    print("Emails(s):" + "\n" .join(map(str, currentPerson.emails)))
    print("Phone Number(s):" + "\n".join(map(str, currentPerson.phones)))
    print("Address(s):" + "\n".join(map(str, currentPerson.addresses)))
    print("Origin Country:" + "\n".join(map(str, currentPerson.origin_countries)))
    print("Education:" + "\n".join(map(str, currentPerson.educations)))
    print("Language:" + "\n".join(map(str, currentPerson.languages)))
    print("Ethnicity:" + "\n".join(map(str, currentPerson.ethnicities)))
    print("Jobs:" + "\n".join(map(str, currentPerson.jobs)))
    print("Education:" + "\n".join(map(str, currentPerson.educations)))
    print("Relationship:" + "\n".join(map(str, currentPerson.relationships)))
    print("Images:" + "\n".join(map(str, currentPerson.images)))
    print("Urls:" + "\n".join(map(str, currentPerson.urls)))
    print("Usernames:" + "\n".join(map(str, currentPerson.usernames)))
    print("User IDs:" + "\n".join(map(str, currentPerson.user_ids)))
    print("\n")


