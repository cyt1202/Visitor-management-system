-- ============================================
--  Users
-- ============================================
CREATE TABLE Users (
    user_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    username       TEXT UNIQUE NOT NULL,
    password_hash  TEXT NOT NULL,
    created_at     DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
--  Visitor_Info
-- ============================================
CREATE TABLE Visitor_Info (
    visitor_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id        INTEGER NOT NULL,
    name           TEXT NOT NULL,
    phone          TEXT NOT NULL,
    affiliation    TEXT,
    updated_at     DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- ============================================
--  Admins
-- ============================================
CREATE TABLE Admins (
    admin_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username       TEXT UNIQUE NOT NULL,
    password_hash  TEXT NOT NULL,
    phone          TEXT,
    created_at     DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- Admin_info
-- ============================================
CREATE TABLE Admin_info (
    admin_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    username    TEXT NOT NULL UNIQUE,
    email       TEXT NOT NULL UNIQUE,
    phone       TEXT NOT NULL UNIQUE
);

-- ============================================
--  Reservations
-- ============================================
CREATE TABLE Reservations (
    reservation_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id         INTEGER NOT NULL,
    visit_date      DATE NOT NULL,
    visit_time      TIME NOT NULL,
    location        TEXT NOT NULL,
    purpose         TEXT NOT NULL,

    status          TEXT NOT NULL CHECK (status IN ('pending','approved','denied')),
    admin_id        INTEGER,     
    review_comment  TEXT,

    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id)
);
