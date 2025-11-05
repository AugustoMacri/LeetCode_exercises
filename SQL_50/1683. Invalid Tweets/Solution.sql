select t.tweet_id
from Tweets as t
where LENGTH(t.content) > 15