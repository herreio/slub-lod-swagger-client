# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install -e git+https://github.com/herreio/slub-lod-swagger-client.git#egg=swagger_client
```

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthoritySearchApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID-String of the authority-identifier to access. Possible Values (examples): 208922695, 118695940, 20474817, Q1585819
authority_provider = 'authority_provider_example' # str | The name of the authority-provider to access. Allowed Values: ['gnd', 'orcid', 'swb', 'isni', 'wd', 'filmportal.de', 'viaf', 'lc'].
format = 'format_example' # str | set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json (optional)
size = 100 # int | Configure the maxmimum amount of hits to be returned (optional) (default to 100)
_from = 0 # int | Configure the offset from the frist result you want to fetch (optional) (default to 0)

try:
    # search for an given ID of a given authority-provider
    api_instance.get_record_by_authority_id(id, authority_provider, format=format, size=size, _from=_from)
except ApiException as e:
    print("Exception when calling AuthoritySearchApi->get_record_by_authority_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://data.slub-dresden.de*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthoritySearchApi* | [**get_record_by_authority_id**](docs/AuthoritySearchApi.md#get_record_by_authority_id) | **GET** /{authority_provider}/{id} | search for an given ID of a given authority-provider
*AuthoritySearchApi* | [**get_record_by_authority_id_and_entity_id**](docs/AuthoritySearchApi.md#get_record_by_authority_id_and_entity_id) | **GET** /{authority_provider}/{entity_type}/{id} | search for an given ID of a given authority-provider on a given entity-index
*ExplorativeSearchApi* | [**aggregate_top_authors_date_published_and_related_topics_around_topics**](docs/ExplorativeSearchApi.md#aggregate_top_authors_date_published_and_related_topics_around_topics) | **GET** /explore/aggregations | aggregate topAuthors, datePublished and relatedTopics around topics
*ExplorativeSearchApi* | [**correlate_topics_with_their_mutual_occurances**](docs/ExplorativeSearchApi.md#correlate_topics_with_their_mutual_occurances) | **GET** /explore/correlations | correlate topics with their mutual occurances
*ExplorativeSearchApi* | [**query_topics**](docs/ExplorativeSearchApi.md#query_topics) | **GET** /explore/topicsearch | perform a simple serach on the topics index
*ReconcileApi* | [**open_refine_reconcilation_service_api__httpsgithub_com_open_refine_open_refinewiki_reconciliation_service_api**](docs/ReconcileApi.md#open_refine_reconcilation_service_api__httpsgithub_com_open_refine_open_refinewiki_reconciliation_service_api) | **GET** /reconcile/ | OpenRefine Reconcilation Service API
*ReconcileApi* | [**openrefine_data_extension_api_httpsgithub_com_open_refine_open_refinewiki_data_extension_api**](docs/ReconcileApi.md#openrefine_data_extension_api_httpsgithub_com_open_refine_open_refinewiki_data_extension_api) | **GET** /reconcile/properties | Openrefine Data-Extension-API
*ReconcileApi* | [**openrefine_suggest_api_flyout_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](docs/ReconcileApi.md#openrefine_suggest_api_flyout_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/flyout/entity | Openrefine Suggest-API suggest Entry Point
*ReconcileApi* | [**openrefine_suggest_api_flyout_property_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](docs/ReconcileApi.md#openrefine_suggest_api_flyout_property_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/flyout/property | Openrefine Suggest-API suggest Entry Point
*ReconcileApi* | [**openrefine_suggest_api_flyout_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](docs/ReconcileApi.md#openrefine_suggest_api_flyout_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/flyout/type | Openrefine Suggest-API suggest Entry Point
*ReconcileApi* | [**openrefine_suggest_api_suggest_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](docs/ReconcileApi.md#openrefine_suggest_api_suggest_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/suggest/entity | Openrefine Suggest-API suggest Entry Point
*ReconcileApi* | [**openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](docs/ReconcileApi.md#openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/suggest/property | Openrefine Suggest-API suggest Entry Point
*ReconcileApi* | [**openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api_0**](docs/ReconcileApi.md#openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api_0) | **GET** /reconcile/suggest/type | Openrefine Suggest-API suggest Entry Point
*ReconcileApi* | [**post_api_data**](docs/ReconcileApi.md#post_api_data) | **POST** /reconcile/ | OpenRefine Reconcilation Service API
*SearchAndAccessApi* | [**get_document_out_of_an_entity_type**](docs/SearchAndAccessApi.md#get_document_out_of_an_entity_type) | **GET** /{entity_type}/{id} | get a single record of an entity-index, or search for all records containing this record as an attribute via isAttr parameter
*SearchAndAccessApi* | [**search_in_index**](docs/SearchAndAccessApi.md#search_in_index) | **GET** /{entity_type}/search | search on one given entity-index
*SearchAndAccessApi* | [**search_over_all_indices**](docs/SearchAndAccessApi.md#search_over_all_indices) | **GET** /search | search over all entity-indices
*SourceApi* | [**get_source_record_by_entity_and_entity_id**](docs/SourceApi.md#get_source_record_by_entity_and_entity_id) | **GET** /source/{source_index}/{id} | 


## Documentation For Models



## Documentation For Authorization

 All endpoints do not require authorization.


## Author
