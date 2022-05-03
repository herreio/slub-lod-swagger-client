# swagger_client.SearchAndAccessApi

All URIs are relative to *https://data.slub-dresden.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_out_of_an_entity_type**](SearchAndAccessApi.md#get_document_out_of_an_entity_type) | **GET** /{entity_type}/{id} | get a single record of an entity-index, or search for all records containing this record as an attribute via isAttr parameter
[**search_in_index**](SearchAndAccessApi.md#search_in_index) | **GET** /{entity_type}/search | search on one given entity-index
[**search_over_all_indices**](SearchAndAccessApi.md#search_over_all_indices) | **GET** /search | search over all entity-indices


# **get_document_out_of_an_entity_type**
> get_document_out_of_an_entity_type(id, entity_type, format=format)

get a single record of an entity-index, or search for all records containing this record as an attribute via isAttr parameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchAndAccessApi()
id = 'id_example' # str | The ID-String of the record to access. Possible Values (examples):118695940, 130909696
entity_type = 'entity_type_example' # str | The name of the entity-type to access. Allowed Values: ['organizations', 'works', 'events', 'topics', 'persons', 'resources', 'geo'].
format = 'format_example' # str | set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json (optional)

try:
    # get a single record of an entity-index, or search for all records containing this record as an attribute via isAttr parameter
    api_instance.get_document_out_of_an_entity_type(id, entity_type, format=format)
except ApiException as e:
    print("Exception when calling SearchAndAccessApi->get_document_out_of_an_entity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID-String of the record to access. Possible Values (examples):118695940, 130909696 | 
 **entity_type** | **str**| The name of the entity-type to access. Allowed Values: [&#39;organizations&#39;, &#39;works&#39;, &#39;events&#39;, &#39;topics&#39;, &#39;persons&#39;, &#39;resources&#39;, &#39;geo&#39;]. | 
 **format** | **str**| set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_in_index**
> search_in_index(entity_type, q=q, format=format, size=size, _from=_from, sort=sort, filter=filter)

search on one given entity-index

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchAndAccessApi()
entity_type = 'entity_type_example' # str | The name of the entity-type to access. Allowed Values: ['organizations', 'works', 'events', 'topics', 'persons', 'resources', 'geo'].
q = 'q_example' # str | Lucene Query String Search Parameter (optional)
format = 'format_example' # str | set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json (optional)
size = 100 # int | Configure the maxmimum amount of hits to be returned (optional) (default to 100)
_from = 0 # int | Configure the offset from the frist result you want to fetch (optional) (default to 0)
sort = 'sort_example' # str | how to sort the returned datasets. like: path_to_property:[asc|desc] (optional)
filter = 'filter_example' # str | filter the search by a defined value in a path. e.g. path_to_property:value (optional)

try:
    # search on one given entity-index
    api_instance.search_in_index(entity_type, q=q, format=format, size=size, _from=_from, sort=sort, filter=filter)
except ApiException as e:
    print("Exception when calling SearchAndAccessApi->search_in_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The name of the entity-type to access. Allowed Values: [&#39;organizations&#39;, &#39;works&#39;, &#39;events&#39;, &#39;topics&#39;, &#39;persons&#39;, &#39;resources&#39;, &#39;geo&#39;]. | 
 **q** | **str**| Lucene Query String Search Parameter | [optional] 
 **format** | **str**| set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json | [optional] 
 **size** | **int**| Configure the maxmimum amount of hits to be returned | [optional] [default to 100]
 **_from** | **int**| Configure the offset from the frist result you want to fetch | [optional] [default to 0]
 **sort** | **str**| how to sort the returned datasets. like: path_to_property:[asc|desc] | [optional] 
 **filter** | **str**| filter the search by a defined value in a path. e.g. path_to_property:value | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_over_all_indices**
> search_over_all_indices(q=q, format=format, sort=sort, size=size, _from=_from, filter=filter)

search over all entity-indices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchAndAccessApi()
q = 'q_example' # str | Lucene Query String Search Parameter (optional)
format = 'format_example' # str | set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json (optional)
sort = 'sort_example' # str | how to sort the returned datasets. like: path_to_property:[asc|desc] (optional)
size = 56 # int | Configure the maxmimum amount of hits to be returned (optional)
_from = 56 # int | Configure the offset from the frist result you want to fetch (optional)
filter = 'filter_example' # str | filter the search by a defined value in a path. e.g. path_to_property:value (optional)

try:
    # search over all entity-indices
    api_instance.search_over_all_indices(q=q, format=format, sort=sort, size=size, _from=_from, filter=filter)
except ApiException as e:
    print("Exception when calling SearchAndAccessApi->search_over_all_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Lucene Query String Search Parameter | [optional] 
 **format** | **str**| set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json | [optional] 
 **sort** | **str**| how to sort the returned datasets. like: path_to_property:[asc|desc] | [optional] 
 **size** | **int**| Configure the maxmimum amount of hits to be returned | [optional] 
 **_from** | **int**| Configure the offset from the frist result you want to fetch | [optional] 
 **filter** | **str**| filter the search by a defined value in a path. e.g. path_to_property:value | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

