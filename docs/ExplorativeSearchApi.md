# swagger_client.ExplorativeSearchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_top_authors_date_published_and_related_topics_around_topics**](ExplorativeSearchApi.md#aggregate_top_authors_date_published_and_related_topics_around_topics) | **GET** /explore/aggregations | aggregate topAuthors, datePublished and relatedTopics around topics
[**correlate_topics_with_their_mutual_occurances**](ExplorativeSearchApi.md#correlate_topics_with_their_mutual_occurances) | **GET** /explore/correlations | correlate topics with their mutual occurances
[**query_topics**](ExplorativeSearchApi.md#query_topics) | **GET** /explore/topicsearch | perform a simple serach on the topics index


# **aggregate_top_authors_date_published_and_related_topics_around_topics**
> aggregate_top_authors_date_published_and_related_topics_around_topics(topics, author=author, restrict=restrict)

aggregate topAuthors, datePublished and relatedTopics around topics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExplorativeSearchApi()
topics = ['topics_example'] # list[str] | multiple topics to aggregate
author = 'author_example' # str | use this specific author name as filter for the aggregation result (optional)
restrict = 'restrict_example' # str | restrict all topic queries to occurrences with this restriction-topic (optional)

try:
    # aggregate topAuthors, datePublished and relatedTopics around topics
    api_instance.aggregate_top_authors_date_published_and_related_topics_around_topics(topics, author=author, restrict=restrict)
except ApiException as e:
    print("Exception when calling ExplorativeSearchApi->aggregate_top_authors_date_published_and_related_topics_around_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topics** | [**list[str]**](str.md)| multiple topics to aggregate | 
 **author** | **str**| use this specific author name as filter for the aggregation result | [optional] 
 **restrict** | **str**| restrict all topic queries to occurrences with this restriction-topic | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **correlate_topics_with_their_mutual_occurances**
> correlate_topics_with_their_mutual_occurances(topics)

correlate topics with their mutual occurances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExplorativeSearchApi()
topics = ['topics_example'] # list[str] | multiple topics to correlate

try:
    # correlate topics with their mutual occurances
    api_instance.correlate_topics_with_their_mutual_occurances(topics)
except ApiException as e:
    print("Exception when calling ExplorativeSearchApi->correlate_topics_with_their_mutual_occurances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topics** | [**list[str]**](str.md)| multiple topics to correlate | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_topics**
> query_topics(q, size=size, fields=fields)

perform a simple serach on the topics index

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExplorativeSearchApi()
q = 'q_example' # str | query string to search
size = 15 # int | size of the response (optional) (default to 15)
fields = ['[preferredName^2, alternateName, description, additionalType.description, additionalType.name]'] # list[str] | list of internal elasticsearch fields to query against. (optional) (default to [preferredName^2, alternateName, description, additionalType.description, additionalType.name])

try:
    # perform a simple serach on the topics index
    api_instance.query_topics(q, size=size, fields=fields)
except ApiException as e:
    print("Exception when calling ExplorativeSearchApi->query_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| query string to search | 
 **size** | **int**| size of the response | [optional] [default to 15]
 **fields** | [**list[str]**](str.md)| list of internal elasticsearch fields to query against. | [optional] [default to [preferredName^2, alternateName, description, additionalType.description, additionalType.name]]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

