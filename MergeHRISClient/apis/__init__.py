
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.account_token_api import AccountTokenApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from MergeHRISClient.api.account_token_api import AccountTokenApi
from MergeHRISClient.api.activities_api import ActivitiesApi
from MergeHRISClient.api.applications_api import ApplicationsApi
from MergeHRISClient.api.attachments_api import AttachmentsApi
from MergeHRISClient.api.available_actions_api import AvailableActionsApi
from MergeHRISClient.api.candidates_api import CandidatesApi
from MergeHRISClient.api.departments_api import DepartmentsApi
from MergeHRISClient.api.eeocs_api import EeocsApi
from MergeHRISClient.api.interviews_api import InterviewsApi
from MergeHRISClient.api.job_interview_stages_api import JobInterviewStagesApi
from MergeHRISClient.api.jobs_api import JobsApi
from MergeHRISClient.api.link_token_api import LinkTokenApi
from MergeHRISClient.api.offers_api import OffersApi
from MergeHRISClient.api.offices_api import OfficesApi
from MergeHRISClient.api.reject_reasons_api import RejectReasonsApi
from MergeHRISClient.api.scorecards_api import ScorecardsApi
from MergeHRISClient.api.tags_api import TagsApi
from MergeHRISClient.api.users_api import UsersApi
