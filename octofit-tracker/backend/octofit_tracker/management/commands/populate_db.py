from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')


        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Create activities
        Activity.objects.create(user_email=tony.email, type='run', duration=30, date=date(2024,1,1))
        Activity.objects.create(user_email=steve.email, type='cycle', duration=45, date=date(2024,1,2))
        Activity.objects.create(user_email=bruce.email, type='swim', duration=60, date=date(2024,1,3))
        Activity.objects.create(user_email=clark.email, type='run', duration=50, date=date(2024,1,4))

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(user_email=tony.email, points=100, rank=1)
        Leaderboard.objects.create(user_email=steve.email, points=90, rank=2)
        Leaderboard.objects.create(user_email=bruce.email, points=80, rank=3)
        Leaderboard.objects.create(user_email=clark.email, points=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
