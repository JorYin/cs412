# File: models.py
# Author: Jordan Yin (jordany@bu.edu), 10/30/2026
# Description: Database models and CSV data-loading functionality for voter analytics.

from django.db import models

class Voter(models.Model):
    """Represent a registered Newton voter and their election history."""
    # name
    first_name = models.TextField()
    last_name = models.TextField()
 
    # location
    street_number = models.IntegerField()
    street_name = models.TextField()
    apartment_number = models.CharField(max_length=10)
    zip_code = models.IntegerField()
 
    # DoB, registration, party, precinct Number
    date_of_birth = models.TextField()
    date_of_registration = models.TextField()
    party_affiliation = models.CharField(max_length=2)
    precinct_number = models.IntegerField()
    
    # voting history
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()
    voter_score = models.IntegerField()
 
    def __str__(self):
        """Return the voter's name."""
        return f'{self.first_name} {self.last_name}'
      
def load_data():
  """Load voter records from the CSV file into the database."""

  # delete existing records to prevent duplicates:
  Voter.objects.all().delete()

  filename = 'voter_analytics/data/newton_voters.csv'
  f = open(filename)
  f.readline() # discard headers

  for line in f:
      fields = line.split(',')
      
      try:
          # create a new instance of Result object with this record from CSV
          voter = Voter(
            last_name = fields[1],
            first_name = fields[2],
            street_number = fields[3],
            street_name = fields[4],
            apartment_number = fields[5],
            zip_code = fields[6],
            date_of_birth = fields[7],
            date_of_registration = fields[8],
            party_affiliation = fields[9],
            precinct_number = fields[10],
            v20state = fields[11] == 'TRUE',
            v21town = fields[12] == 'TRUE',
            v21primary = fields[13] == 'TRUE',
            v22general = fields[14] == 'TRUE',
            v23town = fields[15] == 'TRUE',
            voter_score = fields[16],
          )
      
          voter.save() # commit to database
          print(f'Created voter: {voter}')
          
      except:
          print(f"Skipped: {fields}")
  
  print(f'Done. Created {len(Voter.objects.all())} Results.')