-- Script that creates a trigger that rests
-- the attribute valid_email only when the email has been changed
-- Create the trigger
DELIMITER //

CREATE TRIGGER reset BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;//

DELIMITER ;
