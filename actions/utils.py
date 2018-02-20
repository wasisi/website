import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action

# Create action which avoids saving duplicate actions and return a boolean to tell if the action was saved or not.
def create_action(user, verb, target=None):
	# check for any similar action made in the last minute. Useful e.g. when someone clicks on like button many times
	now = timezone.now()
	last_minute = now - datetime.timedelta(seconds=60) #Can be increased. Retrieves all actions performed in the last minute.
	similar_actions = Action.objects.filter(user_id=user.id,
		verb= verb,
		timestamp__gte=last_minute)
	if target:
		target_ct = ContentType.objects.get_for_model(target)
		similar_actions = similar_actions.filter(
			target_ct=target_ct,
			target_id=target.id)
	if not similar_actions:
		# no existing actions found
		action = Action(user=user, verb=verb, target=target)
		action.save()
	return True
	return False
