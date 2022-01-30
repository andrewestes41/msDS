a = LOAD 'u.user' USING PigStorage('|') AS (userid:int, age:int);
b = FILTER a BY userid < 8;
STORE b INTO 'output';

