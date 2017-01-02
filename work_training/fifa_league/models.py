from django.db import models
from django.utils.translation import ugettext as _

from django.db.models.signals import post_save
from .functions import add_points_to_teams


class League(models.Model):
    """
    League model
    - shortcut field for user-friendly url
    """
    name = models.CharField(max_length=250)
    shortcut = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('League')
        verbose_name_plural = _('Leagues')

    def __str__(self):
        return str(self.name)


class Team(models.Model):
    """
    Team model
    - shortcut field for user-friendly url
    """
    name = models.CharField(max_length=250)
    shortcut = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self):
        return _('Club: {}').format(self.name)


class TeamStat(models.Model):
    """
    TeamStat model
    - each TeamStat model related to one team and one league
    """
    league = models.ForeignKey(League, related_name="teams_stat")
    team = models.ForeignKey(Team, related_name="leagues_stat")
    match_count = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Team statistic')
        verbose_name_plural = _('Teams statistics')

    def __str__(self):
        return _('Statistic: {} in {} league')\
            .format(self.team.name, self.league.name)


class Player(models.Model):
    """
    Player model
    - one player related to one team
    """
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=500)
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Player')

    def __str__(self):
        return _('{} | Club: {}').format(self.name, self.team.name)


class Match(models.Model):
    """
    Match model
    - one match related to two TeamStat
    (home and guest teams in specific league)
    """
    team_home = models.ForeignKey(TeamStat, related_name="home_matches")
    team_guest = models.ForeignKey(TeamStat, related_name="guest_matches")
    team_home_goals = models.IntegerField(default=0)
    team_guest_goals = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')

    def __str__(self):
        return _('{} vs {} ( {}:{})').format(self.team_home.team.name,
                                             self.team_guest.team.name,
                                             self.team_home_goals,
                                             self.team_guest_goals)


post_save.connect(add_points_to_teams, Match)
