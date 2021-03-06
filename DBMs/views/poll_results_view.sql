CREATE OR REPLACE VIEW public.poll_results_view AS 
SELECT
	ans.id,
	ans.id_poll_data,
	poll.id_user,
	ans.answer,
	ans.answered_by,
	usr.user_name,
	poll.question,
	poll.poll_hash,
	poll.created_on,
	poll.options,
	poll.question_type
FROM public.poll_answers AS ans
JOIN public."user" AS usr
	ON ans.answered_by = usr.id
JOIN public.poll_data AS poll
	ON ans.id_poll_data = poll.id