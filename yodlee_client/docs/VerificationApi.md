# swagger_client.VerificationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_verification_status**](VerificationApi.md#get_verification_status) | **GET** /verification | Get Verification Status
[**get_verified_accounts**](VerificationApi.md#get_verified_accounts) | **GET** /verification/verifiedAccounts | Get Verified Accounts
[**initiate_matching_or_challenge_deposite_verification**](VerificationApi.md#initiate_matching_or_challenge_deposite_verification) | **POST** /verification | Initiaite Challenge Deposit
[**verify_challenge_deposit**](VerificationApi.md#verify_challenge_deposit) | **PUT** /verification | Verify Challenge Deposit


# **get_verification_status**
> VerificationStatusResponse get_verification_status(account_id=account_id, provider_account_id=provider_account_id, verification_type=verification_type)

Get Verification Status

The get verification status service is used to retrieve the verification status of all accounts for which the MS or CDV process has been initiated.<br>For the MS process, the account details object returns the aggregated information of the verified accounts. For the CDV process, the account details object returns the user provided account information.<br>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerificationApi()
account_id = 'account_id_example' # str | Comma separated accountId (optional)
provider_account_id = 'provider_account_id_example' # str | Comma separated providerAccountId (optional)
verification_type = 'verification_type_example' # str | verificationType (optional)

try:
    # Get Verification Status
    api_response = api_instance.get_verification_status(account_id=account_id, provider_account_id=provider_account_id, verification_type=verification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->get_verification_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Comma separated accountId | [optional] 
 **provider_account_id** | **str**| Comma separated providerAccountId | [optional] 
 **verification_type** | **str**| verificationType | [optional] 

### Return type

[**VerificationStatusResponse**](VerificationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verified_accounts**
> VerifiedAccountResponse get_verified_accounts(provider_account_id, account_id=account_id, is_selected=is_selected, verification_status=verification_status)

Get Verified Accounts

The Verified Accounts API v1.1 provides information of bank and investment accounts that are verified by the user and applies only to Instant Account Verification (IAV) customers using FastLink 4.0. By default, the API only returns successfully verified accounts's information. <br><br>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerificationApi()
provider_account_id = 'provider_account_id_example' # str | providerAccountId.
account_id = 'account_id_example' # str | Comma separated accountIds. (optional)
is_selected = 'is_selected_example' # str | Comma separated isSelected. Allowed values are true, false (optional)
verification_status = 'verification_status_example' # str | Comma separated verificationStatus. Allowed values are SUCCESS, FAILED (optional)

try:
    # Get Verified Accounts
    api_response = api_instance.get_verified_accounts(provider_account_id, account_id=account_id, is_selected=is_selected, verification_status=verification_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->get_verified_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_account_id** | **str**| providerAccountId. | 
 **account_id** | **str**| Comma separated accountIds. | [optional] 
 **is_selected** | **str**| Comma separated isSelected. Allowed values are true, false | [optional] 
 **verification_status** | **str**| Comma separated verificationStatus. Allowed values are SUCCESS, FAILED | [optional] 

### Return type

[**VerifiedAccountResponse**](VerifiedAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_matching_or_challenge_deposite_verification**
> VerificationResponse initiate_matching_or_challenge_deposite_verification(verification_param)

Initiaite Challenge Deposit

The post verification service is used to initiate the matching service (MS) and the challenge deposit account verification (CDV) process to verify account ownership.<br>The MS and CDV process can verify ownership of only bank accounts (i.e., checking and savings).<br>The MS verification can be initiated only for an already aggregated account or a providerAccount.<br>The prerequisite for the MS verification process is to request the ACCT_PROFILE dataset with the HOLDER_NAME attribute.<br>In the MS verification process, a string-match of the account holder name with the registered user name is performed instantaneously. You can contact the Yodlee CustomerCare to configure the full name or only the last name match.<br>Once the CDV process is initiated Yodlee will post the microtransaction (i.e., credit and debit) in the user's account. The CDV process takes 2 to 3 days to complete as it requires the user to provide the microtransaction details.<br>The CDV process is currently supported only in the United States.<br>The verificationId in the response can be used to track the verification request.<br><br><b>Notes:</b><li>This endpoint cannot be used to test the CDV functionality in the developer sandbox or test environment. You will need a money transmitter license to implement the CDV functionality and also require the Yodlee Professional Services team's assistance to set up a dedicated environment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerificationApi()
verification_param = swagger_client.VerificationRequest() # VerificationRequest | verification information

try:
    # Initiaite Challenge Deposit
    api_response = api_instance.initiate_matching_or_challenge_deposite_verification(verification_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->initiate_matching_or_challenge_deposite_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_param** | [**VerificationRequest**](VerificationRequest.md)| verification information | 

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_challenge_deposit**
> VerificationResponse verify_challenge_deposit(verification_param)

Verify Challenge Deposit

The put verification service is used to complete the challenge deposit verification (CDV) process.<br>This service is used only by the customer of CDV flow.<br>In the CDV process, the user-provided microtransaction details (i.e., credit and debit) is matched against the microtransactions posted by Yodlee. For a successful verification of the account's ownership both the microtransaction details should match.<br>The CDV process is currently supported only in the United States.<br><br><b>Notes:</b><ul><li>This endpoint cannot be used to test the CDV functionality in the developer sandbox or test environment. You will need a money transmitter license to implement the CDV functionality and also require the Yodlee Professional Services team's assistance to set up a dedicated environment.</li></ul>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VerificationApi()
verification_param = swagger_client.UpdateVerificationRequest() # UpdateVerificationRequest | verification information

try:
    # Verify Challenge Deposit
    api_response = api_instance.verify_challenge_deposit(verification_param)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VerificationApi->verify_challenge_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_param** | [**UpdateVerificationRequest**](UpdateVerificationRequest.md)| verification information | 

### Return type

[**VerificationResponse**](VerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

