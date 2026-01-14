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
