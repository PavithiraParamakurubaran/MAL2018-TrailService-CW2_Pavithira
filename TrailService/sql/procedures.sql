CREATE PROCEDURE sp_InsertTrail
    @name VARCHAR(255),
    @description VARCHAR(MAX),
    @difficulty VARCHAR(50),
    @length_km FLOAT,
    @user_id INT
AS
BEGIN
    INSERT INTO CW2.Trail (name, description, difficulty, length_km, user_id)
    VALUES (@name, @description, @difficulty, @length_km, @user_id)
END
GO


CREATE PROCEDURE sp_GetAllTrails
AS
BEGIN
    SELECT * FROM CW2.Trail
END
GO


CREATE PROCEDURE sp_GetTrailById
    @trail_id INT
AS
BEGIN
    SELECT * FROM CW2.Trail WHERE trail_id = @trail_id
END
GO


CREATE PROCEDURE sp_UpdateTrail
    @trail_id INT,
    @name VARCHAR(255),
    @description VARCHAR(MAX),
    @difficulty VARCHAR(50),
    @length_km FLOAT
AS
BEGIN
    UPDATE CW2.Trail
    SET name=@name,
        description=@description,
        difficulty=@difficulty,
        length_km=@length_km
    WHERE trail_id=@trail_id
END
GO


CREATE PROCEDURE sp_DeleteTrail
    @trail_id INT
AS
BEGIN
    DELETE FROM CW2.Trail WHERE trail_id=@trail_id
END
GO
