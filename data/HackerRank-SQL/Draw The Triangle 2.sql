SET @NUMBER := 0;
SELECT REPEAT('* ', @NUMBER
:= @NUMBER + 1) from information_schema.tables where @NUMBER < 20;