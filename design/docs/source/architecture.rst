.. Sections: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#sections

Architecture
############


Layers

- `System`_
	- `Server Hardware`_
	- Operating System
	- `Data Store`_
	- `Database Management System`_
	- `Scripting Language and Interpreter`_
	- `Scripting Frameworks`_
- `Data Layer`_
	- `Database Schema`_: data representation in the database
	- `Data Management`_ (scripting implementation): classes to access and modify the data
- `Business Layer`_
	- ...
- `Presentation Layer`_
	- `Procotol Handling`_ (scripting implementation): translates the protocol into business logic
	- `Communcation Protocol`_: protocol defining how the data can be accessed
	- `Data Formats`_: formats of how the data is represented


Environments
************

- Production
	- The productive environment which is used by the users.
	- It runs the latest released version.
- Sandbox
	- An environment which can be used by developers who are testing their applications against the API.
	- The Sandbox has to run on the latest stable version of the system which is the same as the productive system.
- Integration
	- The integration environment is supposed to be used by testing users only. It is a system with meaningful test data which should be used to test new features by actual humans.
	- The integration environment runs the latest alpha version for testing.
- Development
	- An environment which can be used by developers to test their changes.
	- The development environment runs the latest built version.

Whether or not certain environments should share some of their components
(hardware, operating system, DBMS, etc.) has to be considered.


System
******


Server Hardware
===============

The server's and database's location probably have to be physically located in Germany to comply with German Privacy Law.

Considerations have to be done about the necessary performance of the system.


Data Store
==========

A seperate data store might be needed to store large amounts of data, e.g. the original work uploaded by the artist for acoustic fingerprinting.


Database Management System
==========================

Currently considering PostgreSQL. Open source and has advantages over MySQL. The database management system might be installed on a seperate server which is different from the one running the application. 


Scripting Language and Interpreter
==================================

As the scripting language and its interpreter Python is considered at the moment.


Scripting Frameworks
====================

Python frameworks found suiteable are:

- Pyramid
- SQLAlchemy


Data Layer
**********


Database Schema
===============

The database schema should comply with the principle of `Revisionssicherheit <https://de.wikipedia.org/wiki/Revisionssicherheit>`_.


Data Management
===============

These classes should abstract the Revisionssicherheit.

This layer abstracts the database schema from the application. It is the only place where database requests are performed. All other classes have to use classes from this layer to access the database.

If there's a `Data Store`_, this is the place where the access to it is handled.


Business Layer
**************

This is where the logic is implemented. The logic is independent from the representation.


Presentation Layer
******************


Procotol Handling
=================

This layer translates the available business logic into protocol and formats. It parses the user's requests, calls business logic methods and sends responses in the corresponding data format.

This is the only layer which should be concerned with the REST API.

It's tasks are:

- Transactional
	- Handling the `Communcation Protocol`_
	- Parsing user request from specific `Data Formats`_
	- Calling business logic and receiving business data
	- Transforming business data into specific `Data Formats`_
- Performance
	- Load balancing
	- Load throttling


Communcation Protocol
=====================


Requests
--------

Request are sent by the client to the server


HTTP Request Methods
^^^^^^^^^^^^^^^^^^^^

- `OPTIONS <https://tools.ietf.org/html/rfc2616#section-9.2>`_: retrieving information about what to do with a URI 
	- retrieving allowed methods GET/POST/...
	- schema specifying response content data
	- schema specifying request body data
	- available mime types for requests and responses
- `GET <https://tools.ietf.org/html/rfc2616#section-9.3>`_: reading entities
- `HEAD <https://tools.ietf.org/html/rfc2616#section-9.4>`_:
	- retrieving only the metadata of a GET request for reading entites
	- the HEAD request can be used for caching purposes
- `POST <https://tools.ietf.org/html/rfc2616#section-9.5>`_: creating entities
- `PUT <https://tools.ietf.org/html/rfc2616#section-9.6>`_: updating entities
- `DELETE <https://tools.ietf.org/html/rfc2616#section-9.7>`_: deleting entities
- `TRACE <https://tools.ietf.org/html/rfc2616#section-9.8>`_: (not used)
- `CONNECT <https://tools.ietf.org/html/rfc2616#section-9.9>`_: (not used)


MIME Type
^^^^^^^^^
   
The format will be requested in the "Accept" HTTP header field with specifying a corresponding `MIME Type`_:

::
   GET / HTTP/1.1 Accept:
   application/vnd.vendor_name.application_name+file_format; version=0.1

Reuse of "application/vnd.api+json"? Lacking optional parameter "version".

Specify format and schema "application/wrml; format='http://api.formats.wrml.org/application/json'; schema='http://api.schemas.wrml.org/common/Format-v0.1'"? 
   
A `registration <https://www.iana.org/cgi-bin/mediatypes.pl>`_ of the mime type should be considered to comply with international web standards. A list of already registered vendor mime types can be found `here <https://www.iana.org/assignments/media-types/application>`_


Responses
---------

Responses are sent by the server to the client.


HTTP Status Codes
^^^^^^^^^^^^^^^^^

- `200 OK <https://tools.ietf.org/html/rfc2616#section-10.2.1>`_
	- The request has been valid and performed as requested.
- `201 Created <https://tools.ietf.org/html/rfc2616#section-10.2.2>`_
	- The request has been fulfilled and resulted in a new resource being created
	- Possible Result of a POST request to create a new entity
- `400 Bad Request <https://tools.ietf.org/html/rfc2616#section-10.4.1>`_
	- The request could not be understood by the server due to malformed syntax.
- `401 Unauthorized <https://tools.ietf.org/html/rfc2616#section-10.4.2>`_
	- The request requires user authentication.
	- The user has not been authenticated where authentication is required.
- `403 Forbidden <https://tools.ietf.org/html/rfc2616#section-10.4.4>`_
	- The server understood the request, but is refusing to fulfill it.
	- The user has been authenticated but is not allowed to perform the request.
- `404 Not Found <https://tools.ietf.org/html/rfc2616#section-10.4.5>`_
	- The server has not found anything matching the Request-URI.
- `500 Internal Server Error <https://tools.ietf.org/html/rfc2616#section-10.5.1>`_
	- The server encountered an unexpected condition which prevented it from fulfilling the request.
- `503 Service Unavailable <https://tools.ietf.org/html/rfc2616#section-10.5.4>`_
	- The server is currently unable to handle the request due to a temporary
   overloading or maintenance of the server.


Hypermedia as the Engine of Application State (HATEOAS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The server has to provide information about further possible transitions. E.g. when a track was release, there is the possibility to update or delete it.

This abstracts the URIs as they don't have to be fixed. As the client retrieved the information what is possible to do next, the URIs for doing so are delivered to it. It should not rely on predefined URIs rather than the entry URI to the API.


HTTP Header Fields
^^^^^^^^^^^^^^^^^^

The `HTTP Header Fields <https://tools.ietf.org/html/rfc2616#section-7.1>`_ provide necessary information about interpreting the content and building a caching mechanism.

- `Content-Type <https://tools.ietf.org/html/rfc2616#section-14.17>`_
	- Specifies the `MIME Type`_ of the response.
	- An encoding parameter should be passed (e.g. "charset=UTF-8", "charset=ISO-8859-1")
- `Expires <https://tools.ietf.org/html/rfc2616#section-14.21>`_: The date/time after which the response is considered unstable
- `Last-Modified <https://tools.ietf.org/html/rfc2616#section-14.29>`_: The date/time of the last modification of the resource (e.g. edit date of a user)
- More headers might be used


Pagination
^^^^^^^^^^

The pagination has to be taken care of. The client should be able to specify within a certain limit � how many entities it wants to retrieve per page as well as the number of the page it wants to retrieve.

In the context of HATEOAS the links for previous page, following page, first page and last page should be delivered.


Versioning
^^^^^^^^^^

The version will be requested in the "Accept" HTTP header field with specifying an optional parameter to the `MIME Type`_:

::
	GET / HTTP/1.1
	Accept: application/vnd.vendor_name.application_name+file_format; version=0.1


Charsets
^^^^^^^^

UTF-8 should be considered as the only charset for delivering content to the client as it is best suitable for international special characters.


URI Design
----------

Best practices

- No tailing forward slash ([#masse]_ p. 12)
- Use hyphens not underscores ([#masse]_ p. 12)
- Lowercase letters should be preferred ([#masse]_ p. 13)
- File extensions should not be included in URIs ([#masse]_ p. 13)
	- Use Content-Type and Accept headers to determine the format



Data Formats
============


Formats
-------

- JSON should be the main format as it is commonly used
- XML might be another format as it widely established


Schemas
-------

The schemas for the corresponding formats should be defined.

- `JSON Schema <http://json-schema.org/>`_
- `XML Schema Definitions (XSD) <https://en.wikipedia.org/wiki/XML_Schema_%28W3C%29>`_


References
**********

[#Masse]  Mark Massé, REST API Design Rulebook, O'Reilly, October 2011

