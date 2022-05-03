# swagger_client.SourceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_source_record_by_entity_and_entity_id**](SourceApi.md#get_source_record_by_entity_and_entity_id) | **GET** /source/{source_index}/{id} | 


# **get_source_record_by_entity_and_entity_id**
> get_source_record_by_entity_and_entity_id(id, source_index)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SourceApi()
id = 'id_example' # str | The ID-String of the entity to access.
source_index = 'source_index_example' # str | The name of the source-index to access the source-data.Allowed Values: ['kxp-de14', 'swb-aut', 'gnd_marc21']

try:
    api_instance.get_source_record_by_entity_and_entity_id(id, source_index)
except ApiException as e:
    print("Exception when calling SourceApi->get_source_record_by_entity_and_entity_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID-String of the entity to access. | 
 **source_index** | **str**| The name of the source-index to access the source-data.Allowed Values: [&#39;kxp-de14&#39;, &#39;swb-aut&#39;, &#39;gnd_marc21&#39;] | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

