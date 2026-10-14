// uiStore.ts – Zustand store cho UI state
// Mục tiêu:
// - State: theme ('dark' | 'light'), language ('vi' | 'en'), 
//          gridLayout ('1x1' | '2x2' | '3x3' | '4x4'),
//          sidebarCollapsed: boolean
// - Actions: setTheme, setLanguage, setGridLayout, toggleSidebar
// - Persist tất cả vào localStorage
// - Áp dụng class 'dark' / 'light' lên document.documentElement khi thay đổi theme