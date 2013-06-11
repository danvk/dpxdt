#!/usr/bin/env python
# Copyright 2013 Brett Slatkin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration for local development."""

SQLALCHEMY_DATABASE_URI = (
    'mysql+gaerdbms:///test?instance=dpxdt-project:test')

# Google OAuth2 login config for test version development.
GOOGLE_OAUTH2_CLIENT_ID = '918724168220.apps.googleusercontent.com'
GOOGLE_OAUTH2_EMAIL_ADDRESS = '918724168220@developer.gserviceaccount.com'
GOOGLE_OAUTH2_REDIRECT_PATH = '/oauth2callback'
GOOGLE_OAUTH2_REDIRECT_URI = (
    'https://dpxdt-test.appspot.com' + GOOGLE_OAUTH2_REDIRECT_PATH)


from secrets import *


GOOGLE_OAUTH2_CLIENT_SECRET = GOOGLE_OAUTH2_TEST_DEPLOY_CLIENT_SECRET
