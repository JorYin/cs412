# File: views.py
# Author: Jordan Yin (jordany@bu.edu), 10/30/2026
# Description: Class-based views for listing, filtering, graphing, and viewing voter records.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Voter
import plotly
import plotly.graph_objs as go


def filtered_voters(request):
    """Helper function that returns voter records filtered by query parameters."""
    voters = Voter.objects.all().order_by('last_name', 'first_name')

    party = request.GET.get('party')
    voter_score = request.GET.get('voter_score')
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')

    if party:
        voters = voters.filter(party_affiliation=party)
    if voter_score:
        voters = voters.filter(voter_score=voter_score)
    if min_year:
        voters = voters.filter(date_of_birth__gte=f'{min_year}-01-01')
    if max_year:
        voters = voters.filter(
            date_of_birth__lt=f'{int(max_year) + 1}-01-01'
        )

    # Check which election filters were selected and filter for participating voters.
    for field in ('v20state', 'v21town', 'v21primary', 'v22general', 'v23town'):
        if request.GET.get(field):
            voters = voters.filter(**{field: True})

    return voters

class VoterListView(ListView):
    """Display a paginated, filterable list of voter records."""
 
    model = Voter
    template_name = 'voter_analytics/voter_list_results.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        """Return the filtered voters for the list page."""
        return filtered_voters(self.request)

    def get_context_data(self, **kwargs):
        """Add filter choices and pagination query parameters to the context."""
        context = super().get_context_data(**kwargs)
        query_string = self.request.GET.copy()
        query_string.pop('page', None)
        context['query_string'] = query_string.urlencode()
        
        context['parties'] = (
            Voter.objects.values_list('party_affiliation', flat=True)
            .distinct()
            .order_by('party_affiliation')
        )
        context['years'] = range(1913, 2024)
        context['scores'] = range(6)
        context['form_action'] = 'voters'
        return context
    
class VoterDetailView(DetailView):
    """Display the details for one voter."""

    model = Voter
    template_name = 'voter_analytics/voter_detail_view.html'
    context_object_name = 'voter'


class VoterGraphsView(ListView):
    """Display aggregate voter graphs for the filtered voter records."""

    model = Voter
    template_name = 'voter_analytics/graphs.html'

    def get_queryset(self):
        """Return the filtered voters used to build the graphs."""
        return filtered_voters(self.request)

    def get_context_data(self, **kwargs):
        """Build Plotly graphs and add filter choices to the template context."""
        context = super().get_context_data(**kwargs)
        voters = list(self.object_list)

        # Count how many voters were born in each year.
        birth_years_dict = {}
        for voter in voters:
            DoB = voter.date_of_birth[:4]
            if birth_years_dict.get(DoB, -1) == -1:
                birth_years_dict[DoB] = 1
            else:
                birth_years_dict[DoB] += 1

        years = sorted(birth_years_dict)
        counts = [birth_years_dict[year] for year in years]

        graph_dob = plotly.offline.plot(
            go.Figure(data=[go.Bar(
                    x=years,
                    y=counts,
                    name='Voters',
                )]),
            auto_open=False,
            output_type='div',
        )

        # Count how many voters belong to each party affiliation.
        party_dict = {}

        for voter in voters:
            party = voter.party_affiliation.strip()

            if party_dict.get(party, -1) == -1:
                party_dict[party] = 1
            else:
                party_dict[party] += 1
        
        parties = sorted(party_dict)
        party_counts = [party_dict[party] for party in parties]
        
        graph_party = plotly.offline.plot(
            go.Figure(data=[go.Pie(
                labels=parties,
                values=party_counts,
            )]),
            auto_open=False,
            output_type='div',
        )

        election_fields = (
            'v20state',
            'v21town',
            'v21primary',
            'v22general',
            'v23town',
        )
        
        election_counts = {}
        # Initialize one counter for each election.
        for election_field in election_fields:
            election_counts[election_field] = 0

        # Count participation in each election for every filtered voter.
        for voter in voters:
            # Increment each counter when this voter participated.
            if voter.v20state:
                election_counts['v20state'] += 1

            if voter.v21town:
                election_counts['v21town'] += 1

            if voter.v21primary:
                election_counts['v21primary'] += 1

            if voter.v22general:
                election_counts['v22general'] += 1

            if voter.v23town:
                election_counts['v23town'] += 1
        
        elections = sorted(election_counts)
        counts = [election_counts[election] for election in elections]
        
        graph_elections = plotly.offline.plot(
            go.Figure(data=[go.Bar(
                x=elections,
                y=counts,
                name='Voters',
            )]),
            auto_open=False,
            output_type='div',
        )

        context['graph_dob'] = graph_dob
        context['graph_party'] = graph_party
        context['graph_elections'] = graph_elections
        context['parties'] = (
            Voter.objects.values_list('party_affiliation', flat=True)
            .distinct()
            .order_by('party_affiliation')
        )
        context['years'] = range(1913, 2024)
        context['scores'] = range(6)
        context['form_action'] = 'graphs'
        
        return context