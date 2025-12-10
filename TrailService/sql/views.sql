CREATE VIEW vw_TrailDetails AS
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
