from employee import Employee
from redis import ResponseError
from redisearch import Client, IndexDefinition, TextField, NumericField, TagField, GeoField
from redisearch import reducers
from redisearch.aggregation import AggregateRequest, Asc, Desc

from employee import Employee

def initializeClient():
    SCHEMA = (
        TextField("firstName"),
        TextField("lastName"),
        NumericField("salary"),
        TextField("department"),
        NumericField("isAdmin"),
        TagField("tag"),
        GeoField("location")
    )
    client = Client("myIndex")
    definition = IndexDefinition(prefix=[':employee.Employee:'])
    try:
        client.info()
    except ResponseError:
        # Index does not exist. We need to create it!
        client.create_index(SCHEMA, definition=definition)
    return client
client = initializeClient()
def show_results(results):
    for employee in results:
        print(employee)
        print("")

## Task 1 : find by first name
def find_by_first_name():
    print("find_by_first_name:")
    return Employee.find(Employee.firstName == 'ahmad').all() # search based on first name (could be done like this)
def find_by_first_name_redisearch(client):
    print("find_by_first_name_redisearch")
    res =  client.search("@firstName:ahmad")
    print(res)
# show_results(find_by_first_name())
# find_by_first_name_redisearch(client=client)

## Task 2: Find by firstName (wildcard)
def find_by_name_wildcard_redisearch(client):
    res =  client.search("@firstName:br*")
    # print(res)
    ## then try printing pretty
    for result in res.docs:
        print(result)
# find_by_name_wildcard_redisearch(client=client)

## Task 3: Find by first and last name
def find_by_first_and_last_name():
    print("find_by_name:")
    return Employee.find((Employee.firstName == 'ahmad') & (Employee.lastName == 'bazzi')).all()
# show_results(find_by_first_and_last_name())

## Task 4: Sort in ascending
def sort_by_salary():
    print("find_dogs_in_age_range:")
    return Employee.find(Employee.salary>0).sort_by("salary")
# show_results(sort_by_salary())
def sort_by_salary_redisearch_descending():
    request = AggregateRequest('*').group_by(['@salary','@firstName'], reducers.count().alias('count')).sort_by(Desc('@salary'))
    result = client.aggregate(request)
    for r in result.rows:   
        print(r)
# sort_by_salary_redisearch_descending()

## Task 5: Group employees into different departments 
def group_into_different_departments():
    request = AggregateRequest('*').group_by(['@department'], reducers.count().alias('count'))
    result = client.aggregate(request)
    for r in result.rows:   
        print(r)
# group_into_different_departments()

## Task 6: Group employees into different departments (only those who are admins)
def group_into_different_departments_onlyadmins():
    request = AggregateRequest('*').group_by(['@department','@isAdmin'], reducers.count().alias('count')).filter('@isAdmin == 1')
    result = client.aggregate(request)
    for r in result.rows:   
        print(r)
# group_into_different_departments_onlyadmins()

## Task 7: Aggregate by salary
def aggregate_by_salary():
    request = AggregateRequest('*').group_by(['@salary'], reducers.count().alias('count'))
    result = client.aggregate(request)
    for r in result.rows:   
        print(r)
## Task 8: Count those w/ salary > 75K$
def count_salary_greaterThan75K():
    request = AggregateRequest('*').group_by(['@salary'], reducers.count().alias('count')).filter('@salary > 75000').group_by([],reducers.sum('count').alias('total_number_of_salary_greater_than_75K'))
    result = client.aggregate(request)
    for r in result.rows:   
        print(r)
# count_salary_greaterThan75K()

## Task 9: Search by tags: marketing + us
def filter_by_tags():
    print("find_by_first_name_redisearch")
    res =  client.search("@tag:{us} @tag:{support}")
    for r in res.docs:  
        print(r)
# filter_by_tags()

## Task 10: Search by location + department 
def filter_by_location():
    print("filter_by_geo")
    res =  client.search("@location:[1 1 0.1 mi] @department:sales")
    for r in res.docs:  
        print(r)
filter_by_location()
