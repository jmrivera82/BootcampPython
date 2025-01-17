SELECT
    table_name,
    column_name,
    data_type,
    character_maximum_length,
    is_nullable
FROM
    public.columns
WHERE
    table_schema = 'public'  
    AND table_name IN ('customer','actor','category','film','film_actor','film_category','address','city','country','inventory','language','payment','rental','staff','store')  
ORDER BY
    table_name,
    ordinal_position;