from elenasTest.core.settings import *


DEBUG = False

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

COVER_MIN_PERCENTAGE = 20

NOSE_ARGS = [
    '--with-coverage',
    '--cover-xml',
    '--cover-xml-file=coverage.xml',
    '--cover-package=application',
    '--cover-erase',
    '--cover-branches',
    '--cover-min-percentage=%d' % COVER_MIN_PERCENTAGE,
    '--cover-html',
    '--cover-html-dir=htmlcov',
    '--with-xunit',
    '--xunit-file=xunit-results.xml',
]