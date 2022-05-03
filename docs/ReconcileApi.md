# swagger_client.ReconcileApi

All URIs are relative to *https://data.slub-dresden.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**open_refine_reconcilation_service_api__httpsgithub_com_open_refine_open_refinewiki_reconciliation_service_api**](ReconcileApi.md#open_refine_reconcilation_service_api__httpsgithub_com_open_refine_open_refinewiki_reconciliation_service_api) | **GET** /reconcile/ | OpenRefine Reconcilation Service API
[**openrefine_data_extension_api_httpsgithub_com_open_refine_open_refinewiki_data_extension_api**](ReconcileApi.md#openrefine_data_extension_api_httpsgithub_com_open_refine_open_refinewiki_data_extension_api) | **GET** /reconcile/properties | Openrefine Data-Extension-API
[**openrefine_suggest_api_flyout_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](ReconcileApi.md#openrefine_suggest_api_flyout_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/flyout/entity | Openrefine Suggest-API suggest Entry Point
[**openrefine_suggest_api_flyout_property_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](ReconcileApi.md#openrefine_suggest_api_flyout_property_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/flyout/property | Openrefine Suggest-API suggest Entry Point
[**openrefine_suggest_api_flyout_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](ReconcileApi.md#openrefine_suggest_api_flyout_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/flyout/type | Openrefine Suggest-API suggest Entry Point
[**openrefine_suggest_api_suggest_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](ReconcileApi.md#openrefine_suggest_api_suggest_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/suggest/entity | Openrefine Suggest-API suggest Entry Point
[**openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**](ReconcileApi.md#openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api) | **GET** /reconcile/suggest/property | Openrefine Suggest-API suggest Entry Point
[**openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api_0**](ReconcileApi.md#openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api_0) | **GET** /reconcile/suggest/type | Openrefine Suggest-API suggest Entry Point
[**post_api_data**](ReconcileApi.md#post_api_data) | **POST** /reconcile/ | OpenRefine Reconcilation Service API


# **open_refine_reconcilation_service_api__httpsgithub_com_open_refine_open_refinewiki_reconciliation_service_api**
> open_refine_reconcilation_service_api__httpsgithub_com_open_refine_open_refinewiki_reconciliation_service_api()

OpenRefine Reconcilation Service API

https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation-Service-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()

try:
    # OpenRefine Reconcilation Service API
    api_instance.open_refine_reconcilation_service_api__httpsgithub_com_open_refine_open_refinewiki_reconciliation_service_api()
except ApiException as e:
    print("Exception when calling ReconcileApi->open_refine_reconcilation_service_api__httpsgithub_com_open_refine_open_refinewiki_reconciliation_service_api: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openrefine_data_extension_api_httpsgithub_com_open_refine_open_refinewiki_data_extension_api**
> openrefine_data_extension_api_httpsgithub_com_open_refine_open_refinewiki_data_extension_api(queries=queries, type=type, limit=limit)

Openrefine Data-Extension-API

https://github.com/OpenRefine/OpenRefine/wiki/Data-Extension-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()
queries = 'queries_example' # str | OpenRefine Reconcilation API Call for Multiple Queries (optional)
type = 'type_example' # str | type string (optional)
limit = 'limit_example' # str | how many properties shall be returned (optional)

try:
    # Openrefine Data-Extension-API
    api_instance.openrefine_data_extension_api_httpsgithub_com_open_refine_open_refinewiki_data_extension_api(queries=queries, type=type, limit=limit)
except ApiException as e:
    print("Exception when calling ReconcileApi->openrefine_data_extension_api_httpsgithub_com_open_refine_open_refinewiki_data_extension_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queries** | **str**| OpenRefine Reconcilation API Call for Multiple Queries | [optional] 
 **type** | **str**| type string | [optional] 
 **limit** | **str**| how many properties shall be returned | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openrefine_suggest_api_flyout_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**
> openrefine_suggest_api_flyout_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(id=id)

Openrefine Suggest-API suggest Entry Point

https://github.com/OpenRefine/OpenRefine/wiki/Suggest-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()
id = 'id_example' # str | the identifier of the entity to render (optional)

try:
    # Openrefine Suggest-API suggest Entry Point
    api_instance.openrefine_suggest_api_flyout_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(id=id)
except ApiException as e:
    print("Exception when calling ReconcileApi->openrefine_suggest_api_flyout_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the identifier of the entity to render | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openrefine_suggest_api_flyout_property_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**
> openrefine_suggest_api_flyout_property_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(id=id)

Openrefine Suggest-API suggest Entry Point

https://github.com/OpenRefine/OpenRefine/wiki/Suggest-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()
id = 'id_example' # str | the identifier of the property to render (optional)

try:
    # Openrefine Suggest-API suggest Entry Point
    api_instance.openrefine_suggest_api_flyout_property_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(id=id)
except ApiException as e:
    print("Exception when calling ReconcileApi->openrefine_suggest_api_flyout_property_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the identifier of the property to render | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openrefine_suggest_api_flyout_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**
> openrefine_suggest_api_flyout_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(id=id)

Openrefine Suggest-API suggest Entry Point

https://github.com/OpenRefine/OpenRefine/wiki/Suggest-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()
id = 'id_example' # str | the identifier of the type to render (optional)

try:
    # Openrefine Suggest-API suggest Entry Point
    api_instance.openrefine_suggest_api_flyout_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(id=id)
except ApiException as e:
    print("Exception when calling ReconcileApi->openrefine_suggest_api_flyout_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the identifier of the type to render | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openrefine_suggest_api_suggest_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**
> openrefine_suggest_api_suggest_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(prefix=prefix)

Openrefine Suggest-API suggest Entry Point

https://github.com/OpenRefine/OpenRefine/wiki/Suggest-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()
prefix = 'prefix_example' # str | a string the user has typed (optional)

try:
    # Openrefine Suggest-API suggest Entry Point
    api_instance.openrefine_suggest_api_suggest_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(prefix=prefix)
except ApiException as e:
    print("Exception when calling ReconcileApi->openrefine_suggest_api_suggest_entity_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| a string the user has typed | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api**
> openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(prefix=prefix)

Openrefine Suggest-API suggest Entry Point

https://github.com/OpenRefine/OpenRefine/wiki/Suggest-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()
prefix = 'prefix_example' # str | a string the user has typed (optional)

try:
    # Openrefine Suggest-API suggest Entry Point
    api_instance.openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api(prefix=prefix)
except ApiException as e:
    print("Exception when calling ReconcileApi->openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| a string the user has typed | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api_0**
> openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api_0(prefix=prefix)

Openrefine Suggest-API suggest Entry Point

https://github.com/OpenRefine/OpenRefine/wiki/Suggest-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()
prefix = 'prefix_example' # str | a string the user has typed (optional)

try:
    # Openrefine Suggest-API suggest Entry Point
    api_instance.openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api_0(prefix=prefix)
except ApiException as e:
    print("Exception when calling ReconcileApi->openrefine_suggest_api_suggest_type_entry_point__httpsgithub_com_open_refine_open_refinewiki_suggest_api_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| a string the user has typed | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_data**
> post_api_data()

OpenRefine Reconcilation Service API

https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation-Service-API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReconcileApi()

try:
    # OpenRefine Reconcilation Service API
    api_instance.post_api_data()
except ApiException as e:
    print("Exception when calling ReconcileApi->post_api_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

