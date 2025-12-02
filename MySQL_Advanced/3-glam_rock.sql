-- Query to find the lifespan of Glam rock bands in the metal_bands table.

SELECT band_name,
       COALESCE(split, YEAR(CURDATE())) - formed AS lifespan
FROM metal_bands
WHERE style LIKE 'Glam rock%'
ORDER BY lifespan DESC;
