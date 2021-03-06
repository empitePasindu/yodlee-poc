# coding: utf-8

# flake8: noqa

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.accounts_api import AccountsApi
from swagger_client.api.auth_api import AuthApi
from swagger_client.api.cobrand_api import CobrandApi
from swagger_client.api.configs_api import ConfigsApi
from swagger_client.api.consents_api import ConsentsApi
from swagger_client.api.data_extracts_api import DataExtractsApi
from swagger_client.api.derived_api import DerivedApi
from swagger_client.api.documents_api import DocumentsApi
from swagger_client.api.enrich_data_api import EnrichDataApi
from swagger_client.api.holdings_api import HoldingsApi
from swagger_client.api.institutions_api import InstitutionsApi
from swagger_client.api.provider_accounts_api import ProviderAccountsApi
from swagger_client.api.providers_api import ProvidersApi
from swagger_client.api.statements_api import StatementsApi
from swagger_client.api.transactions_api import TransactionsApi
from swagger_client.api.user_api import UserApi
from swagger_client.api.verification_api import VerificationApi
from swagger_client.api.verify_account_api import VerifyAccountApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.access_tokens import AccessTokens
from swagger_client.models.account import Account
from swagger_client.models.account_address import AccountAddress
from swagger_client.models.account_balance_response import AccountBalanceResponse
from swagger_client.models.account_dataset import AccountDataset
from swagger_client.models.account_historical_balances_response import AccountHistoricalBalancesResponse
from swagger_client.models.account_history import AccountHistory
from swagger_client.models.account_holder import AccountHolder
from swagger_client.models.account_latest_balance import AccountLatestBalance
from swagger_client.models.account_migration_response import AccountMigrationResponse
from swagger_client.models.account_profile import AccountProfile
from swagger_client.models.account_response import AccountResponse
from swagger_client.models.added_provider_account import AddedProviderAccount
from swagger_client.models.added_provider_account_response import AddedProviderAccountResponse
from swagger_client.models.api_key_output import ApiKeyOutput
from swagger_client.models.api_key_request import ApiKeyRequest
from swagger_client.models.api_key_response import ApiKeyResponse
from swagger_client.models.asset_classification import AssetClassification
from swagger_client.models.asset_classification_list import AssetClassificationList
from swagger_client.models.associated_account import AssociatedAccount
from swagger_client.models.associated_accounts_response import AssociatedAccountsResponse
from swagger_client.models.attribute import Attribute
from swagger_client.models.auto_refresh import AutoRefresh
from swagger_client.models.bank_transfer_code import BankTransferCode
from swagger_client.models.capability import Capability
from swagger_client.models.client_credential_token import ClientCredentialToken
from swagger_client.models.client_credential_token_response import ClientCredentialTokenResponse
from swagger_client.models.cobrand import Cobrand
from swagger_client.models.cobrand_login_request import CobrandLoginRequest
from swagger_client.models.cobrand_login_response import CobrandLoginResponse
from swagger_client.models.cobrand_notification_event import CobrandNotificationEvent
from swagger_client.models.cobrand_notification_response import CobrandNotificationResponse
from swagger_client.models.cobrand_public_key_response import CobrandPublicKeyResponse
from swagger_client.models.cobrand_session import CobrandSession
from swagger_client.models.configs_notification_event import ConfigsNotificationEvent
from swagger_client.models.configs_notification_response import ConfigsNotificationResponse
from swagger_client.models.configs_public_key import ConfigsPublicKey
from swagger_client.models.configs_public_key_response import ConfigsPublicKeyResponse
from swagger_client.models.consent import Consent
from swagger_client.models.consent_response import ConsentResponse
from swagger_client.models.contact import Contact
from swagger_client.models.container_attributes import ContainerAttributes
from swagger_client.models.coordinates import Coordinates
from swagger_client.models.coverage import Coverage
from swagger_client.models.coverage_amount import CoverageAmount
from swagger_client.models.create_account_info import CreateAccountInfo
from swagger_client.models.create_account_request import CreateAccountRequest
from swagger_client.models.create_cobrand_notification_event import CreateCobrandNotificationEvent
from swagger_client.models.create_cobrand_notification_event_request import CreateCobrandNotificationEventRequest
from swagger_client.models.create_configs_notification_event import CreateConfigsNotificationEvent
from swagger_client.models.create_configs_notification_event_request import CreateConfigsNotificationEventRequest
from swagger_client.models.create_consent import CreateConsent
from swagger_client.models.create_consent_request import CreateConsentRequest
from swagger_client.models.created_account_info import CreatedAccountInfo
from swagger_client.models.created_account_response import CreatedAccountResponse
from swagger_client.models.created_consent_response import CreatedConsentResponse
from swagger_client.models.data_extracts_account import DataExtractsAccount
from swagger_client.models.data_extracts_event import DataExtractsEvent
from swagger_client.models.data_extracts_event_data import DataExtractsEventData
from swagger_client.models.data_extracts_event_links import DataExtractsEventLinks
from swagger_client.models.data_extracts_event_response import DataExtractsEventResponse
from swagger_client.models.data_extracts_event_user_data import DataExtractsEventUserData
from swagger_client.models.data_extracts_holding import DataExtractsHolding
from swagger_client.models.data_extracts_provider_account import DataExtractsProviderAccount
from swagger_client.models.data_extracts_transaction import DataExtractsTransaction
from swagger_client.models.data_extracts_user import DataExtractsUser
from swagger_client.models.data_extracts_user_data import DataExtractsUserData
from swagger_client.models.data_extracts_user_data_response import DataExtractsUserDataResponse
from swagger_client.models.derived_category_summary import DerivedCategorySummary
from swagger_client.models.derived_category_summary_details import DerivedCategorySummaryDetails
from swagger_client.models.derived_holding import DerivedHolding
from swagger_client.models.derived_holding_summary_response import DerivedHoldingSummaryResponse
from swagger_client.models.derived_holdings_account import DerivedHoldingsAccount
from swagger_client.models.derived_holdings_links import DerivedHoldingsLinks
from swagger_client.models.derived_holdings_summary import DerivedHoldingsSummary
from swagger_client.models.derived_networth import DerivedNetworth
from swagger_client.models.derived_networth_historical_balance import DerivedNetworthHistoricalBalance
from swagger_client.models.derived_networth_response import DerivedNetworthResponse
from swagger_client.models.derived_transaction_summary_response import DerivedTransactionSummaryResponse
from swagger_client.models.derived_transactions_links import DerivedTransactionsLinks
from swagger_client.models.derived_transactions_summary import DerivedTransactionsSummary
from swagger_client.models.description import Description
from swagger_client.models.detail_category import DetailCategory
from swagger_client.models.document import Document
from swagger_client.models.document_download import DocumentDownload
from swagger_client.models.document_download_response import DocumentDownloadResponse
from swagger_client.models.document_response import DocumentResponse
from swagger_client.models.email import Email
from swagger_client.models.enrich_data_account import EnrichDataAccount
from swagger_client.models.enrich_data_request import EnrichDataRequest
from swagger_client.models.enrich_data_transaction import EnrichDataTransaction
from swagger_client.models.enrich_data_user import EnrichDataUser
from swagger_client.models.enrich_user_data import EnrichUserData
from swagger_client.models.enriched_transaction import EnrichedTransaction
from swagger_client.models.enriched_transaction_response import EnrichedTransactionResponse
from swagger_client.models.evaluate_account_address import EvaluateAccountAddress
from swagger_client.models.evaluate_address_request import EvaluateAddressRequest
from swagger_client.models.evaluate_address_response import EvaluateAddressResponse
from swagger_client.models.field import Field
from swagger_client.models.field_operation import FieldOperation
from swagger_client.models.full_account_number_list import FullAccountNumberList
from swagger_client.models.historical_balance import HistoricalBalance
from swagger_client.models.holding import Holding
from swagger_client.models.holding_asset_classification_list_response import HoldingAssetClassificationListResponse
from swagger_client.models.holding_response import HoldingResponse
from swagger_client.models.holding_securities_response import HoldingSecuritiesResponse
from swagger_client.models.holding_type_list_response import HoldingTypeListResponse
from swagger_client.models.identifier import Identifier
from swagger_client.models.institution import Institution
from swagger_client.models.institution_response import InstitutionResponse
from swagger_client.models.loan_payoff_details import LoanPayoffDetails
from swagger_client.models.login_form import LoginForm
from swagger_client.models.merchant import Merchant
from swagger_client.models.money import Money
from swagger_client.models.name import Name
from swagger_client.models.option import Option
from swagger_client.models.payment_bank_transfer_code import PaymentBankTransferCode
from swagger_client.models.payment_identifier import PaymentIdentifier
from swagger_client.models.payment_profile import PaymentProfile
from swagger_client.models.phone_number import PhoneNumber
from swagger_client.models.profile import Profile
from swagger_client.models.provider_account import ProviderAccount
from swagger_client.models.provider_account_detail import ProviderAccountDetail
from swagger_client.models.provider_account_detail_response import ProviderAccountDetailResponse
from swagger_client.models.provider_account_preferences import ProviderAccountPreferences
from swagger_client.models.provider_account_preferences_request import ProviderAccountPreferencesRequest
from swagger_client.models.provider_account_profile import ProviderAccountProfile
from swagger_client.models.provider_account_request import ProviderAccountRequest
from swagger_client.models.provider_account_response import ProviderAccountResponse
from swagger_client.models.provider_account_user_profile_response import ProviderAccountUserProfileResponse
from swagger_client.models.provider_detail import ProviderDetail
from swagger_client.models.provider_detail_response import ProviderDetailResponse
from swagger_client.models.provider_response import ProviderResponse
from swagger_client.models.providers import Providers
from swagger_client.models.providers_count import ProvidersCount
from swagger_client.models.providers_count_response import ProvidersCountResponse
from swagger_client.models.providers_dataset import ProvidersDataset
from swagger_client.models.reward_balance import RewardBalance
from swagger_client.models.row import Row
from swagger_client.models.rule_clause import RuleClause
from swagger_client.models.scope import Scope
from swagger_client.models.security import Security
from swagger_client.models.security_holding import SecurityHolding
from swagger_client.models.statement import Statement
from swagger_client.models.statement_response import StatementResponse
from swagger_client.models.stock_exchange_detail import StockExchangeDetail
from swagger_client.models.total_count import TotalCount
from swagger_client.models.transaction import Transaction
from swagger_client.models.transaction_categorization_rule import TransactionCategorizationRule
from swagger_client.models.transaction_categorization_rule_info import TransactionCategorizationRuleInfo
from swagger_client.models.transaction_categorization_rule_request import TransactionCategorizationRuleRequest
from swagger_client.models.transaction_categorization_rule_response import TransactionCategorizationRuleResponse
from swagger_client.models.transaction_category import TransactionCategory
from swagger_client.models.transaction_category_request import TransactionCategoryRequest
from swagger_client.models.transaction_category_response import TransactionCategoryResponse
from swagger_client.models.transaction_count import TransactionCount
from swagger_client.models.transaction_count_response import TransactionCountResponse
from swagger_client.models.transaction_days import TransactionDays
from swagger_client.models.transaction_request import TransactionRequest
from swagger_client.models.transaction_response import TransactionResponse
from swagger_client.models.transaction_total import TransactionTotal
from swagger_client.models.update_account_info import UpdateAccountInfo
from swagger_client.models.update_account_request import UpdateAccountRequest
from swagger_client.models.update_category_request import UpdateCategoryRequest
from swagger_client.models.update_cobrand_notification_event import UpdateCobrandNotificationEvent
from swagger_client.models.update_cobrand_notification_event_request import UpdateCobrandNotificationEventRequest
from swagger_client.models.update_configs_notification_event import UpdateConfigsNotificationEvent
from swagger_client.models.update_configs_notification_event_request import UpdateConfigsNotificationEventRequest
from swagger_client.models.update_consent import UpdateConsent
from swagger_client.models.update_consent_request import UpdateConsentRequest
from swagger_client.models.update_transaction import UpdateTransaction
from swagger_client.models.update_user_registration import UpdateUserRegistration
from swagger_client.models.update_user_request import UpdateUserRequest
from swagger_client.models.update_verification import UpdateVerification
from swagger_client.models.update_verification_request import UpdateVerificationRequest
from swagger_client.models.updated_consent_response import UpdatedConsentResponse
from swagger_client.models.updated_provider_account import UpdatedProviderAccount
from swagger_client.models.updated_provider_account_response import UpdatedProviderAccountResponse
from swagger_client.models.user import User
from swagger_client.models.user_access_token import UserAccessToken
from swagger_client.models.user_access_tokens_response import UserAccessTokensResponse
from swagger_client.models.user_address import UserAddress
from swagger_client.models.user_detail import UserDetail
from swagger_client.models.user_detail_response import UserDetailResponse
from swagger_client.models.user_registration import UserRegistration
from swagger_client.models.user_request import UserRequest
from swagger_client.models.user_request_preferences import UserRequestPreferences
from swagger_client.models.user_response import UserResponse
from swagger_client.models.user_response_preferences import UserResponsePreferences
from swagger_client.models.user_session import UserSession
from swagger_client.models.verification import Verification
from swagger_client.models.verification_account import VerificationAccount
from swagger_client.models.verification_bank_transfer_code import VerificationBankTransferCode
from swagger_client.models.verification_request import VerificationRequest
from swagger_client.models.verification_response import VerificationResponse
from swagger_client.models.verification_status import VerificationStatus
from swagger_client.models.verification_status_response import VerificationStatusResponse
from swagger_client.models.verification_transaction import VerificationTransaction
from swagger_client.models.verified_account import VerifiedAccount
from swagger_client.models.verified_account_response import VerifiedAccountResponse
from swagger_client.models.verified_accounts import VerifiedAccounts
from swagger_client.models.verify_account import VerifyAccount
from swagger_client.models.verify_account_request import VerifyAccountRequest
from swagger_client.models.verify_account_response import VerifyAccountResponse
from swagger_client.models.verify_transaction_criteria import VerifyTransactionCriteria
from swagger_client.models.yodlee_error import YodleeError
