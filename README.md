# EmployeeDB
Advanced Redis search functionalities on Python applied on an Employee management backend app

## Video tutorial
For visual learners -> https://youtu.be/UhnEyMDWuyI

## Overview
This repositry shows advanced redisearch querying functionalities using python for full text searching, indexing, querying, tag searches, geo localization, aggregation, grouping, filtering and much more. The code is oriented towards an employee management backend - but is pretty generic in a sense that you could re-use the code for your beautiful app that you're trying to develop and sell.

## queries.py
A script designed in a functional programming philosophy that allows you to run the queries you desire. You can do the following functionalities so far:
- RediSearch Client
- Wildcard searches
- SEARCH by first name and last name
- SORT BY Salary (Ascending)
- SORT BY Salary (Descending)
- Aggregate reducers
- Aggregate alias 
- Aggregate limit
- GROUP BY department 
- GROUP BY department only those who are admins
- GROUP BY salary
- Count number of employees w/ salary greater than 75K USD
- SEARCH BY tags ( single tag )
- SEARCH BY tags ( multiple tags ) 
- SEARCH BY GEOLOCATION
