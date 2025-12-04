-- This SQL script creates an index on the 'names' table
-- to optimize queries that filter by 'name' and 'score' columns.

CREATE INDEX idx_name_score ON names(name(1), score);
