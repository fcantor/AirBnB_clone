# AirBnB Clone
### Description - AirBnB Clone
The AirBnB Clone project is Holberton School project that allows us to implement new development skills as we learn them. This web application will be built upon piece-by-piece over the coming months until it looks and functions as a Airbnb would.

### Description - The Console
The Console is a specific-use case command interpreter. It allows for the creation  of new objects (ex. User, Place), retrieval of objects from a file/database, operations on objects, updating objects, and destroying them. 

## Files in this Repository

|   ***File***    |     **File Location**     |     **Decription**     |
|---------------|-------------------------|-----------------------|
|  `console.py` | [console.py](console.py) | Enters the console |
|  `amenity.py` | [models/amenity.py](models/amenity.py) | Amenity subclass |
|  `city.py` | [models/city.py](models/city.py)  | City Subclass |
|  `review.py` |  [models/review.py](models/review.py)	| Review subclass |
|  `user.py`  | [models/user.py](models/usr.py) | User subclass |
|  `state.py` | [models/state.py](models/state.py) | State subclass |
|  `place.py` | [models/place.py](models/place.py)] | Place subclass |
|  `base_model.py'       | [models/base_model.py](models/base_model.py)  | The base model superclass |
|  `__init__py`          | [models/__init__.py](models/__init__.py) | Package init |
|  `file_storage.py`     | [models/file_storage.py](models/file_storage.py)  | Storage class |
|  `test_base_model.py`  | [tests/test_models/test_base_model.py](tests/test_models/test_base_model.py)  | Unittest module for base model |
| `test_console.py`      | [tests/test_console.py](tests/test_console.py)    | Unittest module for console  |
| `test_amenity.py`      | [tests/test_models/test_amenity.py](tests/test_models/test_amenity.py)  | Unittest module for amenity      |
| `test_city.py`         | [tests/test_models/test_city.py](tests/test_models/test_city.py)  | Unittest module for city         |
| `test_place.py`        | [tests/test_models/test_place.py](tests/test_models/test_place.py)   | Unittest module for place        |
| `test_review.py`       | [tests/test_models/test_review.py](tests/test_models/test_review.py)   | Unittest module for review       |
| `test_state.py`        | [tests/test_models/test_state.py](tests/test_models/test_state.py)  | Unittest module for state        |
| `test_user.py`         | [tests/test_models/test_user.py](tests/test_models/test_user.py)  | Unittest module for user  |
| `test_file_storage.py` | [tests/test_models/test_engine/test_file_storage.py](tests/test_models/test_engine/test_file_storage.py) | Unittest module for file storage |

# How to use it
**interactive mode**
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
**non-interactive mode**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

# Examples
```
(hbnb) create BaseModel
3db5387d-2fd6-494e-9b95-e5a62790c1fd
(hbnb) show BaseModel 2013187e-1bc9-4f8f-b0ae-8088e6a2ee43
[BaseModel] (3db5387d-2fd6-494e-9b95-e5a62790c1fd) {'created_at': datetime.datetime(2018, 11, 15, 3, 3, 56, 358245), 'updated_at': datetime.datetime(2018, 11, 15, 3, 3, 56, 358274), 'id': '3db5387d-2fd6-494e-9b95-e5a62790c1fd'}
(hbnb) update BaseModel 3db5387d-2fd6-494e-9b95-e5a62790c1fd name "Ricardo"
(hbnb) show BaseModel 3db5387d-2fd6-494e-9b95-e5a62790c1fd
[BaseModel] (3db5387d-2fd6-494e-9b95-e5a62790c1fd) {'created_at': datetime.datetime(2018, 11, 15, 3, 3, 56\
, 358245), 'updated_at': datetime.datetime(2018, 11, 15, 3, 3, 56, 358274), 'id': '3db5387d-2fd6-494e-9b95\
-e5a62790c1fd'}

```
### Authors
*Diego Murray* - [Github](https://github.com/dmurr) || [Twitter](https://twitter.com/diegocmurray)

*Franchesca Cantor* - [Github](https://github.com/cheska/) || [Twitter](https://twitter.com/servomecatnism)