# swagger_client.VerifyAccountApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**initiate_account_verification**](VerifyAccountApi.md#initiate_account_verification) | **POST** /verifyAccount/{providerAccountId} | Verify Accounts Using Transactions


# **initiate_account_verification**
> VerifyAccountResponse initiate_account_verification(provider_account_id, verification_param)

Verify Accounts Using Transactions

The verify account service is used to verify the account's ownership by  matching the transaction details with the accounts aggregated for the user.<br><ul><li>If a match is identified, the service returns details of all the accounts along with the matched transaction's details.<li>If no transaction match is found, an empty response will be returned.<li>A maximum of 5 transactionCriteria can be passed in a request.<li>The baseType, date, and amount parameters should mandatorily be passed.<li>The optional dateVariance parameter cannot be more than 7 days. For example, +7, -4, or +/-2.<li>Pass the container or accountId parameters for better performance.<li>This service supports the localization feature and accepts locale as a header parameter.</li></ul>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerifyAccountApi()
provider_account_id = 'provider_account_id_example' # str | providerAccountId
verification_param = swagger_client.VerifyAccountRequest() # VerifyAccountRequest | verificationParam

try:
    # Verify Accounts Using Transactions
    api_response = api_instance.initiate_account_verification(provider_account_id, verification_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerifyAccountApi->initiate_account_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_account_id** | **str**| providerAccountId | 
 **verification_param** | [**VerifyAccountRequest**](VerifyAccountRequest.md)| verificationParam | 

### Return type

[**VerifyAccountResponse**](VerifyAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

