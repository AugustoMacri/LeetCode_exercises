with process_time as (
    select
        machine_id,
        process_id,
        MAX(case when activity_type = 'start' then timestamp end) as start_time,
        MAX(case when activity_type = 'end' then timestamp end) as end_time
    from Activity
    group by machine_id, process_id
)


select 
    machine_id,
    round (avg(end_time - start_time), 3) as processing_time
from process_time
group by machine_id
