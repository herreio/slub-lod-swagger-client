# swagger_client.AuthoritySearchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_record_by_authority_id**](AuthoritySearchApi.md#get_record_by_authority_id) | **GET** /{authority_provider}/{id} | search for an given ID of a given authority-provider
[**get_record_by_authority_id_and_entity_id**](AuthoritySearchApi.md#get_record_by_authority_id_and_entity_id) | **GET** /{authority_provider}/{entity_type}/{id} | search for an given ID of a given authority-provider on a given entity-index


# **get_record_by_authority_id**
> get_record_by_authority_id(id, authority_provider, format=format, size=size, _from=_from)

search for an given ID of a given authority-provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthoritySearchApi()
id = 'id_example' # str | The ID-String of the authority-identifier to access. Possible Values (examples): 208922695, 118695940, 20474817, Q1585819
authority_provider = 'authority_provider_example' # str | The name of the authority-provider to access. Allowed Values: ['isni', 'orcid', 'viaf', 'lc', 'filmportal.de', 'wd', 'swb', 'gnd'].
format = 'format_example' # str | set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json (optional)
size = 100 # int | Configure the maxmimum amount of hits to be returned (optional) (default to 100)
_from = 0 # int | Configure the offset from the frist result you want to fetch (optional) (default to 0)

try:
    # search for an given ID of a given authority-provider
    api_instance.get_record_by_authority_id(id, authority_provider, format=format, size=size, _from=_from)
except ApiException as e:
    print("Exception when calling AuthoritySearchApi->get_record_by_authority_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID-String of the authority-identifier to access. Possible Values (examples): 208922695, 118695940, 20474817, Q1585819 | 
 **authority_provider** | **str**| The name of the authority-provider to access. Allowed Values: [&#39;isni&#39;, &#39;orcid&#39;, &#39;viaf&#39;, &#39;lc&#39;, &#39;filmportal.de&#39;, &#39;wd&#39;, &#39;swb&#39;, &#39;gnd&#39;]. | 
 **format** | **str**| set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json | [optional] 
 **size** | **int**| Configure the maxmimum amount of hits to be returned | [optional] [default to 100]
 **_from** | **int**| Configure the offset from the frist result you want to fetch | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record_by_authority_id_and_entity_id**
> get_record_by_authority_id_and_entity_id(id, entity_type, authority_provider, format=format, size=size, _from=_from)

search for an given ID of a given authority-provider on a given entity-index

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthoritySearchApi()
id = 'id_example' # str | The ID-String of the authority-identifier to access. Possible Values (examples): 208922695, 118695940, 20474817, Q1585819
entity_type = 'entity_type_example' # str | The name of the entity-index to access. Allowed Values: ['organizations', 'works', 'events', 'topics', 'persons', 'resources', 'geo'].
authority_provider = 'authority_provider_example' # str | The name of the authority-provider to access. Allowed Values: ['isni', 'orcid', 'viaf', 'lc', 'filmportal.de', 'wd', 'swb', 'gnd'].
format = 'format_example' # str | set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json (optional)
size = 100 # int | Configure the maxmimum amount of hits to be returned (optional) (default to 100)
_from = 0 # int | Configure the offset from the frist result you want to fetch (optional) (default to 0)

try:
    # search for an given ID of a given authority-provider on a given entity-index
    api_instance.get_record_by_authority_id_and_entity_id(id, entity_type, authority_provider, format=format, size=size, _from=_from)
except ApiException as e:
    print("Exception when calling AuthoritySearchApi->get_record_by_authority_id_and_entity_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID-String of the authority-identifier to access. Possible Values (examples): 208922695, 118695940, 20474817, Q1585819 | 
 **entity_type** | **str**| The name of the entity-index to access. Allowed Values: [&#39;organizations&#39;, &#39;works&#39;, &#39;events&#39;, &#39;topics&#39;, &#39;persons&#39;, &#39;resources&#39;, &#39;geo&#39;]. | 
 **authority_provider** | **str**| The name of the authority-provider to access. Allowed Values: [&#39;isni&#39;, &#39;orcid&#39;, &#39;viaf&#39;, &#39;lc&#39;, &#39;filmportal.de&#39;, &#39;wd&#39;, &#39;swb&#39;, &#39;gnd&#39;]. | 
 **format** | **str**| set the Content-Type over this Query-Parameter. Allowed: nt, rdf, ttl, nq, jsonl, json | [optional] 
 **size** | **int**| Configure the maxmimum amount of hits to be returned | [optional] [default to 100]
 **_from** | **int**| Configure the offset from the frist result you want to fetch | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

