CREATE TRIGGER trg_InsertTrailLog
ON CW2.Trail
AFTER INSERT
AS
BEGIN
    INSERT INTO CW2.TrailLog (trail_id, action, info)
    SELECT trail_id, 'INSERT', 'New trail created'
    FROM inserted;
END
GO
