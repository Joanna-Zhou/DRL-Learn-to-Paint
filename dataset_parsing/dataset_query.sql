create view TorontoBusinessReview as

select 

R.user_id as user_id,
R.business_id as business_id,
R.review_id as review_id,

R.stars as review_stars,
R.useful as review_useful,
R.funny as review_funny,
R.cool as review_cool,
R.text as review_text,
R.date as review_date,

B.name as business_name,
B.address as business_address,
B.city as business_city,
B.state as business_state,
B.postal_code as business_postal_code,
B.latitude as business_latitude,
B.longitude as business_longitude,
B.stars as business_stars,
B.review_count as business_review_count,
B.is_open as business_is_open,
B.categories as business_categories,

U.name as user_name,
U.review_count as user_review_count,
U.yelping_since as user_yelping_since,
U.useful as user_useful,
U.funny as user_funny,
U.cool as user_cool,
U.fans as user_fans,
U.average_stars as user_average_stars,
U.compliment_hot as user_compliment_hot,
U.compliment_more as user_compliment_more,
U.compliment_profile as user_compliment_profile,
U.compliment_cute as user_compliment_cute,
U.compliment_list as user_compliment_list,
U.compliment_note as user_compliment_note,
U.compliment_plain as user_compliment_plain,
U.compliment_cool as user_compliment_cool,
U.compliment_funny as user_compliment_funny,
U.compliment_writer as user_compliment_writer,
U.compliment_photos as user_compliment_photos

from public.review R 
join public.business B ON R.business_id = B.business_id
join public.user U on U.user_id = R.user_id
where B.city = 'Toronto'
order by U.user_id, R.date DESC