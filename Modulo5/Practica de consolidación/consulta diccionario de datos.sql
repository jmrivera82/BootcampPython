SELECT
    table_name AS nombre_tabla,
    column_name AS nombre_columna,
    data_type AS tipo_dato,
    character_maximum_length AS longitud,
    is_nullable AS columna_nulo,
    domain_name AS columna_dominio,
    column_default AS columna_defecto
FROM
    information_schema.columns
WHERE
    table_schema = 'public'  
    AND table_name IN ('customer','actor','category','film','film_actor','film_category','address','city','country','inventory','language','payment','rental','staff','store')  
ORDER BY
    table_name;