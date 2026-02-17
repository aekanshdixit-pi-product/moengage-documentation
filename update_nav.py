#!/usr/bin/env python3
"""Update docs.json Developer Guide navigation to use clean file paths matching Zendesk structure."""
import json

with open("docs.json", "r") as f:
    docs = json.load(f)

dg = "developer-guide"

new_groups = [
    {
        "group": "iOS SDK",
        "pages": [
            {
                "group": "SDK Integration",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/ios-sdk/sdk-integration/basic/sdk-integration",
                            f"{dg}/ios-sdk/sdk-integration/basic/sdk-initialization",
                            f"{dg}/ios-sdk/sdk-integration/basic/data-center"
                        ]
                    },
                    {
                        "group": "Advanced",
                        "pages": [
                            f"{dg}/ios-sdk/sdk-integration/advanced/add-on-security"
                        ]
                    }
                ]
            },
            {
                "group": "Data Tracking",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/ios-sdk/data-tracking/basic/install-update-differentiation",
                            f"{dg}/ios-sdk/data-tracking/basic/tracking-user-attributes",
                            f"{dg}/ios-sdk/data-tracking/basic/tracking-events"
                        ]
                    },
                    {
                        "group": "Advanced",
                        "pages": [
                            f"{dg}/ios-sdk/data-tracking/advanced/session-and-source-tracking"
                        ]
                    }
                ]
            },
            {
                "group": "Push",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/ios-sdk/push/basic/push-notifications",
                            f"{dg}/ios-sdk/push/basic/apns-authentication-key",
                            f"{dg}/ios-sdk/push/basic/apns-certificate-pem-file-legacy"
                        ]
                    },
                    {
                        "group": "Optional",
                        "pages": [
                            f"{dg}/ios-sdk/push/optional/push-templates",
                            f"{dg}/ios-sdk/push/optional/push-handled-by-application",
                            f"{dg}/ios-sdk/push/optional/actionable-notifications",
                            f"{dg}/ios-sdk/push/optional/real-time-triggers",
                            f"{dg}/ios-sdk/push/optional/ios-notification-center",
                            f"{dg}/ios-sdk/push/optional/location-triggered"
                        ]
                    },
                    {
                        "group": "Advanced",
                        "pages": [
                            f"{dg}/ios-sdk/push/advanced/custom-notification-handling"
                        ]
                    }
                ]
            },
            {
                "group": "In-App Messages",
                "pages": [f"{dg}/ios-sdk/in-app-messages/in-app-nativ"]
            },
            {
                "group": "Cards",
                "pages": [
                    f"{dg}/ios-sdk/cards/cards-in-ios",
                    f"{dg}/ios-sdk/cards/self-handled-cards"
                ]
            },
            {
                "group": "Checklist",
                "pages": [f"{dg}/ios-sdk/checklist/release-checklist"]
            },
            {
                "group": "Compliance",
                "pages": [f"{dg}/ios-sdk/compliance/compliance"]
            },
            {
                "group": "Manual Integration",
                "pages": [f"{dg}/ios-sdk/manual-integration/manual-integration"]
            },
            {
                "group": "Migration",
                "pages": [
                    f"{dg}/ios-sdk/migration/migration-to-sdk-version-900",
                    f"{dg}/ios-sdk/migration/migration-to-sdk-version-820",
                    f"{dg}/ios-sdk/migration/migration-to-sdk-version-700",
                    f"{dg}/ios-sdk/migration/migration-to-sdk-version-600"
                ]
            },
            {
                "group": "Framework Size Impact",
                "pages": [f"{dg}/ios-sdk/framework-size-impact/framework-size-impact"]
            },
            {
                "group": "OS Updates",
                "pages": [f"{dg}/ios-sdk/os-updates/ios-15"]
            },
            {
                "group": "Apple TV",
                "pages": [f"{dg}/ios-sdk/apple-tv/apple-tv"]
            },
            {
                "group": "Troubleshooting and FAQs",
                "pages": [f"{dg}/ios-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs"]
            },
            {
                "group": "Sample App",
                "pages": [f"{dg}/ios-sdk/sample-app/ios-sample-app"]
            },
            {
                "group": "Integration with Older Version of SDK",
                "pages": [
                    {
                        "group": "Integration",
                        "pages": [
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/integration/data-center",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/integration/sdk-initialization",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/integration/sdk-integration",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/integration/sdk-integration-7xx",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/integration/sdk-initialisation-7xx",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/integration/data-center-7xx"
                        ]
                    },
                    {
                        "group": "Data Tracking",
                        "pages": [
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/session-and-source-tracking",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-events",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-user-attributes",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/install-update-differentiation",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-user-attributes-7xx",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-events-7xx",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/session-and-source-tracking-7xx",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/install-or-update-differentiation-7xx"
                        ]
                    },
                    {
                        "group": "Push",
                        "pages": [
                            {
                                "group": "Basic",
                                "pages": [
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/basic/apns-certificate-pem-file",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/basic/push-notifications",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/basic/push-notifications-7xx",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/basic/apns-certificate-pem-file-7xx"
                                ]
                            },
                            {
                                "group": "Advanced",
                                "pages": [
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/push-notification-implementation",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/push-templates",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/actionable-notifications",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/real-time-triggers",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/ios-notification-center",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/location-triggered",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/push-notification-implementation-7xx",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/push-templates-7xx",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/actionable-notifications-7xx",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/real-time-triggers-7xx",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/ios-notification-center-7xx",
                                    f"{dg}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/location-triggered-7xx"
                                ]
                            }
                        ]
                    },
                    {
                        "group": "In-App Messages",
                        "pages": [
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/in-app-messages/in-app-nativ",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/in-app-messages/in-app-nativ-7xx",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/in-app-messages/in-app-nativ-6xx"
                        ]
                    },
                    {
                        "group": "Cards",
                        "pages": [
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/cards/self-handled-cards",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/cards/cards-in-ios",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/cards/cards-7xx"
                        ]
                    },
                    {
                        "group": "Checklist",
                        "pages": [
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/checklist/release-checklist",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/checklist/release-checklist-7xx"
                        ]
                    },
                    {
                        "group": "Compliance",
                        "pages": [
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/compliance/manual-integration",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/compliance/compliance",
                            f"{dg}/ios-sdk/integration-with-older-version-of-sdk/compliance/compliance-7xx"
                        ]
                    },
                    {
                        "group": "Framework Size Impact",
                        "pages": [f"{dg}/ios-sdk/integration-with-older-version-of-sdk/framework-size-impact/framework-size-impact-7xx"]
                    },
                    {
                        "group": "Troubleshooting and FAQs",
                        "pages": [f"{dg}/ios-sdk/integration-with-older-version-of-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs-7xx"]
                    }
                ]
            }
        ]
    },
    {
        "group": "Android SDK",
        "pages": [
            {
                "group": "SDK Integration",
                "pages": [
                    {
                        "group": "Basic Integration",
                        "pages": [
                            f"{dg}/android-sdk/sdk-integration/basic-integration/configuring-build-settings",
                            f"{dg}/android-sdk/sdk-integration/basic-integration/sdk-initialization",
                            f"{dg}/android-sdk/sdk-integration/basic-integration/data-center",
                            f"{dg}/android-sdk/sdk-integration/basic-integration/exclude-moengage-storage-file-from-auto-backup"
                        ]
                    },
                    {
                        "group": "Advanced or Optional",
                        "pages": [
                            f"{dg}/android-sdk/sdk-integration/advanced-or-optional/installing-sdk-using-artifact-id",
                            f"{dg}/android-sdk/sdk-integration/advanced-or-optional/network-security-configuration",
                            f"{dg}/android-sdk/sdk-integration/advanced-or-optional/add-on-security",
                            f"{dg}/android-sdk/sdk-integration/advanced-or-optional/additional-encryption",
                            f"{dg}/android-sdk/sdk-integration/advanced-or-optional/sdk-configuration"
                        ]
                    }
                ]
            },
            {
                "group": "Data Tracking",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/android-sdk/data-tracking/basic/enable-advertising-identifier-tracking",
                            f"{dg}/android-sdk/data-tracking/basic/track-install-or-update",
                            f"{dg}/android-sdk/data-tracking/basic/track-user-attributes",
                            f"{dg}/android-sdk/data-tracking/basic/track-events"
                        ]
                    },
                    {
                        "group": "Advanced or Optional",
                        "pages": [
                            f"{dg}/android-sdk/data-tracking/advanced-or-optional/tracking-locale",
                            f"{dg}/android-sdk/data-tracking/advanced-or-optional/configuring-opt-outs",
                            f"{dg}/android-sdk/data-tracking/advanced-or-optional/device-identifier-tracking"
                        ]
                    }
                ]
            },
            {
                "group": "Push",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/android-sdk/push/basic/push-configuration",
                            f"{dg}/android-sdk/push/basic/notification-runtime-permissions",
                            f"{dg}/android-sdk/push/basic/push-token-registration-and-display"
                        ]
                    },
                    {
                        "group": "Advanced",
                        "pages": [
                            f"{dg}/android-sdk/push/advanced/callbacks-and-customisation",
                            f"{dg}/android-sdk/push/advanced/push-display-handled-by-application"
                        ]
                    },
                    {
                        "group": "Optional",
                        "pages": [
                            {
                                "group": "Push AMP+",
                                "pages": [
                                    f"{dg}/android-sdk/push/optional/push-amp-plus/push-amp-plus-integration",
                                    f"{dg}/android-sdk/push/optional/push-amp-plus/steps-to-remove-mi-sdk-dependency",
                                    f"{dg}/android-sdk/push/optional/push-amp-plus/configuring-hms-push-kit"
                                ]
                            },
                            f"{dg}/android-sdk/push/optional/push-amplification",
                            f"{dg}/android-sdk/push/optional/device-triggered",
                            f"{dg}/android-sdk/push/optional/location-triggered",
                            f"{dg}/android-sdk/push/optional/notification-center",
                            f"{dg}/android-sdk/push/optional/push-templates"
                        ]
                    }
                ]
            },
            {
                "group": "In-App Messages",
                "pages": [f"{dg}/android-sdk/in-app-messages/in-app-nativ"]
            },
            {
                "group": "Cards",
                "pages": [
                    f"{dg}/android-sdk/cards/cards",
                    f"{dg}/android-sdk/cards/self-handled-cards"
                ]
            },
            {
                "group": "Checklist",
                "pages": [f"{dg}/android-sdk/checklist/release-checklist"]
            },
            {
                "group": "Compliance",
                "pages": [
                    f"{dg}/android-sdk/compliance/prepare-for-google-plays-data-disclosure-requirements",
                    f"{dg}/android-sdk/compliance/compliance"
                ]
            },
            {
                "group": "Migration",
                "pages": [
                    f"{dg}/android-sdk/migration/updating-to-12xxx-from-11xxx",
                    f"{dg}/android-sdk/migration/updating-to-11xxx-from-10xxx",
                    f"{dg}/android-sdk/migration/migration-to-10xxx",
                    f"{dg}/android-sdk/migration/migration-from-4x-to-5x-one-time-activity",
                    f"{dg}/android-sdk/migration/moving-from-manifest-to-code-based-integration",
                    f"{dg}/android-sdk/migration/migration-to-maven-central",
                    f"{dg}/android-sdk/migration/migrating-from-gcm-to-fcm",
                    f"{dg}/android-sdk/migration/migrating-from-addon-inbox-602",
                    f"{dg}/android-sdk/migration/migrating-to-push-amp-plus-2000"
                ]
            },
            {
                "group": "OS Updates",
                "pages": [f"{dg}/android-sdk/os-updates/android-12"]
            },
            {
                "group": "Android TV",
                "pages": [f"{dg}/android-sdk/android-tv/android-tv"]
            },
            {
                "group": "Performance",
                "pages": [
                    f"{dg}/android-sdk/performance/sdk-performance",
                    f"{dg}/android-sdk/performance/sdk-size-impact"
                ]
            },
            {
                "group": "Troubleshooting and FAQs",
                "pages": [
                    f"{dg}/android-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs",
                    f"{dg}/android-sdk/troubleshooting-and-faqs/how-to-fix-token-drop"
                ]
            },
            {
                "group": "Sample App",
                "pages": [f"{dg}/android-sdk/sample-app/android-sample-app"]
            },
            {
                "group": "Integration with Older Version of SDK",
                "pages": [
                    {
                        "group": "Integration",
                        "pages": [
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/configuration-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/integration-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/integration-using-version-catalog-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/sdk-initialisation-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/install-update-differentiation-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/exclude-moengage-storage-file-from-auto-backup-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/network-security-configuration-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/additional-encryption-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/integration/sdk-performance-11xx"
                        ]
                    },
                    {
                        "group": "Data Tracking",
                        "pages": [
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-user-attributes-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-events-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-locale-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-opt-out-11xx"
                        ]
                    },
                    {
                        "group": "Push",
                        "pages": [
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push/push-configuration-for-android-sdk-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push/push-templates-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push/advanced-push-configuration-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push/push-display-handled-by-application-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push/location-triggered-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push/notification-center-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push/notification-center-for-moengage-sdk-version-11100",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push/notification-customisation-11xx"
                        ]
                    },
                    {
                        "group": "Push AMP+",
                        "pages": [
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push-amp-plus/push-amp-plus-integration-11xx",
                            f"{dg}/android-sdk/integration-with-older-version-of-sdk/push-amp-plus/configuring-hms-push-kit-11xx"
                        ]
                    },
                    {
                        "group": "In-App Messages",
                        "pages": [f"{dg}/android-sdk/integration-with-older-version-of-sdk/in-app-messages/in-app-nativ-11xx"]
                    },
                    {
                        "group": "Cards",
                        "pages": [f"{dg}/android-sdk/integration-with-older-version-of-sdk/cards/cards-11xx"]
                    },
                    {
                        "group": "Prepare for Release",
                        "pages": [f"{dg}/android-sdk/integration-with-older-version-of-sdk/prepare-for-release/release-checklist-11xx"]
                    },
                    {
                        "group": "Compliance",
                        "pages": [f"{dg}/android-sdk/integration-with-older-version-of-sdk/compliance/compliance-11xx"]
                    },
                    {
                        "group": "Troubleshooting and FAQs",
                        "pages": [f"{dg}/android-sdk/integration-with-older-version-of-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs-11xx"]
                    },
                    f"{dg}/android-sdk/integration-with-older-version-of-sdk/configuring-pro-guard"
                ]
            }
        ]
    },
    {
        "group": "Web SDK",
        "pages": [
            {
                "group": "Web SDK Overview",
                "pages": [
                    f"{dg}/web-sdk/web-sdk-overview/web-sdk-overview",
                    f"{dg}/web-sdk/web-sdk-overview/web-sdk-browser-compatibility-matrix"
                ]
            },
            {
                "group": "Web SDK Integration",
                "pages": [
                    {
                        "group": "Basic Integration",
                        "pages": [f"{dg}/web-sdk/web-sdk-integration/basic-integration/web-sdk-integration"]
                    },
                    {
                        "group": "Advanced Integration",
                        "pages": [
                            f"{dg}/web-sdk/web-sdk-integration/advanced-integration/debugging-mode",
                            f"{dg}/web-sdk/web-sdk-integration/advanced-integration/cookies-used-by-web-sdk",
                            f"{dg}/web-sdk/web-sdk-integration/advanced-integration/web-sdk-lifecycle-callbacks",
                            f"{dg}/web-sdk/web-sdk-integration/advanced-integration/bot-traffic-blocking"
                        ]
                    },
                    f"{dg}/web-sdk/web-sdk-integration/custom-proxy-domain-web"
                ]
            },
            {
                "group": "Data Tracking",
                "pages": [
                    f"{dg}/web-sdk/data-tracking/web-sdk-data-tracking-introduction",
                    f"{dg}/web-sdk/data-tracking/web-sdk-user-attributes-tracking",
                    f"{dg}/web-sdk/data-tracking/web-sdk-events-tracking"
                ]
            },
            {
                "group": "Web Push",
                "pages": [
                    f"{dg}/web-sdk/web-push/safari-web-push-for-ios-and-ipados",
                    f"{dg}/web-sdk/web-push/web-push-overview",
                    f"{dg}/web-sdk/web-push/configure-and-integrate-web-push",
                    f"{dg}/web-sdk/web-push/configure-self-handled-opt-in",
                    f"{dg}/web-sdk/web-push/opted-out-users"
                ]
            },
            {
                "group": "Onsite Messaging",
                "pages": [f"{dg}/web-sdk/onsite-messaging/configure-and-integrate-on-site-messaging"]
            },
            {
                "group": "Web Personalization",
                "pages": [f"{dg}/web-sdk/web-personalization/configure-and-integrate-web-personalization"]
            },
            {
                "group": "Cards",
                "pages": [
                    f"{dg}/web-sdk/cards/cards",
                    f"{dg}/web-sdk/cards/self-handled-cards"
                ]
            },
            {
                "group": "Integration Validation",
                "pages": [f"{dg}/web-sdk/integration-validation/web-push-notifications-integration-validation"]
            },
            {
                "group": "Other Supported Web SDK Integration",
                "pages": [
                    f"{dg}/web-sdk/other-supported-web-sdk-integration/google-tag-manager-gtm-templates",
                    f"{dg}/web-sdk/other-supported-web-sdk-integration/smart-tv-integration",
                    f"{dg}/web-sdk/other-supported-web-sdk-integration/single-page-app-spa-support",
                    f"{dg}/web-sdk/other-supported-web-sdk-integration/integrating-with-other-web-frameworks",
                    f"{dg}/web-sdk/other-supported-web-sdk-integration/configure-and-integrate-amp-event-analytics",
                    f"{dg}/web-sdk/other-supported-web-sdk-integration/configure-and-integrate-amp-web-push"
                ]
            }
        ]
    },
    {
        "group": "Personalize SDK",
        "pages": [
            {
                "group": "SDK Integration",
                "pages": [f"{dg}/personalize-sdk/sdk-integration/web-personalization-v2"]
            }
        ]
    },
    {
        "group": "Ecommerce Platforms",
        "pages": [
            {
                "group": "Shopify",
                "pages": [
                    f"{dg}/ecommerce-platforms/shopify/shopify-20",
                    f"{dg}/ecommerce-platforms/shopify/events-and-user-data-tracking",
                    f"{dg}/ecommerce-platforms/shopify/user-data-sync",
                    f"{dg}/ecommerce-platforms/shopify/sync-product-catalog",
                    f"{dg}/ecommerce-platforms/shopify/validate-integration",
                    f"{dg}/ecommerce-platforms/shopify/user-profile-management-with-shopify",
                    f"{dg}/ecommerce-platforms/shopify/faqs"
                ]
            },
            {
                "group": "Woo Commerce",
                "pages": [f"{dg}/ecommerce-platforms/woo-commerce/woocommerce"]
            },
            {
                "group": "Magento",
                "pages": [f"{dg}/ecommerce-platforms/magento/magento"]
            }
        ]
    },
    {
        "group": "React Native SDK",
        "pages": [
            {
                "group": "Overview",
                "pages": [f"{dg}/react-native-sdk/overview/getting-started-with-react-native-sdk"]
            },
            {
                "group": "SDK Integration",
                "pages": [
                    {
                        "group": "SDK Installation",
                        "pages": [
                            f"{dg}/react-native-sdk/sdk-integration/sdk-installation/framework-dependency",
                            f"{dg}/react-native-sdk/sdk-integration/sdk-installation/android",
                            f"{dg}/react-native-sdk/sdk-integration/sdk-installation/ios"
                        ]
                    },
                    {
                        "group": "SDK Initialization",
                        "pages": [
                            f"{dg}/react-native-sdk/sdk-integration/sdk-initialization/framework-initialization",
                            f"{dg}/react-native-sdk/sdk-integration/sdk-initialization/android",
                            f"{dg}/react-native-sdk/sdk-integration/sdk-initialization/ios"
                        ]
                    },
                    f"{dg}/react-native-sdk/sdk-integration/limitations"
                ]
            },
            {
                "group": "Data Tracking",
                "pages": [
                    f"{dg}/react-native-sdk/data-tracking/enable-advertising-identifier-tracking",
                    f"{dg}/react-native-sdk/data-tracking/install-update",
                    f"{dg}/react-native-sdk/data-tracking/setting-unique-id-for-sdk-versions-below-1120",
                    f"{dg}/react-native-sdk/data-tracking/tracking-events",
                    f"{dg}/react-native-sdk/data-tracking/delete-user-from-moengage-server"
                ]
            },
            {
                "group": "Push",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/react-native-sdk/push/basic/android-push-configuration",
                            f"{dg}/react-native-sdk/push/basic/android-notification-runtime-permissions",
                            f"{dg}/react-native-sdk/push/basic/ios-push-configuration",
                            f"{dg}/react-native-sdk/push/basic/push-callback"
                        ]
                    },
                    {
                        "group": "Optional",
                        "pages": [
                            f"{dg}/react-native-sdk/push/optional/location-triggered",
                            f"{dg}/react-native-sdk/push/optional/notification-center"
                        ]
                    }
                ]
            },
            {
                "group": "In App Messages",
                "pages": [f"{dg}/react-native-sdk/in-app-messages/inapp-nativ"]
            },
            {
                "group": "Cards",
                "pages": [
                    {
                        "group": "Installation",
                        "pages": [
                            f"{dg}/react-native-sdk/cards/installation/framework-dependency",
                            f"{dg}/react-native-sdk/cards/installation/android",
                            f"{dg}/react-native-sdk/cards/installation/ios"
                        ]
                    },
                    {
                        "group": "Initialization",
                        "pages": [f"{dg}/react-native-sdk/cards/initialization/framework-initialization"]
                    },
                    f"{dg}/react-native-sdk/cards/self-handled-cards",
                    f"{dg}/react-native-sdk/cards/cards-data-payload"
                ]
            },
            {
                "group": "TV",
                "pages": [f"{dg}/react-native-sdk/tv/tv-support"]
            },
            {
                "group": "Sample App",
                "pages": [f"{dg}/react-native-sdk/sample-app/react-native-sample-app"]
            },
            {
                "group": "Integration with Older SDK Version",
                "pages": [
                    {
                        "group": "SDK Integration",
                        "pages": [
                            {
                                "group": "SDK Installation",
                                "pages": [
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency-7xx",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android-7xx",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios-7xx"
                                ]
                            },
                            {
                                "group": "SDK Initialization",
                                "pages": [
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initialization",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initialization-7xx",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-7xx",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios-7xx"
                                ]
                            },
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/limitations",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/limitations-7xx"
                        ]
                    },
                    {
                        "group": "Data Tracking",
                        "pages": [
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/data-tracking/install-update",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/data-tracking/tracking-events",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-7xx",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/data-tracking/install-update-7xx",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-7xx",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-7xx"
                        ]
                    },
                    {
                        "group": "Push",
                        "pages": [
                            {
                                "group": "Basic",
                                "pages": [
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/push/basic/push-callback",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-7xx",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration-7xx",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/push/basic/push-callback-7xx"
                                ]
                            },
                            {
                                "group": "Optional",
                                "pages": [
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/push/optional/notification-center-3xx",
                                    f"{dg}/react-native-sdk/integration-with-older-sdk-version/push/optional/notification-center-7xx"
                                ]
                            }
                        ]
                    },
                    {
                        "group": "InApp Messages",
                        "pages": [
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/inapp-messages/inapp-nativ",
                            f"{dg}/react-native-sdk/integration-with-older-sdk-version/inapp-messages/inapp-nativ-7xx"
                        ]
                    }
                ]
            }
        ]
    },
    {
        "group": "Flutter SDK",
        "pages": [
            {
                "group": "Overview",
                "pages": [f"{dg}/flutter-sdk/overview/getting-started-with-flutter-sdk"]
            },
            {
                "group": "SDK Integration",
                "pages": [
                    {
                        "group": "SDK Installation",
                        "pages": [
                            f"{dg}/flutter-sdk/sdk-integration/sdk-installation/framework-dependency",
                            f"{dg}/flutter-sdk/sdk-integration/sdk-installation/android",
                            f"{dg}/flutter-sdk/sdk-integration/sdk-installation/ios"
                        ]
                    },
                    {
                        "group": "SDK Initialization",
                        "pages": [
                            f"{dg}/flutter-sdk/sdk-integration/sdk-initialization/framework-initialization",
                            f"{dg}/flutter-sdk/sdk-integration/sdk-initialization/android-sdk-initialization",
                            f"{dg}/flutter-sdk/sdk-integration/sdk-initialization/ios-sdk-initialization",
                            f"{dg}/flutter-sdk/sdk-integration/sdk-initialization/web-sdk-initialization"
                        ]
                    },
                    f"{dg}/flutter-sdk/sdk-integration/limitations"
                ]
            },
            {
                "group": "Data Tracking",
                "pages": [
                    f"{dg}/flutter-sdk/data-tracking/delete-user-from-moengage-server",
                    f"{dg}/flutter-sdk/data-tracking/enable-advertising-identifier-tracking",
                    f"{dg}/flutter-sdk/data-tracking/install-update-differentiation",
                    f"{dg}/flutter-sdk/data-tracking/setting-unique-id-for-sdk-versions-below-920",
                    f"{dg}/flutter-sdk/data-tracking/tracking-events"
                ]
            },
            {
                "group": "Push",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/flutter-sdk/push/basic/android-push-configuration",
                            f"{dg}/flutter-sdk/push/basic/android-notification-runtime-permissions",
                            f"{dg}/flutter-sdk/push/basic/ios-push-configuration",
                            f"{dg}/flutter-sdk/push/basic/push-callback"
                        ]
                    },
                    {
                        "group": "Optional",
                        "pages": [
                            f"{dg}/flutter-sdk/push/optional/location-triggered",
                            f"{dg}/flutter-sdk/push/optional/notification-center"
                        ]
                    }
                ]
            },
            {
                "group": "In-App Messages",
                "pages": [f"{dg}/flutter-sdk/in-app-messages/inapp-nativ"]
            },
            {
                "group": "Cards",
                "pages": [f"{dg}/flutter-sdk/cards/self-handled-cards"]
            },
            {
                "group": "Troubleshooting and FAQs",
                "pages": [f"{dg}/flutter-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs-react"]
            },
            {
                "group": "Sample App",
                "pages": [f"{dg}/flutter-sdk/sample-app/flutter-sample-app"]
            },
            {
                "group": "Integration with Older SDK Version",
                "pages": [
                    {
                        "group": "SDK Installation",
                        "pages": [
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/framework-dependency-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/ios-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/android-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/framework-dependency",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/ios",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/android",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/web",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/sdk-installation-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/android-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/ios-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/web-4xx"
                        ]
                    },
                    {
                        "group": "SDK Initialization",
                        "pages": [
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/framework-initialization-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/android-sdk-initialization-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/ios-sdk-initialization-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/web-sdk-initialization-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/framework-initialization",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/android-sdk-initialization",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/ios-sdk-initialization",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/web-sdk-initialization",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/framework-initialization-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/android-sdk-initialization-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/ios-sdk-initialization-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/web-sdk-initialization-4xx"
                        ]
                    },
                    {
                        "group": "Data Tracking",
                        "pages": [
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-events",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/enable-advertiser-identifier-tracking",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation-2",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-4xx",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-4xx"
                        ]
                    },
                    {
                        "group": "Push",
                        "pages": [
                            {
                                "group": "Basic",
                                "pages": [
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/push-callback",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration-520",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-520",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/push-callback-2",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-4xx",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration-4xx",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/basic/push-callback-4xx"
                                ]
                            },
                            {
                                "group": "Optional",
                                "pages": [
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/optional/notification-center-520",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/optional/location-triggered-520",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/optional/notification-center",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/optional/location-triggered",
                                    f"{dg}/flutter-sdk/integration-with-older-sdk-version/push/optional/notification-center-4xx"
                                ]
                            }
                        ]
                    },
                    {
                        "group": "In-App Messages",
                        "pages": [
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ-520",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ",
                            f"{dg}/flutter-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ-4xx"
                        ]
                    }
                ]
            }
        ]
    },
    {
        "group": "Cordova SDK",
        "pages": [
            {
                "group": "SDK Integration",
                "pages": [
                    {
                        "group": "SDK Installation",
                        "pages": [
                            f"{dg}/cordova-sdk/sdk-integration/sdk-installation/framework-dependency",
                            f"{dg}/cordova-sdk/sdk-integration/sdk-installation/android-sdk-installation",
                            f"{dg}/cordova-sdk/sdk-integration/sdk-installation/ios-installation"
                        ]
                    },
                    {
                        "group": "SDK Initialization",
                        "pages": [
                            f"{dg}/cordova-sdk/sdk-integration/sdk-initialization/framework-initialization",
                            f"{dg}/cordova-sdk/sdk-integration/sdk-initialization/android-sdk-initialization",
                            f"{dg}/cordova-sdk/sdk-integration/sdk-initialization/ios-sdk-initialization"
                        ]
                    },
                    f"{dg}/cordova-sdk/sdk-integration/limitations"
                ]
            },
            {
                "group": "Data Tracking",
                "pages": [
                    f"{dg}/cordova-sdk/data-tracking/delete-user-from-moengage-server",
                    f"{dg}/cordova-sdk/data-tracking/enable-advertising-identifier-tracking",
                    f"{dg}/cordova-sdk/data-tracking/install-update-differentiation",
                    f"{dg}/cordova-sdk/data-tracking/tracking-user-attributes",
                    f"{dg}/cordova-sdk/data-tracking/tracking-events"
                ]
            },
            {
                "group": "Push",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/cordova-sdk/push/basic/android-notification-runtime-permissions",
                            f"{dg}/cordova-sdk/push/basic/ios-push-configuration-7xx",
                            f"{dg}/cordova-sdk/push/basic/android-push-configuration",
                            f"{dg}/cordova-sdk/push/basic/ios-push-configuration",
                            f"{dg}/cordova-sdk/push/basic/push-callback"
                        ]
                    },
                    {
                        "group": "Optional",
                        "pages": [f"{dg}/cordova-sdk/push/optional/location-triggered"]
                    }
                ]
            },
            {
                "group": "In App Messages",
                "pages": [f"{dg}/cordova-sdk/in-app-messages/inapp-nativ"]
            },
            {
                "group": "Migration",
                "pages": [f"{dg}/cordova-sdk/migration/migrating-to-4xx"]
            },
            {
                "group": "Integration with Older SDK Version",
                "pages": [
                    {
                        "group": "SDK Integration",
                        "pages": [
                            {
                                "group": "SDK Installation",
                                "pages": [
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android-sdk-installation",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios-sdk-installation",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency-7xx",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android-sdk-installation-7xx",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios-installation-7xx"
                                ]
                            },
                            {
                                "group": "SDK Initialization",
                                "pages": [
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initialization",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-sdk-initialization",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initalization-7xx",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-sdk-initialization-7xx",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios-sdk-initialization-7xx"
                                ]
                            },
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/ios-sdk-initialization",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-integration",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/limitations"
                        ]
                    },
                    {
                        "group": "Data Tracking",
                        "pages": [
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/data-tracking/tracking-events",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/data-tracking/enable-advertiser-identifier-tracking",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-7xx",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-7xx",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-7xx",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation-7xx"
                        ]
                    },
                    {
                        "group": "Push",
                        "pages": [
                            {
                                "group": "Basic",
                                "pages": [
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/push/basic/push-callback",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/push/basic/push-callback-7xx",
                                    f"{dg}/cordova-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-7xx"
                                ]
                            },
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/push/ios-push-configuration",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/push/android-push-configuration"
                        ]
                    },
                    {
                        "group": "In App Messages",
                        "pages": [
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ",
                            f"{dg}/cordova-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ-7xx"
                        ]
                    }
                ]
            }
        ]
    },
    {
        "group": "Unity SDK",
        "pages": [
            {
                "group": "SDK Integration",
                "pages": [
                    {
                        "group": "SDK Installation",
                        "pages": [f"{dg}/unity-sdk/sdk-integration/sdk-installation/sdk-installation"]
                    },
                    {
                        "group": "SDK Initialization",
                        "pages": [
                            f"{dg}/unity-sdk/sdk-integration/sdk-initialization/sdk-initialization",
                            f"{dg}/unity-sdk/sdk-integration/sdk-initialization/android-sdk-initialization",
                            f"{dg}/unity-sdk/sdk-integration/sdk-initialization/ios-sdk-initialization"
                        ]
                    },
                    f"{dg}/unity-sdk/sdk-integration/limitations"
                ]
            },
            {
                "group": "Data Tracking",
                "pages": [
                    f"{dg}/unity-sdk/data-tracking/delete-user-from-moengage-server",
                    f"{dg}/unity-sdk/data-tracking/enable-advertising-identifier-tracking",
                    f"{dg}/unity-sdk/data-tracking/install-update-differentiation",
                    f"{dg}/unity-sdk/data-tracking/tracking-user-attributes",
                    f"{dg}/unity-sdk/data-tracking/tracking-events"
                ]
            },
            {
                "group": "Push",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/unity-sdk/push/basic/android-push-configuration",
                            f"{dg}/unity-sdk/push/basic/android-notification-runtime-permissions",
                            f"{dg}/unity-sdk/push/basic/ios-push-configuration",
                            f"{dg}/unity-sdk/push/basic/push-callback"
                        ]
                    },
                    {
                        "group": "Optional",
                        "pages": [
                            f"{dg}/unity-sdk/push/optional/configuring-push-templates",
                            f"{dg}/unity-sdk/push/optional/location-triggered"
                        ]
                    }
                ]
            },
            {
                "group": "In App Messages",
                "pages": [f"{dg}/unity-sdk/in-app-messages/inapp-nativ"]
            },
            {
                "group": "Compliance",
                "pages": [f"{dg}/unity-sdk/compliance/compliance"]
            },
            {
                "group": "Integration with Older SDK Version",
                "pages": [
                    {
                        "group": "SDK Integration",
                        "pages": [
                            {
                                "group": "SDK Installation",
                                "pages": [f"{dg}/unity-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/sdk-installation-2xx"]
                            },
                            {
                                "group": "SDK Initialization",
                                "pages": [
                                    f"{dg}/unity-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/sdk-initialization-2xx",
                                    f"{dg}/unity-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-sdk-initialization-2xx",
                                    f"{dg}/unity-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios-sdk-initialization-2xx"
                                ]
                            },
                            f"{dg}/unity-sdk/integration-with-older-sdk-version/sdk-integration/limitations-2xx"
                        ]
                    },
                    {
                        "group": "Data Tracking",
                        "pages": [
                            f"{dg}/unity-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-2xx",
                            f"{dg}/unity-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-2xx",
                            f"{dg}/unity-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation-2xx",
                            f"{dg}/unity-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-2xx"
                        ]
                    },
                    {
                        "group": "Push",
                        "pages": [
                            {
                                "group": "Basic",
                                "pages": [
                                    f"{dg}/unity-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-2xx",
                                    f"{dg}/unity-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration-2xx",
                                    f"{dg}/unity-sdk/integration-with-older-sdk-version/push/basic/push-callback-2xx",
                                    f"{dg}/unity-sdk/integration-with-older-sdk-version/push/basic/configuring-push-templates-2xx"
                                ]
                            },
                            {
                                "group": "Optional",
                                "pages": [f"{dg}/unity-sdk/integration-with-older-sdk-version/push/optional/location-triggered-2xx"]
                            }
                        ]
                    },
                    {
                        "group": "InApp Messages",
                        "pages": [f"{dg}/unity-sdk/integration-with-older-sdk-version/inapp-messages/inapp-nativ-2xx"]
                    },
                    {
                        "group": "Compliance",
                        "pages": [f"{dg}/unity-sdk/integration-with-older-sdk-version/compliance/compliance-2xx"]
                    }
                ]
            }
        ]
    },
    {
        "group": "Capacitor SDK",
        "pages": [
            {
                "group": "SDK Integration",
                "pages": [
                    {
                        "group": "SDK Installation",
                        "pages": [
                            f"{dg}/capacitor-sdk/sdk-integration/sdk-installation/framework-dependency",
                            f"{dg}/capacitor-sdk/sdk-integration/sdk-installation/android-sdk-installation",
                            f"{dg}/capacitor-sdk/sdk-integration/sdk-installation/ios-sdk-installation"
                        ]
                    },
                    {
                        "group": "SDK Initialization",
                        "pages": [
                            f"{dg}/capacitor-sdk/sdk-integration/sdk-initialization/framework-initialization",
                            f"{dg}/capacitor-sdk/sdk-integration/sdk-initialization/android-sdk-initialization",
                            f"{dg}/capacitor-sdk/sdk-integration/sdk-initialization/ios-sdk-initialization"
                        ]
                    }
                ]
            },
            {
                "group": "Data Tracking",
                "pages": [
                    f"{dg}/capacitor-sdk/data-tracking/delete-user-from-moengage-server",
                    f"{dg}/capacitor-sdk/data-tracking/enable-advertising-identifier-tracking",
                    f"{dg}/capacitor-sdk/data-tracking/install-update-differentiation",
                    f"{dg}/capacitor-sdk/data-tracking/tracking-user-attributes",
                    f"{dg}/capacitor-sdk/data-tracking/tracking-events"
                ]
            },
            {
                "group": "Push",
                "pages": [
                    {
                        "group": "Basic",
                        "pages": [
                            f"{dg}/capacitor-sdk/push/basic/android-notification-runtime-permissions",
                            f"{dg}/capacitor-sdk/push/basic/android-push-configuration",
                            f"{dg}/capacitor-sdk/push/basic/ios-push-configuration",
                            f"{dg}/capacitor-sdk/push/basic/push-callback"
                        ]
                    },
                    {
                        "group": "Optional",
                        "pages": [f"{dg}/capacitor-sdk/push/optional/location-triggered"]
                    }
                ]
            },
            {
                "group": "In-App Messages",
                "pages": [f"{dg}/capacitor-sdk/in-app-messages/inapp-nativ"]
            },
            {
                "group": "Sample App",
                "pages": [f"{dg}/capacitor-sdk/sample-app/capacitor-sample-app"]
            },
            {
                "group": "Integration with Older SDK Version",
                "pages": [
                    {
                        "group": "SDK Integration",
                        "pages": [
                            {
                                "group": "SDK Installation",
                                "pages": [
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency",
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android-sdk-installation",
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios-sdk-installation"
                                ]
                            },
                            {
                                "group": "SDK Initialization",
                                "pages": [
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initialization",
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-sdk-initialization",
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios-sdk-initialization"
                                ]
                            }
                        ]
                    },
                    {
                        "group": "Data Tracking",
                        "pages": [
                            f"{dg}/capacitor-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking",
                            f"{dg}/capacitor-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation",
                            f"{dg}/capacitor-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes",
                            f"{dg}/capacitor-sdk/integration-with-older-sdk-version/data-tracking/tracking-events"
                        ]
                    },
                    {
                        "group": "Push",
                        "pages": [
                            {
                                "group": "Basic",
                                "pages": [
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration",
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration",
                                    f"{dg}/capacitor-sdk/integration-with-older-sdk-version/push/basic/push-callback"
                                ]
                            },
                            {
                                "group": "Optional",
                                "pages": [f"{dg}/capacitor-sdk/integration-with-older-sdk-version/push/optional/location-triggered"]
                            }
                        ]
                    },
                    {
                        "group": "In-App Messages",
                        "pages": [f"{dg}/capacitor-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ"]
                    }
                ]
            }
        ]
    },
    {
        "group": "Ionic SDK",
        "pages": [
            {
                "group": "SDK Integration",
                "pages": [f"{dg}/ionic-sdk/sdk-integration/sdk-installation"]
            }
        ]
    },
    {
        "group": "TV and OTT Integrations",
        "pages": [
            {
                "group": "Getting Started",
                "pages": [f"{dg}/tv-and-ott-integrations/getting-started/tv-and-ott-integrations"]
            }
        ]
    },
    {
        "group": "Components for SDK",
        "pages": [
            {
                "group": "Tracking",
                "pages": [f"{dg}/components-for-sdk/tracking/real-time-uninstall-tracking"]
            },
            {
                "group": "Javascript Bridge",
                "pages": [f"{dg}/components-for-sdk/javascript-bridge/javascript-bridge-for-html-in-apps"]
            },
            {
                "group": "Push Notification",
                "pages": [f"{dg}/components-for-sdk/push-notification/android-push-configuration-for-hybrid-applications"]
            }
        ]
    },
    {
        "group": "API",
        "pages": [
            {
                "group": "Content",
                "pages": [
                    {
                        "group": "Email templates",
                        "pages": [
                            {
                                "group": "Version 1",
                                "pages": [
                                    f"{dg}/api/content/email-templates/version-1/overview-email-template-apis",
                                    f"{dg}/api/content/email-templates/version-1/create-email-template",
                                    f"{dg}/api/content/email-templates/version-1/get-all-templates",
                                    f"{dg}/api/content/email-templates/version-1/get-a-specific-email-template",
                                    f"{dg}/api/content/email-templates/version-1/bulk-create-update-template",
                                    f"{dg}/api/content/email-templates/version-1/update-a-specific-email-template"
                                ]
                            },
                            {
                                "group": "Version 2",
                                "pages": [
                                    f"{dg}/api/content/email-templates/version-2/overview-email-template-apis",
                                    f"{dg}/api/content/email-templates/version-2/create-email-template-api",
                                    f"{dg}/api/content/email-templates/version-2/search-email-template-api",
                                    f"{dg}/api/content/email-templates/version-2/update-email-template-api"
                                ]
                            }
                        ]
                    },
                    {
                        "group": "Push templates",
                        "pages": [
                            f"{dg}/api/content/push-templates/overview",
                            f"{dg}/api/content/push-templates/create-push-template-api",
                            f"{dg}/api/content/push-templates/search-push-template-api",
                            f"{dg}/api/content/push-templates/update-push-template-api"
                        ]
                    },
                    {
                        "group": "SMS templates",
                        "pages": [
                            f"{dg}/api/content/sms-templates/overview",
                            f"{dg}/api/content/sms-templates/create-sms-template-api",
                            f"{dg}/api/content/sms-templates/search-sms-template-api",
                            f"{dg}/api/content/sms-templates/update-sms-template-api"
                        ]
                    },
                    {
                        "group": "Content blocks",
                        "pages": [
                            f"{dg}/api/content/content-blocks/content-block-apis",
                            f"{dg}/api/content/content-blocks/search-content-block",
                            f"{dg}/api/content/content-blocks/get-specific-content-blocks",
                            f"{dg}/api/content/content-blocks/create-content-block",
                            f"{dg}/api/content/content-blocks/update-content-block"
                        ]
                    }
                ]
            },
            {
                "group": "Inform",
                "pages": [f"{dg}/api/inform/inform-api"]
            },
            {
                "group": "Push",
                "pages": [f"{dg}/api/push/push-api"]
            },
            {
                "group": "Business Events",
                "pages": [
                    f"{dg}/api/business-events/overview",
                    f"{dg}/api/business-events/create-business-event-api",
                    f"{dg}/api/business-events/trigger-business-event-api",
                    f"{dg}/api/business-events/search-business-event-api"
                ]
            },
            {
                "group": "Data",
                "pages": [
                    f"{dg}/api/data/overview",
                    f"{dg}/api/data/track-user",
                    f"{dg}/api/data/get-user",
                    f"{dg}/api/data/merge-user",
                    f"{dg}/api/data/delete-user",
                    f"{dg}/api/data/create-event",
                    f"{dg}/api/data/bulk-import",
                    f"{dg}/api/data/moengage-streams",
                    f"{dg}/api/data/trigger-file-imports",
                    f"{dg}/api/data/install-tracking"
                ]
            },
            {
                "group": "GDPR / CCPA",
                "pages": [f"{dg}/api/gdpr-ccpa/gdpr-ccpa-api"]
            },
            {
                "group": "Subscription Categories",
                "pages": [
                    f"{dg}/api/subscription-categories/overview-subscription-categories-api",
                    f"{dg}/api/subscription-categories/get-subscription-preferences-api",
                    f"{dg}/api/subscription-categories/update-subscription-preferences-api",
                    f"{dg}/api/subscription-categories/bulk-update-subscription-preferences-api"
                ]
            },
            {
                "group": "Email Subscription",
                "pages": [f"{dg}/api/email-subscription/resubscribe-email-api"]
            },
            {
                "group": "Custom Segment",
                "pages": [
                    {
                        "group": "File",
                        "pages": [f"{dg}/api/custom-segment/file/file-segment-api"]
                    },
                    {
                        "group": "Filter",
                        "pages": [
                            f"{dg}/api/custom-segment/filter/overview",
                            f"{dg}/api/custom-segment/filter/create-custom-segment",
                            f"{dg}/api/custom-segment/filter/get-custom-segment-by-id",
                            f"{dg}/api/custom-segment/filter/list-custom-segments",
                            f"{dg}/api/custom-segment/filter/update-custom-segment-api"
                        ]
                    },
                    {
                        "group": "Cohort/Audience",
                        "pages": [f"{dg}/api/custom-segment/cohort-audience/cohort-audience-sync"]
                    }
                ]
            }
        ]
    },
    {
        "group": "Partner Integrations",
        "pages": [
            {
                "group": "Firebase",
                "pages": [f"{dg}/partner-integrations/firebase/getting-fcm-server-key"]
            }
        ]
    },
    {
        "group": "Release Notes",
        "pages": [
            {
                "group": "iOS SDK",
                "pages": [f"{dg}/release-notes/ios-sdk/2023-and-older"]
            },
            {
                "group": "Android SDK",
                "pages": [f"{dg}/release-notes/android-sdk/2023-and-older"]
            },
            {
                "group": "Web SDK",
                "pages": [f"{dg}/release-notes/web-sdk/changelog"]
            },
            {
                "group": "React Native SDK",
                "pages": [f"{dg}/release-notes/react-native-sdk/changelog"]
            },
            {
                "group": "Flutter SDK",
                "pages": [f"{dg}/release-notes/flutter-sdk/changelog"]
            },
            {
                "group": "Cordova SDK",
                "pages": [f"{dg}/release-notes/cordova-sdk/changelog"]
            },
            {
                "group": "Unity SDK",
                "pages": [f"{dg}/release-notes/unity-sdk/changelog"]
            },
            {
                "group": "Capacitor SDK",
                "pages": [f"{dg}/release-notes/capacitor-sdk/changelog"]
            },
            {
                "group": "Segment Integration",
                "pages": [
                    f"{dg}/release-notes/segment-integration/ios-swift-changelog",
                    f"{dg}/release-notes/segment-integration/android-kotlin-sdk-changelog",
                    f"{dg}/release-notes/segment-integration/ios-sdk-changelog",
                    f"{dg}/release-notes/segment-integration/android-sdk-changelog",
                    f"{dg}/release-notes/segment-integration/react-native-plugin-changelog"
                ]
            }
        ]
    }
]

# Find and update the Developer Guide tab
for tab in docs["navigation"]["tabs"]:
    if tab.get("tab") == "Developer Guide":
        tab["groups"] = new_groups
        break

with open("docs.json", "w") as f:
    json.dump(docs, f, indent=2)

print("docs.json updated successfully!")
print(f"Developer Guide now has {len(new_groups)} top-level groups")
