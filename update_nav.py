#!/usr/bin/env python3
"""Update docs.json Developer Guide navigation with clean file paths."""
import json

with open("docs.json", "r") as f:
    docs = json.load(f)

d = "developer-guide"

# Helper to build group
def g(name, pages):
    return {"group": name, "pages": pages}

ios = g("iOS SDK", [
    g("SDK Integration", [
        g("Basic", [f"{d}/ios-sdk/sdk-integration/basic/sdk-integration", f"{d}/ios-sdk/sdk-integration/basic/sdk-initialization", f"{d}/ios-sdk/sdk-integration/basic/data-center"]),
        g("Advanced", [f"{d}/ios-sdk/sdk-integration/advanced/add-on-security"])
    ]),
    g("Data Tracking", [
        g("Basic", [f"{d}/ios-sdk/data-tracking/basic/install-update-differentiation", f"{d}/ios-sdk/data-tracking/basic/tracking-user-attributes", f"{d}/ios-sdk/data-tracking/basic/tracking-events"]),
        g("Advanced", [f"{d}/ios-sdk/data-tracking/advanced/session-and-source-tracking"])
    ]),
    g("Push", [
        g("Basic", [f"{d}/ios-sdk/push/basic/push-notifications", f"{d}/ios-sdk/push/basic/apns-authentication-key", f"{d}/ios-sdk/push/basic/apns-certificate-pem-file-legacy"]),
        g("Optional", [f"{d}/ios-sdk/push/optional/push-templates", f"{d}/ios-sdk/push/optional/push-handled-by-application", f"{d}/ios-sdk/push/optional/actionable-notifications", f"{d}/ios-sdk/push/optional/real-time-triggers", f"{d}/ios-sdk/push/optional/ios-notification-center", f"{d}/ios-sdk/push/optional/location-triggered"]),
        g("Advanced", [f"{d}/ios-sdk/push/advanced/custom-notification-handling"])
    ]),
    g("In-App Messages", [f"{d}/ios-sdk/in-app-messages/in-app-nativ"]),
    g("Cards", [f"{d}/ios-sdk/cards/cards-in-ios", f"{d}/ios-sdk/cards/self-handled-cards"]),
    g("Checklist", [f"{d}/ios-sdk/checklist/release-checklist"]),
    g("Compliance", [f"{d}/ios-sdk/compliance/compliance"]),
    g("Manual Integration", [f"{d}/ios-sdk/manual-integration/manual-integration"]),
    g("Migration", [f"{d}/ios-sdk/migration/migration-to-sdk-version-900", f"{d}/ios-sdk/migration/migration-to-sdk-version-820", f"{d}/ios-sdk/migration/migration-to-sdk-version-700", f"{d}/ios-sdk/migration/migration-to-sdk-version-600"]),
    g("Framework Size Impact", [f"{d}/ios-sdk/framework-size-impact/framework-size-impact"]),
    g("OS Updates", [f"{d}/ios-sdk/os-updates/ios-15"]),
    g("Apple TV", [f"{d}/ios-sdk/apple-tv/apple-tv"]),
    g("Troubleshooting and FAQs", [f"{d}/ios-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs"]),
    g("Sample App", [f"{d}/ios-sdk/sample-app/ios-sample-app"]),
    g("Integration with Older Version of SDK", [
        g("Integration", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/integration/data-center", f"{d}/ios-sdk/integration-with-older-version-of-sdk/integration/sdk-initialization", f"{d}/ios-sdk/integration-with-older-version-of-sdk/integration/sdk-integration", f"{d}/ios-sdk/integration-with-older-version-of-sdk/integration/sdk-integration-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/integration/sdk-initialisation-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/integration/data-center-7xx"]),
        g("Data Tracking", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/session-and-source-tracking", f"{d}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-events", f"{d}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-user-attributes", f"{d}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/install-update-differentiation", f"{d}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-user-attributes-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-events-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/session-and-source-tracking-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/data-tracking/install-or-update-differentiation-7xx"]),
        g("Push", [
            g("Basic", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/basic/apns-certificate-pem-file", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/basic/push-notifications", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/basic/push-notifications-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/basic/apns-certificate-pem-file-7xx"]),
            g("Advanced", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/push-notification-implementation", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/push-templates", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/actionable-notifications", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/real-time-triggers", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/ios-notification-center", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/location-triggered", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/push-notification-implementation-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/push-templates-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/actionable-notifications-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/real-time-triggers-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/ios-notification-center-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/push/advanced/location-triggered-7xx"])
        ]),
        g("In-App Messages", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/in-app-messages/in-app-nativ", f"{d}/ios-sdk/integration-with-older-version-of-sdk/in-app-messages/in-app-nativ-7xx", f"{d}/ios-sdk/integration-with-older-version-of-sdk/in-app-messages/in-app-nativ-6xx"]),
        g("Cards", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/cards/self-handled-cards", f"{d}/ios-sdk/integration-with-older-version-of-sdk/cards/cards-in-ios", f"{d}/ios-sdk/integration-with-older-version-of-sdk/cards/cards-7xx"]),
        g("Checklist", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/checklist/release-checklist", f"{d}/ios-sdk/integration-with-older-version-of-sdk/checklist/release-checklist-7xx"]),
        g("Compliance", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/compliance/manual-integration", f"{d}/ios-sdk/integration-with-older-version-of-sdk/compliance/compliance", f"{d}/ios-sdk/integration-with-older-version-of-sdk/compliance/compliance-7xx"]),
        g("Framework Size Impact", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/framework-size-impact/framework-size-impact-7xx"]),
        g("Troubleshooting and FAQs", [f"{d}/ios-sdk/integration-with-older-version-of-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs-7xx"])
    ])
])

android = g("Android SDK", [
    g("SDK Integration", [
        g("Basic Integration", [f"{d}/android-sdk/sdk-integration/basic-integration/configuring-build-settings", f"{d}/android-sdk/sdk-integration/basic-integration/sdk-initialization", f"{d}/android-sdk/sdk-integration/basic-integration/data-center", f"{d}/android-sdk/sdk-integration/basic-integration/exclude-moengage-storage-file-from-auto-backup"]),
        g("Advanced or Optional", [f"{d}/android-sdk/sdk-integration/advanced-or-optional/installing-sdk-using-artifact-id", f"{d}/android-sdk/sdk-integration/advanced-or-optional/network-security-configuration", f"{d}/android-sdk/sdk-integration/advanced-or-optional/add-on-security", f"{d}/android-sdk/sdk-integration/advanced-or-optional/additional-encryption", f"{d}/android-sdk/sdk-integration/advanced-or-optional/sdk-configuration"])
    ]),
    g("Data Tracking", [
        g("Basic", [f"{d}/android-sdk/data-tracking/basic/enable-advertising-identifier-tracking", f"{d}/android-sdk/data-tracking/basic/track-install-or-update", f"{d}/android-sdk/data-tracking/basic/track-user-attributes", f"{d}/android-sdk/data-tracking/basic/track-events"]),
        g("Advanced or Optional", [f"{d}/android-sdk/data-tracking/advanced-or-optional/tracking-locale", f"{d}/android-sdk/data-tracking/advanced-or-optional/configuring-opt-outs", f"{d}/android-sdk/data-tracking/advanced-or-optional/device-identifier-tracking"])
    ]),
    g("Push", [
        g("Basic", [f"{d}/android-sdk/push/basic/push-configuration", f"{d}/android-sdk/push/basic/notification-runtime-permissions", f"{d}/android-sdk/push/basic/push-token-registration-and-display"]),
        g("Advanced", [f"{d}/android-sdk/push/advanced/callbacks-and-customisation", f"{d}/android-sdk/push/advanced/push-display-handled-by-application"]),
        g("Optional", [
            g("Push AMP+", [f"{d}/android-sdk/push/optional/push-amp-plus/push-amp-plus-integration", f"{d}/android-sdk/push/optional/push-amp-plus/steps-to-remove-mi-sdk-dependency", f"{d}/android-sdk/push/optional/push-amp-plus/configuring-hms-push-kit"]),
            f"{d}/android-sdk/push/optional/push-amplification", f"{d}/android-sdk/push/optional/device-triggered", f"{d}/android-sdk/push/optional/location-triggered", f"{d}/android-sdk/push/optional/notification-center", f"{d}/android-sdk/push/optional/push-templates"
        ])
    ]),
    g("In-App Messages", [f"{d}/android-sdk/in-app-messages/in-app-nativ"]),
    g("Cards", [f"{d}/android-sdk/cards/cards", f"{d}/android-sdk/cards/self-handled-cards"]),
    g("Checklist", [f"{d}/android-sdk/checklist/release-checklist"]),
    g("Compliance", [f"{d}/android-sdk/compliance/prepare-for-google-plays-data-disclosure-requirements", f"{d}/android-sdk/compliance/compliance"]),
    g("Migration", [f"{d}/android-sdk/migration/updating-to-12xxx-from-11xxx", f"{d}/android-sdk/migration/updating-to-11xxx-from-10xxx", f"{d}/android-sdk/migration/migration-to-10xxx", f"{d}/android-sdk/migration/migration-from-4x-to-5x-one-time-activity", f"{d}/android-sdk/migration/moving-from-manifest-to-code-based-integration", f"{d}/android-sdk/migration/migration-to-maven-central", f"{d}/android-sdk/migration/migrating-from-gcm-to-fcm", f"{d}/android-sdk/migration/migrating-from-addon-inbox-602", f"{d}/android-sdk/migration/migrating-to-push-amp-plus-2000"]),
    g("OS Updates", [f"{d}/android-sdk/os-updates/android-12"]),
    g("Android TV", [f"{d}/android-sdk/android-tv/android-tv"]),
    g("Performance", [f"{d}/android-sdk/performance/sdk-performance", f"{d}/android-sdk/performance/sdk-size-impact"]),
    g("Troubleshooting and FAQs", [f"{d}/android-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs", f"{d}/android-sdk/troubleshooting-and-faqs/how-to-fix-token-drop"]),
    g("Sample App", [f"{d}/android-sdk/sample-app/android-sample-app"]),
    g("Integration with Older Version of SDK", [
        g("Integration", [f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/configuration-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/integration-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/integration-using-version-catalog-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/sdk-initialisation-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/install-update-differentiation-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/exclude-moengage-storage-file-from-auto-backup-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/network-security-configuration-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/additional-encryption-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/integration/sdk-performance-11xx"]),
        g("Data Tracking", [f"{d}/android-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-user-attributes-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-events-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-locale-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/data-tracking/tracking-opt-out-11xx"]),
        g("Push", [f"{d}/android-sdk/integration-with-older-version-of-sdk/push/push-configuration-for-android-sdk-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/push/push-templates-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/push/advanced-push-configuration-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/push/push-display-handled-by-application-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/push/location-triggered-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/push/notification-center-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/push/notification-center-for-moengage-sdk-version-11100", f"{d}/android-sdk/integration-with-older-version-of-sdk/push/notification-customisation-11xx"]),
        g("Push AMP+", [f"{d}/android-sdk/integration-with-older-version-of-sdk/push-amp-plus/push-amp-plus-integration-11xx", f"{d}/android-sdk/integration-with-older-version-of-sdk/push-amp-plus/configuring-hms-push-kit-11xx"]),
        g("In-App Messages", [f"{d}/android-sdk/integration-with-older-version-of-sdk/in-app-messages/in-app-nativ-11xx"]),
        g("Cards", [f"{d}/android-sdk/integration-with-older-version-of-sdk/cards/cards-11xx"]),
        g("Prepare for Release", [f"{d}/android-sdk/integration-with-older-version-of-sdk/prepare-for-release/release-checklist-11xx"]),
        g("Compliance", [f"{d}/android-sdk/integration-with-older-version-of-sdk/compliance/compliance-11xx"]),
        g("Troubleshooting and FAQs", [f"{d}/android-sdk/integration-with-older-version-of-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs-11xx"]),
        f"{d}/android-sdk/integration-with-older-version-of-sdk/configuring-pro-guard"
    ])
])

web = g("Web SDK", [
    g("Web SDK Overview", [f"{d}/web-sdk/web-sdk-overview/web-sdk-overview", f"{d}/web-sdk/web-sdk-overview/web-sdk-browser-compatibility-matrix"]),
    g("Web SDK Integration", [
        g("Basic Integration", [f"{d}/web-sdk/web-sdk-integration/basic-integration/web-sdk-integration"]),
        g("Advanced Integration", [f"{d}/web-sdk/web-sdk-integration/advanced-integration/debugging-mode", f"{d}/web-sdk/web-sdk-integration/advanced-integration/cookies-used-by-web-sdk", f"{d}/web-sdk/web-sdk-integration/advanced-integration/web-sdk-lifecycle-callbacks", f"{d}/web-sdk/web-sdk-integration/advanced-integration/bot-traffic-blocking"]),
        f"{d}/web-sdk/web-sdk-integration/custom-proxy-domain-web"
    ]),
    g("Data Tracking", [f"{d}/web-sdk/data-tracking/web-sdk-data-tracking-introduction", f"{d}/web-sdk/data-tracking/web-sdk-user-attributes-tracking", f"{d}/web-sdk/data-tracking/web-sdk-events-tracking"]),
    g("Web Push", [f"{d}/web-sdk/web-push/safari-web-push-for-ios-and-ipados", f"{d}/web-sdk/web-push/web-push-overview", f"{d}/web-sdk/web-push/configure-and-integrate-web-push", f"{d}/web-sdk/web-push/configure-self-handled-opt-in", f"{d}/web-sdk/web-push/opted-out-users"]),
    g("Onsite Messaging", [f"{d}/web-sdk/onsite-messaging/configure-and-integrate-on-site-messaging"]),
    g("Web Personalization", [f"{d}/web-sdk/web-personalization/configure-and-integrate-web-personalization"]),
    g("Cards", [f"{d}/web-sdk/cards/cards", f"{d}/web-sdk/cards/self-handled-cards"]),
    g("Integration Validation", [f"{d}/web-sdk/integration-validation/web-push-notifications-integration-validation"]),
    g("Other Supported Web SDK Integration", [f"{d}/web-sdk/other-supported-web-sdk-integration/google-tag-manager-gtm-templates", f"{d}/web-sdk/other-supported-web-sdk-integration/smart-tv-integration", f"{d}/web-sdk/other-supported-web-sdk-integration/single-page-app-spa-support", f"{d}/web-sdk/other-supported-web-sdk-integration/integrating-with-other-web-frameworks", f"{d}/web-sdk/other-supported-web-sdk-integration/configure-and-integrate-amp-event-analytics", f"{d}/web-sdk/other-supported-web-sdk-integration/configure-and-integrate-amp-web-push"])
])

personalize = g("Personalize SDK", [g("SDK Integration", [f"{d}/personalize-sdk/sdk-integration/web-personalization-v2"])])

ecommerce = g("Ecommerce Platforms", [
    g("Shopify", [f"{d}/ecommerce-platforms/shopify/shopify-20", f"{d}/ecommerce-platforms/shopify/events-and-user-data-tracking", f"{d}/ecommerce-platforms/shopify/user-data-sync", f"{d}/ecommerce-platforms/shopify/sync-product-catalog", f"{d}/ecommerce-platforms/shopify/validate-integration", f"{d}/ecommerce-platforms/shopify/user-profile-management-with-shopify", f"{d}/ecommerce-platforms/shopify/faqs"]),
    g("Woo Commerce", [f"{d}/ecommerce-platforms/woo-commerce/woocommerce"]),
    g("Magento", [f"{d}/ecommerce-platforms/magento/magento"])
])

rn = g("React Native SDK", [
    g("Overview", [f"{d}/react-native-sdk/overview/getting-started-with-react-native-sdk"]),
    g("SDK Integration", [
        g("SDK Installation", [f"{d}/react-native-sdk/sdk-integration/sdk-installation/framework-dependency", f"{d}/react-native-sdk/sdk-integration/sdk-installation/android", f"{d}/react-native-sdk/sdk-integration/sdk-installation/ios"]),
        g("SDK Initialization", [f"{d}/react-native-sdk/sdk-integration/sdk-initialization/framework-initialization", f"{d}/react-native-sdk/sdk-integration/sdk-initialization/android", f"{d}/react-native-sdk/sdk-integration/sdk-initialization/ios"]),
        f"{d}/react-native-sdk/sdk-integration/limitations"
    ]),
    g("Data Tracking", [f"{d}/react-native-sdk/data-tracking/enable-advertising-identifier-tracking", f"{d}/react-native-sdk/data-tracking/install-update", f"{d}/react-native-sdk/data-tracking/setting-unique-id-for-sdk-versions-below-1120", f"{d}/react-native-sdk/data-tracking/tracking-events", f"{d}/react-native-sdk/data-tracking/delete-user-from-moengage-server"]),
    g("Push", [
        g("Basic", [f"{d}/react-native-sdk/push/basic/android-push-configuration", f"{d}/react-native-sdk/push/basic/android-notification-runtime-permissions", f"{d}/react-native-sdk/push/basic/ios-push-configuration", f"{d}/react-native-sdk/push/basic/push-callback"]),
        g("Optional", [f"{d}/react-native-sdk/push/optional/location-triggered", f"{d}/react-native-sdk/push/optional/notification-center"])
    ]),
    g("In App Messages", [f"{d}/react-native-sdk/in-app-messages/inapp-nativ"]),
    g("Cards", [
        g("Installation", [f"{d}/react-native-sdk/cards/installation/framework-dependency", f"{d}/react-native-sdk/cards/installation/android", f"{d}/react-native-sdk/cards/installation/ios"]),
        g("Initialization", [f"{d}/react-native-sdk/cards/initialization/framework-initialization"]),
        f"{d}/react-native-sdk/cards/self-handled-cards", f"{d}/react-native-sdk/cards/cards-data-payload"
    ]),
    g("TV", [f"{d}/react-native-sdk/tv/tv-support"]),
    g("Sample App", [f"{d}/react-native-sdk/sample-app/react-native-sample-app"]),
    g("Integration with Older SDK Version", [
        g("SDK Integration", [
            g("SDK Installation", [f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios-7xx"]),
            g("SDK Initialization", [f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initialization", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initialization-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios-7xx"]),
            f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/limitations", f"{d}/react-native-sdk/integration-with-older-sdk-version/sdk-integration/limitations-7xx"
        ]),
        g("Data Tracking", [f"{d}/react-native-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking", f"{d}/react-native-sdk/integration-with-older-sdk-version/data-tracking/install-update", f"{d}/react-native-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes", f"{d}/react-native-sdk/integration-with-older-sdk-version/data-tracking/tracking-events", f"{d}/react-native-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/data-tracking/install-update-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-7xx"]),
        g("Push", [
            g("Basic", [f"{d}/react-native-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration", f"{d}/react-native-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration", f"{d}/react-native-sdk/integration-with-older-sdk-version/push/basic/push-callback", f"{d}/react-native-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration-7xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/push/basic/push-callback-7xx"]),
            g("Optional", [f"{d}/react-native-sdk/integration-with-older-sdk-version/push/optional/notification-center-3xx", f"{d}/react-native-sdk/integration-with-older-sdk-version/push/optional/notification-center-7xx"])
        ]),
        g("InApp Messages", [f"{d}/react-native-sdk/integration-with-older-sdk-version/inapp-messages/inapp-nativ", f"{d}/react-native-sdk/integration-with-older-sdk-version/inapp-messages/inapp-nativ-7xx"])
    ])
])

flutter = g("Flutter SDK", [
    g("Overview", [f"{d}/flutter-sdk/overview/getting-started-with-flutter-sdk"]),
    g("SDK Integration", [
        g("SDK Installation", [f"{d}/flutter-sdk/sdk-integration/sdk-installation/framework-dependency", f"{d}/flutter-sdk/sdk-integration/sdk-installation/android", f"{d}/flutter-sdk/sdk-integration/sdk-installation/ios"]),
        g("SDK Initialization", [f"{d}/flutter-sdk/sdk-integration/sdk-initialization/framework-initialization", f"{d}/flutter-sdk/sdk-integration/sdk-initialization/android-sdk-initialization", f"{d}/flutter-sdk/sdk-integration/sdk-initialization/ios-sdk-initialization", f"{d}/flutter-sdk/sdk-integration/sdk-initialization/web-sdk-initialization"]),
        f"{d}/flutter-sdk/sdk-integration/limitations"
    ]),
    g("Data Tracking", [f"{d}/flutter-sdk/data-tracking/delete-user-from-moengage-server", f"{d}/flutter-sdk/data-tracking/enable-advertising-identifier-tracking", f"{d}/flutter-sdk/data-tracking/install-update-differentiation", f"{d}/flutter-sdk/data-tracking/setting-unique-id-for-sdk-versions-below-920", f"{d}/flutter-sdk/data-tracking/tracking-events"]),
    g("Push", [
        g("Basic", [f"{d}/flutter-sdk/push/basic/android-push-configuration", f"{d}/flutter-sdk/push/basic/android-notification-runtime-permissions", f"{d}/flutter-sdk/push/basic/ios-push-configuration", f"{d}/flutter-sdk/push/basic/push-callback"]),
        g("Optional", [f"{d}/flutter-sdk/push/optional/location-triggered", f"{d}/flutter-sdk/push/optional/notification-center"])
    ]),
    g("In-App Messages", [f"{d}/flutter-sdk/in-app-messages/inapp-nativ"]),
    g("Cards", [f"{d}/flutter-sdk/cards/self-handled-cards"]),
    g("Troubleshooting and FAQs", [f"{d}/flutter-sdk/troubleshooting-and-faqs/troubleshooting-and-faqs-react"]),
    g("Sample App", [f"{d}/flutter-sdk/sample-app/flutter-sample-app"]),
    g("Integration with Older SDK Version", [
        g("SDK Installation", [f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/web-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/ios-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/android-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/framework-dependency-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/web", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/ios", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/android", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/framework-dependency", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/sdk-installation-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/android-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/ios-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-installation/web-4xx"]),
        g("SDK Initialization", [f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/web-sdk-initialization-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/ios-sdk-initialization-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/android-sdk-initialization-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/framework-initialization-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/web-sdk-initialization", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/ios-sdk-initialization", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/android-sdk-initialization", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/framework-initialization", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/framework-initialization-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/android-sdk-initialization-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/ios-sdk-initialization-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/sdk-initialization/web-sdk-initialization-4xx"]),
        g("Data Tracking", [f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-events", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/enable-advertiser-identifier-tracking", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation-2", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-4xx"]),
        g("Push", [
            g("Basic", [f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/push-callback", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/push-callback-2", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration-4xx", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/basic/push-callback-4xx"]),
            g("Optional", [f"{d}/flutter-sdk/integration-with-older-sdk-version/push/optional/notification-center-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/optional/location-triggered-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/optional/notification-center", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/optional/location-triggered", f"{d}/flutter-sdk/integration-with-older-sdk-version/push/optional/notification-center-4xx"])
        ]),
        g("In-App Messages", [f"{d}/flutter-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ-520", f"{d}/flutter-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ", f"{d}/flutter-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ-4xx"])
    ])
])

cordova = g("Cordova SDK", [
    g("SDK Integration", [
        g("SDK Installation", [f"{d}/cordova-sdk/sdk-integration/sdk-installation/framework-dependency", f"{d}/cordova-sdk/sdk-integration/sdk-installation/android-sdk-installation", f"{d}/cordova-sdk/sdk-integration/sdk-installation/ios-installation"]),
        g("SDK Initialization", [f"{d}/cordova-sdk/sdk-integration/sdk-initialization/framework-initialization", f"{d}/cordova-sdk/sdk-integration/sdk-initialization/android-sdk-initialization", f"{d}/cordova-sdk/sdk-integration/sdk-initialization/ios-sdk-initialization"]),
        f"{d}/cordova-sdk/sdk-integration/limitations"
    ]),
    g("Data Tracking", [f"{d}/cordova-sdk/data-tracking/delete-user-from-moengage-server", f"{d}/cordova-sdk/data-tracking/enable-advertising-identifier-tracking", f"{d}/cordova-sdk/data-tracking/install-update-differentiation", f"{d}/cordova-sdk/data-tracking/tracking-user-attributes", f"{d}/cordova-sdk/data-tracking/tracking-events"]),
    g("Push", [
        g("Basic", [f"{d}/cordova-sdk/push/basic/android-notification-runtime-permissions", f"{d}/cordova-sdk/push/basic/ios-push-configuration-7xx", f"{d}/cordova-sdk/push/basic/android-push-configuration", f"{d}/cordova-sdk/push/basic/ios-push-configuration", f"{d}/cordova-sdk/push/basic/push-callback"]),
        g("Optional", [f"{d}/cordova-sdk/push/optional/location-triggered"])
    ]),
    g("In App Messages", [f"{d}/cordova-sdk/in-app-messages/inapp-nativ"]),
    g("Migration", [f"{d}/cordova-sdk/migration/migrating-to-4xx"]),
    g("Integration with Older SDK Version", [
        g("SDK Integration", [
            g("SDK Installation", [f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android-sdk-installation", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios-sdk-installation", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency-7xx", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android-sdk-installation-7xx", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios-installation-7xx"]),
            g("SDK Initialization", [f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initialization", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-sdk-initialization", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initalization-7xx", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-sdk-initialization-7xx", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios-sdk-initialization-7xx"]),
            f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/ios-sdk-initialization", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/sdk-integration", f"{d}/cordova-sdk/integration-with-older-sdk-version/sdk-integration/limitations"
        ]),
        g("Data Tracking", [f"{d}/cordova-sdk/integration-with-older-sdk-version/data-tracking/tracking-events", f"{d}/cordova-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes", f"{d}/cordova-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation", f"{d}/cordova-sdk/integration-with-older-sdk-version/data-tracking/enable-advertiser-identifier-tracking", f"{d}/cordova-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-7xx", f"{d}/cordova-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-7xx", f"{d}/cordova-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-7xx", f"{d}/cordova-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation-7xx"]),
        g("Push", [
            g("Basic", [f"{d}/cordova-sdk/integration-with-older-sdk-version/push/basic/push-callback", f"{d}/cordova-sdk/integration-with-older-sdk-version/push/basic/push-callback-7xx", f"{d}/cordova-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-7xx"]),
            f"{d}/cordova-sdk/integration-with-older-sdk-version/push/ios-push-configuration", f"{d}/cordova-sdk/integration-with-older-sdk-version/push/android-push-configuration"
        ]),
        g("In App Messages", [f"{d}/cordova-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ", f"{d}/cordova-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ-7xx"])
    ])
])

unity = g("Unity SDK", [
    g("SDK Integration", [
        g("SDK Installation", [f"{d}/unity-sdk/sdk-integration/sdk-installation/sdk-installation"]),
        g("SDK Initialization", [f"{d}/unity-sdk/sdk-integration/sdk-initialization/sdk-initialization", f"{d}/unity-sdk/sdk-integration/sdk-initialization/android-sdk-initialization", f"{d}/unity-sdk/sdk-integration/sdk-initialization/ios-sdk-initialization"]),
        f"{d}/unity-sdk/sdk-integration/limitations"
    ]),
    g("Data Tracking", [f"{d}/unity-sdk/data-tracking/delete-user-from-moengage-server", f"{d}/unity-sdk/data-tracking/enable-advertising-identifier-tracking", f"{d}/unity-sdk/data-tracking/install-update-differentiation", f"{d}/unity-sdk/data-tracking/tracking-user-attributes", f"{d}/unity-sdk/data-tracking/tracking-events"]),
    g("Push", [
        g("Basic", [f"{d}/unity-sdk/push/basic/android-push-configuration", f"{d}/unity-sdk/push/basic/android-notification-runtime-permissions", f"{d}/unity-sdk/push/basic/ios-push-configuration", f"{d}/unity-sdk/push/basic/push-callback"]),
        g("Optional", [f"{d}/unity-sdk/push/optional/configuring-push-templates", f"{d}/unity-sdk/push/optional/location-triggered"])
    ]),
    g("In App Messages", [f"{d}/unity-sdk/in-app-messages/inapp-nativ"]),
    g("Compliance", [f"{d}/unity-sdk/compliance/compliance"]),
    g("Integration with Older SDK Version", [
        g("SDK Integration", [
            g("SDK Installation", [f"{d}/unity-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/sdk-installation-2xx"]),
            g("SDK Initialization", [f"{d}/unity-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/sdk-initialization-2xx", f"{d}/unity-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-sdk-initialization-2xx", f"{d}/unity-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios-sdk-initialization-2xx"]),
            f"{d}/unity-sdk/integration-with-older-sdk-version/sdk-integration/limitations-2xx"
        ]),
        g("Data Tracking", [f"{d}/unity-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes-2xx", f"{d}/unity-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking-2xx", f"{d}/unity-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation-2xx", f"{d}/unity-sdk/integration-with-older-sdk-version/data-tracking/tracking-events-2xx"]),
        g("Push", [
            g("Basic", [f"{d}/unity-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration-2xx", f"{d}/unity-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration-2xx", f"{d}/unity-sdk/integration-with-older-sdk-version/push/basic/push-callback-2xx", f"{d}/unity-sdk/integration-with-older-sdk-version/push/basic/configuring-push-templates-2xx"]),
            g("Optional", [f"{d}/unity-sdk/integration-with-older-sdk-version/push/optional/location-triggered-2xx"])
        ]),
        g("InApp Messages", [f"{d}/unity-sdk/integration-with-older-sdk-version/inapp-messages/inapp-nativ-2xx"]),
        g("Compliance", [f"{d}/unity-sdk/integration-with-older-sdk-version/compliance/compliance-2xx"])
    ])
])

capacitor = g("Capacitor SDK", [
    g("SDK Integration", [
        g("SDK Installation", [f"{d}/capacitor-sdk/sdk-integration/sdk-installation/framework-dependency", f"{d}/capacitor-sdk/sdk-integration/sdk-installation/android-sdk-installation", f"{d}/capacitor-sdk/sdk-integration/sdk-installation/ios-sdk-installation"]),
        g("SDK Initialization", [f"{d}/capacitor-sdk/sdk-integration/sdk-initialization/framework-initialization", f"{d}/capacitor-sdk/sdk-integration/sdk-initialization/android-sdk-initialization", f"{d}/capacitor-sdk/sdk-integration/sdk-initialization/ios-sdk-initialization"])
    ]),
    g("Data Tracking", [f"{d}/capacitor-sdk/data-tracking/delete-user-from-moengage-server", f"{d}/capacitor-sdk/data-tracking/enable-advertising-identifier-tracking", f"{d}/capacitor-sdk/data-tracking/install-update-differentiation", f"{d}/capacitor-sdk/data-tracking/tracking-user-attributes", f"{d}/capacitor-sdk/data-tracking/tracking-events"]),
    g("Push", [
        g("Basic", [f"{d}/capacitor-sdk/push/basic/android-notification-runtime-permissions", f"{d}/capacitor-sdk/push/basic/android-push-configuration", f"{d}/capacitor-sdk/push/basic/ios-push-configuration", f"{d}/capacitor-sdk/push/basic/push-callback"]),
        g("Optional", [f"{d}/capacitor-sdk/push/optional/location-triggered"])
    ]),
    g("In-App Messages", [f"{d}/capacitor-sdk/in-app-messages/inapp-nativ"]),
    g("Sample App", [f"{d}/capacitor-sdk/sample-app/capacitor-sample-app"]),
    g("Integration with Older SDK Version", [
        g("SDK Integration", [
            g("SDK Installation", [f"{d}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/framework-dependency", f"{d}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/android-sdk-installation", f"{d}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-installation/ios-sdk-installation"]),
            g("SDK Initialization", [f"{d}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/framework-initialization", f"{d}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/android-sdk-initialization", f"{d}/capacitor-sdk/integration-with-older-sdk-version/sdk-integration/sdk-initialization/ios-sdk-initialization"])
        ]),
        g("Data Tracking", [f"{d}/capacitor-sdk/integration-with-older-sdk-version/data-tracking/enable-advertising-identifier-tracking", f"{d}/capacitor-sdk/integration-with-older-sdk-version/data-tracking/install-update-differentiation", f"{d}/capacitor-sdk/integration-with-older-sdk-version/data-tracking/tracking-user-attributes", f"{d}/capacitor-sdk/integration-with-older-sdk-version/data-tracking/tracking-events"]),
        g("Push", [
            g("Basic", [f"{d}/capacitor-sdk/integration-with-older-sdk-version/push/basic/android-push-configuration", f"{d}/capacitor-sdk/integration-with-older-sdk-version/push/basic/ios-push-configuration", f"{d}/capacitor-sdk/integration-with-older-sdk-version/push/basic/push-callback"]),
            g("Optional", [f"{d}/capacitor-sdk/integration-with-older-sdk-version/push/optional/location-triggered"])
        ]),
        g("In-App Messages", [f"{d}/capacitor-sdk/integration-with-older-sdk-version/in-app-messages/inapp-nativ"])
    ])
])

ionic = g("Ionic SDK", [g("SDK Integration", [f"{d}/ionic-sdk/sdk-integration/sdk-installation"])])

tv = g("TV and OTT Integrations", [g("Getting Started", [f"{d}/tv-and-ott-integrations/getting-started/tv-and-ott-integrations"])])

components = g("Components for SDK", [
    g("Tracking", [f"{d}/components-for-sdk/tracking/real-time-uninstall-tracking"]),
    g("Javascript Bridge", [f"{d}/components-for-sdk/javascript-bridge/javascript-bridge-for-html-in-apps"]),
    g("Push Notification", [f"{d}/components-for-sdk/push-notification/android-push-configuration-for-hybrid-applications"])
])

api = g("API", [
    g("Content", [
        g("Email templates", [
            g("Version 1", [f"{d}/api/content/email-templates/version-1/overview-email-template-apis", f"{d}/api/content/email-templates/version-1/create-email-template", f"{d}/api/content/email-templates/version-1/get-all-templates", f"{d}/api/content/email-templates/version-1/get-a-specific-email-template", f"{d}/api/content/email-templates/version-1/bulk-create-update-template", f"{d}/api/content/email-templates/version-1/update-a-specific-email-template"]),
            g("Version 2", [f"{d}/api/content/email-templates/version-2/overview-email-template-apis", f"{d}/api/content/email-templates/version-2/create-email-template-api", f"{d}/api/content/email-templates/version-2/search-email-template-api", f"{d}/api/content/email-templates/version-2/update-email-template-api"])
        ]),
        g("Push templates", [f"{d}/api/content/push-templates/overview", f"{d}/api/content/push-templates/create-push-template-api", f"{d}/api/content/push-templates/search-push-template-api", f"{d}/api/content/push-templates/update-push-template-api"]),
        g("SMS templates", [f"{d}/api/content/sms-templates/overview", f"{d}/api/content/sms-templates/create-sms-template-api", f"{d}/api/content/sms-templates/search-sms-template-api", f"{d}/api/content/sms-templates/update-sms-template-api"]),
        g("Content blocks", [f"{d}/api/content/content-blocks/content-block-apis", f"{d}/api/content/content-blocks/search-content-block", f"{d}/api/content/content-blocks/get-specific-content-blocks", f"{d}/api/content/content-blocks/create-content-block", f"{d}/api/content/content-blocks/update-content-block"])
    ]),
    g("Inform", [f"{d}/api/inform/inform-api"]),
    g("Push", [f"{d}/api/push/push-api"]),
    g("Business Events", [f"{d}/api/business-events/overview", f"{d}/api/business-events/create-business-event-api", f"{d}/api/business-events/trigger-business-event-api", f"{d}/api/business-events/search-business-event-api"]),
    g("Data", [f"{d}/api/data/overview", f"{d}/api/data/track-user", f"{d}/api/data/get-user", f"{d}/api/data/merge-user", f"{d}/api/data/delete-user", f"{d}/api/data/create-event", f"{d}/api/data/bulk-import", f"{d}/api/data/moengage-streams", f"{d}/api/data/trigger-file-imports", f"{d}/api/data/install-tracking"]),
    g("GDPR / CCPA", [f"{d}/api/gdpr-ccpa/gdpr-ccpa-api"]),
    g("Subscription Categories", [f"{d}/api/subscription-categories/overview-subscription-categories-api", f"{d}/api/subscription-categories/get-subscription-preferences-api", f"{d}/api/subscription-categories/update-subscription-preferences-api", f"{d}/api/subscription-categories/bulk-update-subscription-preferences-api"]),
    g("Email Subscription", [f"{d}/api/email-subscription/resubscribe-email-api"]),
    g("Custom Segment", [
        g("File", [f"{d}/api/custom-segment/file/file-segment-api"]),
        g("Filter", [f"{d}/api/custom-segment/filter/overview", f"{d}/api/custom-segment/filter/create-custom-segment", f"{d}/api/custom-segment/filter/get-custom-segment-by-id", f"{d}/api/custom-segment/filter/list-custom-segments", f"{d}/api/custom-segment/filter/update-custom-segment-api"]),
        g("Cohort/Audience", [f"{d}/api/custom-segment/cohort-audience/cohort-audience-sync"])
    ])
])

partner = g("Partner Integrations", [g("Firebase", [f"{d}/partner-integrations/firebase/getting-fcm-server-key"])])

release = g("Release Notes", [
    g("iOS SDK", [f"{d}/release-notes/ios-sdk/2023-and-older"]),
    g("Android SDK", [f"{d}/release-notes/android-sdk/2023-and-older"]),
    g("Web SDK", [f"{d}/release-notes/web-sdk/changelog"]),
    g("React Native SDK", [f"{d}/release-notes/react-native-sdk/changelog"]),
    g("Flutter SDK", [f"{d}/release-notes/flutter-sdk/changelog"]),
    g("Cordova SDK", [f"{d}/release-notes/cordova-sdk/changelog"]),
    g("Unity SDK", [f"{d}/release-notes/unity-sdk/changelog"]),
    g("Capacitor SDK", [f"{d}/release-notes/capacitor-sdk/changelog"]),
    g("Segment Integration", [f"{d}/release-notes/segment-integration/ios-swift-changelog", f"{d}/release-notes/segment-integration/android-kotlin-sdk-changelog", f"{d}/release-notes/segment-integration/ios-sdk-changelog", f"{d}/release-notes/segment-integration/android-sdk-changelog", f"{d}/release-notes/segment-integration/react-native-plugin-changelog"])
])

new_groups = [ios, android, web, personalize, ecommerce, rn, flutter, cordova, unity, capacitor, ionic, tv, components, api, partner, release]

for tab in docs["navigation"]["tabs"]:
    if tab.get("tab") == "Developer Guide":
        tab["groups"] = new_groups
        break

with open("docs.json", "w") as f:
    json.dump(docs, f, indent=2)

print("docs.json updated successfully!")
print(f"Developer Guide now has {len(new_groups)} top-level groups")
