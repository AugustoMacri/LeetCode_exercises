select c.name
from customer as c
where c.referee_id is NULL 
    or  c.referee_id <> 2;