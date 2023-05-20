import json

student = {
    "map":{
        "Title" : "Student Enrolment Form",
        "Fieldcount" : "8",
        "Pagecount" : "1",
        "Name" : "Akshay Sharma",
        "Gender" : "Male",
        "Address" : "Noida, UP, India",
        "Phone" : "998-787-7654",
        "Date of Birth" : "28/03/1990",
        "Email" : "akshay@email.com",
        "Emergency Name" : "Sanjay Sharma",
        "Emergency Phone" : "765-434-3232"

    }
}

x = json.dumps(student, indent=2)
with open('mydata.json','w') as f:
    f.write(x)