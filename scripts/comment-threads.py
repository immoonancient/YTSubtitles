#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Adapted from https://github.com/youtube/api-samples/blob/master/python/comment_threads.py

# Usage example:
# python comment_threads.py --channelid='<channel_id>' --videoid='<video_id>' --text='<text>'

import httplib2
import os
import sys
import time

from apiclient.discovery import build_from_document
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains

# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
YOUTUBE_READ_WRITE_SSL_SCOPE = "https://www.googleapis.com/auth/youtube.force-ssl"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0
To make this sample run you will need to populate the client_secrets.json file
found at:
   %s
with information from the APIs Console
https://console.developers.google.com
For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

# Authorize the request and store authorization credentials.
def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("%s-oauth2.json" % sys.argv[0])
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  # Trusted testers can download this discovery document from the developers page
  # and it should be in the same directory with the code.
  with open("youtube-v3-discoverydocument.json", "r") as f:
    doc = f.read()
    return build_from_document(doc, http=credentials.authorize(httplib2.Http()))


# Call the API's commentThreads.insert method to insert a comment.
def insert_comment(args):
  youtube = get_authenticated_service(args)
  insert_result = youtube.commentThreads().insert(
    part = "snippet",
    body = dict(
      snippet = dict(
        channelId = args.channelid,
        videoId = args.videoid,
        topLevelComment = dict(
          snippet = dict(
            textOriginal = args.text
          )
        )
      )
    )
  ).execute()

  comment = insert_result["snippet"]["topLevelComment"]
  author = comment["snippet"]["authorDisplayName"]
  text = comment["snippet"]["textDisplay"]
  print "Inserted comment for %s: %s" % (author, text)


def is_published(args):
  youtube = get_authenticated_service(args)
  request = youtube.videos().list(
    part = "id, status",
    id = args.videoid)
  response = request.execute()
  privacy_status = response["items"][0]["status"]["privacyStatus"]
  return privacy_status != "unlisted"


if __name__ == "__main__":
  # The "channelid" option specifies the YouTube channel ID that uniquely
  # identifies the channel for which the comment will be inserted.
  argparser.add_argument("--channelid",
    help="Required; ID for channel for which the comment will be inserted.")

  # The "videoid" option specifies the YouTube video ID that uniquely
  # identifies the video for which the comment will be inserted.
  argparser.add_argument("--videoid",
    help="Required; ID for video for which the comment will be inserted.")

  # The "timedelta" option specifies the delay (in seconds) to post a comment
  # after the video is changed from unlisted to public.
  # Default: 600s
  argparser.add_argument("--timedelta", help="Required; delay in automated comment posting.")

  # The "text" option specifies the comment test
  argparser.add_argument("--text", help="Optional")

  args = argparser.parse_args()

  if not args.channelid:
    exit("Please specify channelid using the --channelid= parameter.")
  if not args.videoid:
    exit("Please specify videoid using the --videoid= parameter.")
  if not args.timedelta:
    exit("Please specify timedelta using the --timedelta= parameter.")
  if not args.text:
    args.text = u"English subtitles are available. 本视频有英文字幕。\n我们的野生字幕组长期志愿为中文 YouTuber 制作英文字幕，并有独家福利哦，欢迎来玩～\n详情请见 https://github.com/immoonancient/YTSubtitles"

  while not is_published(args):
    time.sleep(float(args.timedelta))
  time.sleep(float(args.timedelta))
  insert_comment(args)
