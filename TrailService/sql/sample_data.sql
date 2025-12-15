INSERT INTO CW2.[User] (user_id, name, email_hash, role)
VALUES (2, 'Pavithira Paramakurubaran', 'pavithira456', 'standard');

INSERT INTO CW2.TrailFeature (name, description)
VALUES ('Canyon Climb', 'Steep canyon with rocky paths'),
       ('Lake Loop', 'Gentle trail around a scenic lake'),
       ('Sunrise Peak', 'Trail leading to a high peak for sunrise views');

INSERT INTO CW2.Trail (user_id, name, description, difficulty, length_km)
VALUES (2, 'Emerald Forest Trail', 'A lush forest trail with lots of greenery.', 'Easy', 5.7);

INSERT INTO CW2.TrailPoint (trail_id, latitude, longitude, point_order)
VALUES (2, 2.1350, 101.1300, 1),
       (2, 2.1362, 101.1315, 2),
       (2, 2.1375, 101.1330, 3),
       (2, 2.1388, 101.1345, 4);
