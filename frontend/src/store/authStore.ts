// authStore.ts – Zustand store cho xác thực
// Mục tiêu:
// - State: user (UserOut | null), accessToken, refreshToken, isAuthenticated
// - Actions: setTokens, setUser, logout, updateUser
// - Persist: lưu token vào localStorage (persist middleware)
// - Không lưu mật khẩu, chỉ lưu token