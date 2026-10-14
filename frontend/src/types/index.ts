// types/index.ts – Định nghĩa kiểu dữ liệu TypeScript dùng chung

// ── Auth ──────────────────────────────────────────
export interface TokenResponse {
  access_token: string
  refresh_token: string
  token_type: string
  expires_in: number
}

// ── User ─────────────────────────────────────────
export type UserRole = 'admin' | 'operator' | 'viewer'

export interface User {
  id: number
  username: string
  email: string
  full_name: string | null
  role: UserRole
  is_active: boolean
  avatar_url: string | null
  created_at: string
  last_login: string | null
}

// ── Camera ───────────────────────────────────────
export interface RoiPolygon { points: [number, number][] }

export interface DetectionRules {
  min_consecutive_frames: number
  cooldown_seconds: number
}

export interface Camera {
  id: number
  name: string
  url: string
  location: string
  is_active: boolean
  confidence_threshold: number | null
  roi: RoiPolygon[] | null
  detection_rules: DetectionRules
  fps_limit: number
  added_by: number
  created_at: string
  updated_at: string
}

export interface CameraStatus extends Camera {
  current_fps: number
  last_detection_at: string | null
  worker_running: boolean
}

// ── Event ────────────────────────────────────────
export type EventStatus = 'new' | 'confirmed' | 'false_alarm'

export interface BoundingBox {
  class_name: string
  confidence: number
  x1: number; y1: number; x2: number; y2: number
}

export interface WeaponEvent {
  id: number
  camera_id: number
  camera_name: string
  detected_at: string
  weapon_class: string
  confidence: number
  snapshot_path: string | null
  clip_path: string | null
  bounding_boxes: BoundingBox[]
  status: EventStatus
  reviewed_by: number | null
  review_note: string | null
  notified: boolean
}

// ── WebSocket Alert Payload ───────────────────────
export interface EventAlertPayload {
  event_id: number
  camera_id: number
  camera_name: string
  weapon_class: string
  confidence: number
  snapshot_url: string
  detected_at: string
  bounding_boxes: BoundingBox[]
}

// ── Analytics ────────────────────────────────────
export interface DashboardStats {
  total_events_today: number
  total_cameras_active: number
  total_false_alarms: number
  avg_confidence: number
}

export interface TimeSeriesPoint { timestamp: string; count: number }
export interface WeaponDist { weapon_class: string; count: number; percentage: number }
export interface HeatmapCell { hour: number; day_of_week: number; count: number }

// ── Pagination ───────────────────────────────────
export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  page_size: number
}

// ── Grid Layout ──────────────────────────────────
export type GridLayout = '1x1' | '2x2' | '3x3' | '4x4'