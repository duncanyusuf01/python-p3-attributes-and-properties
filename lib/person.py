#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]
    def __init__(self, name="Person", job=None):
        if isinstance(name, str) and 1<=len(name)<=25:
            self.name=name.title() 
        else:
            print("Name must be string between 1 and 25 characters.")
            self.name=None
        if job in Person.approved_jobs or job is None:
            self.job=job
        else:
            print("Job must be in list of approved jobs.")
            self.job=None