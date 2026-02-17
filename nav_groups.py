"""Navigation groups for Developer Guide - imported by update_nav.py"""
d = "developer-guide"

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
        g("Optional", [g("Push AMP+", [f"{d}/android-sdk/push/optional/push-amp-plus/push-amp-plus-integration", f"{d}/android-sdk/push/optional/push-amp-plus/steps-to-remove-mi-sdk-dependency", f"{d}/android-sdk/push/optional/push-amp-plus/configuring-hms-push-kit"]), f"{d}/android-sdk/push/optional/push-amplification", f"{d}/android-sdk/push/optional/device-triggered", f"{d}/android-sdk/push/optional/location-triggered", f"{d}/android-sdk/push/optional/notification-center", f"{d}/android-sdk/push/optional/push-templates"])
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
    g("Web SDK Integration", [g("Basic Integration", [f"{d}/web-sdk/web-sdk-integration/basic-integration/web-sdk-integration"]), g("Advanced Integration", [f"{d}/web-sdk/web-sdk-integration/advanced-integration/debugging-mode", f"{d}/web-sdk/web-sdk-integration/advanced-integration/cookies-used-by-web-sdk", f"{d}/web-sdk/web-sdk-integration/advanced-integration/web-sdk-lifecycle-callbacks", f"{d}/web-sdk/web-sdk-integration/advanced-integration/bot-traffic-blocking"]), f"{d}/web-sdk/web-sdk-integration/custom-proxy-domain-web"]),
    g("Data Tracking", [f"{d}/web-sdk/data-tracking/web-sdk-data-tracking-introduction", f"{d}/web-sdk/data-tracking/web-sdk-user-attributes-tracking", f"{d}/web-sdk/data-tracking/web-sdk-events-tracking"]),
    g("Web Push", [f"{d}/web-sdk/web-push/safari-web-push-for-ios-and-ipados", f"{d}/web-sdk/web-push/web-push-overview", f"{d}/web-sdk/web-push/configure-and-integrate-web-push", f"{d}/web-sdk/web-push/configure-self-handled-opt-in", f"{d}/web-sdk/web-push/opted-out-users"]),
    g("Onsite Messaging", [f"{d}/web-sdk/onsite-messaging/configure-and-integrate-on-site-messaging"]),
    g("Web Personalization", [f"{d}/web-sdk/web-personalization/configure-and-integrate-web-personalization"]),
    g("Cards", [f"{d}/web-sdk/cards/cards", f"{d}/web-sdk/cards/self-handled-cards"]),
    g("Integration Validation", [f"{d}/web-sdk/integration-validation/web-push-notifications-integration-validation"]),
    g("Other Supported Web SDK Integration", [f"{d}/web-sdk/other-supported-web-sdk-integration/google-tag-manager-gtm-templates", f"{d}/web-sdk/other-supported-web-sdk-integration/smart-tv-integration", f"{d}/web-sdk/other-supported-web-sdk-integration/single-page-app-spa-support", f"{d}/web-sdk/other-supported-web-sdk-integration/integrating-with-other-web-frameworks", f"{d}/web-sdk/other-supported-web-sdk-integration/configure-and-integrate-amp-event-analytics", f"{d}/web-sdk/other-supported-web-sdk-integration/configure-and-integrate-amp-web-push"])
])

personalize = g("Personalize SDK", [g("SDK Integration", [f"{d}/personalize-sdk/sdk-integration/web-personalization-v2"])])
ecommerce = g("Ecommerce Platforms", [g("Shopify", [f"{d}/ecommerce-platforms/shopify/shopify-20", f"{d}/ecommerce-platforms/shopify/events-and-user-data-tracking", f"{d}/ecommerce-platforms/shopify/user-data-sync", f"{d}/ecommerce-platforms/shopify/sync-product-catalog", f"{d}/ecommerce-platforms/shopify/validate-integration", f"{d}/ecommerce-platforms/shopify/user-profile-management-with-shopify", f"{d}/ecommerce-platforms/shopify/faqs"]), g("Woo Commerce", [f"{d}/ecommerce-platforms/woo-commerce/woocommerce"]), g("Magento", [f"{d}/ecommerce-platforms/magento/magento"])])
