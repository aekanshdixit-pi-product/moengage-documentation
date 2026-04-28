/**
 * Resizable Panels for MoEngage API Documentation
 * Adds a draggable resize handle between request and response code panels
 */

(function() {
  'use strict';

  const CONFIG = {
    minPanelHeight: 80,
    debounceDelay: 100,
    initDelay: 300
  };

  const initializedContainers = new WeakSet();
  let observerTimeout = null;

  function createDragHandle() {
    const handle = document.createElement('div');
    handle.className = 'moe-resize-handle';
    handle.innerHTML = '<div class="moe-resize-handle-dots"><span></span><span></span><span></span></div>';
    handle.setAttribute('role', 'separator');
    handle.setAttribute('aria-orientation', 'horizontal');
    handle.setAttribute('aria-label', 'Drag to resize panels');
    handle.setAttribute('tabindex', '0');
    return handle;
  }

  // Get the actual content height of a panel
  function getContentHeight(panel) {
    // Try to find the code content inside
    const pre = panel.querySelector('pre');
    const codeRegion = panel.querySelector('[role="region"]');
    const codeBlock = panel.querySelector('[class*="codeblock"]');
    
    // Get the scrollHeight of the content element
    let contentHeight = 0;
    
    if (pre) {
      contentHeight = pre.scrollHeight;
    } else if (codeRegion) {
      contentHeight = codeRegion.scrollHeight;
    } else if (codeBlock) {
      contentHeight = codeBlock.scrollHeight;
    }
    
    // Add padding for headers, tabs, etc. (approximately 80px)
    // Also account for the panel's own padding
    const headerHeight = 80;
    
    // Return at least the current height or the content height
    return Math.max(contentHeight + headerHeight, panel.scrollHeight, CONFIG.minPanelHeight);
  }

  function initializeResizer(topPanel, bottomPanel, handle) {
    let isResizing = false;
    let startY = 0;
    let startTopHeight = 0;
    let startBottomHeight = 0;
    let maxTopHeight = 0;
    let maxBottomHeight = 0;

    const startResize = (e) => {
      isResizing = true;
      startY = e.clientY || (e.touches && e.touches[0].clientY);
      
      startTopHeight = topPanel.getBoundingClientRect().height;
      startBottomHeight = bottomPanel.getBoundingClientRect().height;
      
      // Calculate maximum heights based on content
      // This prevents expanding beyond content (which causes grey area)
      maxTopHeight = getContentHeight(topPanel);
      maxBottomHeight = getContentHeight(bottomPanel);

      document.body.classList.add('moe-resizing');
      handle.classList.add('moe-resize-handle--active');
      
      e.preventDefault();
      e.stopPropagation();
    };

    const doResize = (e) => {
      if (!isResizing) return;

      const currentY = e.clientY || (e.touches && e.touches[0].clientY);
      const deltaY = currentY - startY;

      let newTopHeight = startTopHeight + deltaY;
      let newBottomHeight = startBottomHeight - deltaY;

      const totalHeight = startTopHeight + startBottomHeight;
      
      // Enforce MINIMUM heights
      if (newTopHeight < CONFIG.minPanelHeight) {
        newTopHeight = CONFIG.minPanelHeight;
        newBottomHeight = totalHeight - CONFIG.minPanelHeight;
      }
      if (newBottomHeight < CONFIG.minPanelHeight) {
        newBottomHeight = CONFIG.minPanelHeight;
        newTopHeight = totalHeight - CONFIG.minPanelHeight;
      }
      
      // Enforce MAXIMUM heights (prevent grey area)
      // Only cap if expanding beyond content
      if (newTopHeight > maxTopHeight && deltaY > 0) {
        newTopHeight = maxTopHeight;
        newBottomHeight = totalHeight - maxTopHeight;
      }
      if (newBottomHeight > maxBottomHeight && deltaY < 0) {
        newBottomHeight = maxBottomHeight;
        newTopHeight = totalHeight - maxBottomHeight;
      }
      
      // Make sure we don't go below minimum after max capping
      if (newBottomHeight < CONFIG.minPanelHeight) {
        newBottomHeight = CONFIG.minPanelHeight;
        newTopHeight = totalHeight - CONFIG.minPanelHeight;
      }
      if (newTopHeight < CONFIG.minPanelHeight) {
        newTopHeight = CONFIG.minPanelHeight;
        newBottomHeight = totalHeight - CONFIG.minPanelHeight;
      }

      topPanel.style.height = `${newTopHeight}px`;
      topPanel.style.maxHeight = `${newTopHeight}px`;
      topPanel.style.overflow = 'auto';
      
      bottomPanel.style.height = `${newBottomHeight}px`;
      bottomPanel.style.maxHeight = `${newBottomHeight}px`;
      bottomPanel.style.overflow = 'auto';
    };

    const stopResize = () => {
      if (!isResizing) return;
      isResizing = false;
      document.body.classList.remove('moe-resizing');
      handle.classList.remove('moe-resize-handle--active');
    };

    handle.addEventListener('mousedown', startResize);
    document.addEventListener('mousemove', doResize);
    document.addEventListener('mouseup', stopResize);

    handle.addEventListener('touchstart', startResize, { passive: false });
    document.addEventListener('touchmove', doResize, { passive: false });
    document.addEventListener('touchend', stopResize);

    handle.addEventListener('keydown', (e) => {
      const step = 30;
      let topHeight = topPanel.getBoundingClientRect().height;
      let bottomHeight = bottomPanel.getBoundingClientRect().height;
      
      // Recalculate max heights
      const currentMaxTop = getContentHeight(topPanel);
      const currentMaxBottom = getContentHeight(bottomPanel);

      if (e.key === 'ArrowUp' && topHeight > CONFIG.minPanelHeight + step) {
        e.preventDefault();
        topPanel.style.height = `${topHeight - step}px`;
        topPanel.style.maxHeight = `${topHeight - step}px`;
        const newBottomHeight = Math.min(bottomHeight + step, currentMaxBottom);
        bottomPanel.style.height = `${newBottomHeight}px`;
        bottomPanel.style.maxHeight = `${newBottomHeight}px`;
      } else if (e.key === 'ArrowDown' && bottomHeight > CONFIG.minPanelHeight + step) {
        e.preventDefault();
        const newTopHeight = Math.min(topHeight + step, currentMaxTop);
        topPanel.style.height = `${newTopHeight}px`;
        topPanel.style.maxHeight = `${newTopHeight}px`;
        bottomPanel.style.height = `${bottomHeight - step}px`;
        bottomPanel.style.maxHeight = `${bottomHeight - step}px`;
      }
    });

    handle.addEventListener('dblclick', () => {
      topPanel.style.height = '';
      topPanel.style.maxHeight = '';
      topPanel.style.overflow = '';
      bottomPanel.style.height = '';
      bottomPanel.style.maxHeight = '';
      bottomPanel.style.overflow = '';
    });
  }

  function setupResizablePanels() {
    const sideLayout = document.getElementById('content-side-layout');
    if (!sideLayout) return;
    if (sideLayout.querySelector('.moe-resize-handle')) return;

    const codeGroups = sideLayout.querySelectorAll('.code-group');
    const codeRegions = sideLayout.querySelectorAll('[role="region"][aria-label*="Code"]');
    
    let panels = codeGroups.length >= 2 ? Array.from(codeGroups) : Array.from(codeRegions);
    
    if (panels.length < 2) {
      const allDivs = sideLayout.querySelectorAll(':scope > div > div');
      panels = Array.from(allDivs).filter(div => 
        div.querySelector('pre') || 
        div.querySelector('code') || 
        div.classList.contains('code-group') ||
        div.getAttribute('role') === 'region'
      );
    }

    if (panels.length < 2) return;

    const topPanel = panels[0];
    const bottomPanel = panels[1];

    if (initializedContainers.has(topPanel)) return;

    let commonParent = topPanel.parentElement;
    while (commonParent && !commonParent.contains(bottomPanel)) {
      commonParent = commonParent.parentElement;
    }

    const handle = createDragHandle();
    
    if (topPanel.nextElementSibling === bottomPanel) {
      topPanel.after(handle);
      initializeResizer(topPanel, bottomPanel, handle);
    } else {
      let topWrapper = topPanel;
      while (topWrapper.parentElement !== commonParent && topWrapper.parentElement) {
        topWrapper = topWrapper.parentElement;
      }
      
      let bottomWrapper = bottomPanel;
      while (bottomWrapper.parentElement !== commonParent && bottomWrapper.parentElement) {
        bottomWrapper = bottomWrapper.parentElement;
      }
      
      if (topWrapper !== bottomWrapper) {
        topWrapper.after(handle);
        initializeResizer(topWrapper, bottomWrapper, handle);
      }
    }

    initializedContainers.add(topPanel);
  }

  function setupByPosition() {
    const sideLayout = document.getElementById('content-side-layout');
    if (!sideLayout) return;
    if (sideLayout.querySelector('.moe-resize-handle')) return;

    const children = Array.from(sideLayout.children);
    const codePanels = children.filter(child => {
      const rect = child.getBoundingClientRect();
      const hasCode = child.querySelector('pre, code, .code-group, [role="region"]');
      return rect.height > 50 && hasCode;
    });

    if (codePanels.length >= 2) {
      const topPanel = codePanels[0];
      const bottomPanel = codePanels[1];
      
      if (initializedContainers.has(topPanel)) return;
      
      const handle = createDragHandle();
      topPanel.after(handle);
      initializeResizer(topPanel, bottomPanel, handle);
      initializedContainers.add(topPanel);
    }
  }

  function trySetup() {
    setupResizablePanels();
    setupByPosition();
  }

  // Reset panel sizes (used when zoom changes)
  function resetPanelSizes() {
    const sideLayout = document.getElementById('content-side-layout');
    if (!sideLayout) return;
    
    // Find all panels that have been resized (have inline height style)
    const resizedPanels = sideLayout.querySelectorAll('[style*="height"]');
    resizedPanels.forEach(panel => {
      panel.style.height = '';
      panel.style.maxHeight = '';
      panel.style.overflow = '';
    });
  }

  function init() {
    trySetup();
    setTimeout(trySetup, CONFIG.initDelay);

    const observer = new MutationObserver(() => {
      if (observerTimeout) clearTimeout(observerTimeout);
      observerTimeout = setTimeout(trySetup, CONFIG.debounceDelay);
    });

    observer.observe(document.body, { childList: true, subtree: true });

    ['popstate', 'hashchange'].forEach(event => {
      window.addEventListener(event, () => setTimeout(trySetup, 200));
    });

    // Reset panels on window resize (includes zoom changes)
    let resizeTimeout;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => {
        resetPanelSizes();
      }, 150);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.addEventListener('load', () => setTimeout(trySetup, 500));
})();

/* ============================================================ */
/* Use Cases — Cookbook (interactive recipe browser)              */
/* Data + render + multi-select chip filter + search + sort.      */
/* Path-scoped: only runs on /use-cases/introduction.             */
/* ============================================================ */
(function () {
  'use strict';

  const COOKBOOK_PATH = '/use-cases/introduction';

  const CAP_LABELS = {
    push: 'Mobile push',
    email: 'Email',
    'in-app': 'In-app',
    onsite: 'Onsite',
    cards: 'Cards',
    whatsapp: 'WhatsApp',
    facebook: 'Facebook',
    flows: 'Flows',
    recos: 'Recommendations',
    personalize: 'Personalize',
    segments: 'Segmentation',
    analytics: 'Analytics',
    events: 'Business events',
    catalogs: 'Catalogs',
    inform: 'Inform',
    ai: 'Merlin AI',
    integrations: 'Integrations',
  };

  const CHANNEL_LABELS = {
    push: 'Mobile push',
    email: 'Email',
    'in-app': 'In-app',
    onsite: 'Onsite',
    'web-push': 'Web push',
    cards: 'Cards',
    whatsapp: 'WhatsApp',
  };

  const INDUSTRY_LABELS = {
    ecommerce: 'E-Commerce',
    banking: 'Banking',
    fintech: 'FinTech',
    travel: 'Travel',
    ott: 'OTT',
    content: 'Content',
    gaming: 'Gaming',
    telecom: 'Telecom',
    b2b: 'B2B',
  };

  // Recipe catalog. Fields: t=title, h=href, cap=capability, ch=channel(s), ind=industry(ies)
  const RECIPES = [
    // Push (12)
    { t: 'Drive users to try products at store', h: '/use-cases/push/drive-users-to-try-out-products-at-store', cap: 'push', ch: ['push'], ind: ['ecommerce'] },
    { t: 'Get referrals for your app or service', h: '/use-cases/push/get-referrals-for-your-app-or-service', cap: 'push', ch: ['push'], ind: [] },
    { t: 'Highlight an EMI option', h: '/use-cases/push/highlight-an-emi-option', cap: 'push', ch: ['push'], ind: ['banking', 'fintech'] },
    { t: 'Use a custom notification tone on Android', h: '/use-cases/push/how-to-use-custom-notification-tone-for-my-android-app', cap: 'push', ch: ['push'], ind: [] },
    { t: 'Inform users about new EV charging stations', h: '/use-cases/push/inform-users-about-new-charging-station-for-evs', cap: 'push', ch: ['push'], ind: ['travel'] },
    { t: 'Message users when they enter a location', h: '/use-cases/push/message-users-when-they-enter-a-location', cap: 'push', ch: ['push'], ind: [] },
    { t: 'Nudge users before policy renewal', h: '/use-cases/push/nudge-users-before-policy-renewal', cap: 'push', ch: ['push'], ind: ['fintech'] },
    { t: 'Recommend a premium card', h: '/use-cases/push/recommend-a-premium-card', cap: 'push', ch: ['push'], ind: ['banking', 'fintech'] },
    { t: 'Run A/B experiments on push', h: '/use-cases/push/sample-a-b-experiments-for-push', cap: 'push', ch: ['push'], ind: [] },
    { t: 'Send a card payment reminder', h: '/use-cases/push/send-a-card-payment-reminder', cap: 'push', ch: ['push'], ind: ['banking', 'fintech'] },
    { t: 'Send exit-intent push via device triggers', h: '/use-cases/push/send-exit-intent-notification-using-device-triggers', cap: 'push', ch: ['push'], ind: ['ecommerce'] },
    { t: 'Send flight status updates', h: '/use-cases/push/send-flight-status-updates', cap: 'push', ch: ['push'], ind: ['travel'] },

    // Email (3)
    { t: 'Add a countdown timer to emails', h: '/use-cases/email/add-a-countdown-timer-to-emails', cap: 'email', ch: ['email'], ind: ['ecommerce'] },
    { t: 'Add calendar invites to emails', h: '/use-cases/email/add-calendar-invites-to-emails', cap: 'email', ch: ['email'], ind: ['travel'] },
    { t: 'Set up purchase confirmation emails', h: '/use-cases/email/how-to-set-up-purchase-confirmation-emails', cap: 'email', ch: ['email'], ind: ['ecommerce'] },

    // In-App (14)
    { t: 'Boost conversions with in-app pop-ups', h: '/use-cases/in-app-message/how-to-boost-conversions-with-in-app-pop-ups', cap: 'in-app', ch: ['in-app'], ind: ['ecommerce'] },
    { t: 'Collect NPS ratings using a slider', h: '/use-cases/in-app-message/how-to-collect-nps-ratings-using-a-slider', cap: 'in-app', ch: ['in-app'], ind: ['b2b'] },
    { t: 'Show pop-ups based on user location', h: '/use-cases/in-app-message/how-to-configure-different-pop-up-messages-based-on-location', cap: 'in-app', ch: ['in-app'], ind: [] },
    { t: 'Create a landscape pop-up using HTML in-app', h: '/use-cases/in-app-message/how-to-create-a-pop-up-for-landscape-view-using-html-in-app', cap: 'in-app', ch: ['in-app'], ind: ['gaming'] },
    { t: 'Run a customer preference survey', h: '/use-cases/in-app-message/how-to-create-a-survey-using-the-drag-drop-editor-to-understand-customer-preferences', cap: 'in-app', ch: ['in-app'], ind: [] },
    { t: 'Introduce the app with a video pop-up', h: '/use-cases/in-app-message/how-to-create-a-video-pop-up-using-drag-drop-editor-to-introduce-the-app-to-new-customers', cap: 'in-app', ch: ['in-app'], ind: ['gaming'] },
    { t: 'Increase iOS app push opt-ins', h: '/use-cases/in-app-message/how-to-increase-ios-app-push-opt-ins', cap: 'in-app', ch: ['in-app'], ind: [] },
    { t: 'Increase feature adoption with the editor', h: '/use-cases/in-app-message/how-to-increase-the-adoption-of-a-feature-using-the-drag-drop-editor', cap: 'in-app', ch: ['in-app'], ind: ['b2b'] },
    { t: 'Send a multi-step in-app survey', h: '/use-cases/in-app-message/how-to-send-a-multi-step-survey-using-an-in-app', cap: 'in-app', ch: ['in-app'], ind: [] },
    { t: 'Show non-intrusive offers using nudges', h: '/use-cases/in-app-message/how-to-show-offers-to-customer-without-being-intrusive-using-nudge', cap: 'in-app', ch: ['in-app'], ind: ['ecommerce'] },
    { t: 'Show sale offers from a specific time', h: '/use-cases/in-app-message/how-to-show-sale-offers-from-a-specific-time', cap: 'in-app', ch: ['in-app'], ind: ['ecommerce'] },
    { t: 'Trigger app rating pop-up for champion users', h: '/use-cases/in-app-message/how-to-trigger-app-rating-pop-up-for-champion-users', cap: 'in-app', ch: ['in-app'], ind: ['gaming'] },
    { t: 'Profile users through in-app surveys', h: '/use-cases/in-app-message/profile-users-through-in-app-surveys', cap: 'in-app', ch: ['in-app'], ind: [] },
    { t: 'Use GIFs in an onboarding walkthrough', h: '/use-cases/in-app-message/use-gifs-in-an-onboarding-walkthrough', cap: 'in-app', ch: ['in-app'], ind: [] },

    // Onsite / OSM (9)
    { t: 'Bring users back with exit-intent banners', h: '/use-cases/on-site-messaging-(osm)/bring-users-back-with-exit-intent-communications', cap: 'onsite', ch: ['onsite'], ind: ['ecommerce'] },
    { t: 'Collect first-party data using Typeform', h: '/use-cases/on-site-messaging-(osm)/collect-first-party-data-using-typeform', cap: 'onsite', ch: ['onsite'], ind: [] },
    { t: 'Collect leads from first-time users', h: '/use-cases/on-site-messaging-(osm)/collect-leads-from-first-time-users', cap: 'onsite', ch: ['onsite'], ind: [] },
    { t: 'Display a non-intrusive countdown timer banner', h: '/use-cases/on-site-messaging-(osm)/display-a-non-intrusive-countdown-timer-banner', cap: 'onsite', ch: ['onsite'], ind: ['ecommerce'] },
    { t: 'Engage anonymous users on your website', h: '/use-cases/on-site-messaging-(osm)/engage-with-anonymous-users-on-your-website', cap: 'onsite', ch: ['onsite'], ind: [] },
    { t: 'Encourage anonymous users to log in', h: '/use-cases/on-site-messaging-(osm)/how-to-encourage-anonymous-users-to-log-in-to-the-website', cap: 'onsite', ch: ['onsite'], ind: [] },
    { t: 'Retarget customers in real time', h: '/use-cases/on-site-messaging-(osm)/how-to-retarget-customers-in-real-time', cap: 'onsite', ch: ['onsite'], ind: ['ecommerce'] },
    { t: 'Highlight plan benefits and offer an upgrade discount', h: '/use-cases/on-site-messaging-(osm)/how-to-show-an-osm-highlighting-the-benefits-of-a-plan-and-offer-a-discount-for-upgrading', cap: 'onsite', ch: ['onsite'], ind: ['telecom'] },
    { t: 'Increase newsletter subscriptions', h: '/use-cases/on-site-messaging-(osm)/increase-newsletter-subscriptions', cap: 'onsite', ch: ['onsite'], ind: ['content'] },

    // Cards (2)
    { t: 'Add carousel banners on the app home page', h: '/use-cases/cards/how-to-add-carousel-banners-on-app-home-page', cap: 'cards', ch: ['cards'], ind: ['ecommerce'] },
    { t: 'Trigger card deletion via custom connector', h: '/use-cases/cards/trigger-card-deletion-through-custom-connector-campaigns', cap: 'cards', ch: ['cards'], ind: [] },

    // WhatsApp (2)
    { t: 'Send WhatsApp based on last activity', h: '/use-cases/whatsapp/how-to-send-messages-in-whatsapp-based-on-users-last-activity-on-the-app', cap: 'whatsapp', ch: ['whatsapp'], ind: [] },
    { t: 'Use conversational messaging in WhatsApp', h: '/use-cases/whatsapp/use-conversational-messaging-in-whatsapp', cap: 'whatsapp', ch: ['whatsapp'], ind: ['ecommerce'] },

    // Facebook (1)
    { t: 'Retarget customers using Facebook', h: '/use-cases/facebook/retarget-customers-using-facebook', cap: 'facebook', ch: [], ind: [] },

    // Flows (13)
    { t: 'Onboarding experience for FinTech products', h: '/use-cases/flows/how-create-onboarding-experience-in-fintech-products', cap: 'flows', ch: [], ind: ['fintech'] },
    { t: 'Convert free trial users into paid users', h: '/use-cases/flows/how-to-convert-free-trial-users-into-paid-users', cap: 'flows', ch: [], ind: ['b2b'] },
    { t: 'Create a welcome experience for new users', h: '/use-cases/flows/how-to-create-welcome-experience-for-new-users', cap: 'flows', ch: [], ind: [] },
    { t: 'Cross-sell bill payments', h: '/use-cases/flows/how-to-cross-sell-bill-payments', cap: 'flows', ch: [], ind: ['fintech', 'telecom'] },
    { t: 'Nudge users to renew their subscription', h: '/use-cases/flows/how-to-nudge-users-to-renew-their-subscription', cap: 'flows', ch: [], ind: ['telecom'] },
    { t: 'Nudge guests to extend their stay', h: '/use-cases/flows/how-to-nudge-your-guests-to-extend-their-stay', cap: 'flows', ch: [], ind: ['travel'] },
    { t: 'Reduce browse abandonment', h: '/use-cases/flows/how-to-reduce-browse-abandonment', cap: 'flows', ch: [], ind: ['ecommerce'] },
    { t: 'Reduce card application abandonment', h: '/use-cases/flows/how-to-reduce-card-application-abandonment', cap: 'flows', ch: [], ind: ['banking', 'fintech'] },
    { t: 'Reduce eKYC abandonment', h: '/use-cases/flows/how-to-reduce-ekyc-abandonment', cap: 'flows', ch: [], ind: ['banking', 'fintech'] },
    { t: 'Reduce loan application abandonment', h: '/use-cases/flows/how-to-reduce-loan-application-abandonment', cap: 'flows', ch: [], ind: ['banking', 'fintech'] },
    { t: 'Retarget dropped-off customers', h: '/use-cases/flows/how-to-retarget-dropped-off-customers', cap: 'flows', ch: [], ind: ['ecommerce'] },
    { t: 'Use gamification to engage users', h: '/use-cases/flows/how-to-use-gamification-to-engage-the-users', cap: 'flows', ch: [], ind: ['gaming'] },
    { t: 'Win inactive users back', h: '/use-cases/flows/how-to-win-inactive-users-back', cap: 'flows', ch: [], ind: [] },

    // Recommendations (13)
    { t: 'Cross-sell study material packages', h: '/use-cases/recommendations/how-to-cross-sell-study-material-packages-to-students', cap: 'recos', ch: [], ind: [] },
    { t: 'Drive upsells through recommendations', h: '/use-cases/recommendations/how-to-drive-upsells-through-recommendations', cap: 'recos', ch: [], ind: ['ecommerce'] },
    { t: 'Personalized shipping confirmation emails', h: '/use-cases/recommendations/how-to-increase-retention-with-personalized-shipping-confirmation-emails', cap: 'recos', ch: ['email'], ind: ['ecommerce'] },
    { t: 'Nudge users to continue watching content', h: '/use-cases/recommendations/how-to-nudge-users-to-continue-watching-content', cap: 'recos', ch: [], ind: ['ott', 'content'] },
    { t: 'Recommend apparel by size and availability', h: '/use-cases/recommendations/how-to-recommend-apparels-by-size-and-availability', cap: 'recos', ch: [], ind: ['ecommerce'] },
    { t: 'Recommend content by preference sequence', h: '/use-cases/recommendations/how-to-recommend-content-to-users-based-on-the-sequence-of-preferences', cap: 'recos', ch: [], ind: ['ott', 'content'] },
    { t: 'Recommend menu items based on purchase history', h: '/use-cases/recommendations/how-to-recommend-menu-items-based-on-purchase-history', cap: 'recos', ch: [], ind: ['ecommerce'] },
    { t: 'Increase average cart size', h: '/use-cases/recommendations/how-to-recommend-products-to-increase-the-average-cart-size', cap: 'recos', ch: [], ind: ['ecommerce'] },
    { t: 'Reduce bounce rates on websites', h: '/use-cases/recommendations/how-to-reduce-bounce-rates-on-websites', cap: 'recos', ch: [], ind: [] },
    { t: 'Reduce cart abandonment on Shopify', h: '/use-cases/recommendations/how-to-reduce-cart-abandonment-on-shopify-stores', cap: 'recos', ch: [], ind: ['ecommerce'] },
    { t: 'Announce a price drop with recommendations', h: '/use-cases/recommendations/how-to-use-recommendations-to-announce-price-drop', cap: 'recos', ch: [], ind: ['ecommerce'] },
    { t: 'Drive the first purchase', h: '/use-cases/recommendations/how-to-use-recommendations-to-drive-first-purchase', cap: 'recos', ch: [], ind: ['ecommerce'] },
    { t: 'Recommend what to watch next', h: '/use-cases/recommendations/recommend-content-to-watch-next', cap: 'recos', ch: [], ind: ['ott', 'content'] },

    // Personalize (5)
    { t: 'Personalize website by user affinity', h: '/use-cases/personalize/how-to-personalize-website-based-on-user-affinity', cap: 'personalize', ch: [], ind: ['b2b'] },
    { t: 'Personalize the current browsing session', h: '/use-cases/personalize/how-to-personalize-website-user-s-current-browsing-session', cap: 'personalize', ch: [], ind: [] },
    { t: 'Rearrange webpage elements with Personalize', h: '/use-cases/personalize/how-to-rearrange-elements-on-a-webpage-using-personalize', cap: 'personalize', ch: [], ind: [] },
    { t: 'Show recently viewed products', h: '/use-cases/personalize/how-to-show-recently-viewed-products-on-website', cap: 'personalize', ch: [], ind: ['ecommerce'] },
    { t: 'Recommend personalized products with grids', h: '/use-cases/personalize/recommend-personalized-products-using-product-grids', cap: 'personalize', ch: [], ind: ['ecommerce'] },

    // Segmentation (10)
    { t: 'Create a birthday email campaign', h: '/use-cases/segmentation/create-a-birthday-email-campaign', cap: 'segments', ch: ['email'], ind: [] },
    { t: 'Create a birthday push campaign', h: '/use-cases/segmentation/create-a-birthday-push-campaign', cap: 'segments', ch: ['push'], ind: [] },
    { t: 'Find users in MoEngage', h: '/use-cases/segmentation/find-users-in-moengage', cap: 'segments', ch: [], ind: [] },
    { t: 'Analyze web activity', h: '/use-cases/segmentation/how-to-analyze-web-activity', cap: 'segments', ch: [], ind: [] },
    { t: 'Encourage repeat orders without a due date', h: '/use-cases/segmentation/how-to-encourage-users-to-repeat-orders-for-categories-without-a-due-date', cap: 'segments', ch: [], ind: ['ecommerce'] },
    { t: 'Identify web push subscribers', h: '/use-cases/segmentation/how-to-identify-web-push-subscribers', cap: 'segments', ch: ['web-push'], ind: [] },
    { t: 'Segment by links clicked in email campaigns', h: '/use-cases/segmentation/segment-users-based-on-the-links-clicked-in-your-email-campaign', cap: 'segments', ch: ['email'], ind: [] },
    { t: 'Segment users on specific app versions', h: '/use-cases/segmentation/segment-users-of-specific-app-versions', cap: 'segments', ch: [], ind: ['telecom'] },
    { t: 'Segment users to notify about app updates', h: '/use-cases/segmentation/segment-users-to-notify-app-updates', cap: 'segments', ch: [], ind: [] },
    { t: 'Segment users who uninstalled the app', h: '/use-cases/segmentation/segment-users-who-uninstalled-your-application', cap: 'segments', ch: [], ind: [] },

    // Analytics (4)
    { t: 'Analyze OTT content performance', h: '/use-cases/analytics/how-to-analyze-ott-content-performance', cap: 'analytics', ch: [], ind: ['ott', 'content'] },
    { t: 'Group and organize campaigns', h: '/use-cases/analytics/how-to-group-and-organise-campaigns', cap: 'analytics', ch: [], ind: [] },
    { t: 'Identify viewership changes between time periods', h: '/use-cases/analytics/how-to-identify-change-in-viewership-between-two-time-periods', cap: 'analytics', ch: [], ind: ['ott', 'content'] },
    { t: 'Identify reasons for app uninstalls', h: '/use-cases/analytics/identify-reasons-for-users-uninstalling-the-app', cap: 'analytics', ch: [], ind: [] },

    // Business Events (4)
    { t: 'Alert on stock price drops', h: '/use-cases/business-events/alert-about-drop-in-stock-price-using-business-events', cap: 'events', ch: [], ind: ['fintech'] },
    { t: 'Run a price drop campaign', h: '/use-cases/business-events/create-a-price-drop-campaign-using-business-events', cap: 'events', ch: [], ind: ['ecommerce'] },
    { t: 'Notify users about a new episode', h: '/use-cases/business-events/send-notifications-for-a-new-episode', cap: 'events', ch: [], ind: ['ott', 'content'] },
    { t: 'Send weather-based contextual messages', h: '/use-cases/business-events/send-weather-based-contextual-messages', cap: 'events', ch: [], ind: ['travel'] },

    // Catalogs (1)
    { t: 'Activate dormant users with Memories', h: '/use-cases/catalogs/how-to-activate-dormant-users-with-memories', cap: 'catalogs', ch: [], ind: [] },

    // Inform (1)
    { t: 'Update order status with Inform', h: '/use-cases/inform/how-to-update-order-status-using-inform', cap: 'inform', ch: [], ind: ['ecommerce'] },

    // Merlin AI (1)
    { t: 'Merlin AI copywriter (global & local)', h: '/use-cases/merlin-ai/merlin-ai-copywriter-for-global-and-local-language', cap: 'ai', ch: [], ind: [] },

    // Partner Integrations (1)
    { t: 'Harness loyalty data to drive engagement', h: '/use-cases/partner-integrations/how-to-harness-loyalty-data-to-drive-customer-engagement', cap: 'integrations', ch: [], ind: [] },
  ];

  // Filter ordering preserved across capability groups
  const CAP_ORDER = ['push', 'email', 'in-app', 'onsite', 'cards', 'whatsapp', 'facebook', 'flows', 'recos', 'personalize', 'segments', 'analytics', 'events', 'catalogs', 'inform', 'ai', 'integrations'];

  const state = {
    initialized: false,
    activeChannels: new Set(),
    activeIndustries: new Set(),
  };

  function isCookbookPage() {
    return document.documentElement.getAttribute('data-current-path') === COOKBOOK_PATH;
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
    })[c]);
  }

  function arrowSvg() {
    return '<svg class="cb-card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>';
  }

  // Capability icons (Lucide-style stroke paths). Inner shapes only — wrapper SVG is added in iconSvg().
  const CAP_ICON_PATHS = {
    push:         '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    email:        '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    'in-app':     '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    onsite:       '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    cards:        '<rect width="18" height="11" x="3" y="3" rx="2"/><path d="M3 14h18"/><path d="M8 21h8"/><path d="M12 17v4"/>',
    whatsapp:     '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    facebook:     '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    flows:        '<line x1="6" y1="3" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
    recos:        '<path d="M9.94 14.34A2 2 0 0 0 8.5 12.9l-5.13-1.32a.5.5 0 0 1 0-.96L8.5 9.3a2 2 0 0 0 1.44-1.44L11.26 2.7a.5.5 0 0 1 .97 0l1.32 5.16a2 2 0 0 0 1.44 1.44l5.13 1.32a.5.5 0 0 1 0 .96L15 12.9a2 2 0 0 0-1.44 1.44L12.23 19.5a.5.5 0 0 1-.97 0z"/><path d="M20 3v4"/><path d="M22 5h-4"/>',
    personalize:  '<path d="m21.64 3.64-1.28-1.28a1.21 1.21 0 0 0-1.72 0L2.36 18.64a1.21 1.21 0 0 0 0 1.72l1.28 1.28a1.2 1.2 0 0 0 1.72 0L21.64 5.36a1.2 1.2 0 0 0 0-1.72z"/><path d="m14 7 3 3"/><path d="M5 6v4"/><path d="M19 14v4"/><path d="M10 2v2"/><path d="M7 8H3"/>',
    segments:     '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    analytics:    '<line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="3" y1="20" x2="21" y2="20"/>',
    events:       '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    catalogs:     '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    inform:       '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/><path d="M4 2C2.8 3.7 2 5.7 2 8"/><path d="M22 8c0-2.3-.8-4.3-2-6"/>',
    ai:           '<path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"/><path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"/>',
    integrations: '<path d="M9 2v6"/><path d="M15 2v6"/><path d="M12 17v5"/><path d="M5 8h14"/><path d="M6 11V8h12v3a6 6 0 0 1-12 0Z"/>',
  };

  function iconSvg(cap, extraClass) {
    const paths = CAP_ICON_PATHS[cap] || '<circle cx="12" cy="12" r="10"/>';
    const cls = extraClass ? ` class="${extraClass}"` : '';
    return (
      `<svg${cls} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">` +
      paths +
      '</svg>'
    );
  }

  function recipeToHtml(r) {
    const capLabel = CAP_LABELS[r.cap] || r.cap;
    const channels = (r.ch || []).join(',');
    const industries = (r.ind || []).join(',');
    const indTags = (r.ind || [])
      .map((i) => `<span class="cb-tag">${escapeHtml(INDUSTRY_LABELS[i] || i)}</span>`)
      .join('');
    return (
      `<a class="cb-card" href="${escapeHtml(r.h)}" ` +
      `data-cap="${escapeHtml(r.cap)}" ` +
      `data-channels="${escapeHtml(channels)}" ` +
      `data-industries="${escapeHtml(industries)}" ` +
      `aria-label="${escapeHtml(r.t)} — ${escapeHtml(capLabel)}">` +
      `<span class="cb-card-watermark" aria-hidden="true">${iconSvg(r.cap)}</span>` +
      `<div class="cb-card-head">` +
      `<span class="cb-cap" title="${escapeHtml(capLabel)}">${iconSvg(r.cap)}</span>` +
      arrowSvg() +
      `</div>` +
      `<h3 class="cb-card-title">${escapeHtml(r.t)}</h3>` +
      (indTags ? `<div class="cb-card-tags">${indTags}</div>` : '') +
      `</a>`
    );
  }

  function renderGrid() {
    const grid = document.getElementById('cb-grid');
    if (!grid) return;
    const list = RECIPES.slice().sort(
      (a, b) => CAP_ORDER.indexOf(a.cap) - CAP_ORDER.indexOf(b.cap)
    );
    grid.innerHTML = list.map(recipeToHtml).join('');
    grid.setAttribute('aria-busy', 'false');
  }

  function renderActiveChips() {
    const wrap = document.getElementById('cb-active-row');
    const list = document.getElementById('cb-active-chips');
    if (!wrap || !list) return;
    const items = [];
    state.activeChannels.forEach((v) => {
      items.push({ group: 'channel', value: v, label: CHANNEL_LABELS[v] || v });
    });
    state.activeIndustries.forEach((v) => {
      items.push({ group: 'industry', value: v, label: INDUSTRY_LABELS[v] || v });
    });
    if (items.length === 0) {
      wrap.setAttribute('hidden', '');
      list.innerHTML = '';
      return;
    }
    wrap.removeAttribute('hidden');
    list.innerHTML = items
      .map(
        (it) =>
          `<span class="cb-active-chip">${escapeHtml(it.label)}` +
          `<button type="button" class="cb-active-chip-x" data-group="${it.group}" data-value="${escapeHtml(it.value)}" aria-label="Remove ${escapeHtml(it.label)} filter">×</button>` +
          `</span>`
      )
      .join('');
  }

  function applyFilters() {
    const cards = document.querySelectorAll('.cb-card');
    const ch = state.activeChannels;
    const ind = state.activeIndustries;
    let visible = 0;

    cards.forEach((card) => {
      const cardChannels = (card.dataset.channels || '').split(',').filter(Boolean);
      const cardIndustries = (card.dataset.industries || '').split(',').filter(Boolean);

      const channelMatch = ch.size === 0 || cardChannels.some((c) => ch.has(c));
      const industryMatch = ind.size === 0 || cardIndustries.some((i) => ind.has(i));

      if (channelMatch && industryMatch) {
        card.classList.remove('cb-hidden');
        visible++;
      } else {
        card.classList.add('cb-hidden');
      }
    });

    const grid = document.getElementById('cb-grid');
    const empty = document.getElementById('cb-empty');
    if (grid && empty) {
      if (visible === 0) {
        grid.style.display = 'none';
        empty.removeAttribute('hidden');
      } else {
        grid.style.display = '';
        empty.setAttribute('hidden', '');
      }
    }

    renderActiveChips();
  }

  function syncChipPressedState() {
    document.querySelectorAll('.cb-chip').forEach((btn) => {
      const group = btn.dataset.group;
      const value = btn.dataset.value;
      const set = group === 'channel' ? state.activeChannels : state.activeIndustries;
      btn.setAttribute('aria-pressed', set.has(value) ? 'true' : 'false');
    });
  }

  function toggleFilter(group, value) {
    const set = group === 'channel' ? state.activeChannels : state.activeIndustries;
    if (set.has(value)) set.delete(value);
    else set.add(value);
    syncChipPressedState();
    applyFilters();
  }

  function clearAll() {
    state.activeChannels.clear();
    state.activeIndustries.clear();
    syncChipPressedState();
    applyFilters();
  }

  function setupCookbook() {
    if (!isCookbookPage()) return;
    if (state.initialized && document.getElementById('cb-grid')?.querySelector('.cb-card')) {
      return;
    }
    const app = document.getElementById('cb-app');
    if (!app) return;
    if (!document.getElementById('cb-grid')) return;

    renderGrid();
    syncChipPressedState();
    applyFilters();

    if (state.initialized) return;
    state.initialized = true;

    document.addEventListener('click', (e) => {
      if (!isCookbookPage()) return;
      const chip = e.target.closest && e.target.closest('.cb-chip');
      if (chip) {
        const group = chip.dataset.group;
        const value = chip.dataset.value;
        if (group && value) toggleFilter(group, value);
        return;
      }
      const activeX = e.target.closest && e.target.closest('.cb-active-chip-x');
      if (activeX) {
        const group = activeX.dataset.group;
        const value = activeX.dataset.value;
        if (group && value) toggleFilter(group, value);
        return;
      }
      if (e.target.id === 'cb-clear' || e.target.id === 'cb-empty-reset') {
        clearAll();
      }
    });

  }

  function maybeSetup() {
    if (isCookbookPage()) {
      setupCookbook();
    } else {
      state.initialized = false;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', maybeSetup);
  } else {
    maybeSetup();
  }

  let cbDebounce = null;
  const cbObserver = new MutationObserver(() => {
    if (cbDebounce) clearTimeout(cbDebounce);
    cbDebounce = setTimeout(maybeSetup, 100);
  });
  cbObserver.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-current-path'],
  });
  cbObserver.observe(document.body, {
    childList: true,
    subtree: true,
  });

  window.addEventListener('load', () => setTimeout(maybeSetup, 300));
})();
