-------------------------------------------------------
-- 1. CREATE SCHEMA
-------------------------------------------------------
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'CW2')
BEGIN
    EXEC('CREATE SCHEMA CW2');
END;
GO

-------------------------------------------------------
-- 2. CREATE USER TABLE
-------------------------------------------------------
CREATE TABLE CW2.[User] (
    user_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);
GO

-------------------------------------------------------
-- 3. CREATE TRAIL TABLE
-------------------------------------------------------
CREATE TABLE CW2.Trail (
    trail_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(MAX),
    difficulty VARCHAR(50),
    length_km FLOAT,
    created_at DATETIME DEFAULT GETDATE(),

    CONSTRAINT FK_Trail_User FOREIGN KEY (user_id)
        REFERENCES CW2.[User](user_id)
        ON DELETE CASCADE
);
GO

-------------------------------------------------------
-- 4. CREATE TRAILPOINT TABLE
-------------------------------------------------------
CREATE TABLE CW2.TrailPoint (
    point_id INT IDENTITY(1,1) PRIMARY KEY,
    trail_id INT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    point_order INT NOT NULL,

    CONSTRAINT FK_TrailPoint_Trail FOREIGN KEY (trail_id)
        REFERENCES CW2.Trail(trail_id)
        ON DELETE CASCADE
);
GO

-------------------------------------------------------
-- 5. CREATE TRAILFEATURE TABLE
-------------------------------------------------------
CREATE TABLE CW2.TrailFeature (
    feature_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);
GO

-------------------------------------------------------
-- 6. CREATE TRAIL_TAILFEATURE (MANY-TO-MANY LINKING TABLE)
-------------------------------------------------------
CREATE TABLE CW2.Trail_TrailFeature (
    trail_id INT NOT NULL,
    feature_id INT NOT NULL,

    CONSTRAINT FK_TTF_Trail FOREIGN KEY (trail_id)
        REFERENCES CW2.Trail(trail_id)
        ON DELETE CASCADE,

    CONSTRAINT FK_TTF_Feature FOREIGN KEY (feature_id)
        REFERENCES CW2.TrailFeature(feature_id)
        ON DELETE CASCADE
);
GO

-------------------------------------------------------
-- 7. CREATE PHOTO TABLE
-------------------------------------------------------
CREATE TABLE CW2.Photo (
    photo_id INT IDENTITY(1,1) PRIMARY KEY,
    trail_id INT NOT NULL,
    photo_url VARCHAR(MAX),
    uploaded_at DATETIME DEFAULT GETDATE(),

    CONSTRAINT FK_Photo_Trail FOREIGN KEY (trail_id)
        REFERENCES CW2.Trail(trail_id)
        ON DELETE CASCADE
);
GO

-------------------------------------------------------
-- 8. CREATE TRAIL LOG TABLE (USED BY TRIGGER)
-------------------------------------------------------
CREATE TABLE CW2.TrailLog (
    log_id INT IDENTITY(1,1) PRIMARY KEY,
    trail_id INT NOT NULL,
    action VARCHAR(50),
    timestamp DATETIME DEFAULT GETDATE(),
    info VARCHAR(MAX)
);
GO

-------------------------------------------------------
-- 9. TRIGGER FOR AUDIT LOGGING
-------------------------------------------------------
CREATE TRIGGER CW2.trg_InsertTrailLog
ON CW2.Trail
AFTER INSERT
AS
BEGIN
    INSERT INTO CW2.TrailLog (trail_id, action, info)
    SELECT trail_id, 'INSERT', 'New trail created'
    FROM inserted;
END;
GO

-------------------------------------------------------
-- 10. VIEW FOR TRAIL DETAILS
-------------------------------------------------------
CREATE VIEW CW2.vw_TrailDetails AS
SELECT 
    T.trail_id,
    T.name,
    T.description,
    T.difficulty,
    T.length_km,
    TP.latitude,
    TP.longitude,
    TF.name AS feature_name
FROM CW2.Trail T
LEFT JOIN CW2.TrailPoint TP ON T.trail_id = TP.trail_id
LEFT JOIN CW2.Trail_TrailFeature TTF ON T.trail_id = TTF.trail_id
LEFT JOIN CW2.TrailFeature TF ON TTF.feature_id = TF.feature_id;
GO
